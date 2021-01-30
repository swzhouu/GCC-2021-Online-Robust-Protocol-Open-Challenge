FROM python:3
# USER root

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV DEBIAN_FRONTEND=noninteractive 
ENV LANG=C.UTF-8 
ENV LANGUAGE=en_US

RUN mkdir /app
WORKDIR /app

ADD ./proposal/ /app/

RUN pip3 install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-pip

RUN apt-get clean && rm -rf /var/lib/apt/lists/*
# RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 50001
# CMD  echo 'deploy config!' && python3 manage.py makemigrations conndown && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8001 
CMD python3 main.py receiver



# RUN apt-get update
# RUN apt-get -y install locales && \
#     localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
# # ENV LANG ja_JP.UTF-8
# # ENV LANGUAGE ja_JP:ja
# # ENV LC_ALL ja_JP.UTF-8
# # ENV TZ JST-9
# # ENV TERM xterm

# RUN apt-get install -y vim less
# RUN pip install --upgrade pip
# RUN pip install --upgrade setuptools