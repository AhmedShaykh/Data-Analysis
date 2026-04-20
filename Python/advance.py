num = int(input("Enter Your Number: ")); # Exception Handling

try:
    print(10 / num);

except ZeroDivisionError:
    print("Zero Division Error!");

print("Congratulations Your Division Is Successfully Run");

num = input("Enter Your Number: ");

try:
    num = int(num);
    print(10 / num);

except Exception as error:
    print(f"Sorry There Is An Error as {error}");

else:
    print("Good There Is No Exception");

print("Congratulations Your Division Is Successfully Run");

num = input("Enter Your Number: ");

try:
    num = int(num);
    print(10 / num);

except Exception as error:
    pass;

else:
    print("Good There Is No Exception");

print("Congratulations Your Division Is Successfully Run");

num = input("Enter Your Number: ");

try:
    num = int(num);
    print(10 / num);

except Exception as error:
    print(f"Sorry There Is An Error as {error}");

else:
    print("Good There Is No Exception");

finally:
    print("I Will Run No Matter What");

print("Congratulations Your Division Is Successfully Run");

age = int(input("Enter Your Number: "));

try:

    if age < 18:
        raise ValueError("Sorry Your Not Eligible"); # Raise Throw Exception Error

    else:
        print("Welcome To The Club");

except Exception as err:
    print(f"An Error Occured As {err}");

print("The Party Will Start Soon");

data = open("./main.py");  # File Handling

print(data);

print(type(data));

print(dir(data));

print([i for i in dir(data) if "__" not in i]);

print([i for i in dir(data) if not i.startswith("_")]);

data = open("./main.py"); # Connectivity With File

print(data.read());

data.close(); # Close Connectivity

with open("./app.txt") as file: # The With Method Automatically Close Your File After Done

    print(type(file));

    print(file.read());

print("Free Palestine");

with open("./app2.txt") as file:

    print(file.readline()); # Read Only One Line At A Time

    print(file.readline());

with open("./app2.txt") as file:

    print(file.readline(), end="");

    print(file.readline(), end="");

with open("./app2.txt") as file:

    print(file.readlines());

with open("./app2.txt", "r") as file: # By Default Is R (Read)

    print(file.readlines()[1:3]);

with open("./app3.txt", "w") as file: # W Is Create New File & If File Exist Remove Old Content Add New

    file.write("Imran Khan");

with open("./app3.txt") as file:

    print(file.read());

with open("./app3.txt", "r+") as file: # Read & Write Both In File

    print(file.read());

    file.write(" Release Imran Khan"); # After Run Write Method Cursor Go In Last

    print("After:", file.read()); # Then It Show Blank

with open("./app3.txt", "r+") as file:

    print(file.read());

    file.write(" Release Imran Khan");

    file.seek(0); # Select Particular Value In Cursor

    print("After:",file.read());

with open("./app4.txt", "w") as file:

    file.write("Free ");

with open("./app4.txt", "a") as file: # If File Not Exist It Will Create New File & If Exist Add Content In Last Of File Not Remove Like W

    file.write("Palestine");

with open("./app5.txt", "x") as file: # If File Not Exist Then It Will Create New File

    file.write("My Name Is AHM X"); # If File Exist Then Will Thorw Error

class Factory: # OOP (Object Oriented Programming)

    name = "Ahmed"; # Attribute

    def hello(self): # Method
        print("Hello I'm Learning OOP In Python");

obj = Factory();

print(obj.name);

obj.hello();

class Factory:

    def __init__(self, material, zips, pockets): # Constructor (__Init__)
        self.material = material;
        self.zips = zips;
        self.pockets = pockets;
    
    def show(self): # Self Method Like (This Method In JS) But It Must Write In Class Method (Function) 
        print(f"Your Brand Material Is {self.material}, Zips: {self.pockets}, Pockets: {self.zips} ");

Nike = Factory("Leather", 3, 2); # Nike Is Now Instance Of Factory (Object)

Nike.show();

Addidas = Factory("Cotton", 1, 4);

Addidas.show();

print(Addidas.material);

class Animal:

    name = "Lion"; # Class Attribute & Also Static Variable
    
    def __init__(self, name):
        self.name = name; # Instance Attribute

print(Animal.name); # It Default

pet = Animal("Horse");

print(pet.name);

class Animal:

    name = "Lion";
    
    def __init__(self, name=None):
        if name is None:
            self.name = Animal.name; # Use Class Default Attribute
        else:
            self.name = name; # Use Provided Attribute

    def favorite(self): # Instance Method
        print(f"My Favorite Animal Is: {self.name}");

