#!/usr/bin/python3

import sys


def print_msg(status_counts, total_size):
    """
    Prints accumulated metrics.
    Args:
        status_counts: Dictionary with status code counts
        total_size: Total size of processed files
    """
    print("File size: {}".format(total_size))
    for key in sorted(status_counts.keys()):
        if status_counts[key] > 0:
            print("{}: {}".format(key, status_counts[key]))


# Initialize counters
total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            # Parse file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]

            # Update counters
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            # Increment line counter and print every 10 lines
            line_count += 1
            if line_count % 10 == 0:
                print_msg(status_counts, total_size)
        except (IndexError, ValueError):
            # Skip malformed lines
            continue
finally:
    # Print final statistics
    print_msg(status_counts, total_size)
