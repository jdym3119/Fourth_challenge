from classes_.Point import Point
from classes_.Shapes.Equilateral import Equilateral
from classes_.Shapes.Isosceles import Isosceles
from classes_.Shapes.Rectangle import Rectangle
from classes_.Shapes.Scalene import Scalene
from classes_.Shapes.Square import Square
from classes_.Shapes.Triangle import Triangle
from classes_.Shapes.TriRectangle import TriRectangle
#type: ignore



if __name__ == "__main__":
  print(
      "Welcome to this code, this could calculate the area, the perimeter  and the \
inner angles of a shape"
  )
  print("You could choose one of this shapes: ")
  print(
      "rectangle, square, triangle, isosceles triangle, \
      equilateral triangle, scalene triangle, TriRectangle"
  
  )

  shape: str = input("Write the name of the shape that you want to use: ")
  fuction: bool = True   #Ayuda al final a imprimir 
                         #los valores si se escogio una figura
  match shape:
    case "rectangle":
      print("You chose a rectangle")
      vertices = []
      for i in range(4):
        x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
        y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
        vertices.append(Point(x=x, y=y))
      my_shape = Rectangle(vertices=vertices)

    case "square":
      print("You chose a square")
      vertices = []
      for i in range(4):
        x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
        y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
        vertices.append(Point(x=x, y=y))
      my_shape = Square(vertices=vertices)

    case "triangle":
      print("You chose a triangle")
      vertices = []
      for i in range(3):
        x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
        y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
        vertices.append(Point(x=x, y=y))
      my_shape = Triangle(vertices=vertices)

    case "isosceles triangle":
      print("You chose a isosceles triangle")
      vertices = []
      for i in range(3):
        x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
        y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
        vertices.append(Point(x=x, y=y))
      my_shape = Isosceles(vertices=vertices)

    case "equilateral triangle":
      print("You chose a equilateral triangle")
      vertices = []
      for i in range(3):
        x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
        y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
        vertices.append(Point(x=x, y=y))
      my_shape = Equilateral(vertices=vertices)

    case "scalene triangle":
      print("You chose a scalene triangle")
      vertices = []
      for i in range(3):
        x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
        y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
        vertices.append(Point(x=x, y=y))
      my_shape = Scalene(vertices=vertices)

    case "TriRectangle":
      print("You chose a TriRectangle")
      vertices = []
      for i in range(3):
        x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
        y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
        vertices.append(Point(x=x, y=y))
      my_shape = TriRectangle(vertices=vertices)
  
    case _:
      print("Invalid shape")
      fuction: bool = False

if fuction:
  print("The perimeter of the shape is", my_shape.compute_perimeter())
  print("The area of the shape is", my_shape.compute_area())
  print("The inner angles of the shape are",
        my_shape.compute_inner_angles())

else:
  print("Reset the program ")
