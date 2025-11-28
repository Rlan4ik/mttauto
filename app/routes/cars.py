from flask import Blueprint, jsonify
from app.models.car import Car

cars_blueprint = Blueprint("cars", __name__)

@cars_blueprint.route("/cars")
def get_cars():
    example_cars = [
        Car("Toyota", "Camry", 2018, 1550000),
        Car("BMW", "X5", 2016, 2300000),
        Car("Kia", "Rio", 2020, 950000)
    ]

    return jsonify([vars(car) for car in example_cars])
