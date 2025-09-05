# Lead Management System

A web application for lead registration, built with Django and integrated with an n8n automation workflow. The entire infrastructure is containerized using Docker.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-1A1A1A?style=for-the-badge&logo=n8n&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## Prerequisites

Before you begin, ensure you have Docker installed on your machine:
* [Docker](https://www.docker.com/get-started/)

## 🚀 Getting Started

Follow the steps below to run the environment locally.

### 1. Clone the Repository
```bash
git clone https://github.com/luissaster/lead-management-system.git
cd lead-management-system
````

### 2\. Configure Environment Variables

The project uses a `.env` file to handle its settings. Create a copy of the example file:

```bash
cp .env.example .env
```

Now, open the `.env` file and fill in the variables.

⚠️ **Important**: The `N8N_WEBHOOK_URL` variable can only be set after n8n is running.

**Initial example:**

```env
# Django Variables
SECRET_KEY='your-secret-key-here'
DEBUG=1

# Database Variables
DB_NAME=challenge_db
DB_USER=challenge_user
DB_PASS=challenge_pass
DB_HOST=challenge_db
DB_PORT=5432

# n8n Variable (set this after step 4)
N8N_WEBHOOK_URL=http://challenge_n8n:5678/webhook/your-unique-id # Change to your URL
```

### 3\. Launch the Services

With the environment variables set, start all services using Docker Compose:

```bash
docker-compose up -d --build
```

This command will build the Django application image, download the Postgres and n8n images, and start the three services in the background.

### 4\. Apply Django Migrations

Next, run the database migrations inside the application container:

```bash
docker-compose exec challenge_web python manage.py migrate
```

This command creates the necessary tables in the database.

### 5\. Configure the n8n Webhook

1.  Access the n8n interface at: http://localhost:5678.
2.  Create a new workflow or import the one from the `workflow.json` file.
3.  Copy the Webhook URL from the "Webhook" node.
4.  Edit your `.env` file again and update the `N8N_WEBHOOK_URL` variable with the URL you just copied:

```env
N8N_WEBHOOK_URL=http://challenge_n8n:5678/webhook/your-unique-id
```

5.  Restart the services to apply the changes:

```bash
docker-compose up -d
```

## Accessing the Services

Once the setup is complete, the services will be available at the following addresses:

  * **Django Application**: http://localhost:8000
  * **n8n Interface**: http://localhost:5678

## Contributing

Contributions are welcome\! Please feel free to fork the repository and submit a pull request.
