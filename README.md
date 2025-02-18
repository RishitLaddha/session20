[![Python CI](https://github.com/RishitLaddha/session20/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/RishitLaddha/session20/actions/workflows/test.yml)

<img width="1225" alt="Screenshot 2025-02-18 at 23 43 24" src="https://github.com/user-attachments/assets/99c366f4-0a85-483e-808a-3165c695c2ae" />



# Project Overview

This project is designed to demonstrate advanced object-oriented programming concepts using Python. The assignment required the creation of multiple classes with distinct responsibilities, focusing on properties, computed attributes, dynamic behavior, class and static methods, and the implementation of descriptors. The goal was to design well-structured classes that manage data dynamically while enforcing validation and caching computed values where appropriate. This README explains in detail what was expected, what has been implemented, and how the solution meets these objectives.

---

# Requirements and Objectives

The project was divided into several parts, each with specific requirements:

1. **Dynamic and Computed Properties in a Person Class:**  
   The first task was to implement a `Person` class that could manage personal information efficiently. The class was expected to include:
   - A dynamic `age` property that computes the age from the provided birth year and the current year.
   - A read-only `current_year` property that always returns a fixed value, ensuring consistency in calculations.
   - A `full_name` property that combines the `first_name` and `last_name` attributes. The setter for this property must be capable of splitting a full name string into first and last names.
   - A computed `salary` property, derived from a base salary and an annual bonus percentage. The bonus must be validated to ensure it remains within a defined range (0 to 100). Any changes to the base salary or bonus should automatically update the computed salary.

2. **Geometric Computation in a Circle Class:**  
   The second task involved creating a `Circle` class that computes geometric properties dynamically:
   - The class must include a mutable `radius` property, which is validated to ensure it is always a positive number.
   - A `diameter` property should be computed as twice the radius. This property should be recalculated whenever the radius changes.
   - The `area` of the circle must be computed using the formula π * (radius²). To improve efficiency, the computed area should be cached, so that subsequent accesses return the cached value until the radius is updated. This prevents unnecessary recalculation.

3. **Class-Level and Static Functionality in Vehicle Classes:**  
   The next requirement was to implement a hierarchy of vehicle classes that make use of both class and static methods:
   - A `Vehicle` class should maintain a class-level variable that tracks the total number of vehicle instances created. A class method is responsible for returning this count.
   - A static method should be added that classifies a vehicle based on a provided string (for example, "car", "truck", or "motorcycle"). This method returns a message indicating the type of vehicle.
   - A subclass called `ElectricVehicle` should inherit from `Vehicle` and override the classification static method to indicate that the vehicle is electric. This demonstrates inheritance and the ability to redefine behavior in a subclass.

4. **Dynamic Behavior and Attribute Validation:**  
   The final part of the project focuses on dynamic behavior and the enforcement of constraints using descriptors:
   - A `DynamicClass` must be created that allows for the dynamic creation of attributes. This means that attributes can be added or modified at runtime using Python’s dynamic attribute assignment capabilities.
   - In addition, a descriptor must be implemented through a `Descriptor` class and then used in a `ValidatedAttribute` class. This descriptor ensures that any value assigned to a particular attribute is a positive integer. If an invalid value is provided, the descriptor raises a validation error. This use of the descriptor protocol shows how to encapsulate and enforce constraints on attribute assignments in a reusable manner.


# Implementation Details 

## Person Class

The `Person` class encapsulates personal information such as first name, last name, birth year, base salary, and bonus percentage. Instead of storing the age directly, the age is computed dynamically each time it is accessed. This is achieved by subtracting the stored birth year from the current year. For the purpose of consistency and testing, the current year is fixed at a predefined value.

The class also implements a `full_name` property that concatenates the first name and last name. When setting a new full name, the setter splits the input string into its constituent parts, assigning the first element as the first name and joining the remaining elements as the last name. This ensures that the full name is always kept in sync with its individual components.

Furthermore, the salary is computed as the base salary plus a bonus. The bonus is given as a percentage and is validated to remain within a strict range (from 0 to 100). If an invalid bonus value is provided, the class raises an error. This dynamic computation ensures that any change in either the base salary or bonus immediately affects the computed total salary.

## Circle Class

The `Circle` class represents a circle and computes its geometric properties based on its radius. The class uses a property for the radius that includes validation: if a non-positive number is assigned to the radius, the class raises a `ValueError`. When the radius is set or changed, any previously computed values for the diameter and area are invalidated. 

The `diameter` property calculates the diameter as twice the radius. This value is cached so that repeated accesses do not require recalculating the value unless the radius has changed.

Similarly, the `area` property computes the area using the mathematical formula π multiplied by the square of the radius. The area is computed on first access after the radius is updated and then cached. A print statement is included to indicate when the area is being calculated, which helps to verify that caching is working correctly.

A helper method is also provided to set the radius, which internally uses the radius setter to ensure that all validations and cache invalidation are properly executed.

## Vehicle and ElectricVehicle Classes

The vehicle-related classes are designed to demonstrate class-level variables and the use of class and static methods. The `Vehicle` class contains a class variable that keeps track of how many vehicle objects have been created. Every time a new `Vehicle` instance is constructed, this counter is incremented. A class method is provided to retrieve the current vehicle count.

In addition to this, the `Vehicle` class includes a static method that classifies a vehicle based on a string input. This static method simply returns a message based on the provided type, without needing access to any instance or class-specific data.

The `ElectricVehicle` subclass inherits from `Vehicle` and overrides the static classification method. The override modifies the message to indicate that the vehicle is electric. This approach demonstrates how static methods can be overridden in subclasses while preserving the same method signature.

## DynamicClass and Descriptor-Based Validation

Dynamic attribute assignment is a key feature in Python. The `DynamicClass` allows attributes to be added to an instance dynamically. During initialization, any keyword arguments passed to the constructor are set as attributes using the built-in `setattr` function. There is also a dedicated method that allows dynamic attributes to be added or updated after the instance is created.

The project also includes a descriptor implementation to enforce validation on attributes. The `Descriptor` class is defined to manage an attribute by intercepting the getting and setting process. When a value is set through the descriptor, the code checks to ensure that it is an integer and that it is positive. If the validation fails, the descriptor raises a `ValueError`.

The `ValidatedAttribute` class makes use of the `Descriptor` to define a validated attribute. When an instance of `ValidatedAttribute` is created and a value is assigned to the `value` attribute, the descriptor’s logic ensures that the assigned value meets the validation criteria.

---

# Summary

In this project, a variety of object-oriented programming techniques have been employed:

- **Dynamic Properties:**  
  Attributes such as `age`, `full_name`, and `salary` in the `Person` class are computed dynamically. This ensures that the values always reflect the current state of the object without storing redundant data.

- **Computed and Cached Properties:**  
  The `Circle` class demonstrates how properties can be computed and cached. By caching computed values such as the area and diameter, the class optimizes performance by avoiding repeated calculations.

- **Class and Static Methods:**  
  The vehicle classes illustrate how to use class methods for operations that affect the entire class (like tracking the number of instances) and static methods for functionality that does not depend on instance-specific data. Overriding static methods in a subclass is also demonstrated.

- **Dynamic Behavior:**  
  The `DynamicClass` provides a flexible design where attributes can be created at runtime, showing how Python’s dynamic nature can be harnessed to create adaptable and scalable code.

- **Descriptors:**  
  Finally, the descriptor implementation in the `Descriptor` and `ValidatedAttribute` classes provides a robust mechanism for validating attribute assignments. This enforces that certain attributes maintain specific constraints—in this case, being positive integers—ensuring data integrity throughout the application.

Overall, the solution is organized into clear, distinct parts, each addressing a specific set of requirements. Detailed validations, caching mechanisms, and dynamic behavior ensure that the classes are robust, efficient, and easy to maintain. The project not only meets the functional requirements but also demonstrates disciplined coding practices, including proper encapsulation, validation, and the use of advanced Python features.

