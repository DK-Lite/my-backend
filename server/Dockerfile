FROM python:3.7
COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

#RUN pip3 install flask
#RUN pip3 install flask_restfull
#RUN pip3 install pymongo

EXPOSE 3691
CMD ["python", "app.py"]

