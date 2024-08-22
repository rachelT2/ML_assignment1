FROM python:3.11.9 AS builder

WORKDIR /app

# COPY requirements.txt /app
# RUN pip3 install -r /app/requirements.txt

# COPY . /app
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# Copy the contents of the app directory into the container at /app
COPY app/ /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r /app/requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME CarPricePrediction

# Run app.py when the container launches
CMD ["python", "app.py"]
