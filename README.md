## kafka 
This is machine learning pipeline to help us to know how to publish and consume data to and from kafka confluent in json format.
To store the stremming data from the different diffrent producer and store it in confluent and then deserilization on data is done and that data are store in Database(only required data are store from all data)
### To run the code

Step 1: Check if conda if set in cmd or not
```
conda --version
```

Step2: Create  a conda environment
```
conda create -p venv python==3.10 -y
```

Step3:
```
conda activate venv/
```
Step4:
```
pip install -r requirements.txt
```

we have to set some of environment variable in local system
This is obtain from the confluent cloud
Cluster Environment Variable
```
API_KEY
API_SECRET_KEY
BOOTSTRAP_SERVER
```

Schema related Environment Variable
```
SCHEMA_REGISTRY_API_KEY
SCHEMA_REGISTRY_API_SECRET
ENDPOINT_SCHEMA_URL
```
Data base related Environment Variable
```
MONGO_DB_URL
```

## Update the credential in .env file and run below command to run your application in docker container


Create .env file in root dir of your project if it is not available
paste the below content and update the credentials
```
API_KEY=asgdakhlsa
API_SECRET_KEY=dsdfsdf
BOOTSTRAP_SERVER=sdfasd
SCHEMA_REGISTRY_API_KEY=sdfsaf
SCHEMA_REGISTRY_API_SECRET=sdfasdf
ENDPOINT_SCHEMA_URL=sdafasf
MONGO_DB_URL=sdfasdfas
```

Build docker image
```
docker build -t data-pipeline:lts .
```

