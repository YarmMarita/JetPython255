def fig2(arg1, arg2):
    s = arg1 * arg2
    return s

def main():
    n = int(input("Выберите, площадь какой фигуры вы хотите узнать?\n 1-квадрат\n 2-прямоугольник\n 3-трапеция\n 4-параллелограмм\n 5-круг\n n = "))

    if n == 2:
        a = float(input("Введите сторону прямоугольника a = "))
        b = float(input("Введите сторону прямоугольника b = "))
        print("Площадь прямоугольника со стороной а =", a, "и стороной b =", b, "равна S=ab =", fig2(a, b))

if __name__ == '__main__':
    main()