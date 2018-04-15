# -*- coding: utf-8 -*-
import numpy as np


class Ackley:
    def __init__(self):
        self.x_min = -5
        self.x_max = 5

    def func(self, *x):
        x = np.array(x)
        mean1 = np.mean(np.square(x))
        mean2 = np.mean(np.cos(2 * np.pi * x))
        result = -20 * np.exp(-0.2 * np.sqrt(mean1)) - np.exp(mean2) + 20 + np.e
        return -result


class Griewank:
    def __init__(self):
        self.x_min = -600
        self.x_max = 600

    def func(self, *x):
        x = np.array(x)
        first = np.sum(np.square(x)) / 4000
        second = 1
        for i in range(x.shape[0]):
            second *= np.cos(x[i] / np.sqrt(i + 1))
        result = first - second + 1
        return -result


class Rastrigin:
    def __init__(self):
        self.x_min = -5.12
        self.x_max = 5.12

    def func(self, *x):
        x = np.array(x)
        sum = np.sum(np.square(x) - 10 * np.cos(2 * np.pi * x))
        result = 10 * x.shape[0] + sum
        return -result


class Rosenbrock:
    def __init__(self):
        self.x_min = -100
        self.x_max = 100

    def func(self, x1, x2):
        result = np.square(1 - x1) + 100 * np.square(x2 - np.square(x1))
        return -result


class Schwefel:
    def __init__(self):
        self.x_min = 0
        self.x_max = 500

    def func(self, *x):
        x = np.array(x)
        sum = np.sum(x * np.sin(np.sqrt(np.abs(x))))
        result = 418.9829 * x.shape[0] - sum
        return -result