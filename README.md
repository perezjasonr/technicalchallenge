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

{'GroupId': '<redacted>', 'Tags': [{'Key': 'EnvName', 'Value': 'Test Environment'}], 'ResponseMetadata': {'RequestId': '2e23db10-a607-4258-acb1-557abadd9bb0', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '2e23db10-a607-4258-acb1-557abadd9bb0', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '416', 'date': 'Tue, 30 Nov 2021 19:26:37 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
{'Return': True, 'SecurityGroupRules': [{'SecurityGroupRuleId': '<redacted>', 'GroupId': '<redacted>', 'GroupOwnerId': '<redacted>', 'IsEgress': False, 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'CidrIpv4': '<redacted>', 'Description': 'ssh from home ip'}, {'SecurityGroupRuleId': '<redacted>', 'GroupId': '<redacted>', 'GroupOwnerId': '<redacted>', 'IsEgress': False, 'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'CidrIpv4': '<redacted>', 'Description': 'http from home ip'}], 'ResponseMetadata': {'RequestId': '93cedee4-4f8a-4aa1-95c9-9173f83e4722', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '93cedee4-4f8a-4aa1-95c9-9173f83e4722', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '1251', 'date': 'Tue, 30 Nov 2021 19:26:38 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
{'Return': True, 'SecurityGroupRules': [{'SecurityGroupRuleId': '<redacted>', 'GroupId': '<redacted>', 'GroupOwnerId': '<redacted>', 'IsEgress': True, 'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'CidrIpv4': '0.0.0.0/0', 'Description': 'http from any IP address'}, {'SecurityGroupRuleId': '<redacted>', 'GroupId': '<redacted>', 'GroupOwnerId': '<redacted>', 'IsEgress': True, 'IpProtocol': 'tcp', 'FromPort': 443, 'ToPort': 443, 'CidrIpv4': '0.0.0.0/0', 'Description': 'https any IP address'}], 'ResponseMetadata': {'RequestId': '03b70673-f6bb-4183-a553-93b395777871', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '03b70673-f6bb-4183-a553-93b395777871', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '1246', 'date': 'Tue, 30 Nov 2021 19:26:38 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-0d15082500b576303', 'InstanceId': '<redacted>', 'InstanceType': 't3.micro', 'LaunchTime': datetime.datetime(2021, 11, 30, 19, 26, 40, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': '<redacted>', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': '<redacted>', 'PrivateIpAddress': '<redacted>', 'ProductCodes': [], 'PublicDnsName': '', 'State': {'Code': 0, 'Name': 'pending'}, 'StateTransitionReason': '', 'SubnetId': '<redacted>', 'VpcId': '<redacted>', 'Architecture': 'x86_64', 'BlockDeviceMappings': [], 'ClientToken': '<redacted>', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Attachment': {'AttachTime': datetime.datetime(2021, 11, 30, 19, 26, 40, tzinfo=tzutc()), 'AttachmentId': '<redacted>', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attaching', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'techchalsg5', 'GroupId': '<redacted>'}], 'Ipv6Addresses': [], 'MacAddress': '<redacted>', 'NetworkInterfaceId': '<redacted>', 'OwnerId': '<redacted>', 'PrivateIpAddress': '<redacted>', 'PrivateIpAddresses': [{'Primary': True, 'PrivateIpAddress': '<redacted>'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': '<redacted>', 'VpcId': '<redacted>', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'techchalsg5', 'GroupId': '<redacted>'}], 'SourceDestCheck': True, 'StateReason': {'Code': 'pending', 'Message': 'pending'}, 'Tags': [{'Key': 'EnvName', 'Value': 'Test Environment'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 2}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'MetadataOptions': {'State': 'pending', 'HttpTokens': 'optional', 'HttpPutResponseHopLimit': 1, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}}], 'OwnerId': '<redacted>', 'ReservationId': '<redacted>', 'ResponseMetadata': {'RequestId': 'b92f3152-9b08-4ed0-a07a-86f509c65fb0', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'b92f3152-9b08-4ed0-a07a-86f509c65fb0', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '5306', 'date': 'Tue, 30 Nov 2021 19:26:39 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}

```
