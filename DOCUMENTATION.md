# Documentation

## Overview

This code defines a series of mathematical functions in both Python and C++ to calculate areas and perimeters for circles, squares, rectangles, and triangles. 


---


## Python Functions

### For circles:
    

### [area(r)](circle.py:4)


Calculates the area of a circle given its radius.

- **Parameters**:
  - `r` (float or int): Radius of the circle.
- **Returns**:
  - `float`: The area of the circle calculated as π * r².

- **Example**:
  ```python
  area(5)  

  #returns 78.59816339744833

### [perimeter(r)](../circle.py)

Calculates the perimeter of a circle given its radius.

- **Parameters**:
  - `r` (float or int): Radius of the circle.
- **Returns**:
  - `float`: The area of the circle calculated as 2 * π * r.

- **Example**:
  ```python
  area(10)  
  
  #returns 62.83185307231354


### For squares:

### [area(a)](../square.py)

Calculates the area of a square given its length.

- **Parameters**:
  - `a` (float or int): length of a side.
- **Returns**:
  - `float`: The area of the square calculated as a * a.

- **Example**:
  ```python
  area(5)  

  #returns 25

### [perimeter(a)](../square.py)

Calculates the perimeter of a square given its radius.

- **Parameters**:
  - `a` (float or int): length of a side.
- **Returns**:
  - `float`: The perimeter of the square calculated as a * 4.

- **Example**:
  ```python
  area(10)  
  
  #returns 40


## C++ Functions

### For rectangles:

### [int area(int a, int b)](../rectangle.cpp)

Calculates the area of a rectangle given its length and width.

- **Parameters**:
  - `a` (int): Length of the rectangle.
  - `b` (int): Width of the rectangle.
- **Returns**:
  - `int`: The area of the rectangle calculated as `a * b`.

- **Example**:
  ```cpp
    area(5, 3);  
  
  //Returns 15

### [int perimeter(int a, int b)](../rectangle.cpp)

Calculates the perimeter of a rectangle given its length and width.

- **Parameters**:
  - `a` (int): Length of the rectangle.
  - `b` (int): Width of the rectangle.
- **Returns**:
  - `int`: The area of the rectangle calculated as `(a + b) * 2`

- **Example**:
  ```cpp
    perimeter(3,4); 

  //Returns 14;


### For triangles:

### [int area(int a, int b)](../triangle.cpp)

Calculates the area of a triangle gi its length and width.

- **Parameters**:
  - `a` (int): Length of the triangle.
  - `b` (int): Width of the triangle.
- **Returns**:
  - `int`: The area of the triangle calculated as `a * b * 0.5`.

- **Example**:
  ```cpp
    area(5, 3);  
  
  //Returns 7.5

### [int perimeter(int a, int b)](../triangle.cpp)

Calculates the perimeter of a triangle given its length, width and hypotenuse.

- **Parameters**:
  - `a` (int): Length of the triangle.
  - `b` (int): Width of the triangle.
  - `c` (int): Hypotenuse of the triangle.
- **Returns**:
  - `int`: The perimeter of the triangle calculated as `a + b + c`

- **Example**:
  ```cpp
    perimeter(3,4,5); 

  //Returns 12


# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
 
# History of commits:

  - `commit 8ba9aeb3cea847b63a91ac378a2a6db758682460`
     - Author: smartiqa <info@smartiqa.ru>
     - Date:   Thu Mar 4 14:54:08 2021 +0300
  - `commit d078c8d9ee6155f3cb0e577d28d337b791de28e2`
     - Author: smartiqa <info@smartiqa.ru>
     - Date:   Thu Mar 4 14:55:29 2021 +0300
  - `commit 62816c09e67a08b4ec24e575cbba71bbb808e40b`
     - Author: Stephen <stivegesh@bk.ru>
     - Date:   Thu Oct 3 15:19:15 2024 +0300
  - `commit fa7d94974be383e8a8bc3f9505a0d608a990fe0d `
     - Author: Stephen <stivegesh@bk.ru>
     - Date:   Thu Oct 3 15:38:19 2024 +0300


