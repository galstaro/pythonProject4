from Lottery import *
from unittest import TestCase, mock
from unittest.mock import patch

class TestLottery(TestCase):
    def setUp(self):
        print("setUp")
        self.lottery=Lottery()

    def test_rand_numbers(self):
        rand=self.lottery.rand_numbers()
        print(rand)
        self.assertNotEqual(rand,[])

    # using mock as a decorator
    @mock.patch('Lottery.Lottery.rand_numbers', return_value=[10, 31, 11, 20, 67, 20])
    def test_valid_numbers_False(self, mock_rand_numbers):
        # tests a case in which a number is duplicated
        self.assertFalse(self.lottery.valid_numbers())
        print(self.lottery.numbers)

    @mock.patch('Lottery.Lottery.rand_numbers', return_value=[10, 31, 11, 40, 67, 20])
    def test_valid_numbers_True(self, mock_rand_numbers):
        # tests a case in which a number is duplicated
        self.assertTrue(self.lottery.valid_numbers())
        print(self.lottery.numbers)

    def test_valid_numbers(self):
        vali= self.lottery.valid_numbers()
        self.assertTrue(vali)


    def test_valid_range_out_of_range(self):
        #using mock as a context manager
        with patch('Lottery.Lottery.rand_numbers') as mock_rand_num:
            mock_rand_num.return_value=[0,31,11,12,12,20]
            print("out of range values",mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_range())
            mock_rand_num.return_value = [46, 31, 11, 12, 12, 20]
            print("out of range values", mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_range())



    def test_valid_range(self):
        vail_range=self.lottery.valid_range()
        self.assertTrue(vail_range)

    def tearDown(self):
        print("tearDown")