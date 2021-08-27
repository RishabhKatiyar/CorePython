import unittest
from src.Models.Query import Query


class TestQuery(unittest.TestCase):

    def test_empty_query(self):
        query = Query()
        self.assertEqual(query.Command, None)
        self.assertEqual(query.StartTime, None)
        self.assertEqual(query.EndTime, None)
        self.assertEqual(query.PersonCapacity, 0)
        self.assertEqual(query.Reason, None)

    def test_populated_query(self):
        query = Query()
        query.Command = "Book"
        query.StartTime = "12:00"
        query.EndTime = "13:00"
        query.PersonCapacity = 4
        query.Reason = "Test Reason"
        self.assertEqual(query.Command, "Book")
        self.assertEqual(query.StartTime, "12:00")
        self.assertEqual(query.EndTime, "13:00")
        self.assertEqual(query.PersonCapacity, 4)
        self.assertEqual(query.Reason, "Test Reason")


if __name__ == '__main__':
    unittest.main()

