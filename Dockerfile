##
##

##
# Start from an existing image with Miniconda installed
FROM continuumio/miniconda3
MAINTAINER Mark Foley
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=awmProjects.settings
# Ensure that everything is up-to-date
RUN apt-get -y update && apt-get -y upgrade
RUN conda update -n base conda && conda update -n base --all


# Make a working directory in the image and set it as working
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get -y install build-essential python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

COPY ENV.yml /usr/src/app
RUN conda env create -n awmProjects --file ENV.yml


RUN echo "conda activate awmProjects" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]
# Set up conda to match our test environment
RUN conda config --add channels conda-forge && conda config --set channel_priority strict
RUN cat ~/.condarc
RUN conda install uwsgi
# Copy everything in your Django project to the image.
COPY . /usr/src/app
# Make sure that static files are up to date and available
RUN python manage.py collectstatic --no-input
# Expose port 8001 on the image. We'll map a localhost port to

EXPOSE 8001

# web applications.
CMD uwsgi --ini uwsgi.ini