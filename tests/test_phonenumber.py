import pytest
import project1
from project1 import main

line = "phone numbers: 854-235-6526"

def test_redactphonenum():
    test = main.redact_phnum(line)
    assert test is not None