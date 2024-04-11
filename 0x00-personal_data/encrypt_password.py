#!/usr/bin/env python3
"""
Encrypting passwords using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypting passwords using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
