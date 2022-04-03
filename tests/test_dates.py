import pytest
import project1
from project1 import main

line = "The given regex pattern detects the following patterns of dates: 2/10/2009"

def test_redactdate():
    test = main.redact_date(line)
    assert test is not None