# Development Tickets

## Ticket [ID: 001]: Hello World Functionality
**-Description**  
- This ticket addresses the implementation of the "Hello, World!" functionality for the GrowEbuddy_PSA project. The goal is to ensure that users can see a "Hello, World!" message when they access the application.

**-Who is in charge**  
- Frontend Developer, Backend Developer, API Developer, QA Engineer, Project Manager

**-Why**  
- Each role is responsible for implementing their respective parts of the functionality, ensuring a cohesive and functional application.

**-Acceptance Criteria**  
- [x] The frontend displays "Hello, World!" when the homepage is accessed.
- [x] The backend responds with "Hello, World!" when the root endpoint is accessed.
- [x] The API returns a JSON response with the message when the /api/hello endpoint is accessed.
- [x] Tests are written and pass successfully for all functionalities.
- [x] Documentation for the "Hello, World!" functionality is complete.

**-Complete**  
- [x] 

**-Results/Changes**  
- The frontend implementation of the "Hello, World!" functionality has been completed successfully. The homepage now displays "Hello, World!" styled appropriately.
- The backend implementation has been successfully completed. The server now responds with "Hello, World!" at the root endpoint.
- The API endpoint has been successfully implemented. The /api/hello endpoint returns a JSON response with {"message": "Hello, World!"}.
- The database implementation has been successfully completed, with the necessary models created and registered in the admin interface.
- The documentation for the "Hello, World!" functionality has been completed and is available in `docs/functionalities/hello_world.md`.

**-Has Subtickets?**  
- [x] Yes
- [ ] No
        
  ## *[Sub-Ticket Title: Frontend Development], [Sub-Ticket ID: 001-01]*
  *-Description*  
  - Create a simple UI that displays "Hello, World!" on the homepage.
  *-Who is in charge*  
  - Frontend Developer
    *-Why*  
    - Responsible for implementing the user interface using Vue.js.
  *-Acceptance Criteria*  
  - [x] The homepage displays "Hello, World!" styled appropriately.
  *-Complete*  
  - [x] 
  *-Results/Changes*  
  - The frontend UI has been successfully implemented to display "Hello, World!" on the homepage.

  ## *[Sub-Ticket Title: Backend Development], [Sub-Ticket ID: 001-02]*
  *-Description*  
  - Set up a simple server that responds with "Hello, World!".
  *-Who is in charge*  
  - Backend Developer
    *-Why*  
    - Responsible for creating the backend functionality using Django.
  *-Acceptance Criteria*  
  - [x] The backend server responds with "Hello, World!" when the root endpoint is accessed.
  *-Complete*  
  - [x] 
  *-Results/Changes*  
  - The backend implementation has been successfully completed. The server now responds with "Hello, World!" at the root endpoint.
  - New application structure created:
    - **myapp/**: Contains the application-specific files.
      - **views.py**: Implements the `home` view returning "Hello, World!".
      - **urls.py**: Routes the root URL to the `home` view.
      - **admin.py**, **apps.py**, **models.py**, **tests.py**: Standard Django files for managing the app.

  ## *[Sub-Ticket Title: API Development], [Sub-Ticket ID: 001-03]*
  *-Description*  
  - Create an API endpoint that returns "Hello, World!".
  *-Who is in charge*  
  - API Developer
    *-Why*  
    - Responsible for implementing the API functionality.
  *-Acceptance Criteria*  
  - [x] The /api/hello endpoint returns a JSON response with {"message": "Hello, World!"}.
  *-Complete*  
  - [x] 
  *-Results/Changes*  
  - The API endpoint has been successfully implemented. The /api/hello endpoint returns a JSON response with {"message": "Hello, World!"}.
  - The following changes were made:
    - **myapp/views.py**: Added the `hello_api` view to return the JSON response.
    - **myapp/urls.py**: Updated to include the new API endpoint.

  ## *[Sub-Ticket Title: Testing], [Sub-Ticket ID: 001-04]*
  *-Description*  
  - Write tests for the "Hello, World!" functionality.
  *-Who is in charge*  
  - QA Engineer
    *-Why*  
    - Responsible for ensuring the functionality works as expected through testing.
  *-Acceptance Criteria*  
  - [x] All tests pass without errors when the test suite is run.
  *-Complete*  
  - [x] 
  *-Results/Changes*  
  - The tests for the API endpoint have been successfully implemented and passed without errors.
  - The following changes were made:
    - **myapp/tests.py**: Added a test case for the `/api/hello/` endpoint to verify the JSON response.
    - **myapp/urls.py**: Confirmed the routing for the `/api/hello/` endpoint to the `hello_api` view.
    - **myapp/views.py**: Verified the implementation of the `hello_api` view returning the expected JSON response.

  ## *[Sub-Ticket Title: Database Implementation], [Sub-Ticket ID: 001-05]*
  *-Description*  
  - Set up a database to store user interactions and logs for the "Hello, World!" functionality.
  *-Who is in charge*  
  - Database Administrator / Backend Developer
    *-Why*  
    - Responsible for designing and implementing the database schema and ensuring data persistence.
  *-Acceptance Criteria*  
  - [x] A database using PostgreSQL is set up and connected to the backend.
  - [x] The necessary tables are created to store relevant data.
  - [x] Data can be successfully read from and written to the database.
  *-Complete*  
  - [x] 
  *-Results/Changes*  
  - The database implementation has been successfully completed. The following changes were made:
    - **backendwithDjango/settings.py**: Configured the database settings to use PostgreSQL.
    - **myapp/models.py**: Created the `UserInteraction` and `TodoItem` models to store user interactions.
    - **myapp/admin.py**: Registered the `UserInteraction` and `TodoItem` models in the Django admin interface.
    - **myapp/tests.py**: Verified that data can be created and retrieved from the database.

  ## *[Sub-Ticket Title: Documentation], [Sub-Ticket ID: 001-06]*
  *-Description*  
  - Document the "Hello, World!" functionality for future reference.
  *-Who is in charge*  
  - Project Manager
    *-Why*  
    - Responsible for creating clear documentation for onboarding and reference.
  *-Acceptance Criteria*  
  - [x] Documentation clearly explains the "Hello, World!" feature and its implementation.
  *-Complete*  
  - [x] 
  *-Results/Changes*  
  - The documentation for the "Hello, World!" functionality has been successfully completed. The following changes were made:
    - Created a detailed documentation file in `docs/functionalities/hello_world.md` that covers the frontend, backend, database implementation, and testing results.
  