print(Animal.name);

animal1 = Animal();

animal1.favorite();

animal2 = Animal("Horse");

animal2.favorite();

class Animal:

    name = "Lion";
    
    def __init__(self, name):
            self.name = name;

    def favorite(self):
        print(f"My Favorite Animal Is: {self.name}");

    @classmethod
    def pet(cls): # Class Method
        print(f"My Favorite Pet Is: {cls.name}"); # Target Class Attribute

    @staticmethod
    def static(): # Its Not Target (Object, Attribute & Method)
        print("Hi Everyone"); # Its Simple Static Fucntion

pet = Animal("Horse");

pet.favorite();

pet.pet();

pet.static();

pet2 = Animal("Cat");

pet2.favorite();

pet2.pet();

class Teacher:

    def __init__(self, teacherId, teacherName):

        self.name = teacherName;

        self.teacherId = teacherId;

        self.organizationName = "Panaversity";

    def teaching(self, subject ):
        print(f"{self.name} Is Teaching {subject}...!");

obj1 : Teacher = Teacher(1, "Andrew NG");

obj2 : Teacher = Teacher(2, "Elon Musk");

print(f"Name: {obj1.name}, ID: {obj1.teacherId} & Organiztion: {obj1.organizationName} \n");

print(f"Name: {obj2.name}, ID: {obj2.teacherId} & Organiztion: {obj2.organizationName}");

obj1.teaching("Agentic AI");

obj2.teaching("Generative AI");

print(dir(obj1));

class Teacher:

    counter = 0;

    classTiming = "10PM In USA Time";

    def __init__(this, teacherName):

        this.name = teacherName;

        this.organizationName = "Panaversity";

        Teacher.counter += 1;

    def teaching(self, subject ):
        print(f"{self.name} Is Teaching {subject}...!");

    def details(self):

        information = f"""
        Teacher Name Is {self.name}
        Class Timing is {Teacher.classTiming}
        """;

        print(information);

print(Teacher.counter);

obj1 : Teacher = Teacher("Andrew NG"); # Create New Object & Automatically Increase The Value Of Counter

print(obj1.counter);

print(Teacher.counter);

obj2 : Teacher = Teacher("Elon Musk");

print(obj1.counter);

print(obj2.counter);

print(Teacher.counter);

obj1.details();

class Parents(): # Inheritance

    def __init__(self):

        self.eyeColor = "Brown";

        self.hairColor = "Black";

    def speak(self, words):
        print(f"Speaking: {words}");

    def watching(self, objectName):
        print(f"Watching: {objectName}");

class Child(Parents):
    pass;

obj1 = Parents();

print(obj1.eyeColor);

print(obj1.hairColor);

obj1.speak("Urdu");

obj1.watching("TV \n");

obj2 = Child();

obj2.speak("English & Urdu");

obj2.watching("Netflix");

print(obj2.eyeColor);

print(obj2.hairColor);

class Parents():

    def __init__(self):

        self.eyeColor = "Brown";

        self.hairColor = "Black";

    def speak(self, words):
        print(f"Speaking: {words}");

    def watching(self, objectName):
        print(f"Watching: {objectName}");

class Child(Parents):
   
   def music(self, genre):
        print(f"I Love {genre}");

obj1 = Parents();

print(obj1.eyeColor);

print(obj1.hairColor);

obj1.speak("Urdu");

obj1.watching("TV \n");

obj2 = Child();

obj2.speak("English & Urdu");

obj2.watching("Netflix");

print(obj2.eyeColor);

print(obj2.hairColor);

obj2.music("EDM");

class Employee():

    def __init__(self, name):

        self.name = name;

class Designer(Employee):

    def __init__(self, title, name):

        super().__init__(name);

        self.title = title;

    def show(self):
        print(f"Hi! My Name Is {self.name} & I'm {self.title}");

class Developer(Employee):

    def __init__(self, title, name):

        super().__init__(name);

        self.title = title;

        self.programming_skills = ["JavaScript", "TypeScript", "Python"];

    def show(self):
        print(f"Hi! My Name Is {self.name} & I'm {self.title}");

design = Designer("Animation Artist", "Ahsan");

dev = Developer("Full Stack Developer & AI Engineer", "Ahmed");

print(design.name);

print(design.title);

print(dev.title);

print(dev.programming_skills);

design.show();

dev.show();

