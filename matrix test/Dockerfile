# Base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the working directory
COPY unit_test.py /app/

# Install dependencies
#RUN pip install unit_test

# Run the unit test
CMD ["python", "unit_test.py"]
