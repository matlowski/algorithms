from fcfs import fcfs
from fifo import fifo
from lcfs import lcfs
from lru import lru
import random


# Display menu 
def start():
    random.seed(10) 
    print("*** AVAILABLE ALGORITHMS ***")
    print("1. FCFS (First-Come First-Served)")
    print("2. LCFS (Last-Come First-Served)")
    print("3. FIFO (First-In First-Out)")
    print("4. LRU (Least Recently Used)")
    algorithm = int(input("* Select the algorithm number: "))
    number_of_simulations = int(input("* Enter the number of simulations: "))
    if algorithm == 1:
        fcfs(number_of_simulations)
    elif algorithm == 2:
        lcfs(number_of_simulations)
    elif algorithm == 3:
        fifo(number_of_simulations)
    elif algorithm == 4:
        lru(number_of_simulations)


if __name__ == '__main__':
    start()