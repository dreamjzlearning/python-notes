# survey_test.py

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    # 执行测试时，先执行 setUp，再执行测试函数
    def setUp(self):
        question = "What is your favorite number?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = [1, 2, 3]

    def test_store_single_response(self):
        question = "What is the result of 1+2 ?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response(3)

        self.assertIn(3, my_survey.responses)


unittest.main()
