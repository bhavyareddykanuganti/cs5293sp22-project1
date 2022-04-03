import pytest
import project1
from project1 import main

line = "From:  Tim Belden"

def test_redactname():
    test = main.redact_name(line)
    assert test is not None