import pytest
from ..helloworld import greet

def test_greet():
    assert greet() == "Hello World!"