def max_of_two_numbers(a, b):
     if a > b:
         print("a")
     else:
         print("b")
max_of_two_numbers(4, 3)

def  check_difference(c, d):
     if (c-d) == 135 or c-d == -135:
         print("Yes")
     else:
         print("No")

check_difference(135, 270)

def season_by_month(month_number):
    if month_number == 12 or month_number == 1 or month_number == 2:
        print("Зима")
    elif month_number in range(3, 6):
        print("Весна")
    elif month_number in range(6, 9):
        print("Лето")
    elif month_number in range(9, 12):
        print("Осень")
season_by_month(1)

def check_all_greater(f, g, h):
    if f > 10 and g > 10 and h > 10:
        print ("Yes")
    else:
        print("No")

check_all_greater(3, 7, 11)

