FROM python:3.7
COPY . /app
WORKDIR /app

RUN pip install -r grocery_store/requirements.txt
RUN pip install -e .
RUN python grocery_store/fixtures/populate_data.py
CMD ["python", "grocery_store/wsgi.py"]