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
* FIFO - First In First Out - algorytm, który decyduje, która strona powinna zostać usunięta z ramki, gdy konieczne jest zwolnienie miejsca. FIFO usuwa najstarszą stronę pamięci (tę która była w pamięci najdłużej),
* LRU - Least Recent Used - trochę bardziej zaawansowany algorytm stronnicowania, który usuwa stronę, która była najrzadziej używana w ostatnim czasie, czyli taką, której dostępność do pamięci była najdalsza w przeszłości
Page replacement performance metrics:
* process - program lub zadanie wykonywane przez system operacyjny. Składa się ze stron, 
* page - część danych procesu, która jest przechowywana w ramce, 
* frame - miejsce w pamięci, gdzie przechowywane są dane, 

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

