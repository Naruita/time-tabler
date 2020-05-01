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
    
    def day_return(self):
        return self.day

    def put_info(self):
        return self.time_table

# available_days = r'^[sun,mon,tues,wednes,thurs,fri]day$' need to verify days later

input_day_name = input("Enter the day : ").lower()
day_timetable(input_day_name).get_info()
day_timetable()
