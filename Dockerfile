ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}
RUN pip3 install Flask

EXPOSE 5000