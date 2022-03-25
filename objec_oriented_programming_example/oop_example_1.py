

class BaseClassTotalAreaToLaminate:

    def __init__(self):
        self.depth = 3
        self.width = 4


class TotalAreaWithSquarePillar(BaseClassTotalAreaToLaminate):

    def __init__(self, square_length):
        BaseClassTotalAreaToLaminate.__init__(self)
        self.square_length = square_length

    def total_area(self):
        area_without_pillar = self.depth * self.width
        area_without_pillar = area_without_pillar - (self.square_length * self.square_length)
        return area_without_pillar


class TotalAreaWithCircularBasedPillar(BaseClassTotalAreaToLaminate):

    def __init__(self, radius):
        BaseClassTotalAreaToLaminate.__init__(self)
        self.radius = radius

    def total_area(self):
        area_without_pillar = self.depth * self.width
        area_without_pillar = area_without_pillar - (3.14 * self.radius * self.radius)
        return area_without_pillar


total = BaseClassTotalAreaToLaminate()
total_with_square_pillar = TotalAreaWithSquarePillar(1)
total_with_circular_based_pillar = TotalAreaWithCircularBasedPillar(1)

print("hello world 2")

print("total depth = " + str(total.depth))
print("total width = " + str(total.width))

print("total_with_square_pillar depth = " + str(total_with_square_pillar.depth))
print("total_with_square_pillar width = " + str(total_with_square_pillar.width))

print("total_with_square_pillar area = " + str(total_with_square_pillar.total_area()))
print("total_with_circular_based_pillar area = " + str(total_with_circular_based_pillar.total_area()))



