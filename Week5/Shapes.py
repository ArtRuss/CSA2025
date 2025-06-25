import math

class GeoShapes:
    def __init__(self, sides):
        self.sides = sides
    def getNumSides(self):
        return self.sides
    
class TwoDimensional(GeoShapes):
    def __init__(self, sides, perim, area):
        GeoShapes.__init__(self, sides)
        self.perim = perim
        self.area = area
    def getPerim(self):
        return self.perim
    def getArea(self):
        return self.area
    
class ThreeDimensional(GeoShapes):
    def __init__(self, sides, surface_area, volume):
        GeoShapes.__init__(self, sides)
        self.surface_area = surface_area
        self.volume = volume
    def getSurfaceArea(self):
        return self.surface_area
    def getVolume(self):
        return self.volume

class EquilateralTriangle(TwoDimensional):
    def __init__(self, sideLength):
        self.sideLength = sideLength
        sides = 3
        area = math.sqrt(3) / 4 * sideLength ** 2
        perim = sideLength * 3
        TwoDimensional.__init__(self, sides, perim, area)

class Cube(ThreeDimensional):
    def __init__(self, sideLength):
        self.sideLength = sideLength
        sides = 6
        volume = sideLength ** 3
        surface_area = sideLength ** 2 * sides
        ThreeDimensional.__init__(self, sides, surface_area, volume)

# Test the classes
if __name__ == "__main__":
    triangle = EquilateralTriangle(5)
    print(f"Equilateral Triangle: Sides = {triangle.getNumSides()}, Perimeter = {triangle.getPerim()}, Area = {triangle.getArea()}")

    cube = Cube(3)
    print(f"Cube: Sides = {cube.getNumSides()}, Surface Area = {cube.getSurfaceArea()}, Volume = {cube.getVolume()}")