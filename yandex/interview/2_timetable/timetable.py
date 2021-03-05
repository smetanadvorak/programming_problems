
import bisect

class Meeting:
	def __init__(self, day, hour, minute, duration, participants):
		self.day, self.hour, self.minute, self.duration, self.participants = \
			 day,      hour,      minute,      duration,      participants
		self.start = (24 * self.day + self.hour) * 60 + self.minute
		self.finish = self.start + self.duration


class Timetable:
	def __init__(self):
		self.appointments = []

	def check_appointment(self, new_appointment):
		flag = True
		for a in self.appointments:
			# Check if new appointment is conflicting in time with an existing one :
			if a.start < new_appointment.finish and new_appointment.start < a.finish:
				if not set(a.participants).isdisjoint(set(new_appointment.participants)):
					flag = False
		return flag

	def add_appointment(self, new_appointment):
		if self.check_appointment(new_appointment):
			chronological_position = bisect.bisect([a.start for a in self.appointments], new_appointment.start)
			self.appointments.insert(chronological_position, new_appointment)
			return True
		else:
			return False

	def get_appointments(self, day, name):
		relevant_appointments = [a for a in self.appointments if a.day == day and name in set(a.participants)]
		return relevant_appointments

timetable = Timetable()

with open('input.txt', 'r') as f:
	n = int(f.readline())
	appointments = []
	for i in range(n):
		request = list(f.readline().split())
		if request[0] == 'APPOINT':
			new_appointment = Meeting(int(request[1]), int(request[2][0:2]), int(request[2][3:5]), int(request[3]), request[4:])
			if timetable.add_appointment(new_appointment):
				print('OK')
			else:
				print('FAIL')


		if request[0] == 'PRINT':
			day, name = int(request[1]), request[2]
			relevant_appointments = timetable.get_appointments(day, name)
			for a in relevant_appointments:
				print('%d:%d %d %s' % (a.hour, a.minute, a.duration, ' '.join(a.participants)))
