## WHAT IT IS?
This is a project in which two process scheduling algorithms (FCFS, LCFS) and two page replacement algorithms (FIFO, LRU) have been implemented. The application allows the user to simulate the chosen algorithm in the console. The parameters and the number of simulations are selected by the user from the menu in the terminal.
### Process Scheduling Algorithms:
* **FCFS - First Come First Serve** - an algorithm where processes are executed in the order they arrive in the system, regardless of their execution time.
* **LCFS - Last Come First Serve** - an algorithm where the last arrived process is executed first.
  
  CPU scheduling performance metrics:
  * **arrival time** - the moment when the process arrives in the system,
  * **burst time** - the time the process needs to complete all its instructions,
  * **start time** - the moment when the process begins execution,
  * **finish time** - the moment when the process finishes execution,
  * **waiting time** - the time the process had to wait before it started executing, \
    waiting time = start time - arrival time  
  * **turnaround time** - the time that has passed from the moment the process arrived to the moment it finished, \
    turnaround time = waiting time + burst time 
### Memory Paging Algorithms: 
* **FIFO - First In First Out** - an algorithm that decides which page should be removed from the frame when it is necessary to free up space. FIFO removes the oldest page from memory (the one that has been in memory the longest).
* **LRU - Least Recent Used** - a more advanced page replacement algorithm that removes the page that has been used the least recently, i.e., the one whose access to memory was the farthest in the past.

  Page replacement performance metrics:
  * **process** - a program or task executed by the operating system. It consists of pages, 
  * **page** - a portion of the process's data that is stored in a frame,
  * **frame** - a place in memory where data is stored,

## HOW TO USE IT? 
Using the simulator is very simple; just clone the repository, run the project, and follow the commands displayed in the console.

## EXAMPLE USAGE
After cloning the repository to the local machine, the simulator was launched using the command:
```
$ python main.py
```
Then, the algorithm was selected from the menu - FCFS:
<p align="left">
  <img src="images/menu.PNG" alt="Opis obrazka" width="400"/>
</p>
Next, the number of simulations was selected, and the ranges of process parameters were provided:
<p align="left">
  <img src="images/parameters.PNG" alt="Opis obrazka" width="400"/>
</p>
The result of the simulation:
<p align="left">
  <img src="images/results.PNG" alt="Opis obrazka" width="700"/>
</p>
