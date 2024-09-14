Okla Recipe Finder Backend

Welcome to the Okla Recipe Finder backend repository! This project is built with Django and Django REST Framework and provides a robust API for managing recipes and user favorites.

Table of Contents
Project Overview
Features
Technologies Used
Installation and Setup
Usage
API Endpoints
Testing
Contributing
License
Project Overview
The Okla Recipe Finder backend provides an API to:

Search for recipes.
View detailed information about recipes.
Manage user favorites securely.
Features
Recipe Management: Add, update, and delete recipes.
Favorites Management: Users can save and manage their favorite recipes.
Secure Authentication: JWT-based authentication for secure user management.
User Management: Allows users to register, log in, and manage their profiles.
Technologies Used
Django: A high-level Python web framework that encourages rapid development.
Django REST Framework (DRF): A powerful toolkit for building Web APIs.
SQLite: A lightweight database for development and testing.
JWT: JSON Web Token for secure user authentication.
Installation and Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/okla-recipe-finder-backend.git
cd okla-recipe-finder-backend
Create a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser (optional but recommended for admin access):

bash
Copy code
python manage.py createsuperuser
Run the Development Server:

bash
Copy code
python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.

Usage
Authentication: Use the /api/token/ endpoint to obtain JWT tokens.
Recipe Endpoints: Access recipe data through /api/meal/.
Favorites Endpoints: Manage favorites through /api/favorites/.
API Endpoints
Authentication
Obtain Token: POST /api/token/
Refresh Token: POST /api/token/refresh/
Verify Token: POST /api/token/verify/
Recipes
List Recipes: GET /api/meal/
Retrieve Recipe Details: GET /api/meal/{id}/
Create Recipe: POST /api/meal/
Update Recipe: PUT /api/meal/{id}/
Delete Recipe: DELETE /api/meal/{id}/
Favorites
List Favorites: GET /api/favorites/
Add Favorite: POST /api/favorites/
Remove Favorite: DELETE /api/favorites/{id}/
Testing
To run tests for the application:

bash
Copy code
python manage.py test
Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
