from classes_.Shapes.Shape import Shape
#type: ignore

class Rectangle(Shape):
# más tarde meto formulas
  def __init__(self, vertices: list):
    super().__init__(vertices)

  def compute_area(self):
      side1_length = self.get_edges()[0].length()
      side2_length = self.get_edges()[1].length()
      return side1_length * side2_length
  def compute_perimeter(self):
      perimeter = 0
      for line in self.get_edges():
          perimeter += line.length()
      return perimeter
  def compute_inner_angles(self):
    return [90, 90, 90, 90]

