from unittest import TestCase
from Course import *

class TestCourse(TestCase):
    def setUp(self):
        print("setUp")
        self.course=Course(1,"QA",20)

    def tearDown(self):
        print("tearDown")

    def test__init_true(self):
        self.course = Course(1, "QA", 20)

    def test__init_false(self):
        with self.assertRaises(Exception) as context:
            self.course = Course("slon", 345,"45")
        with self.assertRaises(Exception) as context:
            self.course = Course(1, "QA", [1,2])

    def test_add_studentTrue(self):
        self.course.add_student(Student(123, "gal", {}))

    def test_add_studentFalse1(self):
        self.course.student_list=[Student(123, "gal", {}),Student(432, "tal", {})]
        self.assertFalse(self.course.add_student(Student(123, "saal", {})))

    def test_add_studentFalse2(self):
        self.assertFalse(self.course.add_student("galgal"))
        self.assertFalse(self.course.add_student(123))

    def test_add_factorTrue(self):
        self.course.subject_teacher={"Testing":"moshe"}
        self.course.add_factor("Testing",5)

    def test_add_factorFalse1(self):
        self.course.subject_teacher={"Testing":"moshe"}
        with self.assertRaises(Exception) as context:
            self.course.add_factor("painting",5)

    def test_add_factorFalse2(self):
        with self.assertRaises(Exception) as context:
            self.course.add_factor(1,5)
        with self.assertRaises(Exception) as context:
            self.course.add_factor("Testing","math")


    def test_del_studentTrue(self):
        self.course.add_student(Student(123, "gal", {}))
        self.course.del_student(123)
        self.assertEqual(self.course.student_list,[])

    def test_del_studentFalse1(self):
        self.course.add_student(Student(123, "gal", {}))
        self.assertFalse(self.course.del_student(345))
        self.assertEqual(self.course.student_list,[Student(123, "gal", {})])

    def test_del_studentFalse2(self):
        self.course.add_student(Student(123, "gal", {}))
        self.assertFalse(self.course.del_student("king"))
        self.assertEqual(self.course.student_list,[Student(123, "gal", {})])

