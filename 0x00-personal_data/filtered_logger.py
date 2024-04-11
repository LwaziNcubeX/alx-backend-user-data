#!/usr/bin/env python3
"""
Filtered logger that returns log messages
"""
import re
import typing


def filter_datum(fields: typing.List, redaction: str,
                 message: str, separator: str) -> str:
    """Filter log messages using regex"""
    for field in fields:
        pattern = re.compile(
            rf"({re.escape(separator)}{field}=)[^{separator}]*")
        message = pattern.sub(fr"\1{redaction}", message)
    return message
