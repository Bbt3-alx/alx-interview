#!/usr/bin/python3
"""utf8 validator"""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character sequence
    remaining_bytes = 0

    for byte in data:

        byte & 0xFF

        if remaining_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte sequence
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte sequence
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte sequence
                remaining_bytes = 3
            elif (byte >> 7) != 0:  # Invalid 1-byte (must start with 0)
                return False
        else:
            # Check if byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # If remaining_bytes is not zero, we have an incomplete UTF-8 character
    return remaining_bytes == 0
