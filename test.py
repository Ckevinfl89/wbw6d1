from unittest import TestCase, main

from whiteboard import solution


class MatchTestCase_Twosum(TestCase):
    def test_example_one(self):
        self.assertEqual(solution([2,7,11,15],9),[0,1])
    def test_example_two(self):
        self.assertEqual(solution([2,3,4],6),[0,2])
    def test_neg(self):
        self.assertEqual(solution([-1,0], -1),[0,1])
    def test_multiple(self):
        self.assertEqual(solution([0,0,1,2,2,5],4), [3,4])