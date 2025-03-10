# ✨ MIDI REST API ✨

## 📌 Index
- [📝 About the Project](#-about-the-project)
- [⚡ Main Features](#-main-features)
- [⛔ Current Issues](#-current-issues)
- [🔧 Possible Improvements](#-possible-improvements)
- [👨‍💻 Technologies Used](#-technologies-used)
- [⚙ Installation & Usage](#-installation--usage)
- [🌟 Project Status](#-project-status)
- [🧑‍💻 Collaborators](#-collaborators)

---

## 📝 About the Project
MIDI REST API is a backend system developed using Django and MySQL. It is designed for **MIDI**, a real company that provides therapy for children in schools. The primary purpose of this API is to allow therapists to mark attendance for children, including date tracking and observations.

The system supports two main roles:
- **Business Owner**
- **Therapists**

Future improvements will include a role for the **Accounting Department**, which will manage the company's expenses. The API includes authentication and role-based access control to ensure data security.

The project follows the **Scrum methodology**, is organized on **GitHub**, and includes **unit tests** for code reliability.

Additionally, scripts in **Python** and **SQL** have been created for:
- Database creation.
- Exploratory Data Analysis (EDA) on client data.
- Preparing and uploading old client data.

An **Excel file** has been provided to the client for easy data management. A script reads this file and inserts the old data into the system. However, new data will be inserted directly through the API.

---

## ⚡ Main Features
✅ User authentication & role-based access control  
✅ Attendance tracking for therapy sessions  
✅ Observations and notes for each session  
✅ User and permission management using Django's built-in models  
✅ Structured database with **7 additional tables**:
   - Therapists
   - Students
   - Legal Guardians/Parents Info
   - Enrollments
   - Courses
   - Schools
   - Sessions

✅ API documentation created with **Postman**  
✅ Basic exception handling for error management  
✅ Frontend aligned with the company’s brand identity manual  
✅ Scripts for **database creation, EDA, and old data migration**  

---

## ⛔ Current Issues
❌ Exception handling is basic and needs improvement.  
❌ Accounting module is not yet implemented.  
❌ Some unit tests need further refinement and coverage expansion.  

---

## 🔧 Possible Improvements
✅ Enhance exception handling for better error feedback.  
✅ Implement an accounting module for managing expenses (awaiting client requirements).  
✅ Improve unit testing coverage for better reliability.  
✅ Optimize API performance for handling a larger dataset.  
✅ Continue developing more views.  
✅ Implement CSV data exports for easier client reporting.  

---

## 👨‍💻 Technologies Used
- **Backend:** Django (Python)
- **Database:** MySQL
- **API Documentation:** Postman
- **Version Control:** GitHub
- **Methodology:** Scrum
- **Testing:** Unit Tests (Django's Test Framework)
- **Data Handling:** Python & SQL scripts for database creation and data migration

---

## ⚙ Installation & Usage

### 🔽 Clone the Repository
```sh
git clone https://github.com/Yael-Parra/Repo---Midi.git
# Better go to check the correct link and use that one
# Be sure you are on the repository's folder
cd Repo---Midi
```
### 📂 Folder's Structure
````markdown
apps/
├── alumnos/
├── colegios/
├── cursos/
├── info_padres_tutores_legales/
├── inscripciones/
├── terapias/
└── sesiones/

bbdd/
├── creation_db.py
├── midi_datos/
└── preparacion_e_insercion_datos.py

config_global/
└── settings/

templates/
main.py
manage.py
````

### 📦 Install Dependencies
Create and activate a virtual environment:
```sh
# This is an example using "uv" for virtual environments
uv venv --python 3.10 .venv
# Activate your virtual environment
source .venv/Scripts/activate   # Beware this might change from "Scripts" or "bin" depending if you are running windows or linux
# Installing "uv"
pip install uv
# Create toml
uv init
# Adding dependencies
uv add --active django dotenv mysql-connector-python openpyxl pandas pymysql django-widget-tweaks djangorestframework 
# Installing requirements
uv export --format requirements-txt > requirements.txt
```

### ⚙ Set Up the Database
Ensure you have **MySQL** installed and configured. Then, create a `.env` file with your database credentials.
```sh
touch .env # you must be on the project's folder
#.env file must contain this exact variables for the code to run properly.
mysql_username = 'your user name'
mysql_password = 'your password'
mysql_host = 'your host'
mysql_port =                <-- Remember the port must not be quoted as it is the rest.
bbdd_name = 'bbdd_midi'

# Creating the database on Mysql
# Place yourself first on the folder were the database Scripts and excel are.
cd bbdd
python creation_db.py # this is the script that connects to Mysql and creates the database we will work on
cd .. # return to he project
```
### ↩️ Make migrations
```sh
# Remember to be on the project's folder.
python manage.py makemigrations
python manage.py migrate
```

### 📊 Load Old Client Data (Optional)
For confidentiality reasons, the data shared is not real.
```sh
# Place yourself first on the folder were the database Scripts and excel are. 
cd bbdd
python preparacion_e_insercion_datos.py
cd .. 
```

### 🚀 Run the Server
```sh
python manage.py runserver
```
Access the API at: `http://127.0.0.1:8000/`

---

## 🌟 Project Status
🚧 **Project in Development** 🚧  
We are continuously improving the API. Stay tuned for updates!

If you find this project useful, please ⭐ **star the repository** ⭐ on GitHub!

---

## 🧑‍💻 Colaborators
If you liked this project feel free to contact us:

- [Yael Parra](https://www.linkedin.com/in/yael-parra/) - Database Architect / Data Engineer / Backend Developer / Project Documenter
- [Andreina Suescum](https://www.linkedin.com/in/andreina-suescum-a44860231) - Frontend Developer / Client Liaison
- [Maxi Scarlato](https://www.linkedin.com/in/maximiliano-carlos-scarlato-830a94284/) - Founding Developer /Backend Developer / Developer Advocate
- [Jorge](https://github.com/michaeljohnson) - 


