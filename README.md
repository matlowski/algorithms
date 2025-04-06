## WHAT IT IS?
Jest to projekt, w ramach którego zaimplementowano dwa algorytmy planowania procesów (FCFS, LCFS) oraz dwa algorytmy stronnicowania (FIFO, LRU). Aplikacja umożliwia symulację wybranego algorytmu w konsoli. Parametry oraz liczba symulacji są wybierane przez użytkownika w menu.
### Algorytmy planowania procesów:
* FCFS - First Come First Serve - algorytm, w którym procesy wykonywane są w kolejności, w jakiej pojawiły się w systemie, bez względu na czas ich wykonania.  
* LCFS - Last Come First Serve - algorytm, w którym ostatni przybyły proces jest wykonywany jako pierwszy. 
CPU scheduling performance metrics:
* arrival time - to moment, w którym proces pojawił się w systemie,
* burst time - to czas, który proces potrzebuje na wykonanie wszystkich swoich instrukcji,
* start time - to moment, w którym proces zaczyna sie wykonywać,
* finish time - to moment, w którym proces kończy swoje wykonywanie,
* waiting time - to czas, który proces musiał poczekać, zanim zaczął się wykonywać,
  waiting time = start time - arrival time  
* turnaround time - to czas, który upłynął od momentu przybycia procesu do momentu jego zakończenia,
  turnaround time = waiting time + burst time 
### Algorytmy stronnicowania pamięci: 
* FIFO - First In First Out - algorytm, który decyduje, która strona powinna zostać usunięta z ramki, gdy konieczne jest zwolnienie miejsca. FIFO usuwa najstarszą stronę pamięci (tę która była w pamięci najdłużej),
* LRU - Least Recent Used - trochę bardziej zaawansowany algorytm stronnicowania, który usuwa stronę, która była najrzadziej używana w ostatnim czasie, czyli taką, której dostępność do pamięci była najdalsza w przeszłości
Page replacement performance metrics:
* frame - 



## HOW TO USE IT? 
Użytkowanie symulatora jest bardzo proste, wystarczy sklonować te repozytorim.

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
