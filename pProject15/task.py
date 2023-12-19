#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func_show(inner_func):
    def wrapper(*args, **kwargs):
        result = inner_func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        return result
    return wrapper


@func_show
def get_sq(width, height):
    return width * height


if __name__ == "__main__":
    try:
        width = float(input("Введите ширину прямоугольника: "))
        height = float(input("Введите высоту прямоугольника: "))

        get_sq(width, height)

    except ValueError:
        print("Ошибка: Введите числовые значения для ширины и высоты.")
