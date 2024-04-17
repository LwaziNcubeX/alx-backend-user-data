#!/usr/bin/env python3
"""
Auth related functions and class
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Auth related functions and class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the path is valid
        """
        if path is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if path.rstrip('/') == excluded_path.rstrip('/'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Checks if the request is valid and extracts the authorization header
        """

        return None

    User = TypeVar('User')

    def current_user(self, request=None) -> User:
        """
        gets current user
        """
        return None
