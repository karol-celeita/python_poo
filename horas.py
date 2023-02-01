#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator
from functools import total_ordering, wraps


def _time_required(f):
    @wraps(f)
    def wrapper(self, other):
        if not isinstance(other, Time):
            raise TypeError("Can only operate on Time objects.")
        return f(self, other)

    return wrapper


def _int_required(f):
    @wraps(f)
    def wrapper(self, value):
        if not isinstance(value, int):
            raise TypeError("An integer is required.")
        return f(self, value)

    return wrapper


def _balance(a, b):
    if b >= 0:
        while b >= 60:
            a += 1
            b -= 60
    elif b < 0:
        while b < 0:
            a -= 1
            b += 60
    return a, b


@total_ordering
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property
    def h(self):
        return self._h

    @h.setter
    @_int_required
    def h(self, value):
        self._h = value

    @property
    def m(self):
        return self._m

    @m.setter
    @_int_required
    def m(self, value):
        self._m = value
        self._h, self._m = _balance(self._h, self._m)

    @property
    def s(self):
        return self._s

    @s.setter
    @_int_required
    def s(self, value):
        self._s = value
        self._m, self._s = _balance(self._m, self._s)

    def _operation(self, other, method):
        h = method(self.h, other.h)
        m = method(self.m, other.m)
        s = method(self.s, other.s)
        return Time(h, m, s)

    @_time_required
    def __add__(self, other):
        return self._operation(other, operator.add)

    @_time_required
    def __sub__(self, other):
        return self._operation(other, operator.sub)

    @_time_required
    def __eq__(self, other):
        return self.h == other.h and self.m == other.m and self.s == other.s

    @_time_required
    def __lt__(self, other):
        if self.h < other.h:
            return True
        if self.h > other.h:
            return False
        if self.m < other.m:
            return True
        if self.m > other.m:
            return False
        return self.s < other.s

    def __repr__(self):
        return f"<Time {self.h:02}:{self.m:02}:{self.s:02}>"
