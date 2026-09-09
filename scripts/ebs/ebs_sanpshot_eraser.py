import os
import boto3
import datetime

def SnapshotEraser():
    
    retention = 1 # In days

    ec2_client = boto3.client("ec2", "us-east-1")
    reservations = ec2_client.describe_snapshots(OwnerIds=["self"])

    for snapshot in reservations["Snapshots"]:
        print("Checking snapshot %s which was created on %s" %(snapshot["SnapshotId"], snapshot["StartTime"]))
        snaptime = snapshot["StartTime"].date()
        current = datetime.datetime.now().date()
        age = (current - snaptime)
        if(age.days > retention):
            SnapID = snapshot["SnapshotId"]
            ec2_client.delete_snapshot(SnapshotId=SnapID)
            print("[INFO]: Snapshot %s successfully deleted." %(snapshot["SnapshotId"]))
        else:
            print("[INFO]: Skipping this snapshot.")

if __name__ == "__main__":
    SnapshotEraser()
