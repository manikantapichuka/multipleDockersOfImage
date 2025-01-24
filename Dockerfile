
# Use an official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app
COPY . /app

# Environment variable for container to determine which directory to work with (sql_scripts or server_scripts)
ARG APP_DIR
ENV APP_DIR=${APP_DIR}

# Ensure Python can find the application and runtime files
ENV PYTHONPATH=/app:/app/${APP_DIR}:/app/${APP_DIR}/pyarmor_runtime_000000

# Copy requirements.txt and install dependencies
COPY ${APP_DIR}/requirements.txt ${APP_DIR}/requirements.txt

COPY dist/pyarmor_runtime_000000 /app/dist/pyarmor_runtime_000000


# Install dependencies for the specific app (either sql_scripts or server_scripts)
RUN pip install --no-cache-dir -r ${APP_DIR}/requirements.txt

# Expose the port passed via APP_PORT environment variable
EXPOSE $APP_PORT
