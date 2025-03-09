# 🔄 Project Retrospective - MIDI REST API

## 📅 Date: [09-Mars-2025]

### 📌 Project Overview
The MIDI REST API is a backend system developed using Django and MySQL, designed to facilitate therapy attendance tracking and reporting for the real company **MIDI**, which provides therapy for children in schools. The API handles roles including **Business Owner** and **Therapist**, with future support for the **Accounting Department**. The project follows the **Scrum methodology** and is organized using **GitHub**.

---

## 📝 Retrospective Overview
This retrospective aims to reflect on the progress of the project, analyze the challenges faced, identify the solutions implemented, and highlight the lessons learned. The migration from a monolithic to a modular architecture was a significant step in the development process, leading to both improvements and difficulties.

### 🌟 What Went Well
- Successful transition to a modular architecture, making the project more scalable and maintainable.
- Timely identification and resolution of database duplication issues.
- Improved project structure and code organization after modularization.
- Effective use of Django's models to align the database structure with application requirements.

### 🪲 Challenges and How We Solved Them

#### 1. Duplicate Databases During Migration
- **Problem:** Databases were created using scripts instead of Django models, causing duplication during migration.
- **Attempted Solution:** Used `--fake` migrations to capture the database state without duplicating.
- **Outcome:** Although this prevented duplication, Django could not correctly read the tables.
- **Final Solution:** Rebuilt the database using Django models to ensure compatibility with migrations.
- **Lesson Learned:** Always use Django models for database creation to maintain consistency and avoid duplication.

#### 2. MySQL Database Not Read Correctly During Server Run
- **Problem:** The database created from scripts in MySQL was not properly read when executing `runserver`.
- **Solution:** Modified the script to only create the database, while tables were generated through Django models.
- **Additional Fix:** Applied `class Meta = db_table` to customize table names, ensuring proper naming conventions.
- **Lesson Learned:** Leverage Django's built-in features to maintain standardized table structures.

#### 3. Data Population Script Misalignment
- **Problem:** The data insertion script for historical data failed due to foreign key discrepancies.
- **Solution:** Implemented `db_column` within the `models.py` to explicitly define foreign key column names.
- **Lesson Learned:** Pay close attention to how Django handles foreign keys to avoid compatibility issues.

#### 4. Transition from Monolithic to Modular Architecture
- **Problem:** The project was initially designed as a monolithic application, creating challenges when scaling and modularizing.
- **Solution:** Used `startapp` to split the project into modular components.
- **Lesson Learned:** Adopting a modular approach from the beginning would have saved time and reduced technical debt.

#### 5. Minor Issues During Modularization
- **Problem:** Minor errors arose from adapting variable names and adding new tables during the modularization process.
- **Solution:** Conducted thorough code reviews to align names and structures.
- **Lesson Learned:** Pay close attention to naming conventions and consistent structure during modularization.

---

## 💡 Key Takeaways and Next Steps
- Modularization proved beneficial, but starting with a modular structure would have been more efficient.
- Using Django models from the outset is crucial to avoid database inconsistencies.
- Enhanced testing practices are necessary to catch discrepancies early.
- Improved documentation during modularization can help reduce adaptation errors.

### 🚀 Next Steps
1. Enhance error handling and testing to increase code robustness.
2. Finalize the accounting module as per client requirements.
3. Plan for cloud deployment to increase availability and scalability.
4. Continue refining project documentation to facilitate team onboarding.

---

## 📝 Contributors
- **Yael Parra** - Database Architect / Data Engineer / Backend Developer
- **Andreina Suescum** - Frontend Developer / Client Liaison
- **Maxi Scarlato** - Founding Developer / Backend Developer / Developer Advocate
- **Jorge** - [Developer/Position]

Feel free to reach out to the contributors for further questions or collaboration opportunities.

