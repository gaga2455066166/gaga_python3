import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return math.pi * self.get_radius() * self.get_radius()


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def get_area(self):
        return super().get_area() * 2 + self.radius * self.height * 2 * math.pi

    def get_volume(self):
        return super().get_area() * self.height

    def __str__(self):
        return 'BasalArea:{:.3f}\nSupfaceArea:{:.3f}\nVolume:{:.3f}' \
            .format(super().get_area(), self.get_area(), self.get_volume())


if __name__ == '__main__':
    r, h = map(float, input().split())
    cy = Cylinder(r, h)
    print(cy)
