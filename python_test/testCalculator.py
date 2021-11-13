#! /usr/bin/python
# -*- coding: utf-8 -*-
from decimal import Decimal

import pytest
import yaml
from python_code.Calculator import Calculator

# 读取yaml文件
# def get_datas(name,type):
#     with open("././datas/data.yml") as f:
#         # pip install pyyaml
#         datas = yaml.safe_load(f)
#         print(datas)



class TestCalc:
    def setup(self):
        self.calc = Calculator()
        print('开始计算')

    def teardown(self):
        print('结束计算')

    def teardown_class(self):
        print('结束测试')

    @pytest.mark.parametrize("a, b, expected",
                             [[1,1,2],[-0.01,0.02,0.01],[10,0.02,10.02]],
                             ids=["forward1","forward2","forward3"])
    def test_case1_add(self, a, b, expected):
        assert expected == self.calc.add(a,b)

    @pytest.mark.parametrize("a, b, expected",
                             [[98.99, 99, 197.99], [99, 98.99, 197.99], [-98.99, -99, -197.99], [-99, -98.99, -197.99]],
                             ids=["validbignum1", "validbignum2", "validbignum3","validbignum4"])
    def test_case2_add(self, a, b, expected):
        assert expected == self.calc.add(a, b)

    @pytest.mark.parametrize("a, b, expected",
                             [[99.01, 0, '参数大小超出范围'], [-99.01, -1, '参数大小超出范围'], [2, 99.01, '参数大小超出范围'], [1, -99.01, '参数大小超出范围']],
                             ids=["invalidbignum1", "invalidbignum2", "invalidbignum3", "invalidbignum4"])
    def test_case3_add(self, a, b, expected):
        assert expected == self.calc.add(a, b)

    @pytest.mark.parametrize("a, b, errortype", [['文', 9.3, 'TypeError'], [4, '字', 'TypeError']], ids=['specialStr1', 'specialStr2'])
    def test_case4_add(self, a, b, errortype):
        with pytest.raises(eval(errortype)) as e:
            self.calc.add(a, b)