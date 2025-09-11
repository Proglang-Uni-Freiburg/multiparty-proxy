# to be able to use modules from other files
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from proxy.session_logic.session_types import *

def test_label_equality():
    l1 = Label("Hello")
    l2 = Label("Hello")
    assert l1 == l2

# -- test choice functions ---------------------------------------------------

m_one_one = Message(name=Label("pay"), dir=Dir("to"), actor="lorelai", payload="int", cont=None)
m_one_two = Message(name=Label("get"), dir=Dir("to"), actor="monica", payload="int", cont=None)
m_two_one = Message(name=Label("timeout"), dir=Dir("to"), actor="lorelai", payload="int", cont=None)
m_two_two = Message(name=Label("accept"), dir=Dir("to"), actor="monica", payload="int", cont=None)
m_two_three = Message(name=Label("stock"), dir=Dir("from"), actor="monica", payload="int", cont=None)

temp_choice = Choice(actor="act", alternatives=[[m_one_one, m_one_two], [m_two_one, m_two_two, m_two_three]], cont=None, actors_involved=[])

def test_update_conts_choice():
    temp_choice.update_conts()

    assert temp_choice.alternatives[0][0].cont.label == Label("get")
    assert temp_choice.alternatives[0][1].cont == None
    assert temp_choice.alternatives[1][0].cont.label == Label("accept")
    assert temp_choice.alternatives[1][1].cont.label == Label("stock")
    assert temp_choice.alternatives[1][2].cont == None

def test_update_actors_involved():
    temp_choice.update_actors_involved()
    assert temp_choice.actors_involved == ["lorelai", "monica"]

def test_update_error_handling():
    temp_choice.update_error_handling()
    assert temp_choice.errors == ["timeout"]

# -- test rec functions ---------------------------------------------------

def test_update_conts_rec():
    r_one_one = Message(name=Label("pay"), dir=Dir("to"), actor="lorelai", payload="int", cont=None)
    r_one_two = Message(name=Label("get"), dir=Dir("to"), actor="monica", payload="int", cont=None)
    r_two_one = Message(name=Label("timeout"), dir=Dir("to"), actor="lorelai", payload="int", cont=None)
    r_two_two = Message(name=Label("accept"), dir=Dir("to"), actor="monica", payload="int", cont=None)
    r_two_three = Message(name=Label("stock"), dir=Dir("from"), actor="monica", payload="int", cont=None)
    temp_rec = Rec(label=Label("something"), actions=[r_one_one, r_one_two, r_two_one, r_two_two, r_two_three], cont=None)

    temp_rec.update_conts()
    assert temp_rec.actions[0].cont.label == Label("get")
    assert temp_rec.actions[1].cont.label == Label("timeout")
    assert temp_rec.actions[2].cont.label == Label("accept")
    assert temp_rec.actions[3].cont.label == Label("stock")