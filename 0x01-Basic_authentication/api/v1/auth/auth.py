#!/usr/bin/env python3
"""
Auth related functions and class
"""
from typing import List, TypeVar
from flask import request


class Auth:

    def requires_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the path is valid
        """

        return False

    def authorization_header(self, request=None) -> str:
        """
        Checks if the request is valid and extracts the authorization header
        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        gets current user
        """
        return None
