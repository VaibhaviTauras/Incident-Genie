## Project Setup

**1. Clone the repo:**
  ```
  $ git clone git@bitbucket.org:navatechgroup/nai_configuration_service.git
  $ cd nai_configuration_service
  ```

**2. Initialize and activate a virtualenv:**
  ```
  $ virtualenv env
  $ source env/bin/activate
  ```

**3. Install the dependencies:**
  ```
  $ pip install -r requirements.txt
  ```

**4. Run following Alembic commands to Migrate your Schema(Tables/Models) into the Database.:**
  ```
  $ alembic revision --autogenerate -m "Auto migrations"
  $ alembic upgrade head
  ```

**5. Run the development server:**
  ```
  $ python run.py
  ```

**6. Navigate to [http://localhost:8000](http://localhost:8000)**

**OR**

**Navigate to open Swagger Docs[http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)**

**7. Run the Unit Test:**
  ```
  $ cd test
  $ pytest
  ```

**8. Run the docker dev server:**
  ```
  $ docker compose -f docker-compose_dev.yml up
  ```
