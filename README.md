# technicalchallenge
boto3 technical challenge

Usage instructions:

1) Have python 3 installed, as well as pip/pipenv

2) Git clone this repository

3a) from the base dir of this project, run command*:
```
pipenv install
```

*This challenge was done with pipenv, if you only want to use pip use step 3b

3b) from the base dir of this project, run command:
```
pip install -r requirements.txt
```

4) ensure aws credentials are configured
this script assumes credentials will be coming from standard aws sdk locations:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

5) run the main script using command like so:
```
pipenv run python main.py
```
or
```
pipenv shell
python main.py
```

for just regular pip/non pipenv setup, use:
```
python main.py
```


Usage example using env vars for credentials, in powershell:

```
# clone git repo
git clone https://github.com/perezjasonr/technicalchallenge.git

# change to project's base dir
cd technicalchallenge

# install libraries/dependencies
pipenv install

# configure aws credentials
$env:AWS_ACCESS_KEY_ID = '<redacted>'
$env:AWS_SECRET_ACCESS_KEY = '<redacted>'
$env:AWS_DEFAULT_REGION = 'eu-north-1'

# confirm env vars carry over into venv
pipenv run python -c "import os; print(os.getenv('AWS_ACCESS_KEY_ID', 'Env Not found'))"

# confirm boto3 can leverage credentials
pipenv run python -c "import boto3; sts = boto3.client('sts'); response = sts.get_caller_identity(); print(response)"

{'UserId': '<redacted>', 'Account': '<redacted>', 'Arn': '<redacted>', 'ResponseMetadata': {'RequestId': 'a4afeb37-daef-4682-ba94-b11a3abd7c7f', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'a4afeb37-daef-4682-ba94-b11a3abd7c7f', 'content-type': 'text/xml', 'content-length': '416', 'date': 'Fri, 26 Nov 2021 17:02:13 GMT'}, 'RetryAttempts': 0}}

# run script
pipenv run python main.py

```
