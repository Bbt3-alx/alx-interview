#!/usr/bin/python3
"""
    Log parsing -
    a script that reads stdin line by line and computes metrics
"""


import sys
import re
import signal


def parse_log():
    log_format = re.compile(
        r'^\d{1,3}(\.\d{1,3}){3} - \[.*\] "GET /projects/260 HTTP/1.1" '
        r'(200|301|400|401|403|404|405|500) \d+$'
    )

    total_size = 0
    status_codes = {}
    line_count = 0

    def signal_handler(signum, frame):
        print_stats(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    def print_stats(total_size, status_codes):
        print(f"File size: {total_size}")
        for key, value in sorted(status_codes.items()):
            if value:
                print(f"{key}: {value}")

    for line in sys.stdin:
        line = line.strip()
        line_count += 1

        if re.match(log_format, line):
            parts = line.split()
            total_size += int(parts[-1])
            status_code = parts[-2]
            if status_code in ['200', '301', '400',
                               '401', '403', '404', '405', '500']:
                status_codes[status_code] = \
                    status_codes.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)


if __name__ == "__main__":
    parse_log()
