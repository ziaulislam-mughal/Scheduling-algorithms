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


# SJF Scheduling (Non-Preemptive)
def sjf_non_preemptive():

    print("\n --- SJK (Non - Preemptive) ---")

    processes  = get_input()

    n = len(processes)
    completed = 0 
    current_time = 0 
    visited = [False] * n 
    result_list = []

    while completed != n :
        idx = -1 
        min_bt = float("inf")

        for i in range(n):
            #process arrive ho choka ha per excute nia hova
            if(processes[i].arrival_time <= current_time and not visited[i]):
                if processes[i].brust_time < min_bt:
                    min_bt = processes[i].brust_time
                    idx = 1 
                elif processes[i].brust_time == min_bt:
                    if processes[i].arrival_time < processes[idx].arrival_time:
                        idx = i

        if idx != -1:
            p = processes[idx]
            p.waiting_time = current_time - p.arrival_time
            current_time += p.burst_time 
            visited[idx] = True
            completed += 1 
            result_list.append(p)
        else:
            current_time += 1 

    print_table(result_list)

# SJF (Preemptive)
def sjf_preemptive():
    print("\n --- SJF (Preemptive) --- ")
    processes = get_input()
    n = len(processes)

    current_time = 0
    completed = 0
    min_rem_time = float("inf")
    shortest = -1

    while completed != n:
        check = False

        for i in range(n):
            if (processes[i].arrival_time <= current_time and processes[i].remaining_time > 0 and processes[i].remaining_time < min_rem_time):
                min_rem_time = processes[i].remaining_time
                shortest = i
                check = True

        if not check:
            current_time += 1
            continue

        processes[shortest].remaining_time -= 1
        min_rem_time = processes[shortest].remaining_time

        if processes[shortest].remaining_time == 0:
            completed += 1
            finish_time = current_time + 1
            processes[shortest].waiting_time = ( finish_time - processes[shortest].arrival_time - processes[shortest].burst_time)
            if processes[shortest].waiting_time < 0:
                processes[shortest].waiting_time = 0

            min_rem_time = float("inf")

        current_time += 1

    print_table(processes)



