import pytest
import project1
from project1 import main

line = "2657 Classen Blvd"

def test_redactaddress():
    test = main.redact_address(line)
    assert test is not None