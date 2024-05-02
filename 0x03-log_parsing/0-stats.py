#!/usr/bin/python3
"""Parse a log line and extract"""

import fileinput


def print_logs(file_size: int, status_codes: dict):
    """Prints file size and status code counts.

    Args:
        file_size (int): Total file size.
        status_codes (dict): Dictionary of status codes and their counts.

    Returns:
        None
    """
    print("File size:", file_size)
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


def parse_log():
    """Print total file size and number of lines"""
    file_size = 0
    status_codes = {
                    "200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0
    }
    current_line = 0

    try:
        for line in fileinput.input():
            data = line.split()
            if len(data) < 10:
                continue
            file_size += int(data[-1])
            status = data[-2]
            if status in status_codes:
                status_codes[status] += 1
            current_line += 1
            if current_line % 10 == 0:
                print_logs(file_size, status_codes)
                file_size = 0
                status_codes = {code: 0 for code in status_codes}
    except KeyboardInterrupt:
        pass
    print_logs(file_size, status_codes)


if __name__ == "__main__":
    parse_log()