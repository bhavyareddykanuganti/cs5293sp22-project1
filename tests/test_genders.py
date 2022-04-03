import pytest
import project1
from project1 import main

line = "he is probably close enough"

def test_redact_gender():
    test = main.redact_gender(line)
    assert test is not None