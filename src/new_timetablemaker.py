import json
'''
{
    "tuesday": {
        "08:50":
        [
            "https://m.teamlink.co/3456575612",
            "https://mail.google.com"
        ],
        "09:55":
        [
            "https://m.teamlink.co/1559268139",
            "https://www.github.com"
        ]
    }
}
'''

class day_timetable:
    def __init__(self, day):
        self.day = day
        self.time_table = {}

    def get_info(self):
        self.in_time = input("Enter time in HH:MM format : ")
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
