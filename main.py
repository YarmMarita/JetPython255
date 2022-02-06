from math import *

def fig1(arg1):
    s = arg1 ** 2
    return s

def fig5(arg1):
    s = pi * (arg1 ** 2)
    return s

def main():
    n = int(input("Выберите, площадь какой фигуры вы хотите узнать?\n 1-квадрат\n 2-прямоугольник\n 3-трапеция\n 4-параллелограмм\n 5-круг\n n = "))

    if n == 1:
        a = float(input("Введите сторону квадрата = "))
        print("Площадь квадрата со стороной = ", a, "равна квадрату стороны S=a² = ", fig1(a))

    elif n == 5:
        b = float(input("Введите радиус круга = "))
        print("Площадь круга с радиусом = ", b, "равна кругу радиусом πR² = ", fig5(b))


if __name__ == '__main__':
    main()