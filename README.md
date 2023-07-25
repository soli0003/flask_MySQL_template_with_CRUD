# Flask API for managing cars

This project is a simple Flask API that allows you to create, retrieve, update, and delete cars.

## Endpoints

* `/cars`: Get a list of all cars.
* `/cars/<int:car_id>`: Get a specific car by ID.
* `/cars`: Create a new car.
* `/cars/<int:car_id>`: Update a specific car.
* `/cars/<int:car_id>`: Delete a specific car.

## Usage

To use the API, you can use the following curl commands:

* Get a list of all cars:

```
curl -X GET http://localhost:5000/cars
```

* Get a specific car by ID:

```
curl -X GET http://localhost:5000/cars/1
```

* Create a new car:


curl -X POST -H "Content-Type: application/json" -d '{ "model": "Tesla Model 3", "color": "Black", "plate_number": "ABC123" }' http://localhost:5000/cars


* Update a specific car:


curl -X PUT -H "Content-Type: application/json" -d '{ "model": "Tesla Model S", "color": "White", "plate_number": "XYZ456" }' http://localhost:5000/cars/1


* Delete a specific car:

```
curl -X DELETE http://localhost:5000/cars/1
```

## Running the project

To run the project, you need to have Python 3 and Flask installed. Once you have installed the dependencies, you can run the project by following these steps:

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies by running `pip install -r requirements.txt`.
4. Start the Flask app by running `python app.py`.

The API will be available at `http://localhost:5000/`.

## Database

The project uses a MySQL database to store the cars. The database configuration is defined in the `app.config` file.

## Example

The following code shows how to get a list of all cars:

```
import requests

url = "http://localhost:5000/cars"
response = requests.get(url)

if response.status_code == 200:
    cars = response.json()
    print(cars)
```
