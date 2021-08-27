import unittest
from src.Validators.InputValidator import InputValidator
from src.Service.MeetingRoomFactory import MeetingRoomFactory
from src.Service.BookingService import BookingService
from src.Service.VacancyService import VacancyService


class TestServices(unittest.TestCase):
    def setUp(self) -> None:
        self.meetingRooms = MeetingRoomFactory().CreateMeetingRooms()
    
        self.bookingService = BookingService()
        self.vacancyService = VacancyService()

    def test_successful_booking(self):
        _input = InputValidator("BOOK 09:30 13:15 2")
        result = self.bookingService.BookRoom(_input.Query, self.meetingRooms)
        self.assertTrue(result)
        self.assertEqual(self.bookingService.Result, "C-Cave")

        _input = InputValidator("BOOK 09:30 13:15 2")
        result = self.bookingService.BookRoom(_input.Query, self.meetingRooms)
        self.assertTrue(result)
        self.assertEqual(self.bookingService.Result, "D-Tower")

    def test_unsuccessful_booking_done_in_buffer_time(self):
        _input = InputValidator("BOOK 09:00 13:15 2")
        result = self.bookingService.BookRoom(_input.Query, self.meetingRooms)
        self.assertFalse(result)
        self.assertEqual(self.bookingService.Result, "")

    def test_unsuccessful_booking_no_room_with_enough_capacity(self):
        _input = InputValidator("BOOK 09:00 13:15 100")
        result = self.bookingService.BookRoom(_input.Query, self.meetingRooms)
        self.assertFalse(result)
        self.assertEqual(self.bookingService.Result, "")
        
    def test_vacancy(self):
        _input = InputValidator("VACANCY 09:30 13:15")
        result = self.vacancyService.GetVacancy(_input.Query, self.meetingRooms)
        self.assertTrue(result)
        self.assertEqual(self.vacancyService.Result, "C-Cave D-Tower G-Mansion")

    def test_vacancy_no_room_in_buffer_time(self):
        _input = InputValidator("VACANCY 09:00 13:15")
        result = self.vacancyService.GetVacancy(_input.Query, self.meetingRooms)
        self.assertFalse(result)
        self.assertEqual(self.vacancyService.Result, "")

        
if __name__ == '__main__':
    unittest.main()