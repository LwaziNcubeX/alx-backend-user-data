#!/usr/bin/env python3
"""
Filtered logger that returns log messages
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Filter log messages using regex
    """
    for field in fields:
        pattern = re.compile(
            rf"({re.escape(separator)}{field}=)[^{separator}]*")
        message = pattern.sub(fr"\1{redaction}", message)
    return message
