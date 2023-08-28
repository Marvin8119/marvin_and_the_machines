# Marvin_and_the_Machines

This README provides instructions on how to build and run your application using virtual environments (venv) and Docker.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.11.4 64bit
- Docker

## Build and Run with venv

1. Clone this repository to your local machine:

   git clone https://github.com/Marvin8119/marvin_and_the_machines.git

2.1 Navigate to the project directory:
	cd your-repo
2.2 Create a virtual environment and activate it:
	python -m venv venv
	source venv/bin/activate  # On Windows, use: venv\Scripts\activate
2.3 Install the project dependencies:
	pip install -r requirements.txt
2.4 Run the application:
	python manage.py runserver

*Build and Run with Docker*
3.1 Clone this repository to your local machine (if not already done):
	git clone https://github.com/Marvin8119/marvin_and_the_machines.git
3.2 Navigate to the project directory:
	cd your-repo
3.3 Build the Docker image:
	docker build -t marvin_and_the_machines-app .
3.4 Run the Docker container:
	docker run -p 8000:8000 marvin_and_the_machines-app