class Mother:

    def __init__(self, name):

        self.motherName = name;

        self.eyeColor = "Blue";

class Father:

    def __init__(self, name):

        self.fatherName = name;

        self.height = "7 Feet";

class Child(Mother, Father):

    def __init__(self, motherName, fatherName, childName):

        Mother.__init__(self, motherName);

        Father.__init__(self, fatherName);

        self.childName = childName;

    def speaking(self, words):
        return f"Imran Khan Said: {words}";

    def parents(self):
        return f"Khan Mother Name: {self.motherName} & Khan Father Name: {self.fatherName}"

imran = Child("Shaukat Khanum", "Ikramullah Khan", "Imran Khan");

print(f"Imran Khan Height {imran.height}");

print(f"Imran Khan Eye Color {imran.eyeColor}");

print(imran.speaking("Absolutely Not"));

print(imran.childName);

print(imran.fatherName);

print(imran.motherName);

print(imran.parents());

class Factory:

    def __init__(self, material, zips):

        self.material = material;

        self.zips = zips;

class NikeFactory(Factory):

    def __init__(self, material, zips, color):

        super().__init__(material, zips);

        self.color = color;
    
class AdidasFactory(NikeFactory):

    def __init__(self, material, zips, color, pockets):

        super().__init__(material, zips, color);

        self.pockets = pockets;

myFactory = Factory("Leather", 2);

nike = NikeFactory("Leather", 2, "Black");

adidas = AdidasFactory("Leather", 2, "Black", 4);

print(myFactory.material, myFactory.zips);

print(adidas.material, adidas.zips, adidas.color, adidas.pockets);

print(nike.material, nike.zips, nike.color);

class Animal(): # Polymorphism

    def eating(self, food):

        print(f"Animal Is Eating {food}");

class Bird(Animal):

    def eating(self, food):

        print(f"Bird Is Eating {food}"); # OverRide

bird = Bird();

bird.eating("Bread");

animal = Animal();

animal.eating("Meat");

animal : Animal = Bird(); # Object Will Decide Which Object Method Will Run

animal.eating("Grain");

bird : Bird = Animal(); # It's Called Polymorphism

bird.eating("Seeds");

def add(x, y): # Overloading

    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y;

    elif isinstance(x, str) and isinstance(y, str):
        return x + y;

    else:
        raise TypeError("Invalid Argument Types!");

print(add(1, 2));

print(add(2.5, 2.5));

print(add("Hello", " World!"));

class Duck: # Duck Typing

    def quack(self):

        return "Quack!";

class Person:

    def quack(self):

        return "I'm Quacking Like A Duck!";

def inTheForest(param):

    print(param.quack());

donald = Duck();

john = Person();

inTheForest(donald);

inTheForest(john);

class VU: # Access Modifiers

      def __init__(self):

        self.vuHelpline = "123456789"; # Public

        self._totalExpense = 6000; # Protected

        self.__testAnouncement = "10 June 2026"; # Private

uni = VU();

print(uni.vuHelpline);

uni.vuHelpline = "1234567890";

print(uni.vuHelpline);

print(uni._totalExpense); # Technically It Should Not Work But It Python Problem Not My Code

print(uni._VU__testAnouncement); # Its Also Access Private Value But Can't Update Value That's Not Pure Object Oriented

class StudentLogin(): # Encapsulation

    def __init__(self):

        self.__username = "Admin";

        self.__password = "Admin";

    def __dbConnectivity(self, user, passwrod):

        print("Successfully Connected");

        if user == self.__username and passwrod == self.__password:

            return "Valid User";

        else:

            return "Invalid User";

    def updatePassword(self, password):

        self.__password = password; # Setter Method

        print("Password Updated!");

    def login(self, user1 , pass1):

        message: str = self.__dbConnectivity(user1, pass1);

        print(message);

    def displayInformation(self):

        print(f"Hello Dear {self.__username}"); # Getter Method

ahmed = StudentLogin();

ahmed.login("Admin", "Ahmed");

ahmed.login("Admin", "Admin");

ahmed.updatePassword("Admin1234");

ahmed.displayInformation();

ahmed.login("Admin", "Admin1234");

class BankAccount:

    def __init__(self):

        self.__balance = 1000;

    def deposit(self, amount):

        self.__balance += amount;

        print(f"Deposited Amount: {amount}");

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount;

            print(f"Withdrawn Amount: {amount}");

        else:

            print(f"Insufficient Balance: {amount}");

    def getBalance(self):

        print("Balance:", self.__balance);

account = BankAccount();

