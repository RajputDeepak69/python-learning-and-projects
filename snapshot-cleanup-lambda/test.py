# this is just a practice work of mine, which i done during this small project journey  ...... 
# why should I manually create multiple ec2 instances, volumes or snapshot ...
# lets implement what i'm learning  ... 
import boto3
ec2 = boto3.client('ec2')

# --- Timeline 1: Create EC2 Instances ---
# This block creates multiple EC2 instances.
response = ec2.run_instances(
    ImageId='any-os-image-you-want',
    MinCount=1,
    MaxCount=7,
    InstanceType='t2.nano', 
    NetworkInterfaces=[
        {
            'SubnetId': 'your-own-sub-id',  
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': True, 
            'Groups': ['enter-ur-own-security-group-id'] 
        }
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Testing-series'
                }
            ]
        }
    ]
)
 
# --- Timeline 2: Create Snapshots for All Volumes ---

list = ec2.describe_volumes()
for volume in list['Volumes'] :
    ec2.create_snapshot(
         VolumeId= volume['VolumeId'],
        Description='Snapshot of {}'.format(volume['VolumeId'])
    )

# for deleting ec2 instance or instances ....
# instanceid = input("enter intance id :").strip()
# client.terminate_instances(
#     InstanceIds=[instanceid]
# )   