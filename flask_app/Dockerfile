FROM python:3.6
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=localhost
COPY * ./
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 8010
CMD ["flask", "run"]