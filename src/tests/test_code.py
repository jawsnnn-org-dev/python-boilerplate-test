# -*- coding: utf-8 -*-
"""
Author: Arpan Malviya
Purpose: Sample test file
Date: 24-JUN-2019
"""
import pytest

from ..helloworld import greet

def test_greet():
    """Test code here"""
    assert greet() == "Hello World!"