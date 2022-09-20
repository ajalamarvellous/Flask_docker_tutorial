# Deploying a machine learning model

### Aim
The purpose of this project is to provide a simple walkthrough for people learning
to deploy machine learning models.
The focus of this project is to deploy the machine learning model as an API
(Application Programming Interface) using
* Flask
* Docker
> Just for a little clarification, the deployed docker form will still use a
> flask endpoints, the difference is flask app without docker image and flask app
> within a docker image
I hope to add the fastapi code also soon

### Folder structure
---------------------
   ├── LICENSE
   ├── README.md          <- The README file.
   │
   ├── deployment.py      <- The flask deployment script
   │
   ├── DockerFile         <- The docker file
   │
   ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
   │                         generated with `pip freeze > requirements.txt`
   │
   └── assets             <- Assets used in this project
       ├──test_logit.pkl  <- pickled linear regression model
       │
       └──vectorizer      <- pickled preprocessing function

### Note
To run the flask app
```bash
   python deployment.py
```

To test the api within python
```python
   install requests

   url = "http://0.0.0.0:1200"
   response = requests.post(url, json=data)
```
where you create the data in the form you want and prepocess in your python
script before feeding your model (check the notebook for more explanation)

To run the flask app in production (and not deployment mode)
* Download gunicorn first (if windows use WSL)
```bash
   pip install gunicorn
```
* Run the syntax on the terminal
```bash
   gunicorn --bind 0.0.0.0:1200 deployment:app
```

To download docker
```bash

```

To load and run a docker image
```bash
   docker run -it --rm python:3.8.2-slim
```
### To get started
* Create a new directory on your PC
```bash
   mkdir deployment-tutotial
   cd deployment-tutorial
```
* Create a new virtual environment where you'll run the codes
```bash
   python 3 -m venv venv
```
* Activate the new virtual environment
```bash
   source venv/bin/activate
```
* Create a new folder in here where you will clone the repo into
```bash
   mkdir src
   cd src
```
* Clone the repository
```bash
   git clone git:github.com/ajalamarvellous/<repo-name>
```
* Download the requirements
```bash
   pip -r requirements.txt
```
* EXperiment things by yourself
