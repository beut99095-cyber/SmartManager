def say_shynakov():
    print("shynakov")


def print_to_three():
    print(1)
    print(2)
    print(3)


def multiplication_table_bu_2():
    for i in range(1, 11):
        result = i * 2
        print(f"{i} * 2 = {result}")


def print_square(number):
    result = number ** 2
    print(f"m2 {number} = {result}")


def print_max(a, b):
    if a > b:
        print(f"{a} > {b}")
    elif b > a:
        print(f"{b} > {a}")
    else:
        print(f"{a} и {b} =")


def check_age(age):
    if age >= 18:
        print("adult (of legal age)")
    else:
        print("minor")


say_shynakov()
print_to_three()
multiplication_table_bu_2()
print_square(5)

\\\\
print_max(10, 20)
check_age(19)
print("Изменино на GitHub")









print('Это именная ветка shynakov')
