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
Użytkowanie symulatora jest bardzo proste, wystarczy sklonować te repozytorim, uruchomić projekt oraz postępować zgodnie z komendami wyświetlanymi w konsoli.


!!!
## EXAMPLE USAGE
Po sklonowaniu repozytorim na lokalną maszynę uruchomiono symulator za pomocą komendy: 
```
$ python main.py
```
Następnie z menu wybrano jeden algorytm - FCFS:
fota menu
Kolejno wybrano liczbę sumulacji:
fota liczby symulacji 
Podano zakresy parametrów procesów:
fota zakresów parametrów 
Wynik symulacji:
fota końcowa

Całą operację powtórzono dla algorytmu - FIFO: 

