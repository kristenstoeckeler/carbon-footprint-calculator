# Carbon Footprint Calculator

## This is the backend of a Carbon Footprint Calculator in the making!

Users can choose from a list of daily lifestyle habits and activities and calculate their average daily carbon footprint. This is currently a work in progress.

## Technologies

This is a Python application built using Django, PostgreSQL and Docker. It is hosted by AWS.

## Available URLs

### HTML Views

| URL                                 | Description                  | Dev Status
| ----------------------------------- | ---------------------------- | -----------
| `http://localhost:8000/`            | Register page                | In progress
| `http://localhost:8000/register/`   | Register page                | In pogress
| `http://localhost:8000/login/`      | Login page                   | In progress
| `http://localhost:8000/logout/`     | Logout page                  | In progress
| `http://localhost:8000/footprints/` | Choices list (HTML template) | Barebones UI for visualization

### REST API Endpoints

| URL                                                     | Description                                                |
| ------------------------------------------------------- | ---------------------------------------------------------- |
| `http://localhost:8000/api/lifestyles/`                 | All lifestyle categories                                   |
| `http://localhost:8000/api/choices/`                    | All choices (GET/POST/DELETE)                              |
| `http://localhost:8000/api/choices/<id>/`               | Single choice (GET/PUT/PATCH/DELETE)                       |
| `http://localhost:8000/api/users/`                      | All users                                                  |
| `http://localhost:8000/api/users/<id>/choices/`         | User choices (GET) and pick choice (POST with `choice_id`) |
| `http://localhost:8000/api/users/<id>/total-footprint/` | Recalculate and save total footprint (POST)                |
