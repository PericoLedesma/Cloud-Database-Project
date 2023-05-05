# Dockerfile: blueprint to build the image
# Image is a template to running containers
# Container is the actual process


# Base image
FROM python:3.8.2-alpine


# Inside container: make a new folder inside container
WORKDIR /milestone

# Second dot to say in the current container
COPY client.py .

# Outside container --> Inside container: copy from outside to inside.
#This file has the libraries we want to install
#  adds files from your Docker client’s current directory.
COPY requirements.txt .
#COPY . .


# Inside container: install the python libraries used for the app
#RUN builds your application with make.
RUN pip3 install -r requirements.txt

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt


# Outside container -> Inside container
# When you run an image and generate a container, you add a new writable layer, also called the container layer, on top of the underlying layers.
# All changes made to the running container, such as writing new files, modifying existing files, and deleting files, are written to this writable container layer.
# . means everything int eh current directory
# First period . -/backend-flask (outside container)
# Second period . /backend-flask (inside container)
COPY . .

# Enviroment variables
#ENV FLASK_DEBUG=1
#ENV PORT=8080

# Where to run it
#EXPOSE ${PORT}

# CMD (command)
# To run flask.  python3 -m flask run --host=0.0.0.0 --port=4567
# CMD specifies what command to run within the container.
CMD [ "python", "./client.py" ]


#CMD [ "python", "./helloworld.py"]