import json


class day_timetable:
    def __init__(self, day):
        self.day = day
        self.time_table = {}

    def get_info(self):
        self.in_time = input("Enter time in HH:MM format : ")
        self.course_code = input("Enter the course code : ").upper()
        self.links = []
        print("Add links now. Type 'quit' to stop.")
        while True:
            temp_link = input("> ")
            if temp_link == "quit":
                break
            else:
                self.links.append(temp_link)
        self.time_table[self.in_time] = {self.course_code: self.links}
        print(
            str(self.time_table)
        )  # just prints to console for debugging. Can remove later.

    def day_return(self):
        return self.day

    def put_info(self):
        return self.time_table


# available_days = r'^[sun,mon,tues,wednes,thurs,fri]day$' need to verify days later
def make():
    week_timetable = {}

    while True:
        input_day_name = input("Enter the day : ").lower()
        current_day = day_timetable(input_day_name)
        while True:
            if input("Enter the upcoming class?(y/n) : ")[0] == "y":
                current_day.get_info()
                week_timetable[current_day.day_return()] = current_day.put_info()
            else:
                break
        if input("Do you wish to continue?(y/n) : ")[0] == "n":
            break

    with open("../src/schedule.txt", "w") as f:
        f.write(json.dumps(week_timetable, indent=4, sort_keys=True))


if __name__ == "__main__":
    make()
