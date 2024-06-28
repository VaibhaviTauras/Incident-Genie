import requests


def get_language_code(language_id: int = 1):
    language_mapping = {
        1: "en",
        2: "ar",
        3: "hi",
        4: "ur",
        5: "bn",
        6: "ml",
        7: "zh"
        # Add more languages here
    }
    return language_mapping.get(language_id, "en")


def translate_text(message: str, language_id: int = 1):
    """
    Get translated message according to language
    @param message:
    @param language_code:
    @return: translated message
    """
    try:
        if language_id != 1:
            from config.config import settings
            language_url = settings.LANGUAGE_TRANSLATE_URL
            paylod = {
                "text": message,
                "SourceLanguageCode": "en",
                "TargetLanguageCode": get_language_code(language_id)
            }
            data = requests.post(language_url, json = paylod)
            response = data.json()
            if response["status"] == 200:
                message = response["translated_text"]
        return message
    except:
        return message