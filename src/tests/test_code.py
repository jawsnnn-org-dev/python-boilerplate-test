# -*- coding: utf-8 -*-
import pytest
"""
Author: Arpan Malviya
Purpose: Sample test file
Date: 24-JUN-2019
"""
from ..helloworld import greet

def test_greet():
    """Intentionally failing test template"""
    assert greet() == "Helloo World!"