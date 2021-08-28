import unittest
from src.Validators.InputValidator import InputValidator
from src.Service.MakeSpaceService import MakeSpaceService


class TestMakeSpaceService(unittest.TestCase):
    def setUp(self) -> None:
        self.makeSpaceService = MakeSpaceService()

    def test_successful_booking(self):
        _input = InputValidator("BOOK 09:30 13:15 2")
        response = self.makeSpaceService.ExecuteRequest(_input.Query)
        self.assertEqual(response, "C-Cave")

        _input = InputValidator("BOOK 09:30 13:15 2")
        response = self.makeSpaceService.ExecuteRequest(_input.Query)
        self.assertEqual(response, "D-Tower")

    def test_unsuccessful_booking_done_in_buffer_time(self):
        _input = InputValidator("BOOK 09:00 13:15 2")
        response = self.makeSpaceService.ExecuteRequest(_input.Query)
        self.assertEqual(response, "NO_VACANT_ROOM")

    def test_unsuccessful_booking_no_room_with_enough_capacity(self):
        _input = InputValidator("BOOK 09:00 13:15 100")
        response = self.makeSpaceService.ExecuteRequest(_input.Query)
        self.assertEqual(response, "NO_VACANT_ROOM")
        
    def test_vacancy(self):
        _input = InputValidator("VACANCY 09:30 13:15")
        response = self.makeSpaceService.ExecuteRequest(_input.Query)
        self.assertEqual(response, "C-Cave D-Tower G-Mansion")

    def test_vacancy_no_room_in_buffer_time(self):
        _input = InputValidator("VACANCY 09:00 13:15")
        response = self.makeSpaceService.ExecuteRequest(_input.Query)
        self.assertEqual(response, "NO_VACANT_ROOM")

        
if __name__ == '__main__':
    unittest.main()