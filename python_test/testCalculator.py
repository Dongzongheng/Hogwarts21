#! /usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from python_code.Calculator import Calculator

calc = Calculator()
class TestCalculator:
    def setup(self):
        print('开始计算')
    def teardown(self):
        print('结束计算')
    def teardown_class(self):
        print('结束测试')
    def test_add_001(self):
        a = calc.add(1,1)
        assert a == 2
    def test_add_002(self):
        a = calc.add(-0.01,0.02)
        assert a == 0.01
    def test_add_003(self):
        a = calc.add(10,0.02)
        assert a == 10.02
    def test_add_004(self):
        a = calc.add(98.99,99)
        assert a == 197.99
    def test_add_005(self):
        a = calc.add(99,98.99)
        assert a == 197.99
    def test_add_006(self):
        a = calc.add(-98.99,-99)
        assert a == -197.99
    def test_add_007(self):
        a = calc.add(-99,-98.99)
        assert a == -197.99
    def test_add_008(self):
        a = calc.add(-99.01,0)
        print('参数大小超出范围')