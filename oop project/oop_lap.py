# Person Class
class Person:
    def __init__(self, name, money, hours, meals):
        self.name = name
        self.money = money
        self.mood = self.sleep(hours)
        self.healthRate = self.eat(meals)

    def sleep(self, hours):
        if hours == 7:
            return "happy" 
        elif hours > 7:
            return "lazy"
        else:
            return "tired"
        
    def eat(self, meals):
        if meals == 3:
            return "100%"
        elif meals == 2:
            return "75%"
        else:
            return "50%"

    def buy(self, items):
        total_cost = items * 10
        if self.money >= total_cost:
            self.money -= total_cost
            print(f"{self.name} bought {items} items for {total_cost}")
        else:
            print("Not enough money!")

# Car Class with property validation
class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name 
        self._fuelRate = None
        self._velocity = None
        self.fuelRate = fuelRate  # Using setter for validation
        self.velocity = velocity   # Using setter for validation

    @property
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self._fuelRate = value
        else:
            raise ValueError("Fuel rate must be between 0 and 100")
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            raise ValueError("Velocity must be between 0 and 200")

    def run(self, distance, velocity):
        print(f"Car is starting to run with velocity {velocity} km/h for distance {distance} km.")
        self.velocity = velocity
        fuel_needed = distance * 0.25 
        
        if fuel_needed <= self.fuelRate:
            self.fuelRate -= fuel_needed
            print(f"Car moved {distance} km. Remaining fuel: {self.fuelRate:.2f}")
            self.stop(0)
        else:
            # Calculate how far we can go with current fuel
            max_distance = self.fuelRate / 0.25
            remaining_distance = distance - max_distance
            self.fuelRate = 0
            print(f"Ran out of fuel after {max_distance:.2f} km")
            self.stop(remaining_distance)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance == 0:
            print("You have arrived at your destination.")
        else:
            print(f"Car stopped. Remaining distance: {remaining_distance:.2f} km.")

# Employee Class (inherits from Person)
class Employee(Person):
    def __init__(self, name, money, hours, meals, id, car, email, salary, distance_to_work):
        super().__init__(name, money, hours, meals)  # Fixed super() call
        self.id = id 
        self.car = car
        self.email = email 
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "happy" 
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance, velocity):
        self.car.run(distance, velocity)
    
    def refuel(self, gasAmount=100):
        """Add gasAmount to fuelRate"""
        new_fuel = self.car.fuelRate + gasAmount
        if new_fuel > 100:
            self.car.fuelRate = 100
            print(f"Tank is full! Added {100 - (new_fuel - gasAmount)} liters.")
        else:
            self.car.fuelRate = new_fuel
            print(f"Added {gasAmount} liters. Current fuel: {self.car.fuelRate}")

# Office Class
class Office:
    numbers_of_employees = 0  # Class variable
    
    def __init__(self, name):
        self.name = name
        self.employees = {}
    
    def get_all_employees(self):  # Fixed method name
        """Return a list of all current employees"""
        return list(self.employees.values())

    def get_employee(self, emp_id):  # Fixed method name
        """Return the employee with given ID"""
        return self.employees.get(emp_id)

    def hire(self, employee):
        """Hire the given employee"""
        if isinstance(employee, Employee):
            self.employees[employee.id] = employee
            Office.numbers_of_employees += 1
            print(f"{employee.name} is hired in {self.name}")
        else:
            print("Enter object from Employee class")              

    def fire(self, emp_id):
        """Fire employee with the given ID"""
        if emp_id in self.employees:
            fired_employee_name = self.employees[emp_id].name
            del self.employees[emp_id]
            Office.numbers_of_employees -= 1 
            print(f"{fired_employee_name} is fired from {self.name}")
        else:
            print("Employee does not exist")
    
    def deduct(self, emp_id, deduction):
        """Deduct money from salary from employee"""
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary -= deduction
            print(f"{deduction} was deducted from {employee.name}")
        else: 
            print("Employee does not exist")

    def reward(self, emp_id, reward):  # Fixed parameter name
        """Add money to salary from employee"""
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary += reward
            print(f"{reward} was added to {employee.name} as a reward for his effort")
        else:
            print("Employee ID does not exist")

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        """Static method to calculate if employee is late or not"""
        if velocity <= 0: 
            return False 
        time_needed = distance / velocity
        arrival_time = move_hour + time_needed
        return arrival_time > target_hour  # True = late, False = on time

    def check_lateness(self, emp_id, move_hour, distance, velocity, target_hour=9):
        """Check if employee is late or not and deduct if late (-10) or reward if not late (+10)"""
        employee = self.get_employee(emp_id)
        if not employee:
            print(f"Employee does not exist: {emp_id}")
            return

        is_late = Office.calculate_lateness(target_hour, move_hour, distance, velocity)

        if is_late:
            print(f"Employee {employee.name} is late")
            self.deduct(emp_id, 10)
        else:                             
            print(f"{employee.name} arrived on time")
            self.reward(emp_id, 10)
    
    @classmethod
    def change_emps_num(cls, num):
        """Class method to modify the number of employees in all offices"""
        cls.numbers_of_employees = num
        print(f"Total employees count changed to: {num}")


# Test the classes
if __name__ == "__main__":
    # Create a car
    car1 = Car("Toyota", 80, 60)
    
    # Create an employee
    emp1 = Employee("Ahmed", 5000, 7, 3, 101, car1, "ahmed@company.com", 8000, 20)
    
    # Create an office
    office = Office("Tech Company")
    
    # Test hiring
    office.hire(emp1)
    
    # Test employee methods
    emp1.work(8)
    emp1.drive(10, 50)
    emp1.refuel(20)
    
    # Test office methods
    print(f"All employees: {[emp.name for emp in office.get_all_employees()]}")
    
    # Test lateness check
    office.check_lateness(101, 8.5, 20, 40, 9)  # Should be on time
    office.check_lateness(101, 8.8, 20, 30, 9)  # Should be late
    
    # Test class variable
    print(f"Total employees: {Office.numbers_of_employees}")
    Office.change_emps_num(50)