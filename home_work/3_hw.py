def maxnumber(a, b):
     if a > b:
         print("a")
     else:
         print("b")
maxnumber(4, 3)

def raznost(c, d):
     if c-d == 135:
         print("Yes")
     else:
         print("No")
raznost(270, 135)

def sezon(e):
    if e == 12 or e == 1 or e == 2:
        print("Зима")
    elif e in range(3, 6):
        print("Весна")
    elif e in range(6, 9):
        print("Лето")
    elif e in range(9, 12):
        print("Осень")
sezon(1)

def znaki(f, g, h):
    if f > 10 and g > 10 and h > 10:
        print ("Yes")
    else:
        print("No")

znaki(3, 7, 11)