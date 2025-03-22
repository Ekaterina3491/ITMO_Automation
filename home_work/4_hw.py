#1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def square (self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width+ self.height)

Rect1 = Rectangle (5, 4)
Rect2 = Rectangle (3,1)
Rect3 = Rectangle (9,10)

print(f"Площадь 1 прямоугольника: {Rect1.square()}")
print(f"Периметр 1 прямоугольника: {Rect1.perimeter()}")

print(f"Площадь 2 прямоугольника: {Rect2.square()}")
print(f"Периметр 2 прямоугольника: {Rect2.perimeter()}")

print(f"Площадь 3 прямоугольника: {Rect3.square()}")
print(f"Периметр 3 прямоугольника: {Rect3.perimeter()}")

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

math1 = Math (2, 7)
print(math1.addition())
print(math1.multiplication())
print(math1.division())
print(math1.subtraction())

class Buttons:
        def __init__(self, text, loc=None):
            self.text = text

        def click(self):
            return f"Клик по кнопке  {self.text}"

text_box = Buttons('Text Box')
check_box = Buttons('Check box')
radio_button = Buttons('Radio button')
web_tables = Buttons('Web tables')
buttons = Buttons('Buttons')
links = Buttons('Links')
broken_links_images = Buttons('Broken links-Images')
upload_and_download = Buttons('Upload and Download')
dynamic_properties = Buttons('Dynamic properties')

print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(broken_links_images.click())
print(upload_and_download.click())
print(dynamic_properties.click())