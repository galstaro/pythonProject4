from unittest import TestCase
from Student import *

class TestStudent(TestCase):
    def setUp(self):
        print("setUp")
        self.student=Student(123,"gal",dict({}))

    def tearDown(self):
        print("tearDown")

    def test__init__true(self):
        self.student = Student(123, "gal", {})

    def test__init__false(self):
       with self.assertRaises(Exception) as context:
           Student([123,1], 12, "moshe")

       with self.assertRaises(Exception) as context:
            Student(1345, "moshe1", {})

    # check case of try insert wrong arguments to function
    def test_add_grade_False(self):
        self.assertFalse(self.student.add_grade(1,"udhfuh"))
        self.assertFalse(self.student.add_grade("sdhfhff","fjffnjf"))
        self.assertFalse(self.student.add_grade(["sdhfhff",1], 88))

    # check case of try insert right arguments to function
    def test_add_grade_True(self):
        self.student.add_grade("computer", 89)
        self.assertDictEqual({"computer": 89}, self.student.subject_grade)

    def test_calc_factorTrue(self):
        self.student.subject_grade={"computer":89,"math":77,"english":69}
        self.student.calc_factor("math",10)
        self.assertDictEqual({"computer":89,"math":85,"english":69}, self.student.subject_grade)
        self.student.subject_grade = {"computer": 89, "math": 97, "english": 69}
        self.student.calc_factor("math", 10)
        self.assertDictEqual({"computer": 89, "math": 100, "english": 69}, self.student.subject_grade)

    def test_calc_factorFalse(self):
        self.student.subject_grade={"computer":89,"math":77,"english":69}
        self.assertFalse(self.student.calc_factor(1,1))
        self.assertFalse(self.student.calc_factor("computer","computer"))
        self.assertFalse(self.student.calc_factor("art",10))
        self.assertDictEqual({"computer":89,"math":77,"english":69}, self.student.subject_grade)

    def test_averageTrue(self):
        self.student.subject_grade = {"computer": 100, "math": 80, "english": 60}
        self.assertEqual(80,self.student.average())

    def test_averageFalse(self):
        self.assertFalse(self.student.average())
