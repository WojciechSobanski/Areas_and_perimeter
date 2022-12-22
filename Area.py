###Calculates the areas and perimeters of geometric figures. ###

#Calculates the areas and perimeters of a square
class Square: 

    def __init__(self, a): 
        self.a = a 

        
    def area(self): 
        return self.a * self.a 

    
    def perimeter(self): 
        return 4 * self.a 

#Sample calculations
square = Square(3) 
print(square.area())

print(square.perimeter())

#Calculates the areas and perimeters of a triangle
class Triangle: 
    def __init__(self, a, b, c, h): 
        self.a = a 
        self.b = b 
        self.c = c 
        self.h = h 

        
    def area(self): 
        return 0.5 * self.a * self.h 

    
    def perimeter(self): 
        return self.a + self.b + self.c 

#Sample calculations
triangle = Triangle(4, 6, 6, 5) 
print(triangle.area())
print(triangle.perimeter())

#Calculates the areas and perimeters of a circle
class Circle: 
    def __init__(self, r): 
        self.r = r 
        self.pi = 3.14 


    def area(self): 
        return self.pi * self.r * self.r 

    
    def perimeter(self): 
        return 2 * self.pi * self.r 

#Sample calculations
circle = Circle(4) 
print(circle.area())
print(circle.perimeter())