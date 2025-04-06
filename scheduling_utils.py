

###############
# FCFS i LCFS # 
###############


# Display the execution details for the scheduling algorithm 
def display_scheduling_algorithm_results(statistics):
    avg_waiting = 0
    print()
    print("* PROCESS EXECUTION DETAILS:")
    for i in range(0, len(statistics)):
        process_number = statistics[i][0]
        waiting_time = statistics[i][2] - statistics[i][1]
        turnaround_time = statistics[i][3] - statistics[i][1]
        print("Process number: " + str(process_number) + ", waiting time: " + str(waiting_time) + ", turnaround: " + str(
            turnaround_time) + ", arrival time: " + str(statistics[i][1]) + ", start time: " + str(
            statistics[i][2]) + ", finish time: " + str(statistics[i][3]))
        avg_waiting += waiting_time
    avg_waiting = avg_waiting / len(statistics)
    print(f'* AVERAGE WAITING TIME: {round(avg_waiting, 5)}')


# Calculate the average waiting time based on process execution statistics
def get_average_waiting_time(statistics):
    avg_waiting = 0
    for i in range(0, len(statistics)):
        waiting_time = statistics[i][2] - statistics[i][1]
        avg_waiting += waiting_time
    return avg_waiting / len(statistics)



################
# FIFO and LRU # 
################


# Add the current frame state to history
def add_to_frames_history(reference, frame, frames_history, is_page_missing):
    frames_history.append((reference, is_page_missing, frame[:]))


# Display the frames history for page replacement simulation
def display_frames_history(frames_history):
    _, _, frame = frames_history[0]
    number_of_frames = len(frame)
    lines = [[] for _ in range(number_of_frames)]
    list_of_references = []

    missing_pages = 0 # Counter for page faults
    for reference, is_page_missing, frame in frames_history:
        list_of_references.append(f'{reference:>3}')

        for frame_id, frame_value in enumerate(frame):
            if frame_value is None:
                frame_value = ''
            if is_page_missing and reference == frame_value:
                frame_value = f'*{frame_value}' # Mark page fault with an asterisk
                missing_pages += 1

            frame_value = f'{frame_value:>3}'
            lines[frame_id].append(frame_value)

    time_stamp = [f'{i:>3}' for i in range(1, len(frames_history) + 1)]
    
    print()
    title = "Moment:"
    print(f'{title:10}', end='')
    print(' '.join(time_stamp))

    title = "Reference:"
    print(f'{title:10}', end='')
    print(' '.join(list_of_references))

    for line_id, line in enumerate(lines):
        title = f'Frame {line_id+1}:'
        print(f'{title:10}', end='')
        print(' '.join(line))

    print()
    print(f'* REUSED PAGES: {len(frames_history) - missing_pages}')
    print(f'* PAGE FAULTS: {missing_pages}')


# Counts the number of missing pages in the history
def get_missing_page_count(history_of_frames):
    missing_pages = 0
    for row in history_of_frames:
        if row[1]:  # is_page_missing
            missing_pages += 1
    return missing_pages
