from math import *

def fig1(arg1):
    s = arg1 ** 2
    return s
  
def fig3(arg1, arg2, arg3):
    s = arg3*(arg1+arg1)/2
    return s

def fig4(arg1, arg2):
    s = arg1 * arg2
    return s

def fig5(arg1):
    s = pi * (arg1 ** 2)
    return s

def main():
    n = int(input("Выберите, площадь какой фигуры вы хотите узнать?\n 1-квадрат\n 2-прямоугольник\n 3-трапеция\n 4-параллелограмм\n 5-круг\n n = "))

    if n == 1:
        a = float(input("Введите сторону квадрата = "))
        print("Площадь квадрата со стороной = ", a, "равна квадрату стороны S=a² = ", fig1(a))

    if n == 3:
        a = float(input("введите сторону трапеции a="))
        b = float(input("введите сторону трапеции b="))
        h = float(input("введите сторону трапеции h="))
        print("площадь трапеции со сторонами a=", a, "b=", b, "h=", h, "равна ", fig3(h*(a+b)/2))

    if n == 4:
        a = float(input("Введите сторону параллелограмма а = "))
        h = float(input("Введите высоту параллелограмма = "))
        print("Площадь параллелограмма со стороной а = ", a, "и высотой = ", h, "равна S=ah = ", fig4(a, h))

    if n == 5:
        a = float(input("Введите радиус круга = "))
        print("Площадь круга с радиусом = ", a, "равна кругу радиусом πR² = ", fig5(a))


if __name__ == '__main__':
    main()