import schedule
import time
import datetime
import converting_timestamps as ct
import deploy

def find_day():
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = week_days[datetime.date.today().weekday()]
    return day

def main(links):
    temp_stamps = ct.time_stamp_return(find_day())
    day = find_day()
    for timestamp in temp_stamps:
        schedule.every().day.at(timestamp).do(deploy.deploy_links, links)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main(["https://www.google.com", "https://www.youtube.com"])