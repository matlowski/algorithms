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
  <img src="https://private-user-images.githubusercontent.com/180983359/430721796-0979c9a9-2af0-4b3f-94d4-012898506078.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5NTgyMDEsIm5iZiI6MTc0Mzk1NzkwMSwicGF0aCI6Ii8xODA5ODMzNTkvNDMwNzIxNzk2LTA5NzljOWE5LTJhZjAtNGIzZi05NGQ0LTAxMjg5ODUwNjA3OC5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxNjQ1MDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05NjQ5YWE3NzFkYWNhNTI2OGRmMDc1NWJkYjQ4ZGFmY2NjNDJmM2M0MDZkODA0ZmRlZmM5ZDQxNzY0ZGY2ZmNiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.AhYrEKMWB8qolQ3iikhtiQTsDX9wP50c6wrpU1Alt8A" alt="Opis obrazka" width="400"/>
</p>
Next, the number of simulations was selected, and the ranges of process parameters were provided:
<p align="left">
  <img src="https://private-user-images.githubusercontent.com/180983359/430721860-fb81d402-ea92-4326-a1e9-e5aeb0a77688.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5NTk2MjYsIm5iZiI6MTc0Mzk1OTMyNiwicGF0aCI6Ii8xODA5ODMzNTkvNDMwNzIxODYwLWZiODFkNDAyLWVhOTItNDMyNi1hMWU5LWU1YWViMGE3NzY4OC5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxNzA4NDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZTZiYzkwNGFhNjBiM2M3NzhhZDE2MzgxMGVkYmIwYjk3NmU0NjQ3Y2IwNzZmNTM5MGU3NTVmMjIxNGRjOWY3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.e999sMgHE-iRv69Cd0H1veCp6l9JZFCkJBXJ2CfN1b0" alt="Opis obrazka" width="400"/>
</p>
The result of the simulation:
<p align="left">
  <img src="https://private-user-images.githubusercontent.com/180983359/430721923-640ebdbb-67ce-45c6-b2c8-e88acb42e46b.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5NTk2NjksIm5iZiI6MTc0Mzk1OTM2OSwicGF0aCI6Ii8xODA5ODMzNTkvNDMwNzIxOTIzLTY0MGViZGJiLTY3Y2UtNDVjNi1iMmM4LWU4OGFjYjQyZTQ2Yi5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxNzA5MjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kOGJlMTJmYTkzZTVkZjRkOWQ2MGYzNmYyMzU5NmM0NjFiYzllMjJlODk5MzIzM2I5ZDBmMWYyODk0MjJiYzUxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Dta05Urxd33hcsWiM7EicSLeryK9fEdxvSGHft9uxcE" alt="Opis obrazka" width="700"/>
</p>
