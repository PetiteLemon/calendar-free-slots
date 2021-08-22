from timeslot import TimeSlot
from datacontainer import DataContainer


class SlotFinder:
    def __init__(self, raw_data):
        self.data = DataContainer(raw_data)
        self.free_slots = []
        self._find()

    def result(self):
        return [f.toDict() for f in self.free_slots]

    def humane_readable_result(self):
        return self.free_slots

    def _find(self):
        self._free_slot_start_time = self.data.first_free_slot_start_time()
        while self.data.has_more_meetings():
            next_meeting = self.data.next_meeting()
            if self._free_slot_start_time < next_meeting.startTime:
                self.free_slots.append(TimeSlot(self._free_slot_start_time, next_meeting.startTime))
                self._free_slot_start_time = next_meeting.endTime
            else:
                self._free_slot_start_time = max(self._free_slot_start_time, next_meeting.endTime)
