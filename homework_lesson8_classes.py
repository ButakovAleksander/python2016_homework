# -*- coding: utf-8 -*-

'''
№8

А. 1. Есть базовый класс Фигура.
Далее есть набор фигур:
- круг
- прямоугольник
- треугольник
2. У них есть:
- точки с координатами - x и y
- толщина линии
- цвет
Создаем классы этих фигур.
3. Создаем некоторый "неслучайный" набор этих фигур (экземпляры классов).
По координатам позиционируем их так, чтобы потом когда мы научимся работать
с картинками, получилось осмысленное изображение.

Б. 4. Представим, что делаем игру роботами.
У робота есть:
- скорость бега
- сила удара + дальность удара
- уровень брони
Придумайте 3-5 типов роботов и разместите их на поле боя.
'''

import math

class Shape(object):

    description = 'This is an undefined shape.'

    def __init__(self, x=.0, y=.0):
        self.x = x
        self.y = y

    def __str__(self):

        return "{0} ({1}, {2})".format(self.__class__.__name__, self.x, self.y)


class Circle(Shape):

    def __init__(self, x=.0, y=.0, radius=0., line_width, color):
        super(Circle, self).__init__(x, y)
        self.radius = float(radius)
        self.line_width = line_width
        self.color = color

    def area(self):
        return math.pi * self.radius**2

    def get_center(self):
        return (self.x, self.y)

    def set_center(self, x, y):
        self.x = x
        self.y = y

    def set_radius(self, r):
        self.radius = r


class Rectangle(Shape):

    def __init__(self, x=.0, y=.0, z=.0, line_width, color):
        super(Rectangle, self).__init__(x, y)
        self.line_width = line_width
        self.color = color

    def area(self):
        return self.x * self.y


class Triangle(Shape):

    def __init__(self, x=.0, y=.0, line_width, color, n_sides):
        super(Triangle, self).__init__(x, y)
        self.line_width = line_width
        self.color = color

    def area(self):
        s = (self.x + self.y + self.z)/2
        return math.sqrt(s*((s-self.x)*(s-self.y)*(s-self.z)))


# create Circle object
circle = Circle(26, 42, 5.5, 2, 'green')
# create Rectangle object
rect = Rectangle(58, 32, 1, 'red')
# create Triangle object
triangle = Triangle(78, 54, 3, 'blue')

print "Circle X coordinate is:", circle.x
print "Circle Y coordinate is:", circle.y
print "Circle Radius is:", circle.radius
print circle
print "area: %.2f" % circle.area()

print rect
print "area: %.2f" % rect.area()

print triangle
print "area: %.2f" % triangle.area()
