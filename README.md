# GrowEbuddy_PSA
gamified personal development application that combines elements of virtual pet care, habit tracking, and mental wellness to help users improve their overall well-being.


# GrowgrEbuddy_PSA Project Documentation

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Product Description](#2-product-description)
3. [System Architecture](#3-system-architecture)
4. [Data Model](#4-data-model)
5. [API Specification](#5-api-specification)
6. [User Stories](#6-user-stories)
7. [Work Tickets](#7-work-tickets)
8. [Pull Requests](#8-pull-requests)

## 1. Project Overview

### 1.1 Your Full Name
Carlos Arturo Araque Montoya

### 1.1.2 Project Name
GrowEbuddy_PSA

### 1.1.3 Brief Project Description
GrowEbuddy_PSA is a gamified personal development application that combines elements of virtual pet care, habit tracking, and mental wellness to help users improve their overall well-being.

### 1.1.4 Project Scope
The current project scope focuses on implementing the following key features:

- **Virtual Mascot**: A dynamic mascot that evolves based on user progress and interactions.
- **Virtual Spaces**: Interactive environments like "The Cave" for introspection and "Samsara" for life challenges.
- **User Progression**: A system that rewards users with daily login bonuses, streaks, and achievements.

### 1.1.5 Project URL
www.growebuddy.com?

### 1.1.6 Repository URL or Compressed File

[GrowEbuddy_PSA](https://github.com/yaguarnecro/GrowEbuddy_PSA)

## 1.2. Product Description

### 1.2.1 Objective
The primary objectives of GrowEbuddy_PSA are:
1. To encourage users to engage in daily personal development activities.
2. To promote mental wellness through guided exercises and reflection.
3. To foster habit formation through gamification and rewards.
4. To provide a sense of progress and achievement in personal growth.

### 1.2.2 Main Features and Functionalities

#### MVP Features
1. **Virtual Mascot**: Evolves based on user progress and interactions.
2. **Virtual Spaces**: "The Cave" for introspection and "Samsara" for life challenges.
3. **User Progression System**: Levels, achievements, and customization options.
4. **Point System**: EXP for progress and Coins for in-app purchases.
5. **Daily Challenges and Habit Tracking**: Encourages consistent personal development activities.

#### Future Enhancements
1. **Mini-Games**: Memory Pairs and Simon Says Breath.
2. **Mood Tracking and Guided Meditations**: Supports mental wellness through reflection and mindfulness exercises.

### 1.3. Design and User Experience
The design of GrowEbuddy_PSA focuses on creating an engaging and intuitive user experience. Key design principles include:

- **Simplicity**: A clean and minimalist interface that is easy to navigate.
- **Consistency**: Uniform design patterns and elements across the application, utilizing Vuetify components.
- **Feedback**: Immediate and clear feedback for user actions to enhance interactivity.
- **Accessibility**: Ensuring the app is usable by people with diverse abilities.
- **Visual Style Guide**: Consistent use of color palette and typography to maintain a cohesive look.
- **Responsive Design**: Mobile-first approach with a responsive grid system for various devices.

*[Insert screenshots, wireframes, or links to video tutorials showcasing the user experience]*

### 1.4. Installation Instructions

To set up the GrowgrEbuddy_PSA project locally, follow these steps:

#### Prerequisites
- Ensure you have the following installed on your machine:
  - **Node.js** (version X.X.X or higher)
  - **Python** (version X.X or higher)
  - **PostgreSQL** (version X.X or higher)

#### Step 1: Clone the Repository
Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/yaguarnecro/GrowEbuddy_PSA.git
```

### Frontend Setup

To set up the frontend, navigate to the root directory and create the Vue.js project:

```bash
cd C:\Users\yagua\AI4Devs\startOver1\AI4Devs-finalproject-CAAM\GrowEbuddy_PSA
vue create frontend
cd frontend
vue add vuetify
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

This will create a new Vue.js project with Vuetify and Tailwind CSS, and start the development server:
```bash
npm run serve
```

This will create a new Vue.js project with Vuetify and Tailwind CSS and start the development server.

## 2. System Architecture

### 2.1 Architecture Diagram
The architecture of GrowgrEbuddy_PSA consists of the following components:

- **Frontend**: Built with Vue.js and Vuetify, providing a responsive user interface.
- **Backend**: Developed using Django, serving RESTful APIs to handle requests from the frontend.
- **Database**: PostgreSQL is used for data storage, ensuring data integrity and reliability.
- **Deployment**: The application is hosted on Heroku, allowing for easy scaling and management.

![Architecture Diagram](GrowEbuddy_PSA/docs/design/diagrams/information_architecture/architecture_diagram.mmd)  <!-- Replace with the actual path to your diagram -->

+-------------------+          +-------------------+
|                   |          |                   |
|   Frontend        | <------> |   Backend         |
|   (Vue.js)        |          |   (Django)       |
|                   |          |                   |
+-------------------+          +-------------------+
          |                             |
          |                             |
          |                             |
          v                             v
+-------------------+          +-------------------+
|                   |          |                   |
|   User Interface   |          |   REST API        |
|   (Vuetify)       |          |                   |
|                   |          |                   |
+-------------------+          +-------------------+
          |                             |
          |                             |
          v                             v
+-------------------+          +-------------------+
|                   |          |                   |
|   PostgreSQL      |          |                   |
|   (Database)      |          |                   |
|                   |          |                   |
+-------------------+          +-------------------+


### 2.2 Architectural Components

- **Backend**: 
  - **Python**: A versatile programming language that is easy to learn and use.
  - **Django**: A high-level Python web framework that provides a robust foundation for building web applications, ensuring rapid development and clean design.
  - **Django REST Framework**: A powerful toolkit for building Web APIs, enabling seamless communication between the frontend and backend.
  - **Caching**: 
    - Implement a caching layer (e.g., Redis or Memcached) to store frequently accessed data such as user profiles, Vpet states, and notes. This will reduce the load on the database and improve response times.

- **Database**: 
  - **PostgreSQL**: A powerful, open-source relational database management system that ensures data integrity and supports complex queries.

- **Deployment**: 
  - **Heroku**: A cloud platform as a service (PaaS) that simplifies the deployment, management, and scaling of web applications.

- **Containerization**: 
  - **Docker**: A tool designed to make it easier to create, deploy, and run applications by using containers, ensuring consistent environments across development, testing, and production.

- **Purpose**: Serves as the core logic layer, handling API requests and business logic.
  - **Features**:
     - API endpoints for creating, updating, and managing notes and challenges.
     - Logic for updating Vpet states based on user interactions and time elapsed.
     - Secure user authentication and authorization.

### 2.3 High-Level Project Description and File Structure

The GrowgrEbuddy_PSA project is organized into several key directories, each serving a specific purpose. Below is an overview of the project's file structure:

```
GrowEbuddy_PSA/
├── frontend/                  # Contains the frontend application built with Vue.js
│   ├── src/                  # Source files for the Vue.js application
│   ├── public/               # Public assets and index.html
│   ├── package.json           # Frontend dependencies and scripts
│   └── ...
├── backend/                   # Contains the backend application built with Django
│   ├── api/                  # API endpoints and views
│   ├── models/               # Database models
│   ├── migrations/           # Database migrations
│   ├── settings.py           # Django settings configuration
│   └── ...
├── docs/                      # Documentation files
│   ├── api/                  # API documentation
│   ├── development/          # Development-related documents
│   └── ...
├── tests/                     # Test cases for both frontend and backend
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── ...
├── scripts/                   # Utility scripts for development and deployment
├── .gitignore                 # Git ignore file
├── README.md                  # Project overview and instructions
└── docker-compose.yml         # Docker configuration for the application
```

#### Directory Descriptions:
- **frontend/**: Contains the source code for the Vue.js application, including components, views, and assets.
- **backend/**: Contains the Django application, including models, views, and API endpoints.
- **docs/**: Holds all documentation related to the project, including API documentation and development guides.
- **tests/**: Contains test cases for both the frontend and backend, organized into unit and integration tests.
- **scripts/**: Utility scripts that assist with development tasks, such as database seeding or deployment scripts.
- **.gitignore**: Specifies files and directories that should be ignored by Git.
- **README.md**: Provides an overview of the project, installation instructions, and other relevant information.
- **docker-compose.yml**: Configuration file for Docker, defining services, networks, and volumes for the application.

This structure ensures that the project is organized and maintainable, making it easier for developers to navigate and contribute to the codebase.

### 2.4 Infrastructure and Deployment
The GrowgrEbuddy_PSA application is deployed on Heroku, utilizing Docker containers to ensure consistent environments across development, testing, and production. The deployment process includes:

- **Docker Compose**: Used to define and run multi-container Docker applications, simplifying the setup of the development environment.
- **Heroku**: The application is hosted on Heroku, which provides a cloud platform as a service (PaaS) for easy scaling and management.
- **Continuous Integration/Continuous Deployment (CI/CD)**: GitHub Actions are configured to automate testing and deployment processes, ensuring that code changes are automatically tested and deployed to Heroku.
- **Regular Maintenance**: 
  - Schedule regular database maintenance tasks such as vacuuming and analyzing to optimize performance and reclaim storage. This can be done using cron jobs or a task scheduler like Celery.

### 2.5 Security
The application implements several security measures to protect user data and ensure safe interactions:

- **Data Encryption**: User data is encrypted both at rest and in transit to prevent unauthorized access.
- **Authentication**: A secure authentication system is implemented using OAuth 2.0, allowing users to log in safely.
- **Privacy Settings**: Users have control over their shared information, with options to manage privacy settings.
- **Data Management**: Users can export or delete their data upon request, ensuring compliance with data protection regulations.
- **Monitoring and Logging**: 
  - Integrate logging for API requests and database queries using a logging framework. Set up monitoring tools (e.g., Prometheus, Grafana) to track performance metrics and alert on anomalies.

### 2.6 Tests
The testing strategy for GrowgrEbuddy_PSA includes various testing methodologies to ensure the application is robust and reliable:

- **Unit Testing**: 
  - **Frontend**: Jest is used for unit testing Vue.js components, ensuring that each component functions as expected.
  - **Backend**: Pytest is utilized for unit testing Django models and views, verifying the correctness of backend logic.

- **Integration Testing**: 
  - **Frontend**: Cypress is employed for integration testing of user interactions within the Vue.js application.
  - **Backend**: Pytest is also used for integration tests to ensure that API endpoints work correctly with the database.

- **System Testing**: Selenium WebDriver is used for end-to-end testing, simulating user interactions with the application to validate the overall functionality.

- **User Acceptance Testing**: Beta testers provide feedback through in-app feedback forms, allowing for real-world testing and validation of user stories.

## 3. Data Model

### 3.1 Data Model Diagram
The data model for GrowgrEbuddy_PSA is designed to support the application's core features, including the virtual pet, user progression, and note management. Below is the Entity-Relationship Diagram (ERD) representing the main entities and their relationships.

![Data Model Diagram](pGrowEbuddy_PSA\docs\development\technical_diagrams\ERD_Diagram_DB.mmd)  <!-- Replace with the actual path to your ERD -->

### 3.2 Main Entities Description
The following are the main entities in the data model:

1. **User**
   - **Attributes**:
     - `user_id`: Unique identifier for the user (Primary Key)
     - `username`: The user's chosen name
     - `email`: The user's email address
     - `password_hash`: Hashed password for authentication
     - `created_at`: Timestamp of account creation
   - **Relationships**:
     - One-to-Many with **Vpet** (a user can have multiple Vpets)

2. **Vpet**
   - **Attributes**:
     - `vpet_id`: Unique identifier for the virtual pet (Primary Key)
     - `user_id`: Foreign key referencing the User entity
     - `level`: Current level of the virtual pet
     - `experience_points`: Points accumulated by the virtual pet
     - `mood`: Current mood state of the virtual pet
   - **Relationships**:
     - Many-to-One with **User**

3. **Note**
   - **Attributes**:
     - `note_id`: Unique identifier for the note (Primary Key)
     - `user_id`: Foreign key referencing the User entity
     - `title`: Title of the note
     - `content`: Content of the note
     - `created_at`: Timestamp of note creation
   - **Relationships**:
     - Many-to-One with **User**

4. **Challenge**
   - **Attributes**:
     - `challenge_id`: Unique identifier for the challenge (Primary Key)
     - `user_id`: Foreign key referencing the User entity
     - `description`: Description of the challenge
     - `points_reward`: Points awarded upon completion
     - `is_completed`: Boolean indicating if the challenge has been completed
   - **Relationships**:
     - Many-to-One with **User**

This data model supports the core functionalities of the GrowgrEbuddy_PSA application, allowing for user management, virtual pet evolution, note management, and challenge completion.

## 4. API Specification

The GrowgrEbuddy_PSA application exposes several RESTful API endpoints to facilitate communication between the frontend and backend. Below are the specifications for the main API endpoints. Note that user authentication endpoints are currently mocked and not implemented.

### 1. User Authentication (Mocked)

- **Endpoint**: `/api/auth/register`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
      "username": "string",
      "email": "string",
      "password": "string"
    }
    ```
  - **Response**:
    - **200 OK**: User registration is mocked.
      ```json
      {
        "message": "User registration is currently mocked."
      }
      ```

- **Endpoint**: `/api/auth/login`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
      "email": "string",
      "password": "string"
    }
    ```
  - **Response**:
    - **200 OK**: User login is mocked.
      ```json
      {
        "message": "User login is currently mocked."
      }
      ```

### 2. Vpet Management

- **Endpoint**: `/api/vpets`
  - **Method**: GET
  - **Headers**: 
    - `Authorization: Bearer <token>`
  - **Response**:
    - **200 OK**: Returns the user's Vpet details.
      ```json
      {
        "vpets": [
          {
            "vpet_id": "string",
            "level": "number",
            "mood": "string",
            "experience_points": "number"
          }
        ]
      }
      ```

### 3. Notes Management

- **Endpoint**: `/api/notes`
  - **Method**: POST
  - **Headers**: 
    - `Authorization: Bearer <token>`
  - **Request Body**:
    ```json
    {
      "title": "string",
      "content": "string"
    }
    ```
  - **Response**:
    - **201 Created**: Note successfully created.
      ```json
      {
        "note_id": "string",
        "message": "Note created successfully."
      }
      ```
    - **400 Bad Request**: Validation errors.
      ```json
      {
        "error": "Validation error message."
      }
      ```

### 4. Challenge Management

- **Endpoint**: `/api/challenges`
  - **Method**: POST
  - **Headers**: 
    - `Authorization: Bearer <token>`
  - **Request Body**:
    ```json
    {
      "description": "string",
      "points_reward": "number"
    }
    ```
  - **Response**:
    - **201 Created**: Challenge successfully created.
      ```json
      {
        "challenge_id": "string",
        "message": "Challenge created successfully."
      }
      ```
    - **400 Bad Request**: Validation errors.
      ```json
      {
        "error": "Validation error message."
      }
      ```

This API specification provides a clear overview of the key endpoints that will be used in the GrowgrEbuddy_PSA application, facilitating communication between the frontend and backend components.

## 5. User Stories

### User Story 1
As a user, I want to interact with a virtual pet (Vpet) that evolves based on my progress, so that I can feel a sense of connection and achievement in my personal development journey.

### User Story 2
As a user, I want to access different virtual spaces, such as "The Cave" for introspection and "Samsara" for life challenges, so that I can engage in activities that promote my mental wellness and personal growth.

### User Story 3
As a user, I want to track my daily notes and receive rewards for completing challenges, so that I can stay motivated and build positive routines.

### User Story 4
As a user, I want to set daily challenges for myself, so that I can push my boundaries and achieve personal growth goals.

### User Story 5
As a user, I want to monitor my Vpet's mood and progress, so that I can understand how my actions impact my personal development journey.

## 6. Work Tickets

### Ticket 1 (Backend)
#### [Ticket DEV-007: Backend Development for GrowgrEbuddy_PSA](GrowEbuddy_PSA\docs\development\tickets\Backend_Development_Tickets.md)
**-Description**  
This ticket encompasses the entire backend development process for the GrowgrEbuddy_PSA application. It includes implementing user authentication, developing API endpoints for Vpets, Notes, and Challenges, integrating caching, setting up monitoring and logging, and ensuring thorough testing and documentation.
**-Who is in charge**  
- Backend Development Team
**-Why**  
This ticket is critical for establishing the core functionality of the backend, enabling user management, data handling, and performance optimization. It ensures that the application can effectively support user interactions and maintain a high level of performance.
**-Acceptance Criteria**  
- User authentication is implemented and tested.
- API endpoints for Vpets, Notes, and Challenges are developed and documented.
- Caching is integrated and tested for performance improvements.
- Monitoring and logging systems are set up and verified.
- All new features are covered by unit and integration tests.
- Documentation is updated to reflect changes in the backend.
**-Complete**  
- [ ] 
**-Results/Changes**  
- Document the results or changes made after the ticket is completed.
### **-Subtickets**
  - [X] Yes

### Ticket 2 (Frontend)
**Ticket DEV-002: Implement Virtual Vpet**
- **Description:** Develop the core virtual pet feature.
- **Priority:** High
- **Assignee:** Frontend Developer
- **Acceptance Criteria:**
  - Create basic Vpet design with emoticon-based expressions
  - Implement Vpet evolution based on user progress
  - Develop Vpet interaction animations and sounds

### Ticket 3 (Database)
**Ticket DEV-003: Develop Point System**
- **Description:** Implement the EXP and Coins system.
- **Priority:** High
- **Assignee:** Full-stack Developer
- **Acceptance Criteria:**
  - Create backend logic for earning and spending points
  - Develop frontend UI for displaying user points
  - Implement point transactions for completing activities and purchasing items

## 8. Pull Requests

### Pull Request 1
[[Insert pull request details](https://github.com/yaguarnecro/Growgrebuddy_PSA/pull/5)]
´´´´
This pull request encompasses a series of significant updates and enhancements to the documentation and workflow processes for the GrowEbuddy_PSA project. The key changes include:
Completion of Ticket 2.4: Create Visual Aids for Workflow Guide:
Developed and integrated visual aids (diagrams and flowcharts) to enhance the clarity of the workflow guide.
Created the following .mmd files:
shutting_down_local_env.mmd
shutting_down_Docker_env.mmd
local_setup.mmd
docker_setup.mmd
ChangeBetweenEnv.mmd
Generated corresponding .png images for each flowchart:
shutting_down_local.png
shutting_down_docker.png
local_setup.png
docker_setup.png
ChangeBetweenEnv.png
Updated the SETUPv2.md file to include references to these newly created images.
2. Completion of Ticket 3: Update .gitignore:
Reviewed and updated the .gitignore file to ensure all necessary entries for temporary files and sensitive information are included, maintaining the integrity of the codebase.
3. Completion of Ticket 4: Organize Documentation:
Proposed and implemented a new structure for the SETUPv2.md file, which includes:
A table of contents for easy navigation.
Categorized sections for setup instructions, shutdown procedures, visual aids, and best practices.
Enhanced the overall clarity and accessibility of the documentation.
Closing of Subticket 2.5:
Closed Subticket 2.5, confirming that all necessary diagrams and workflows have been created and integrated into the documentation.
These updates aim to improve the usability and maintainability of the project documentation, ensuring that all team members can easily access and understand the necessary workflows and processes.
Please review the changes and provide feedback or approval for merging into the main branch. Thank you!
´´´´

### Pull Request 2
[Insert pull request details]

### Pull Request 3
[Insert pull request details]

### API Endpoints

- **GET /api/hello/**: Returns a simple "Hello, World!" message.
  - **Response**:
    ```json
    {
      "message": "Hello, World!"
    }
    ```
