from queue import PriorityQueue as pq
import datetime as dt
import time

class Queue:
    def __init__(self):
        self.order = pq()

class Time:
    def now_time():
        time.sleep(1) 
        now = dt.datetime.now()
        time_string = now.strftime("%H%M%S")
        time_int = int(time_string)
        return time_int
    
    def show_time(time):
        time_str = ""
        if (time == 0):
            time_str = "000000"
        elif (time > 0 and time < 10):
            time_str = "00000" + str(time)
        elif (time >= 10 and time < 100):
            time_str = "0000" + str(time)
        elif (time >= 100 and time < 1000):
            time_str = "000" + str(time)
        elif (time >= 1000 and time < 10000):
            time_str = "00" + str(time)
        elif (time >= 10000 and time < 100000):
            time_str = "0" + str(time)
        elif (time >= 100000):
            time_str = str(time)
        return time_str[0:2]+ ":" + time_str[2:4] + ":" + time_str[4:6]
    
class QueueFunc:
    def push_note(pq, note):
        priority = Time.now_time()
        pq.put((priority, note))
        return pq
    
    def pop_note(pq):
        if (pq.qsize() == 0):
            return False
        note = pq.get()
        note_str = note[1]
        note_time = Time.show_time(note[0])
        print(f"Час: {note_time}, Нотатка: {note_str}")
        return note

    def emptify_notes(pq):
        for i in range (pq.qsize()):
            pq.get()
        return pq
    
    def delete_notes(pq):
        if (pq == None):
            raise ValueError
        else:
            del pq
            return None