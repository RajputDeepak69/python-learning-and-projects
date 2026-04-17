# 🔗 GitHub Webhook to Jira Ticket Automation (Flask)

## 👨‍💻 About This Project

I am currently learning Python and exploring real-world automation use cases in DevOps, and this project is part of my hands-on practice with API integrations.

This project uses a Flask API to create Jira tickets automatically, helping reduce manual effort in issue tracking workflows.

---

## 🚀 Problem Statement

In many development workflows, issues from tools like GitHub need to be tracked in Jira.

Manually creating Jira tickets is repetitive and inefficient — so this project automates the process.

---

## ⚙️ How It Works

Receives a request (via webhook or API call)

Sends a POST request to Jira API

Creates a new Jira ticket automatically

---

## 🧪 Example Logic

### Request Trigger:

POST `/create`

### Action:

Creates a Jira ticket with:

* Project key
* Issue type
* Summary

---

## 🛠️ Tech Used

Python
Flask
Jira REST API
requests
dotenv

---

## 📂 Project Structure

```
jira-ticket-automation/
 ├── app.py
 ├── .env
 └── README.md
```

---

## 🔐 Environment Variables Required

Create a `.env` file:

```
ISSUE_URL=your_jira_api_url
API_TOKEN=your_api_token
MAIL=your_email
```

---

## 🚀 How to Run

Install dependencies:

```
pip install flask requests python-dotenv
```

Run the application:

```
python app.py
```

---

## 💡 Key Learnings

Working with REST APIs
Building APIs using Flask
Handling authentication using API tokens
Understanding webhook-based automation
Integrating multiple tools (GitHub → Jira)

---

## ⚠️ Notes

Project key and issue type ID are specific to your Jira setup

Ensure correct permissions are configured

Always check API responses for debugging

---

## ⭐ Why I Built This

To understand how real-world tools integrate with each other and how automation can simplify development workflows and reduce manual effort.
