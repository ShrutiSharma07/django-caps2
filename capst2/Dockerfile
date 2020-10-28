FROM python:3.7 
MAINTAINER Shruti <sharmashrutiy7@gmail.com> 
ADD . /usr/src/capst2
WORKDIR /usr/src/capst2
COPY requirements.txt ./
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]