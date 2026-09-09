def f(x):
    return x**3 - x - 2
def main():
    a = 1.0
    b = 2.0
    eps = 0.0001
    if f(a) * f(b) >= 0:
        print("Ошибка: на концах отрезка функция должна иметь разные знаки")
        return
    while (b - a) / 2.0 > eps:
        c = (a + b) / 2.0
        if f(c) == 0.0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    root = (a + b) / 2.0
    print(f"Корень уравнения: {root:.5f}")
if __name__ == "__main__":
    main()
