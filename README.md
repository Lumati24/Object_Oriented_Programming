📘 OOP Assignment – Classes, Inheritance & Polymorphism
🏗️ Assignment 1: Design Your Own Class

In this assignment, we designed a Smartphone class that inherits from a Device base class.

Device (Base Class):

Attributes: brand, model

Method: device_info()

Smartphone (Derived Class):

Attributes: os, storage (in addition to inherited ones)

Methods:

call(contact) → Simulates making a phone call

install_app(app_name) → Simulates app installation

Example usage:

phone1 = Smartphone("Apple", "iPhone 15 Pro", "iOS", "256GB")
phone1.call("Alice")  

🎭 Activity 2: Polymorphism Challenge

We implemented polymorphism using different vehicles, each with its own move() method.

Car → move() prints "Driving 🚗"

Plane → move() prints "Flying ✈️"

Boat → move() prints "Sailing 🚤"

Example usage:

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()

⚙️ How to Run the Program

Save the code in a Python file (e.g., assignment.py).

Open a terminal or command prompt.

Run:

python assignment.py

✅ Learning Outcomes

By completing this assignment, we practiced:

Class design with constructors (__init__()).

Encapsulation by grouping related attributes & methods.

Inheritance to reuse and extend functionality.

Polymorphism by giving the same method (move()) different behaviors.
