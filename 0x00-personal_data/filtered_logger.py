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
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
