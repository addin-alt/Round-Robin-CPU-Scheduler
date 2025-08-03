# Round Robin CPU Scheduling Simulation
# Author: Al Addin
# GitHub: https://github.com/addin-alt

def find_waiting_time(processes, n, bt, wt, quantum):
    rem_bt = bt[:]
    t = 0  # Current time

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break

def find_turnaround_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def display_result(processes, n, bt, wt, tat):
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"P{processes[i]}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")

def main():
    print("Round Robin CPU Scheduling\n")
    n = int(input("Enter number of processes: "))
    processes = [i+1 for i in range(n)]
    bt = list(map(int, input(f"Enter Burst Times for {n} processes (space-separated): ").split()))
    quantum = int(input("Enter Time Quantum: "))

    wt = [0] * n
    tat = [0] * n

    find_waiting_time(processes, n, bt, wt, quantum)
    find_turnaround_time(processes, n, bt, wt, tat)
    display_result(processes, n, bt, wt, tat)

if __name__ == "__main__":
    main()
