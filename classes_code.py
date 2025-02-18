import datetime
from math import pi

#############################
# Part 1: Properties and Property Decorators
#############################

class Person:
    # Use a class-level variable to fix the current year for testing purposes.
    _current_year = 2024

    def __init__(self, first_name, last_name, birth_year, base_salary=50000, bonus=10):
        # Store first and last names with underscore prefix to indicate "private" attributes.
        self._first_name = first_name
        self._last_name = last_name
        # Use the set_birth_year method to validate and set the birth year.
        self.set_birth_year(birth_year)
        # Store base salary in a private attribute.
        self._base_salary = base_salary
        # Use the bonus setter to validate and store bonus percentage.
        self.bonus = bonus

    def set_birth_year(self, year):
        """Validate and set the birth year.
        
        Birth year must be between 1900 and the fixed current year (_current_year).
        """
        current_year = datetime.datetime.now().year
        if not (1900 <= year <= Person._current_year):
            raise ValueError("Invalid birth year. Year must be between 1900 and the current year.")
        self._birth_year = year

    @property
    def full_name(self):
        """Return the full name by combining first and last names."""
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, full_name):
        """Split a full name string into first and last names.
        
        Raises:
            ValueError: If the full name does not contain at least two parts.
        """
        parts = full_name.split()
        if len(parts) < 2:
            raise ValueError("Full name must include at least a first and last name.")
        # Set first name to the first part and last name to the remaining parts.
        self._first_name = parts[0]
        self._last_name = " ".join(parts[1:])

    @property
    def first_name(self):
        """Return the first name."""
        return self._first_name

    @property
    def last_name(self):
        """Return the last name."""
        return self._last_name

    @property
    def age(self):
        """Dynamically calculate age as current year minus birth year."""
        return self.current_year - self._birth_year

    @property
    def birth_year(self):
        """Return the stored birth year."""
        return self._birth_year

    @property
    def base_salary(self):
        """Return the base salary."""
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value):
        """Set the base salary; it cannot be negative."""
        if value < 0:
            raise ValueError("Base salary cannot be negative.")
        self._base_salary = value

    @property
    def bonus(self):
        """Return the bonus percentage."""
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        """Set bonus percentage ensuring it is between 0 and 100."""
        if not (0 <= value <= 100):
            raise ValueError("Bonus percentage must be between 0 and 100.")
        self._bonus = value

    @property
    def salary(self):
        """Calculate total salary including bonus.

        Salary is computed as base_salary + (bonus% of base_salary).
        """
        return self.base_salary + (self.base_salary * self.bonus / 100)

    @property
    def current_year(self):
        """Read-only property returning the fixed current year (2024 for testing)."""
        return Person._current_year


#############################
# Part 2: Read-Only and Computed Properties
#############################

class Circle:
    def __init__(self, radius):
        # Initialize the circle using the radius setter for validation.
        self.radius = radius

    @property
    def radius(self):
        """Return the circle's radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the circle's radius after validating that it is positive.
        
        Also invalidates any cached area or diameter.
        """
        if value <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = value
        # Invalidate cached values when the radius changes.
        self._area = None
        self._diameter = None

    @property
    def diameter(self):
        """Return the diameter, which is 2 * radius.
        
        The diameter is computed and then cached.
        """
        if self._diameter is None:
            self._diameter = 2 * self.radius
        return self._diameter

    @property
    def area(self):
        """Return the area of the circle.
        
        The area is computed as pi * (radius squared) and cached until radius changes.
        """
        if self._area is None:
            print("Calculating area...")
            self._area = pi * (self.radius ** 2)
        return self._area

    def set_radius(self, new_radius):
        """Helper method to set the radius using the defined setter (with validation)."""
        self.radius = new_radius


#############################
# Part 3: Class and Static Methods with Complex Use Cases
#############################

class Vehicle:
    # Class-level variable to track total number of Vehicle instances.
    vehicle_count = 0

    def __init__(self, make, model, year):
        # Initialize instance attributes.
        self.make = make
        self.model = model
        self.year = year
        # Increment the class-level counter upon each new instance.
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        """Return the total number of Vehicle instances created."""
        return cls.vehicle_count

    @staticmethod
    def classify_vehicle(vehicle_type):
        """Classify the vehicle based on the provided string."""
        return f"This is a {vehicle_type}"

class ElectricVehicle(Vehicle):
    @staticmethod
    def classify_vehicle(vehicle_type):
        """Overrides Vehicle's static method to indicate the vehicle is electric."""
        return f"This is an electric {vehicle_type}"


#############################
# Part 4: Class Body Scope and Dynamic Behavior
#############################

class DynamicClass:
    """
    A class that demonstrates dynamic attribute assignment.
    
    The class includes a class-level static variable and allows
    adding attributes dynamically at runtime.
    """
    static_value = "Static Value"

    def __init__(self, **kwargs):
        # Dynamically set any attributes provided via keyword arguments.
        for name, value in kwargs.items():
            setattr(self, name, value)

    def dynamic_attr(self, name, value):
        """
        Dynamically adds or updates an attribute on the instance.
        
        Args:
            name (str): The attribute name.
            value: The value to assign to the attribute.
        """
        setattr(self, name, value)


class Descriptor:
    """
    A descriptor that validates the assigned value to ensure it is a positive integer.
    
    This class implements the descriptor protocol with __get__ and __set__.
    """
    def __init__(self, name):
        # Store the attribute name that this descriptor will manage.
        self.name = name

    def __get__(self, instance, owner):
        # If accessed from the class, return the descriptor itself.
        if instance is None:
            return self
        # Otherwise, return the value from the instance's dictionary.
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # Validate that the value is an integer greater than zero.
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Attribute must be a positive integer.")
        # Set the value in the instance's __dict__.
        instance.__dict__[self.name] = value


class ValidatedAttribute:
    """
    A class that uses the Descriptor to ensure that its 'value' attribute
    is always a positive integer.
    """
    # Associate the 'value' attribute with the Descriptor.
    value = Descriptor("value")

    def __init__(self, value=None):
        # If an initial value is provided, set it using the descriptor.
        if value is not None:
            self.value = value
