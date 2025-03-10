# 🔄 Project Retrospective - MIDI REST API

## 📅 Date: [10-Mars-2025]

### 📌 Project Overview
The MIDI REST API is a backend system developed using Django and MySQL, designed to facilitate therapy attendance tracking and reporting for the real company **MIDI**, which provides therapy for children in schools. The API handles roles including **Business Owner** and **Therapist**, with future support for the **Accounting Department**. The project follows the **Scrum methodology** and is organized using **GitHub**.

---

## 📝 Retrospective Overview
This retrospective aims to reflect on the progress of the project, analyze the challenges faced, identify the solutions implemented, and highlight the lessons learned. The project has been divided into distinct phases, including **Database Development** and **Frontend Implementation**. During each phase, we encountered challenges that were addressed with specific solutions and improvements.

### 🌟 What Went Well
- Successful transition to a modular architecture, making the project more scalable and maintainable.
- Timely identification and resolution of database duplication issues.
- Improved project structure and code organization after modularization.
- Effective use of Django's models to align the database structure with application requirements.
- Enhanced frontend consistency by implementing reusable components and templates.

---

## 🪲 Challenges and How We Solved Them

### 🗃️ Database Phase

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

### 💻 Frontend Phase

#### 1. Project Structure and Organization
- **Problem:** Managing relationships and dependencies between modules (e.g., enrollments depend on students and courses).
- **Solution:** Created a modular structure where each application clearly defines its dependencies and models.
- **Lesson Learned:** Maintaining consistent architecture across applications is crucial to avoiding integration issues.

#### 2. Challenges with Models
- **Problem:** Ensuring data consistency and selecting appropriate field types with adequate validation.
- **Solution:** Conducted detailed reviews of model definitions, implementing field validation and enforcing referential integrity.
- **Lesson Learned:** Designing data models with validation in mind from the start reduces future maintenance efforts.

#### 3. View Handling Issues
- **Problem:** Inconsistent use of function-based views (FBVs) and class-based views (CBVs), causing irregularity in code structure.
- **Solution:** Established a guideline to standardize view types based on complexity and reusability.
- **Additional Fixes:** Implemented reusable mixins and helper functions to avoid code duplication.
- **Lesson Learned:** Clearly defining view strategies helps maintain code consistency and readability.

#### 4. URL Configuration Issues
- **Problem:** Inconsistent URL naming and structuring between applications.
- **Solution:** Organized URLs hierarchically and standardized naming conventions with `name` and `namespace` usage.
- **Lesson Learned:** A clear and consistent URL structure greatly enhances navigation and maintainability.

#### 5. Templates and Frontend Consistency
- **Problem:** Inconsistent visual presentation and lack of reusable template components.
- **Solution:** Implemented a structured template hierarchy with base templates and reusable blocks.
- **Lesson Learned:** Standardizing the template structure from the beginning avoids duplication and maintains a consistent user experience.

#### 6. Form Handling and User Experience
- **Problem:** Lack of validation in nested forms and inconsistent user feedback.
- **Solution:** Developed custom validation methods and improved user feedback mechanisms within forms.
- **Lesson Learned:** Designing intuitive and responsive forms from the start improves user satisfaction and reduces input errors.

---

## 💡 Key Takeaways and Next Steps
- Modularization proved beneficial, but starting with a modular structure would have been more efficient.
- Using Django models from the outset is crucial to avoid database inconsistencies.
- Frontend consistency is critical to providing a uniform user experience.
- Clearly defined architecture and guidelines prevent structural inconsistencies.

### 🚀 Next Steps
1. Enhance error handling and testing to increase code robustness.
2. Finalize the accounting module as per client requirements.
3. Plan for cloud deployment to increase availability and scalability.
4. Continue refining project documentation to facilitate team onboarding.
5. Review frontend components to ensure consistency across all modules.

---

## 📝 Contributors
- **Yael Parra** - Database Architect / Data Engineer / Backend Developer
- **Andreina Suescum** - Frontend Developer / Client Liaison
- **Maxi Scarlato** - Founding Developer / Backend Developer / Developer Advocate
- **Jorge** - [Role/Position Not Specified]

Feel free to reach out to the contributors for further questions or collaboration opportunities.

