Api_challenge

The Api_challenge API is a Django-based RESTful API designed to manage country data. It allows users to create, edit, and retrieve information about countries.

Introduction

The API is built with Django. It utilizes Django REST framework to expose the country data through a RESTful API.

Features

- List all countries with their details
- Retrieve information about a specific country by its ID
- Create a new country
- Update country details
- Delete a country

Setup

1. Clone the repository:

git clone https://github.com/KlaraNemeckova/api_challenge.git
cd api_challenge

2. Create a virtual environment and activate it:

python3 -m venv env
# For Windows:
. env/Scripts/activate

# For macOS/Linux:
source . env/bin/activate

3. Install the required dependencies:

pip install -r requirements.txt

4. Configure the database settings:

This project uses SQLite as the database, which comes pre-configured with Django for development purposes. There is no need for external database setup, making it ideal for rapid development and testing.

In the settings.py file, the database is already configured to use SQLite by default. You can confirm or modify the settings as follows:

Open the api_challenge/settings.py file.

In the DATABASES section, ensure the following configuration is in place:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # This will create the SQLite database in the project folder
    }
}

Since SQLite does not require complex configurations, you do not need to specify a username, password, or host. The database will be created automatically in the root directory of your project as db.sqlite3 when you run migrations.

5. Apply migrations:

Once the database is configured, apply the migrations to set up your tables:

python manage.py migrate

6. Start the development server:

Finally, start the Django development server to run the API locally:

python manage.py runserver

The API will now be accessible at http://localhost:8000/.

API Endpoints

The Country Management API provides the following endpoints for interacting with country data:

GET /countries/: Retrieve a list of all countries.
GET /countries/{id}/: Retrieve information about a specific country by its ID.
POST /countries/: Create a new country.
PUT /countries/{id}/: Update the details of a specific country by its ID.
DELETE /countries/{id}/: Delete a specific country by its ID.


Example Usage:

1. To retrieve all countries:

cURL:

curl -X GET http://localhost:8000/countries/

Postman:

Open Postman and create a new GET request.
Set the URL to http://localhost:8000/countries/.
Click Send to retrieve the list of countries.

2. To create a new country:

cURL:

curl -X POST -H "Content-Type: application/json" -d '{"name":"Czech Republic", "country_code":"CZ"}' http://localhost:8000/countries/

Postman:

Open Postman and create a new POST request.
Set the URL to http://localhost:8000/countries/.
In the Body tab, select raw and choose JSON format.
Paste the following JSON data:
json

{
  "name": "Czech Republic",
  "country_code": "CZ"
}
Click Send to create the new country.

3. To update a country:

cURL:

curl -X PUT -H "Content-Type: application/json" -d '{"name":"Czech republic", "country_code":"CZ"}' http://localhost:8000/countries/1/

Postman:

Open Postman and create a new PUT request.
Set the URL to http://localhost:8000/countries/1/ (where 1 is the ID of the country you want to update).
In the Body tab, select raw and choose JSON format.
Paste the updated JSON data:
json

{
  "name": "Czech republic",
  "country_code": "CZ"
}
Click Send to update the country.

4. To delete a country:

cURL:


curl -X DELETE http://localhost:8000/countries/1/

Postman:

Open Postman and create a new DELETE request.
Set the URL to http://localhost:8000/countries/1/ (where 1 is the ID of the country you want to delete).
Click Send to delete the country.

Contributing

Contributions are welcome! If you encounter any issues or would like to add new features, feel free to open a pull request.

Contribution Guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make sure to add tests for any new features or bug fixes.
Ensure your code is well-documented.
Submit a pull request describing your changes.

License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.