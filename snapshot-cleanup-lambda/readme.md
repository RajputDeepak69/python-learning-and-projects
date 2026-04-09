# ☁️ AWS Snapshot Cleanup Lambda (Python)

## 👨‍💻 About This Project

I am currently learning Python and cloud technologies, and this project is part of my hands-on practice with AWS automation.

This is an AWS Lambda function written in Python that automatically deletes old EBS snapshots to help reduce cloud storage costs.

---

## 🚀 Problem Statement

In AWS environments, unused EBS snapshots can accumulate over time and increase storage costs.

Manually cleaning them is inefficient — so this script automates the process.

---

## ⚙️ How It Works

* Fetches all EBS snapshots owned by the account
* Filters snapshots older than **30 days**
* Skips snapshots tagged with:

  ```
  Keep = true
  ```
* Deletes the remaining snapshots automatically

---

## 🧪 Example Logic

### Skipped:

```
Snapshot: snap-12345
Reason: Tagged with Keep=true
```

### Deleted:

```
Snapshot: snap-67890
Reason: Older than 30 days and no Keep tag
```

---

## 🛠️ Tech Used

* Python
* AWS Lambda
* Boto3

---

## 📂 Project Structure

```
snapshot-cleanup-lambda/
 ├── lambda_function.py
 ├── tes.py
 └── README.md
```

---

## 🔐 IAM Permissions Required

The Lambda function requires:

* `ec2:DescribeSnapshots`
* `ec2:DeleteSnapshot`

---

## 🚀 Deployment Steps

1. Create a Lambda function in AWS
2. Upload this script
3. Attach IAM role with required permissions
4. (Optional) Add CloudWatch trigger to run daily

---

## 💡 Key Learnings

* Writing AWS Lambda functions in Python
* Using Boto3 to interact with AWS services
* Automating cost optimization tasks
* Working with timestamps and filtering logic
* Using tags for safe resource management

---

## ⚠️ Safety Considerations

* Ensure critical snapshots are tagged with:

  ```
  Keep = true
  ```
* Test in a non-production environment first

---

## ⭐ Why I Built This

To understand how automation can help in real-world cloud cost optimization and to gain hands-on experience with AWS Lambda and Python scripting.
