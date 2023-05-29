#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Polinom для работы с многочленами до 100-й степени. Коэффициенты
должны быть представлены списоком из 100 элементов-коэффициентов.
Младшая степень имеет меньший индекс (нулевая степень — нулевой индекс).
Размер списка задается как аргумент конструктора инициализации.
Реализовать арифметические операции и операции сравнения, вычисление значения
полинома для заданного значения, дифференцирование, интегрирование.
"""


class Polynom:
    MAX_SIZE = 100
    def __init__(self, degree):
        # Степень полинома
        self.__degree = degree
        # Размер списка
        self.__size = degree + 1
        # Список коэффициентов
        self.__coef_list = []

    # Возвращает установленную длину
    def get_size(self):
        return self.__size

    # Получить индекс коэффициента полинома
    def get_index(self):
        print(self.__coef_list[-1])
        return self.__coef_list

    # Вывести коэффициенты полинома
    def print_coef(self):
        print(self.__coef_list)

    # Считываем значение коэффициентов
    def read_coef(self, strr=None):
        # Если на вход функции строка -> преобразуем
        if isinstance(strr, str):
            coeffs = strr.split(", ")
            if len(coeffs) <= Polynom.MAX_SIZE:
                for i in coeffs:
                    self.__coef_list.append(float(i))
        # Если на вход ничего не подано -> вводится по значению
        else:
            for i in range(self.__size):
                if self.__size <=Polynom.MAX_SIZE:
                    coef = float(input("Введите коэффициенты полинома: "))
                    self.__coef_list.append(coef)

    # Вычисление значения полинома для заданного значения x
    def count_value(self, x):
        res = []
        for idx, elem in enumerate(self.__coef_list):
            res.append(elem * x**idx)
        return sum(res)

    # Сумма двух полиномов
    def sum_polynom(self, pol_deg, index_pol2):
        if self.__degree > pol_deg:
            res_idx = [0] * self.__size
            index = 0
            for idx, elem in enumerate(index_pol2):
                res_idx[idx] = elem + self.__coef_list[idx]
                index = idx
            for index in range(index + 1, self.__size):
                res_idx[index] = self.__coef_list[index]
            return res_idx
        else:
            res_idx = [0] * (pol_deg + 1)
            index = 0
            for idx, elem in enumerate(self.__coef_list):
                res_idx[idx] = elem + index_pol2[idx]
                index = idx
            for index in range(index + 1, pol_deg + 1):
                res_idx[index] = index_pol2[index]
            return res_idx

    # Разность двух полиномов
    def sub_polynom(self, pol_deg, index_pol2):
        for idx in range(len(index_pol2)):
            index_pol2[idx] *= -1
        res = self.sum_polynom(pol_deg, index_pol2)
        return res

    # Произведение двух полиномов
    def multiply_pol(self, pol_deg, index_pol2):
        res_idx = [0] * (self.__degree + pol_deg + 1)
        for idx1, elem1 in enumerate(self.__coef_list):
            for idx2, elem2 in enumerate(index_pol2):
                res_idx[idx1 + idx2] += elem1 * elem2
        return res_idx

    # Умножение полиноса на число (всех его коэффициентов)
    def multiply_pol_num(self, num):
        for idx in range(len(self.__coef_list)):
            self.__coef_list[idx] *= num
        return self.__coef_list

    # Проверка. Полиномы равны.
    def __eq__(self, val_pol2):
        if isinstance(val_pol2, Polynom):
            if self.__coef_list == val_pol2.__coef_list:
                return True
            else:
                return False

    # Проверка. Полином больше чем заданный
    def __gt__(self, val_pol2):
        if isinstance(val_pol2, Polynom):
            if self.__coef_list > val_pol2.__coef_list:
                return True
            else:
                return False

    # Проверка. Полином меньше чем заданный
    def __lt__(self, val_pol2):
        if self.__coef_list <= val_pol2.__coef_list:
            return True
        else:
            return False

    # Проверка. Полином не равен другому.
    def __ne__(self, val_pol2):
        if not self.__coef_list == val_pol2.__coef_list:
            return True
        else:
            return False

    # Дифференцирование полинома
    def differentiation(self):
        res = []
        for idx, elem in enumerate(self.__coef_list):
            if idx > 0:
                res.append(elem * idx)
        return res

    # Интегрирование полинома
    def integrate(self):
        res = [0] * (self.__size + 1)
        for idx, elem in enumerate(self.__coef_list):
            res[idx + 1] = elem / (idx + 1)
        return res

    # Получить конкретный коэффициент полинома
    def __getitem__(self, item):
        return self.__coef_list[item]


if __name__ == "__main__":
    pol1 = Polynom(3)
    pol1.print_coef()
    pol1.read_coef()
    pol1.print_coef()
    pol2 = Polynom(3)
    pol2.print_coef()
    pol2.read_coef("1, 3, 4, 4")
    pol2.print_coef()

    print(f"Сумма: {pol1.sum_polynom(3, pol2.get_index())}")
    print(f"Разность: {pol1.sub_polynom(3, pol2.get_index())}")
    print(f"Произведение: {pol1.multiply_pol(3, pol2.get_index())}")
    # print(f"Полином 1, умноженный на 2: {pol1.multiply_pol_num(2)}")
    print(f"pol1 == pol2: {pol1 == pol2}")
    print(f"pol1 > pol2: {pol1 > pol2}")
    print(f"pol1 < pol2: {pol1 < pol2}")
    print(f"pol1 != pol2: {pol1 != pol2}")
    print(f"Дифференцирование полинома 1: {pol1.differentiation()}")
    print(f"Интегрирование полинома 1: {pol1.integrate()}")
