# json imports
import json
import jsonschema

# for getting json schemas of basic python types
from pydantic import TypeAdapter


def create_type_checker(schema_list)-> dict:
    '''
    Creates a dict of JSON schemas (type_name: json_schema) against which a session can check payload types comply.

        Args:
            schema_list(): list of schemas defined by the user, if any

        Returns:
            A dict of JSON schemas.
    '''
    
    schemas = {} # initialize dict

    # first define the basic python types
    schemas["int"] = TypeAdapter(int).json_schema()
    schemas["float"] = TypeAdapter(float).json_schema()
    schemas["bool"] = TypeAdapter(bool).json_schema()
    schemas["str"] = TypeAdapter(str).json_schema()
    schemas["list"] = TypeAdapter(list).json_schema()
    schemas["dict"] = TypeAdapter(dict).json_schema()
    schemas["tuple"] = TypeAdapter(tuple).json_schema()
    # schemas[""] = TypeAdapter(None).json_schema()

    # then define the custom ones if any
    if schema_list:
        for new_schema in schema_list:
            schemas[new_schema.get("title")] = new_schema # title is name of type in JSON schemas
    
    return schemas

def check_payload(msg, expected:str, schema_dict) -> bool:
    '''
    Checks if a payload is of the expected type.

        Args:
            msg(): payload we whose type we want to check
            expected(): name of the type the session expects the payload to be
            schema_dict(dict): contains all JSON schemas referenced by type

        Returns:
            True if the payload is of the expected type, False if it isn't.
    '''

    try:
        print(f"checking {expected} for {json.loads(msg)}") # debug
        jsonschema.validate(instance=json.loads(msg), schema=schema_dict[expected])
        return True
    except jsonschema.ValidationError:
        return False
        # raise jsonschema.ValidationError(f"Invalid data type! Expected type {expected} for {json.loads(msg)}")
    except Exception as e:
        print(f"Something went wrong with the type validation {e}") # TODO: make proper exception

# debug/test
"""
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
"""
    