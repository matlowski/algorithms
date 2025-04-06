import generators
import scheduling_utils
from scheduling_utils import add_to_frames_history, display_frames_history


# FIFO page replacement algorithm
def fifo_page_replacement_algorithm(number_of_frames, list_of_references):
    frames_history = [] # Store the history of frames
    frame = [None] * number_of_frames # List representing empty frames
    next_frame_id = 0 # Pointer to the next frame to be replaced

    for reference in list_of_references:
        # Page is already in frame -> No replacement needed
        if reference in frame:
            add_to_frames_history(reference, frame, frames_history, is_page_missing=False)
        # Replace the oldest page in FIFO manner
        else:
            frame[next_frame_id] = reference
            next_frame_id += 1
            if next_frame_id >= number_of_frames:
                next_frame_id = 0

            add_to_frames_history(reference, frame, frames_history, is_page_missing=True)

    return frames_history


def fifo(number_of_simulations):
    parameters = generators.generate_process_references_parameters()
    number_of_processes, number_of_frames, number_of_references = parameters

    # Run the single simulation and display the frame history
    if number_of_simulations == 1:
        list_of_references = generators.generate_process_references_data(parameters)
        frames_history = fifo_page_replacement_algorithm(number_of_frames, list_of_references)
        display_frames_history(frames_history)
        return 

    # Run multiple simulations
    missing_pages = [] # List to store missing page counts per simulation
    for _ in range(number_of_simulations):
        list_of_references = generators.generate_process_references_data(parameters)
        frames_history = fifo_page_replacement_algorithm(number_of_frames, list_of_references)
        missing_pages.append(scheduling_utils.get_missing_page_count(frames_history))

    # Display results for multiple simulations
    print()
    print('* NUMBER OF MISSING PAGES: ')
    for simulation_num, miss_pages in enumerate(missing_pages):
        print(f'Simulation nr {simulation_num + 1}: {miss_pages}')
    print('* AVERAGE NUMBER OF MISSING PAGES ACROSS ALL SIMULATIONS: ', round(sum(missing_pages) / len(missing_pages), 5))



if __name__ == '__main__': 
    fifo()