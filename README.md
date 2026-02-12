 Vehicle Rental System (Python OOP)

A menu-driven Vehicle Rental System built using Python Object-Oriented Programming concepts.
This project demonstrates inheritance, method overriding, polymorphism, and clean class design.

 Purpose of the Project

This project was built to practice and demonstrate:

Object-Oriented Programming in Python

Inheritance using parent and child classes

Use of super() to reuse parent logic

Method overriding

Runtime polymorphism

Clean separation between logic and user input

 OOP Concepts Used

Encapsulation

Inheritance

Method Overriding

Polymorphism

super() function

__str__() method

 Class Structure
🔹 Vehicle (Parent Class)

Attributes

vehicle_id

brand

base_rate

Methods

calculate_rent(days)

__str__()

 Car (Child Class)

Inherits from Vehicle

Additional Attribute

air_conditioned (True / False)

Overridden Method

Adds 20% extra rent if air-conditioned

 Bike (Child Class)

Inherits from Vehicle

Additional Attribute

engine_cc

Overridden Method

Adds extra charge if engine CC is greater than 200

 Features

Add Car or Bike

Calculate rent based on number of days

Automatic rent calculation using polymorphism

Menu-driven command-line interface

Clean and readable output

 How the Program Works

User selects vehicle type (Car / Bike)

User enters vehicle details

Vehicles are stored in a list

Rent is calculated using polymorphic method calls

Same method name behaves differently for each vehicle type
