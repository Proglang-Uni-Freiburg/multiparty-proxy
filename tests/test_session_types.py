"""# to be able to use modules from other files
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# for testing
import pytest

from proxy.session_logic.session_types import *

def test_label_equality():
    l1 = Label("Hello")
    l2 = Label("Hello")
    assert l1 == l2


# to test: functions INSIDE sessions, mazbe cont.? -> should i test exceptions?

# -- test choice functions ---------------------------------------------------

def test_update_conts():

def test_update_actors_involved():

def test_update_error handling():


# -- test rec functions ---------------------------------------------------

def test_update_conts():
"""