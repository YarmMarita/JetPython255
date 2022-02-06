# Это пример программы рассчета площадей фигур"

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def fig1(arg1):
    s = arg1*arg1 # здесь, вместо 0, пишется формула вычисления площади фигуры fig1 при значениях аргументов arg1, arg2...
    return s

def fig3(arg1, arg2, arg3):
    s = arg3*(arg1+arg1)/2
    return s

def main():
    n = int(input("Выберите, площадь какой фигуры вы хотите узнать?\n 1-квадрат\n 2-прямоугольник\n 3-трапеция\n 4-параллелограмм\n 5-круг\n n="))

    if (n == 1):
        a = float(input("введите сторону квадрата a="))
        print("площадь квадрата со стороной a=", a, "равна квадрату стороны s=a*a=", fig1(a))

    if (n == 3):
        a = float(input("введите сторону трапеции a="))
        b = float(input("введите сторону трапеции b="))
        h = float(input("введите сторону трапеции h="))
        print("площадь трапеции со сторонами a=", a, "b=", b, "h=", h, "равна ", fig3(h*(a+b)/2))


# Нажмите зеленую кнопку для выполнения программы
if __name__ == '__main__':
    main()

# Смотрите помощь по PyCharm help at https://www.jetbrains.com/help/pycharm/