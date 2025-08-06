
import json
import jsonschema

from pydantic import TypeAdapter


def create_type_checker(schema_list)->dict:
    schemas = {}
    # passes back to proxy dict with all json schemas

    # first define the basic python types
    schemas["int"] = TypeAdapter(int).json_schema()
    schemas["float"] = TypeAdapter(float).json_schema()
    schemas["bool"] = TypeAdapter(bool).json_schema()
    schemas["str"] = TypeAdapter(str).json_schema()
    schemas["list"] = TypeAdapter(list).json_schema()
    schemas["dict"] = TypeAdapter(dict).json_schema()
    schemas["tuple"] = TypeAdapter(tuple).json_schema()

    # then define the custom ones if any
    if schema_list:
        for new_schema in schema_list:
            schemas[""] = new_schema # missing how to know name
    
    return schemas

def check_payload(msg, expected:str, schema_dict) -> bool: 
    # true if its valid and false if it isnt
    try:
        jsonschema.validate(instance=json.loads(msg), schema=schema_dict[expected])
        return True
    except jsonschema.ValidationError:
        return False
        # raise jsonschema.ValidationError(f"Invalid data type! Expected type {expected} for {json.loads(msg)}")
    except Exception as e:
        print(f"Something went wrong with the type validation {e}") # make proper exception



if __name__ == "__main__":
    types = create_type_checker([])
    temp_dict = {}
    temp_dict["entry"] = 1
    # trying basic types checker
    print(check_payload(json.dumps(4), "int", types)) # int
    print(check_payload(json.dumps(5.7), "float", types)) # float
    print(check_payload(json.dumps(True), "bool", types)) # bool
    print(check_payload(json.dumps("bla"), "str", types)) # string
    print(check_payload(json.dumps((5, 6)), "tuple", types)) # tuple
    print(check_payload(json.dumps(["hi", False]), "list", types)) # list
    print(check_payload(json.dumps(temp_dict), "dict", types)) # dict
    
    