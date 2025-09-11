# to be able to use modules from other files
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import json


from proxy.session_logic.type_validation import *

schema = '''{
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title":   "book",
        "type":    "object",
        "properties": {
        "name":  { "type": "string" },
        "author": { "type": "string" },
        "published": { "type": "integer" }
        },
        "required": ["name","author","published"]
        }
    ''' 
schemas: list[Any]
schemas = []
schemas.append(json.loads(schema))
types = create_type_checker(schemas)
merged_types = types[0].copy()
merged_types.update(types[1])

def test_basic_python_types():
    temp_dict = {}
    temp_dict["entry"] = 1

    assert check_payload(json.dumps(4), "int", merged_types) == True
    assert check_payload(json.dumps(5.7), "float", merged_types) == True
    assert check_payload(json.dumps(True), "bool", merged_types)  == True
    assert check_payload(json.dumps("bla"), "str", merged_types)  == True
    assert check_payload(json.dumps((5, 6)), "tuple", merged_types)  == True
    assert check_payload(json.dumps(["hi", False]), "list", merged_types)  == True
    assert check_payload(json.dumps(temp_dict), "dict", merged_types)  == True

def test_custom_type():
    book_ok:dict[str, Any] = {"name": "M Train", "author": "Patti Smith", "published":2015}
    book_wrong = {"name": "M Train", "author": "Patti Smith"}
    assert check_payload(json.dumps(book_wrong), "book", merged_types) == False
    assert check_payload(json.dumps(book_ok), "book", merged_types) == True