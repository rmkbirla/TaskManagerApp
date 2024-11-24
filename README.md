Running the Django app directly by installing dependencies from the `requirements.txt` file and using Docker for containerization.

# Task Manager App

This is a Django-based task management application that allows users to manage their personal tasks. Users can log in using Google authentication, create, view, edit, and delete tasks. The app also features an admin panel for managing OAuth keys and inviting new users.

## Features
- Google login authentication
- Task management (Create, View, Edit, Delete tasks)
- Admin panel for managing OAuth keys and inviting new users

## Requirements
- Python 3.10 or higher
- Django 4.x or higher
- Docker (optional for containerized approach)

## Getting Started

You can run the project in two ways: by directly installing the required dependencies or by using Docker to run the app in a container. Below are the steps for both approaches.

### Approach 1: Running the App Directly (Without Docker)

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/rmkbirla/TaskManagerApp.git
   cd TaskManagerApp
   ```

2. **Create and Activate a Virtual Environment** (optional but recommended)

   - For Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - For macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Required Dependencies**

   Install all the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory of your project and add the necessary environment variables for Google OAuth and any other settings like Django `SECRET_KEY`, `DEBUG`, and `DATABASE_URL`.

   Example `.env` file:

   ```env
   EMAIL_HOST_USER= your_id 
   EMAIL_HOST_PASSWORD= **** **** **** **** (generate app password grom google console 2 factor authentication passsword will not work)

   SECRET_KEY = 'your_django_secret_key'   

   client_id= 'your_google_OAuth_client_id'
   secret= 'your_google_OAuth_secret'
   ```

5. **Run Migrations**

   Apply the database migrations to set up the necessary tables:

   ```bash
   python manage.py migrate
   ```

6. **Collect Static Files**

   Collect static files for deployment (optional for local development but recommended for production):

   ```bash
   python manage.py collectstatic
   ```

7. **Create a Superuser (Optional)**

   If you need to create a superuser for accessing the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**

   Finally, run the development server:

   ```bash
   python manage.py runserver
   ```

   Now, the app should be accessible at `http://127.0.0.1:8000`.

### Approach 2: Running the App Using Docker

If you'd prefer to run the app using Docker, follow these steps:

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd TaskManagerApp
   ```

2. **Build and Run the Docker Containers**

   Use Docker Compose to build and run the containers:

   ```bash
   docker-compose up --build
   ```

   Docker will automatically build the image and start the containers, including the database and web app. It will map port 8000 on your local machine to port 8000 in the container.

3. **Access the App**

   After the containers are up and running, the app will be available at `http://localhost:8000` in your web browser.

4. **Access the Admin Panel**

   You can access the Django admin panel by navigating to `http://localhost:8000/admin` in your web browser. Use the superuser credentials you created in the previous step.

### Stopping the Containers

If you want to stop the Docker containers, use the following command:

```bash
docker-compose down
```

### Additional Notes

- **Database**: The app uses SQLite as the database for simplicity, so there is no need for setting up a separate database server.
- **Google OAuth**: Make sure you have set up Google OAuth 2.0 credentials in the Google Developer Console and provided the `CLIENT_ID` and `CLIENT_SECRET` in the `.env` file.

## Troubleshooting

- **Docker Connection Error**: If Docker fails to connect to the daemon or containers, ensure that Docker Desktop is running on your machine.
- **Missing Environment Variables**: If the app doesn’t run as expected, double-check that all required environment variables are set correctly in your `.env` file.


```

### Key Points to Note:
- **Docker Approach**: The instructions explain how to use Docker Compose to handle containerization. Docker is used to create an isolated environment for your application, ensuring consistency across different environments.
- **Local Development**: Instructions for setting up the project without Docker, including setting up a virtual environment and installing dependencies from the `requirements.txt`.
- **Environment Variables**: It's important to mention that the project requires setting up environment variables for sensitive information such as the Google OAuth credentials and Django settings.
