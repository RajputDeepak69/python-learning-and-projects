import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client('ec2')

def lambda_handler(event, context): 
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=30)

    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        start_time = snapshot['StartTime']
        tags = snapshot.get('Tags', [])

        if start_time > cutoff_date:
            continue

        # although in practical scenarios there can bd other tags like backup = true or anything like that....
        if any(tag['Key'] == 'Keep' and tag['Value'] == 'true' for tag in tags):
            print(f"Skipping {snapshot_id} (Keep tag)")
            continue

        # real deletion part ...
        ec2.delete_snapshot(SnapshotId=snapshot_id)
        print(f"Deleted {snapshot_id}")

    return {
        'statusCode': 200,
        'body': 'Saaf Safai done!'
    }