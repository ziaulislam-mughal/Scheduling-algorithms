import sys

#class to represent a process 
class Process:
    def __init__(self,pid,arrival_time,burst_time,priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time 
        self.completion_time  = 0
        self.turn_around_time = 0 
        self.waiting_time = 0 
        self.start = -1 

