import boto3

def main():
    client = boto3.client('ec2')

    # create sg
    sgresponse = client.create_security_group(
        Description='technical challenge sg',
        GroupName='techchalsg',
        VpcId='vpc-038af654e26ee20df',
        TagSpecifications=[
            {
                'ResourceType': 'security-group',
                'Tags': [
                    {
                        'Key': 'EnvName',
                        'Value': 'Test Environment'
                    },
                ]
            },
        ],
        DryRun=True
    )


    ec2 = boto3.resource('ec2')
    security_group = ec2.SecurityGroup(sgresponse["GroupId"])

    # sg rules ingress
    ingressresponse = security_group.authorize_ingress(
        IpPermissions=[
            {
                'FromPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '73.201.70.132/32',
                        'Description': 'ssh from home ip'
                    },
                ],
                'ToPort': 22,
            },
            {
                'FromPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '73.201.70.132/32',
                        'Description': 'http from home ip'
                    },
                ],
                'ToPort': 80,
            }
        ],
        DryRun=True
    )

    # sg rules egress
    egressresponse = security_group.authorize_egress(
        DryRun=True,
        IpPermissions=[
            {
                'FromPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'http from any IP address'
                    },
                ],
                'ToPort': 80
            },
            {
                'FromPort': 443,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'https any IP address'
                    },
                ],
                'ToPort': 443
            }
        ]
    )

    # ec2 instance
    response = client.run_instances(
        ImageId='ami-0d15082500b576303',
        InstanceType='t3.micro',
        Placement={
            'AvailabilityZone': 'eu-north-1'
        },
        SecurityGroupIds=[
            sgresponse["GroupId"],
        ],
        SubnetId='subnet-0ba47feb798f9e376',
        DryRun=True,
        # InstanceInitiatedShutdownBehavior='stop'|'terminate',
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': True,
                'DeleteOnTermination': True,
                'Description': 'technical challenge ec2',
                'SubnetId': 'subnet-0ba47feb798f9e376',
            }
        ],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'EnvName',
                        'Value': 'Test Environment'
                    }
                ]
            }
        ]
    )

    # info section
    print(sgresponse)
    print(ingressresponse)
    print(egressresponse)
    print(response)

if __name__ == "__main__":
    main()
