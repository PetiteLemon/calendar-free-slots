import pytz
import heapq
import datetime
from timeslot import TimeSlot


class DataContainer:
	def __init__(self, raw):
		self._parse_meetings(raw)
		self._fake_meeting_for_last_free_slot()

	def first_free_slot_start_time(self):
		return datetime.datetime(self.first_day.year, self.first_day.month, self.first_day.day, 0, 0, 0, 0, tzinfo=pytz.UTC)

	def next_meeting(self):
		return heapq.heappop(self._meetings)

	def has_more_meetings(self):
		return self._meetings != []

	def _parse_meetings(self, raw_data):
		self._meetings = [TimeSlot(m["startTime"], m["endTime"], m["subject"]) for calendar in raw_data for m in calendar["meetings"]]
		self._keep_first_and_last_day()
		heapq.heapify(self._meetings)

	def _keep_first_and_last_day(self):
		self.first_day = heapq.nsmallest(1, self._meetings)[0].startTime
		self.last_day = heapq.nlargest(1, self._meetings)[0].endTime

	def _fake_meeting_for_last_free_slot(self):
		last_moment = datetime.datetime(self.last_day.year, self.last_day.month, self.last_day.day, 23, 59, 59, 0, tzinfo=pytz.UTC)
		self._meetings.append(TimeSlot(last_moment, last_moment))
		heapq.heappush(self._meetings, TimeSlot(last_moment, last_moment))


