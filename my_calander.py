class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for event in self.calendar:
            if start < event[1] and end > event[0]:
                return False

        self.calendar.append((start, end))
        return True


