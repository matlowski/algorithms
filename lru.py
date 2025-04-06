import generators
import scheduling_utils
from scheduling_utils import add_to_frames_history, display_frames_history


# LRU page replacement algorithm
def lru_page_replacement_algorithm(number_of_frames, list_of_references):
    frames_history = [] # Store the history of frames
    frame = [None] * number_of_frames # List representing empty frames
    frame_timestamps = [[-1, i] for i in range(number_of_frames)] # Store timestamps for pages in format: [timestamp, frame_index]

    for i, reference in enumerate(list_of_references):
        # Page is already in frame
        if reference in frame: 
            reference_id = frame.index(reference) # Get the index of the existing reference
            frame_timestamps[reference_id][0] = i # Time update 
            add_to_frames_history(reference, frame, frames_history, is_page_missing=False)
        # Replace the oldest page in LRU manner
        else:
            # Find the least recently used frame
            value_frame_index = min(frame_timestamps)[1] 
            # Replace the page in the frame
            frame[value_frame_index] = reference 
            # Time update
            frame_timestamps[value_frame_index][0] = i 
            add_to_frames_history(reference, frame, frames_history, is_page_missing=True)

    return frames_history


def lru(number_of_simulations):
    parameters = generators.generate_process_references_parameters()
    number_of_processes, number_of_frames, number_of_references = parameters

    # Run the single simulation and display the frame history
    if number_of_simulations == 1:
        list_of_references = generators.generate_process_references_data(parameters)
        frames_history = lru_page_replacement_algorithm(number_of_frames, list_of_references)
        display_frames_history(frames_history)
        return

    # Run multiple simulations
    missing_pages = [] # List to store missing page counts per simulation
    for _ in range(number_of_simulations):
        list_of_references = generators.generate_process_references_data(parameters)
        frames_history = lru_page_replacement_algorithm(number_of_frames, list_of_references)
        missing_pages.append(scheduling_utils.get_missing_page_count(frames_history))

    # Display results for multiple simulations
    print()
    print('* NUMBER OF MISSING PAGES: ')
    for simulation_num, miss_pages in enumerate(missing_pages):
        print(f'Simulation {simulation_num + 1}: {miss_pages}')
    print('* AVERAGE NUMBER OF MISSING PAGES ACROSS ALL SIMULATIONS: ', round(sum(missing_pages) / len(missing_pages), 5))



if __name__ == '__main__':
    lru() 