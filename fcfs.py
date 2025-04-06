import generators
import scheduling_utils


# FCFS cpu scheduling algorithm
def fcfs_cpu_scheduling_algorithm(parameters):
    data = generators.generate_process_data(parameters) # Data in format: [[process_number, arrival_time, burst_time], ...]

    statistics = [] # Data in format: [process_number, arrival_time, start_time, finish_time] 
    current_process = []  # Data in format: [process_number, burst_time, arrival_time, position (index) in 'statistics', start_time] 
    queue = [] # List of processes to be executed, sorted by arrival time

    counter = 0
    while True:
        counter += 1 
        # Add new processes to the queue when they arrive
        i = 0
        while i < len(data): 
            if data[i][1] == counter:
                queue.append(data[i])
                statistics.append([data[i][0], counter]) # Save [process_number, arrival_time]
                data.remove(data[i])
                i -= 1
            i += 1

        # Check if the current process has finished execution
        if len(current_process) > 0:
            if counter == current_process[1] + current_process[4]: # burst_time + start_time = finish_time 
                statistics[current_process[3]].append(counter) # Save finish_time
                current_process = []

        # Starting new processes
        if len(current_process) == 0:
            # End the simulation because no new process will arrive
            if len(queue) == 0 and len(data) == 0: 
                break 
            # CPU is idle, but new processes will arrive later
            if len(queue) == 0 and len(data) > 0: 
                continue
            # Find the position of the new process in the statistics list and set the arrival_time
            position = 0  
            for i in range(len(statistics)):
                if statistics[i][0] == queue[0][0]:
                    position = i
                    break
            arrival_time = statistics[position][1]
            # Initialize the current process with relevant details
            current_process = [queue[0][0], queue[0][2], arrival_time, position, counter] # counter = start_time
            statistics[position].append(counter) # Save start_time
            queue.remove(queue[0]) 


    # Sort the 'statistics' list by the second element - arrival_time
    statistics = sorted(statistics, key=lambda x: x[1])
    return statistics


def fcfs(number_of_simulations):
    parameters = generators.generate_process_parameters()

    # Run the single simulation and display the scheduling algorithm results
    if number_of_simulations == 1:
        statistics = fcfs_cpu_scheduling_algorithm(parameters)
        scheduling_utils.display_scheduling_algorithm_results(statistics)
        return

    # Run multiple simulations and display waiting time for each simulation
    avg_waiting_times = [] 
    for _ in range(number_of_simulations):
        statistics = fcfs_cpu_scheduling_algorithm(parameters)
        avg_waiting_times.append(scheduling_utils.get_average_waiting_time(statistics))

    print()
    print('* AVERAGE WAITING TIME FOR EACH SIMULATION: ')
    for simulatoin_num, avg_waiting_time in enumerate(avg_waiting_times):
        print(f'Simulation {simulatoin_num + 1}: {round(avg_waiting_time, 5)}')
    print('* AVERAGE OF THE AVERAGE WAITING TIMES: ', round(sum(avg_waiting_times) / len(avg_waiting_times), 5))


if __name__ == '__main__':
    fcfs()