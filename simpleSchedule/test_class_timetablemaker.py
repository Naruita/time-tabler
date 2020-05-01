import pickle

class day_timetable:
    def __init__(self, day):
        self.day = day
        self.time_table = {}

    def get_info(self):
        self.in_time = input("Enter time in HHMM format : ")
        self.course_code = input("Enter the course code : ")
        self.links = []
        print("Add links now. Type 'quit' to stop.")
        while True:
            temp_link = input("> ")
            if temp_link == 'quit':
                break
            else:
                self.links.append(temp_link)
        self.time_table[self.in_time] = {self.course_code: self.links}
        print(str(self.time_table)) # just prints to console for debugging. Can remove later.
    
    def day_return(self):
        return self.day

    def put_info(self):
        return self.time_table

# available_days = r'^[sun,mon,tues,wednes,thurs,fri]day$' need to verify days later
week_timetable = {}

while True:
    input_day_name = input("Enter the day : ").lower()
    current_day = day_timetable(input_day_name)
    while True:
        if input('Enter the upcoming class?(y/n)') == 'y':
            current_day.get_info()
            week_timetable[current_day.day_return()] = current_day.put_info()
        else:
            break
    if input("Do you wish to continue?(y/n) : ") == 'n':
        break

with open('schedule.txt', 'w') as f:
    f.write(str(week_timetable))