# 🏋️‍♂️ FitForge – Fitness Tracker Web App

## 📌 Project Overview
FitForge is a web-based fitness tracking application built using Python (Flask).  
It allows users to enter their fitness details, calculate BMI automatically, track workouts, store records in a database, and visualize fitness data using charts.

This project demonstrates how frontend, backend, and database systems work together in a real-world web application.

---

## 🚀 Features

- Add user fitness details (Name, Weight, Height)
- Automatically calculate BMI
- Display BMI category (Underweight, Normal, Overweight, Obese)
- Add workout type and duration
- Automatically calculate calories burned
- Store all records in SQLite database
- Edit and delete entries
- Display records in a dashboard table
- Show BMI chart
- Show Calories burned chart

---

## 🛠️ Technologies Used

- Python
- Flask (Backend Framework)
- SQLite (Database)
- HTML5
- CSS3
- Chart.js (Data Visualization)

---

## 🧠 How It Works

### 1. User Input
The user enters:
- Name
- Weight (kg)
- Height (cm)
- Workout type
- Workout duration (minutes)

### 2. BMI Calculation
BMI is calculated using:

BMI = Weight (kg) / (Height in meters)²

BMI Categories:
- Below 18.5 → Underweight
- 18.5 – 24.9 → Normal
- 25 – 29.9 → Overweight
- 30+ → Obese

### 3. Calories Calculation
Calories burned are calculated based on workout duration and activity intensity (basic backend logic).

### 4. Data Storage
All records are stored in a SQLite database using Flask.

Each record contains:
- Name
- Weight
- Height
- BMI
- BMI Category
- Workout Type
- Duration
- Calories Burned

### 5. Dashboard
The dashboard:
- Displays all stored entries in a table
- Allows editing and deleting records
- Shows BMI chart
- Shows Calories Burned chart

Charts are generated using Chart.js.

---

## 📂 Project Structure

FitForge/
│
├── app.py  
├── fitness.db  
├── README.md  
│  
├── templates/  
│   ├── index.html  
│   ├── dashboard.html  
│   ├── edit.html  
│  
├── static/  
│   └── style.css  

---

## ▶️ How to Run the Project

1. Install Flask:
pip install flask

2. Run the application:
python app.py

3. Open browser and go to:
http://127.0.0.1:5000

---

## 🎯 Learning Outcomes

- Understanding Flask backend development
- Working with SQLite database
- Handling CRUD operations
- Integrating frontend and backend
- Creating dynamic charts
- Building a complete web application

---

## 🔮 Future Improvements

- User authentication system
- Improved UI design
- Advanced calorie calculation
- Weekly / monthly analytics
- Deployment to cloud platform

---

## 👨‍💻 Author

Developed as a learning project to understand full-stack web development using Flask.
