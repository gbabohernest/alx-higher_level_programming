# 0x0C. Python - Almost a circle


## Synopsis

### This project is a review of the following python concepts

 - Import
 - Exceptions
 - Class
 - Private attribute
 - Getter/Setter
 - Class method
 - Static method
 - Inheritance
 - Unittest
 - Read/Write files
 - *args and **kwargs
 - Serialization / Deserialization
 - JSON


## Tests

 - Directory containing test files for python almost a circle modules (base.py, rectangle.py, square.py):

   - test_base.py
   - test_rectangle.py
   - test_square.py


## Classes

### Base

**This class will be the “base” of all other classes in this project.**
**The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)**

- Class Base:
   - private class attribute __nb_objects = 0
   - class constructor: **def __init__(self, id=None)**::
    - if id is not None, assign the public instance attribute id with this argument value - 
      you can assume id is an integer and you don’t need to test the type of it
    - otherwise, increment __nb_objects and assign the new value to the public instance attribute id


### Rectangle

**Represent a rectangle**.

- Class **Rectangle** inherits from **Base**
- Private instance attributes, each with its own public getter and setter:
   - __width -> width
   - __height -> height
   - __x -> x
   - __y -> y
    
- Class constructor: **def __init__(self, width, height, x=0, y=0, id=None)**:
  - Call the super class with **id** - this super call with use the logic of the **__init__** of the **Base** class
  - Assign each argument **width**, **height**, **x** and **y** to the right attribute


### Square

**Represent a square**

- **Square** inherits from **Rectangle**
- Class constructor: **def __init__(self, size, x=0, y=0, id=None)**::
   - Call the super class with **id**, **x**, **y**, **width** and **height** - this super call 
     will use the logic of the __init__ of the Rectangle class. The width and height must be assigned to the value of size
   - You must not create new attributes for this class, use all attributes of **Rectangle** - As reminder: 
     a Square is a Rectangle with the same width and height
   - All **width**, **height**, **x** and **y** validation must inherit from **Rectangle** - same behavior in case of wrong data

- The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, **width** or **height**
