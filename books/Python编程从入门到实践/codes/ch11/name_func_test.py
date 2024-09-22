# name_func_test.py

import unittest
from name_func import get_formatted_name


# 继承 unittest.TestCase
class NamesTestCase(unittest.TestCase):
    """test name_func.py"""

    # 测试函数以 test 开头
    def test_first_last_name(self):
        formatted_name = get_formatted_name("j", "k")
        self.assertEqual(formatted_name, "j k")


# 执行单元测试
unittest.main()
