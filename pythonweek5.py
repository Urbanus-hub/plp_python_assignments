# Assignment 1: Design Your Own Class! 🏗️
# Creating a Superhero class with attributes, methods, constructors, and inheritance

class Superhero:
    """Base class for superheroes"""
    
    def __init__(self, name, real_name, power_level):
        self.name = name
        self.real_name = real_name
        self.power_level = power_level
        self.health = 100
        self.energy = 100
    
    def introduce(self):
        return f"I am {self.name}, also known as {self.real_name}!"
    
    def use_power(self):
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} uses their power! Energy remaining: {self.energy}"
        else:
            return f"{self.name} is too tired to use their power!"
    
    def rest(self):
        self.energy = min(100, self.energy + 30)
        return f"{self.name} rests and recovers energy. Current energy: {self.energy}"

# Inheritance: Flying Superhero
class FlyingSuperhero(Superhero):
    """Superhero that can fly"""
    
    def __init__(self, name, real_name, power_level, flight_speed):
        super().__init__(name, real_name, power_level)
        self.flight_speed = flight_speed
        self.is_flying = False
    
    def fly(self):
        if self.energy >= 10:
            self.energy -= 10
            self.is_flying = True
            return f"{self.name} takes flight at {self.flight_speed} mph! ✈️"
        else:
            return f"{self.name} is too tired to fly!"
    
    def land(self):
        self.is_flying = False
        return f"{self.name} lands safely on the ground."

# Inheritance: Super Strength Hero
class StrengthSuperhero(Superhero):
    """Superhero with super strength"""
    
    def __init__(self, name, real_name, power_level, strength_multiplier):
        super().__init__(name, real_name, power_level)
        self.strength_multiplier = strength_multiplier
    
    def lift_heavy_object(self, weight):
        max_lift = self.strength_multiplier * 100
        if weight <= max_lift and self.energy >= 15:
            self.energy -= 15
            return f"{self.name} lifts {weight} tons with ease! 💪"
        elif weight > max_lift:
            return f"{self.name} cannot lift {weight} tons. Maximum capacity: {max_lift} tons"
        else:
            return f"{self.name} is too tired to lift heavy objects!"

# Activity 2: Polymorphism Challenge! 🎭
# Creating Vehicle classes with the same move() method but different implementations

class Vehicle:
    """Base class for vehicles"""
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        return f"{self.name} is moving at {self.speed} mph"

class Car(Vehicle):
    """Car class with driving movement"""
    
    def move(self):
        return f"{self.name} is driving on the road at {self.speed} mph 🚗"

class Plane(Vehicle):
    """Plane class with flying movement"""
    
    def move(self):
        return f"{self.name} is flying through the sky at {self.speed} mph ✈️"

class Boat(Vehicle):
    """Boat class with sailing movement"""
    
    def move(self):
        return f"{self.name} is sailing across the water at {self.speed} mph ⛵"

class Bicycle(Vehicle):
    """Bicycle class with pedaling movement"""
    
    def move(self):
        return f"{self.name} is pedaling down the path at {self.speed} mph 🚲"

# Demonstration of the classes
if __name__ == "__main__":
    print("=== SUPERHERO CLASS DEMONSTRATION ===")
    
    # Create superhero objects
    superman = FlyingSuperhero("Superman", "Clark Kent", 95, 1000)
    hulk = StrengthSuperhero("Hulk", "Bruce Banner", 90, 50)
    
    print(superman.introduce())
    print(hulk.introduce())
    print()
    
    # Demonstrate methods
    print(superman.fly())
    print(hulk.lift_heavy_object(2000))
    print(superman.use_power())
    print(hulk.use_power())
    print()
    
    print("=== POLYMORPHISM CHALLENGE DEMONSTRATION ===")
    
    # Create vehicle objects
    vehicles = [
        Car("Toyota Camry", 65),
        Plane("Boeing 747", 550),
        Boat("Speed Boat", 35),
        Bicycle("Mountain Bike", 15)
    ]
    
    # Demonstrate polymorphism - same method name, different behaviors
    for vehicle in vehicles:
        print(vehicle.move())