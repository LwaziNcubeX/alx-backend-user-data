#!/usr/bin/env python3
"""
Filtered logger that returns log messages
"""
import os
import re
import typing
import logging
import datetime
import mysql.connector


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


PII_FIELDS = ['name', 'email', 'phone', 'ssn', 'password']


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get mysql database connector"""
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD")
    host = os.environ.get("PERSONAL_DATA_DB_HOST")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    db = mysql.connector.connection.MySQLConnection(
        host=host,
        user=username,
        password=password,
        database=db_name
    )

    return db


def main() -> None:
    """Main function that displays filtered rows"""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row in rows:
        formatted_row = ""
        for i, value in enumerate(row):
            field = cursor.column_names[i]
            if field in PII_FIELDS:
                formatted_row += f"{field}={RedactingFormatter.REDACTION}; "
            elif isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
                formatted_row += f"{field}={value}; "
            else:
                formatted_row += f"{field}={value!r}; "
        logger.info(formatted_row.strip())

    cursor.close()
    db.close()
    return


if __name__ == "__main__":
    main()
