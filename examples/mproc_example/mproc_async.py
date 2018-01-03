"""Simple example to use an async multiprocessing function."""
from common_python.mproc import mproc_async, mproc_func


# STEP - 1
# Define a function that is supposed to simulate a computationally intensive function.
# Add the `mproc_func` decorator to it in order to make it mproc compatible.
@mproc_func
def get_square(x):
    """Return square of a number after sleeping for a random time."""
    import random
    import time
    time.sleep(random.random())
    return x**2


# STEP - 2
# Create a list of list of argument for the `get_square` function.
# The length of the outer list determines the number of times the function is going to be called asynchronously.
# In this example, the length is 20. The final `iterof_iterof_args` will look like [[0], [1], [2] ...]
iterof_iterof_args = [[i] for i in range(20)]


# STEP -3
# Call the function 20 times using multiprocessing.
# We limit the number of processes to be 4 and at any time there will be a max of 4 results.
# The output is a generator of results.
results_gen = mproc_async(get_square,
                          iterof_iterof_args=iterof_iterof_args,
                          n_processes=4,
                          queue_size=4)


# STEP - 4
# Print the results.
# Each result looks like a tuple of (original_index, function_output)
for async_index, result in enumerate(results_gen):
    call_index, func_output = result
    print(async_index, call_index, func_output)
