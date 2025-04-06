import random


#############
# FCFS LCFS #
#############

# Prompt user for process parameters
def generate_process_parameters():
    number_of_processes = int(input('* Enter the number of processes: '))
    arrival_lower = int(input('* Enter the lower bound [arrival time]: '))
    arrival_upper = int(input('* Enter the upper bound [arrival time]: '))
    burst_lower = int(input('* Enter the lower bound [burst time]: '))
    burst_upper = int(input('* Enter the upper bound [burst time]: '))
    parameters = [number_of_processes, arrival_lower, arrival_upper, burst_lower, burst_upper]
    return parameters

# Generate a list of process data
def generate_process_data(parameters):
    n, zd, zg, bzd, bzg = parameters
    data = []  
    for i in range(1, n + 1):
        process_number = i
        arrival_time = random.randint(zd, zg)
        burst_time = random.randint(bzd, bzg)
        data.append([process_number, arrival_time, burst_time])
    print()
    print('* LIST OF ALL PROCESSES IN THE FORMAT: [process number, arrival time, burst time]')
    print(data)
    return data


############
# FIFO LRU #
############

# Prompt user for process reference parameters
def generate_process_references_parameters():
    number_of_processes = int(input('* Enter the number of processes: ')) 
    number_of_frames = int(input('* Enter the number of frames: ')) 
    number_of_references = int(input('* Enter the number of process references: ')) 
    parameters = [number_of_processes, number_of_frames, number_of_references]
    return parameters

# Generates a list of process references
def generate_process_references_data(parameters):
    number_of_processes, number_of_frames, number_of_references = parameters
    references = []
    for _ in range(number_of_references):
        references.append(random.randint(1, number_of_processes))
    return references



if __name__ == '__main__':
    parameters = generate_process_references_parameters()
    print(generate_process_references_data(parameters))