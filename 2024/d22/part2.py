# https://adventofcode.com/2024/day/22

import numpy as np
import itertools
from multiprocessing import Pool

input = """
1
2
3
2024
"""

input = open('data', 'r').read()
initial = [int(i) for i in input.split('\n') if i.strip() != '']

print(initial)

def pseudo(x):
    x = (x ^ 64*x) % 16777216
    x = (x ^ (x // 32)) % 16777216
    x = (x ^ 2048*x)  % 16777216
    return x

secrets = initial
prices = []
for i in range(2000):
    #print(i, secrets)
    prices.append([x%10 for x in secrets])
    secrets = [pseudo(x) for x in secrets]

prices = np.array(prices)
print(prices)
all_diffs = []
for i in range(1, len(prices)):
    current_prices = np.array(prices[i])
    previous_prices = np.array(prices[i-1])
    differences = current_prices - previous_prices
    #print(f"Iteration {i}: Current prices: {current_prices}, Previous prices: {previous_prices}, Differences: {differences}")
    all_diffs.append(differences)

diffs = np.array(all_diffs)
print(diffs)

def bananas(seq):
    # Search for the first match of seq in each column of the diffs array
    total = 0
    for col in range(diffs.shape[1]):
        column_data = diffs[:, col]
        for i in range(len(column_data) - len(seq) + 1):
            if np.array_equal(column_data[i:i + len(seq)], seq):
                #print(col, i, prices[i+len(seq), col])
                total += prices[i+len(seq), col]
                break  # Stop after finding the first match in the column
    return total

def fast_bananas(seq):
    seq = np.array(seq)
    seq_len = len(seq)

    total = 0
    for col in range(diffs.shape[1]):
        column_data = diffs[:, col]
        windows = np.lib.stride_tricks.sliding_window_view(column_data, seq_len)
        match_indices = np.where(np.all(windows == seq, axis=1))[0]

        # Store the first match in this column if it exists
        if len(match_indices) > 0:
            #matches.append((col, match_indices[0]))  # (column index, row index)
            total += prices[match_indices[0]+len(seq), col]
    return total

def find_max_bananas():
    """
    Finds the 4-element sequence that maximizes the value of bananas2.

    Returns:
        tuple: The sequence and the maximum total.
    """
    max_total = float('-inf')
    best_sequence = None

    # Generate all possible 4-element sequences with values from -9 to 9
    for seq in itertools.product(range(-9, 10), repeat=4):
        total = fast_bananas(seq)
        print(seq, total)
        if total > max_total:
            max_total = total
            best_sequence = seq

    return best_sequence, max_total

# Call the function to find the optimal sequence
# best_seq, max_val = find_max_bananas()
# print(f"The best sequence is {best_seq} with a maximum total of {max_val}.")

def compute_for_chunk(chunk):
    max_total = float('-inf')
    best_sequence = None
    for seq in chunk:
        total = fast_bananas(seq)
        print(seq, total)
        if total > max_total:
            max_total = total
            best_sequence = seq
    return best_sequence, max_total

def find_max_bananas_parallel():
    sequences = list(itertools.product(range(-9, 10), repeat=4))
    n_cores = 8  # Adjust based on your CPU
    chunk_size = len(sequences) // n_cores

    with Pool(n_cores) as pool:
        results = pool.map(compute_for_chunk, [sequences[i:i + chunk_size] for i in range(0, len(sequences), chunk_size)])

    # Combine results from all processes
    best_sequence, max_total = max(results, key=lambda x: x[1])
    return best_sequence, max_total

# Run the parallel version
best_seq, max_val = find_max_bananas_parallel()
print(f"The best sequence is {best_seq} with a maximum total of {max_val}.")
