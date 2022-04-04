import pytest
import project1
from project1 import main

line = "I have attached my schedule"
word = "schedule"
def test_redactname():
    test = main.concept(word, line)
    assert test is not None