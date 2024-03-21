from classes_.Shapes.Shape import Shape
#type: ignore

class Triangle(Shape):

  def __init__(self, vertices: list):
    super().__init__(vertices)

  def compute_area(self):
    pass

  def compute_perimeter(self):
    pass
