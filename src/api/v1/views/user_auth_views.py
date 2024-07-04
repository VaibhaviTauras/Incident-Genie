from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from database.db_connection import get_db

from ..repository.user_auth_repository import add_organisation_questions, get_organisation_questions
from pydantic import BaseModel
import openai
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

router = APIRouter(prefix="/user-auth")


class IncidentPrompt(BaseModel):
    prompt: str


def generate_first_question():
    first_question_prompt = (
        "Generate a question asking the user to describe the incident in detail. response_type should be textbox "
        "Format the output as 'Question - Response Type - Question Type'."
        "Example Format: Question: Please describe the incident in detail - Response Type: textbox - Question Type: free response"
    )
    vertexai.init(project="ai-hackathon-2024-428412", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-pro-001",
    )
    responses = model.generate_content(
        [first_question_prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )
    data = str()
    for response in responses:
        print(response.text, end="")
        data = data + response.text
    parts = data.split(' - ')
    if len(parts) == 3:
        question, response_type, question_type = parts
        if response_type.strip().lower() == 'open-ended':
            response_type = 'Textbox'
        if ':' in response_type:
            response_type = response_type.split(':', 1)[1].strip()
        if ':' in question_type:
            question_type = question_type.split(':', 1)[1].strip()
        if ':' in question:
            question = question.split(':', 1)[1].strip()
        return {
            "question": question.strip(),
            "response_type": response_type.strip(),
            "question_type": question_type.strip(),
            "options": None
        }
    else:
        raise ValueError("Unexpected response format")


def generate_questions(user_prompt: str):
    possible_hazards = (
        "Unsafe excavations, Struck by / against, Health Falling objects, Unsafe access / egress, PPE, "
        "Unsafe working platforms / scaffolds, Electrical equipment and connections, Vehicle use and movement, PPE, "
        "Environment / noise / spills, Use of tools and equipment, Falls from same level, Open shafts, edges, holes, "
        "Fire / explosion, Falls from height, Lifting operations, Mechanical / guarding, At-Risk Behaviour, "
        "Traffic Management, Housekeeping, Chemical, Confined Spaces, Design, Workplace violence, Heat / cold related, "
        "Travel, Ergonomic field / office, Non Hazard"
    )

    severity = (
        "Low, Medium, High"
    )

    root_cause = ('Human error', 'Equipment failure', 'Procedural error', 'Environmental factors')

    location = ('On the Ground Floor', 'In Zone 1', 'Area 2', 'Level 1 room 2')
    ai_prompt = (
        f"Generate at least 7 questions for an incident report based on the following prompt: '{user_prompt}'. "
        "Do not ask about description of the incident, "
        "For each question, response type must be multiple choice, dropdown or textbox, "
        "the question type (e.g., location, severity, hazard_type, root_cause), and if the response type is multiple choice or dropdown, also provide possible options. "
        f"Possible hazard types are: {possible_hazards}. "
        f"Possible severities are: {severity}. "
        f"Possible root causes are: {root_cause}. "
        f"Possible locations are: {location}. "
        "Format the output as 'Question - Response Type - Question Type - Options (if any) '. "
        "Example Format: Question: Please give hazard type - Response Type: textbox - Question Type: free response - Options: High, Low"
        "PLEASE DON'T INCLUDE **"
    )

    vertexai.init(project="ai-hackathon-2024-428412", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-pro-001",
    )
    responses = model.generate_content(
        [ai_prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )
    data = str()
    for response in responses:
        print(response.text, end="")
        data = data + response.text
    return data


import re


def remove_numbering(text):
    return re.sub(r'^\d+\.\s*', '', text)


@router.post("/generate_workflow/")
async def generate_workflow(incident_prompt: IncidentPrompt):
    user_prompt = incident_prompt.prompt

    try:
        # Generate the initial question
        initial_question = generate_first_question()

        # Generate the rest of the questions
        response = generate_questions(user_prompt)

        if not response:
            raise HTTPException(status_code=400, detail="No content generated.")

        questions_and_types = response.strip().split('\n')
        questions = [initial_question]  # Start with the initial question

        for q_and_t in questions_and_types:
            parts = q_and_t.split(' - ')
            if len(parts) == 3:
                question, response_type, question_type = parts
                options = []
            elif len(parts) == 4:
                question, response_type, question_type, options = parts
                options = [option.strip() for option in options.split(',')]
            else:
                continue

            question_text = remove_numbering(question.strip())
            possible_hazards = (
                "Unsafe excavations, Struck by / against, Health Falling objects, Unsafe access / egress, PPE, "
                "Unsafe working platforms / scaffolds, Electrical equipment and connections, Vehicle use and movement, PPE, "
                "Environment / noise / spills, Use of tools and equipment, Falls from same level, Open shafts, edges, holes, "
                "Fire / explosion, Falls from height, Lifting operations, Mechanical / guarding, At-Risk Behaviour, "
                "Traffic Management, Housekeeping, Chemical, Confined Spaces, Design, Workplace violence, Heat / cold related, "
                "Travel, Ergonomic field / office, Non Hazard"
            )
            # Correct response types as needed
            if response_type.strip().lower() == 'open-ended':
                response_type = 'Textbox'
            elif response_type.strip().lower() == 'boolean':
                response_type = 'multiple choice'
                options = ['Yes', 'No']
            elif question_type.strip().lower() == 'location':
                options = ['On the Ground Floor', 'In Zone 1', 'Area 2', 'Level 1 room 2']
            elif question_type.strip().lower() == 'hazard_type':
                options = possible_hazards.split(', ')
            elif question_type.strip().lower() == 'severity':
                options = ['Low', 'Medium', 'High']
            elif question_type.strip().lower() == 'root_cause':
                options = ['Human error', 'Equipment failure', 'Procedural error', 'Environmental factors']

            if ':' in response_type:
                response_type = response_type.split(':', 1)[1].strip()
            if ':' in question_type:
                question_type = question_type.split(':', 1)[1].strip()
            if ':' in question:
                question_text = question_text.split(':', 1)[1].strip()
            if options:
                if ':' in options[0]:
                    options[0] = options[0].split(':', 1)[1].strip().replace('*', '').lstrip(' ')

            questions.append({
                "question": question_text.replace('*', '').lstrip(' '),
                "response_type": response_type.strip().replace('*', '').lstrip(' '),
                "question_type": question_type.strip().replace('*', '').lstrip(' '),
                "options": options if options else None
            })

        if not questions:
            raise HTTPException(status_code=400, detail="No questions generated.")
        data = {"questions": questions}
        return data

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")


# Define data models
class Incident(BaseModel):
    description: str


# API endpoint to predict incident details
@router.post("/predict/")
async def predict_incident_details(incident: Incident):
    try:
        # Prepare prompt for the language model
        user_prompt = f"Predict hazard type, severity, root cause, and location based on the following incident description: '{incident.description}'."

        vertexai.init(project="ai-hackathon-2024-428412", location="us-central1")
        model = GenerativeModel(
            "gemini-1.5-pro-001",
        )
        responses = model.generate_content(
            [user_prompt],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=True,
        )
        data = str()
        for response in responses:
            print(response.text, end="")
            data = data + response.text

        return {"predictions": data}

    except openai.error.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


class OrganisationWorkFlow(BaseModel):
    organisation_name: str
    question_list: list


@router.post("/add_organisation_workflow/")
async def add_organisation_workflow(ow: OrganisationWorkFlow, db: Session = Depends(get_db), ):
    try:
        # Save the questions to the database
        db_question = await add_organisation_questions(db, ow.organisation_name, ow.question_list)
        return True
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")


@router.post("/get_organisation_workflow/")
async def get_organisation_workflow(db: Session = Depends(get_db), ):
    try:
        # Save the questions to the database
        organisation = await get_organisation_questions(db)
        return organisation
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")


# Function to elaborate and improve the user prompt using the LLM
def elaborate_and_improve_prompt(user_prompt: str):
    ai_prompt = (
        f"Please reframe this prompt in 3-4 sentences: '{user_prompt}'. "
        "Provide additional details and make it more comprehensive."
        "Give only one option."
    )
    vertexai.init(project="ai-hackathon-2024-428412", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-pro-001",
    )
    responses = model.generate_content(
        [ai_prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )
    data = str()
    for response in responses:
        print(response.text, end="")
        data = data + response.text
    return data


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}


# API endpoint to receive the user prompt and return the improved version
@router.post("/elaborate_prompt/")
async def elaborate_prompt(incident_prompt: IncidentPrompt):
    user_prompt = incident_prompt.prompt

    try:
        response = elaborate_and_improve_prompt(user_prompt)

        if not response:
            raise HTTPException(status_code=400, detail="No content generated.")

        return {"elaborated_prompt": response}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