account.getBalance();

account.deposit(500);

account.withdraw(800);

account.getBalance();

account.withdraw(900);

from abc import ABC, abstractmethod; # ABC Means (Abstract Base Classes)

class Animal(ABC):  # Abstraction

    def __init__(self):
        self.livingThing = True

    @abstractmethod
    def eat(self, food):
        ...

class Cat(Animal):

    def __init__(self):
        super().__init__();

    def eat(self, food):
        return f"Cat Is Eating {food}";

myCat = Cat();

print(myCat.livingThing);

print(myCat.eat("Fish"));

class Abstract(ABC):

    @abstractmethod
    def perimeter(self):
        pass;
    
    @abstractmethod
    def area(self):
        pass;

class Square(Abstract):

    def __init__(self, side):
        self.side = side;

    def perimeter(self):
        return 4 * self.side;

    def area(self):
        return self.side * self.side;

class Circle(Abstract):

    def __init__(self, radius):
        self.radius = radius;

    def perimeter(self):
        return 2 * 3.14 * self.radius;

    def area(self):
        return 3.14 * self.radius * self.radius;

square = Square(4);

circle = Circle(3);

print("Square Perimeter:", square.perimeter());

print("Square Area:", square.area());

print("Circle Perimeter:", circle.perimeter());

print("Circle Area:", circle.area());

class Person: # Dunder Methods

    def __init__(self, name ,age):
        self.name = name;
        self.age = age;
    
    def __str__(self):
        return f"Hello Everyone! My Name Is: {self.name}"; # Return String Not Print

    def __add__(self, other): # Other Is Present (Other Object)
        return f"Your Sum Of Ages Are: {self.age + other.age}";

person1 = Person("Ahmed", 25);

person2 = Person("AHM X", 25);

print(person1); # Default Call __Str__ Method

print(person1 + person2);

class Person:

    def __init__(self, name ,age):
        self.name = name;
        self.age = age;

    def __add__(self, other):
        sum = 0;
        for i in other: # Multiple Objects Addition
            sum = sum + i.age;
        return f"Your Sum Of Ages Are: {self.age + sum}";

person1 = Person("Ahmed", 25);

person2 = Person("AHM X", 25);

person3 = Person("Emmett", 25);

print(person1 + (person2, person3));

class MainWindow:

    def show(self):
        print("Showing The App Main Window...");

    def __str__(self):
        return "Main Window Object Is Running";

    def __call__(self):
        self.show();

window = MainWindow();

window(); # Default Call __Call__ Method & Call Method Convert Object Use Like Fucntion

print(window); # Default Call __Str__ Method

class Greet: # Decorator

    @property
    def show(self):
        print("Hello How Are You!");
    
obj = Greet();

obj.show; # I Use @Property Decorator Thats Why I Direct Show Method Without Using Parentheses

def decorate(func):

    def wrapper():

        print("Hi!");

        func();

        print("Bye Bye!");

    return wrapper;

@decorate
def hello():
    print(f"How Is Going");

hello();

def decorate(func):

    def wrapper(*args,**kwargs):

        print("Addition Your Numbers Are:");

        func(*args,**kwargs);

        print("Thats Your Result");

    return wrapper;

@decorate
def addition(a, b):
    print(f"Your Total Is {a + b} ");

addition(12, 67);

def add(*args):

    sum = 0;

    for i in args:
        sum = sum + i;

    print(sum);

add(12, 45, 567, 6781);

def info(**kwargs):

    print("Your Information Is: ");

    for i in kwargs:
        print(f"{i} : {kwargs[i]}");

info(name = "Ahmed", age = 25, designation = "AI Engineer");

print(list(range(1, 11))); # List Comprehensive

for i in range(1, 11):

    print(i ** 2);

print([i ** 2 for i in range(1, 11)]);

lis = [i for i in range(1, 21) if i % 2 == 0]; # Also Called Single Line Expression

print(lis);

key = {i : i ** 2 for i in range(1, 10)};

print(key);

checkEven = lambda x: print(f"Even: {x}") if x % 2 == 0 else print(f"Odd: {x}");

checkEven(7);

numbers = [1, 2, 3, 4];

result = map(lambda x: x * 2, numbers);

print(list(result));

def even(x):
    if x % 2 == 0:
        return True;
    else:
        False;

num = [1, 3, 4, 5, 6, 9];

result = filter(even, num);

print(result);

print(list(result));

import math;

print(math.sqrt(16));

print(int(math.sqrt(16)));