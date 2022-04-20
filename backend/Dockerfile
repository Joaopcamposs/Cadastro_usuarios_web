# pull official base image
FROM python:3.9

# set work directory
WORKDIR /projetoWeb

# copy requirements file
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /projetoWeb/backend

# expose the 3000 port from the localhost system
EXPOSE 8000

# run app
CMD ["uvicorn", "backend.app.main:app", "--reload",  "--host", "0.0.0.0", "--port", "8000"]
