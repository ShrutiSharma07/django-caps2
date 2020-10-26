FROM python:3.7 
MAINTAINER Shruti <sharmashrutiy7@gmail.com> 
ADD . /usr/src/caps2
WORKDIR /usr/src/caps2
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]