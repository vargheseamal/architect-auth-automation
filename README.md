# Architect Auth Module – QA Automation

## 📌 Project Overview
This project contains automation tests for the Login module of:
https://architect-testing.projectsmate.com/login

The scope includes UI validation and login functionality testing using Playwright and Pytest.

---

## 🛠 Tech Stack
- Python 3.x
- Pytest
- Playwright

---

## 📂 Project Structure

architect-auth-tests/
│
├── tests/
│   └── test_signup.py
│
├── .gitignore
├── requirements.txt
└── README.md

---

## ⚙ Installation Steps

1️⃣ Clone the repository:
git clone https://github.com/vargheseamal/architect-auth-automation.git

2️⃣ Navigate into the project folder:
cd architect-auth-tests

3️⃣ Install dependencies:
pip install -r requirements.txt

4️⃣ Install Playwright browsers:
playwright install

---

## ▶ Run Tests

pytest

---

## 📊 Generate HTML Report

Install pytest-html:
pip install pytest-html

Run:
pytest --html=report.html

Open report.html in browser.

---

## ✅ Test Coverage

- Login page UI validation
- Email and password field validation
- Negative login scenarios
- Google Sign-in button validation

---

## 🔎 Observations

- No visible Sign Up option available on login page.
- Login functionality tested as per available UI.
