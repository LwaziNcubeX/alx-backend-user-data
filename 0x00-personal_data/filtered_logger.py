#!/usr/bin/env python3
"""
Filtered logger that returns log messages
"""
import re
import typing
import logging


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter log messages using regex"""
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format log that uses filter_datum"""
        return filter_datum(fields=self.fields, redaction=self.REDACTION,
                            message=super().format(record),
                            separator=self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Get logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


PII_FIELDS = ['name', 'email', 'phone', 'ssn', 'password']
