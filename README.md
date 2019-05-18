# sendgrid-django
This is an implementaion of an email backend for Django that relies on sendgrid's REST API for message delivery.

To use the backend, simply install the package (using pip), set the
`EMAIL_BACKEND` setting in Django, and add a `bash SENDGRID_API_KEY` key (set to the appropriate value) to your Django settings.

In your project's settings.py script:
Set `EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"`
Set the `SENDGRID_API_KEY` in settings.py to your api key that was provided to you by sendgrid.`SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]`

### Setup Environment Variables

Mac/Linux

Update the development environment with your `SENDGRID_API_KEY`_ (more info `here <https://sendgrid.com/docs/User_Guide/Settings/api_keys.html>`__), for example:

    echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
    echo "export EMAIL_HOST_USER='YOUR_EMAIL_HOST_USER'" >> sendgrid.env
    echo "export EMAIL_HOST_PASSWORD='YOUR_EMAIL_HOST_PASSWORD'" >> sendgrid.env
    echo "sendgrid.env" >> .gitignore
    source ./sendgrid.env

Twilio SendGrid also supports local environment file ``.env``.
Copy or rename ``.env_sample`` into ``.env`` and update `SENDGRID_API_KEY`_ with your key.

## Installation
1. Clone or download the repository.
2. Create a new virtual environment for the project.
    ```bash
    virtualenv venv
    source venv/bin/activate
    ```
3. Install required python libraries giving in the requirements.txt file.
    ```bash
    pip install -r requirements.txt
    ```
4. Run Django migrations.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Setup environment variables.
6. Start the application.
    ```bash
    python manage.py runserver
    ```
