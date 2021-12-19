# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    x = set(input("Введите первую строку: "))
    y = set(input("Введите вторую строку: "))
    common_letters = x.intersection(y)
    print(', '.join(common_letters))