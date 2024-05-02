#!/usr/bin/python3
"""Parse a log line and extract"""
import sys
import re


def parse_line(line):
    """Parse a log line and extract IP address, status code, and file size."""
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' \
              r' - \[(.*?)\]' \
              r' "GET \/projects\/260 HTTP\/1\.1"' \
              r' (\d{3}) (\d+)'
    match = re.match(pattern, line)
    if match:
        ip_address = match.group(1)
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        return ip_address, status_code, file_size
    return None, None, None


def print_stats(total_size, status_codes):
    """Print total file size and number of lines for each status code."""
    print(f'Total file size: {total_size}')
    for code, count in sorted(status_codes.items()):
        print(f'{code}: {count}')


def main():
    """Print total file size and number of lines"""
    total_size = 0
    status_codes = {
                    200: 0,
                    301: 0,
                    400: 0,
                    401: 0,
                    403: 0,
                    404: 0,
                    405: 0,
                    500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is not None:
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
    except BrokenPipeError:
        pass