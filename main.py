import datetime
import time
import math
import os
import json

tomato_records_path = "/home/Qtmd/pylab/simple-scheduler/data/tomato-records.json"
task_pool_path = "/home/Qtmd/Journal/gaokao/task pool.md"

def main():
    end_time = tomato_clock_emulation()
    record_tomato(end_time)
    manipulate_tasks_pool()
    play_end_riff()

def tomato_clock_emulation():
    """
    count down 30 minutes
    """
    tomato_time = datetime.timedelta(minutes=30)
    end_time = datetime.datetime.now() + tomato_time;
    time_remain = end_time - datetime.datetime.now()
    while time_remain.total_seconds() > 0:
        if bool(time_remain.microseconds):
            print(f"\rtomato: {datetime.datetime.strptime(str(time_remain), "0:%M:%S.%f").strftime("%M:%S")}", end='')
        else:
            print(f"\rtomato: {datetime.datetime.strptime(str(time_remain), "0:%M:%S").strftime("%M:%S")}", end='')
        time.sleep(1)
        time_remain = end_time - datetime.datetime.now()
    print("A tomato is done!")
    return end_time

def record_tomato(end_time):
    today = datetime.datetime.now().strftime("%Y/%m/%d") # a string representing today's date for record access
    with open(tomato_records_path, "w+", encoding="utf-8") as f:
        tomato_records = json.load(f)
        # read the record for today
        tomato_record = tomato_records[today]
        # add value str(end_time) to the list of completion_times
        tomato_record["completion_times"].append(str(end_time))
        # count up number of tomatos
        tomato_record["tomato_number"] += 1
        # write back to json file
        json.dump(tomato_records, f, indent=4)

def play_end_riff():
    print("play end riff...")
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(1, devnull)
    os.execl("/usr/bin/mpv", "mpv", "./resources/Last guitar riff before World War 3.mp3")

def read_tasks_pool():
    # TODO
    pass

def manipulate_tasks_pool():
    """
    parse task pool and cross checkbox
    """
    is_completed = bool(input("task completed? (Any for yes/Enter for no) "))
    # TODO

if __name__ == "__main__":
    main()
