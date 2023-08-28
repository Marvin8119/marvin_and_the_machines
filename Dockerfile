# Use an official Python runtime as a parent image
FROM pypy:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a directory for your application
RUN mkdir /app

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that your Django application will run on
EXPOSE 8000

# Define the command to run your Django application with the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
