import sys

# Class to represent a process
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turn_around_time = 0
        self.waiting_time = 0
        self.start = -1


# Input function
def get_input(needs_priority=False):
    n = int(input("Enter Number of Jobs: "))
    processes = []

    print("Enter Details (Arrival Time, Burst Time" +
          (", Priority" if needs_priority else "") + "):")

    for i in range(n):
        print(f"Job {i+1}:")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        p = 0
        if needs_priority:
            p = int(input("Priority (lower value = higher priority): "))
        processes.append(Process(i+1, at, bt, p))

    return processes


# Display output in table
def print_table(processes):
    print("\nJob\tAT\tBT\tWT")
    total_wt = 0

    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}")
        total_wt += p.waiting_time

    print(f"\nAverage Waiting Time: {total_wt / len(processes):.2f}")


# FCFS Scheduling
def fcfs():
    print("\n--- FCFS Scheduling ---")
    processes = get_input()

    # Heart of FCFS
    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0
    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time

        p.waiting_time = current_time - p.arrival_time
        current_time += p.burst_time
        p.turn_around_time = p.waiting_time + p.burst_time

    print_table(processes)



