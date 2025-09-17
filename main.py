import datetime
import time
import os
import json
import marko
from marko import Markdown
from marko.md_renderer import MarkdownRenderer

TOMATO = 0 # minutes
tomato_records_path = "/home/Qtmd/pylab/simple-scheduler/test/tomato-records.json"
task_pool_path = "/home/Qtmd/Journal/gaokao/task pool.md"
MD = Markdown(renderer=MarkdownRenderer)

def main():
    read_tasks_pool()
    end_time = tomato_clock_emulation()
    record_tomato(end_time)
    edit_tasks_pool()
    #play_end_riff()

def tomato_clock_emulation():
    """
    count down 30 minutes
    return the string representation of end time of tomato clock
    """
    tomato_time = datetime.timedelta(minutes=TOMATO)
    end_time = datetime.datetime.now() + tomato_time;
    time_remain = end_time - datetime.datetime.now()
    while time_remain.total_seconds() > 0:
        if bool(time_remain.microseconds):
            print(f"\rtomato: {datetime.datetime.strptime(str(time_remain), "0:%M:%S.%f").strftime("%M:%S")}", end='')
        else:
            print(f"\rtomato: {datetime.datetime.strptime(str(time_remain), "0:%M:%S").strftime("%M:%S")}", end='')
        time.sleep(1)
        time_remain = end_time - datetime.datetime.now()
    print("\nA tomato is done!\a")
    return end_time.strftime("%Y/%m/%d %H:%M:%S")

def record_tomato(end_time: str):
    """
    open json file and update the record of today
    """
    today = datetime.datetime.now().strftime("%Y/%m/%d") # a string representing today's date for record access
    with open(tomato_records_path, "r+", encoding="utf-8") as f:
        if f.readline() == '':
            # create dictionary for representing tomato record
            tomato_records = {}
            tomato_records[today] = {"completion_times": [end_time], "tomato_number": 1}
            json.dump(tomato_records, f, indent=4)
        else:
            f.seek(0)
            tomato_records = json.load(f)
            if today in tomato_records:
                # read the record for today
                tomato_record = tomato_records[today]
                # add value end_time to the list of completion_times
                tomato_record["completion_times"].append(end_time)
                # count up number of tomatos
                tomato_record["tomato_number"] += 1
                # write back to json file
            else:
                # create the record for today
                tomato_records[today] = {"completion_times": [end_time], "tomato_number": 1}

            f.seek(0)
            f.truncate()
            json.dump(tomato_records, f, indent=4)

def play_end_riff():
    print("playing end riff...")
    os.execl("/usr/bin/mpv", "mpv", "--no-terminal", "--really-quiet", "./resources/Last guitar riff before World War 3.mp3")

def read_tasks_pool() -> list[marko.block.BlockElement]:
    """
    read the tasks pool and return ElementBlock the top task for each pool
    """
    with open("./tests/task pool.md", "r", encoding="utf-8") as f:
        md_text = f.read()
        doc_node = MD.parse(md_text)
        # find the top task element of each pool
        for child in doc_node.children:
            # find heading first
            if isinstance(child, marko.block.Heading):

def edit_tasks_pool():
    """
    """
    is_completed = bool(input("task completed? (Any for yes/Enter for no) "))
    # TODO

if __name__ == "__main__":
    main()
