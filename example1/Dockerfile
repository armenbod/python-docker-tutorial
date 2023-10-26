FROM python:3.9

ADD main.py .

RUN pip install requests beautifulsoup4

CMD ["python", "./main.py"]


# Dockerfile: A blueprint for building images
# Image: Template for running containers (e.g. python-based image, like regular, slim or alpine)
# Container: Running process with application in it.
# Application: in this case, python file for scraping IMDB
