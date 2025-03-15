def task_1(int, float, str, list, bool) -> int :
int = 1
float = 1,1
str = 'ДЗ'
list = [1, 2, 3]
bool = True

print( int, "Относится к типу, type(int)")
print(float, "Относится к типу, type(float)")
print(str, "Относится к типу, type(str)")
print(list, "Относится к типу, type(list)")
print(bool, "Относится к типу, type(bool)")
task_1(int, float, str, list, bool)



def task_2(a = [1, 2, 3, 5, 8, 13, 21]) -> int :
print("Первые три значения списка:", a[0:3])
print (task_2())


def task_3(a: int) -> int:
return a ** 2
print(task_3(7))

