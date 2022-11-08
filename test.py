import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_checkHorizon(self):
        board = [
            [None, '0', None],
            ['X', 'X', '0'],
            [None, None, '0']
        ]
        self.assertEqual(logic.checkHorizon(board), False)

    def test_checkRow(self):
        board = [
            [None, '0', None],
            ['X', 'X', 'X'],
            [None, None, '0']
        ]
        self.assertEqual(logic.checkRow(board), False)

    def test_checkDig(self):
        board = [
            ['X', '0', None],
            ['X', 'X', '0'],
            [None, None, 'X']
        ]
        self.assertEqual(logic.checkDig(board), True)


if __name__ == '__main__':
    unittest.main()