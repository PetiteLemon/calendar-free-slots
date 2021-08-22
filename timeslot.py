import dateutil.parser
import datetime


class TimeSlot:
	def __init__(self, star_time, end_time, name=""):
		self.startTime = self._timeObject(star_time)
		self.endTime = self._timeObject(end_time)
		self.name = name

	def toDict(self):
		return {
			'startTime': self.startTime.isoformat(),
			'endTime': self.endTime.isoformat()}

	def __lt__(self, other):
		return self.startTime < other.startTime

	def __repr__(self):
		return f"{self.startTime.strftime('%d/%m/%Y %H:%M')}-{self.endTime.strftime('%d/%m/%Y %H:%M')} {self.name}"

	def _timeObject(self, i):
		if type(i) is datetime.datetime:
			return i
		if type(i) is str:
			return dateutil.parser.isoparse(i)
		raise Exception("TimeSlot supports parsing fom datetime or ISO-str")
