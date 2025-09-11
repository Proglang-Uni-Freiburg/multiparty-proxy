# json imports
import json
import jsonschema

# for getting json schemas of basic python types
from pydantic import TypeAdapter
from typing import Any

# JSON defined as Any as there is no proper definition in Python
def create_type_checker(schema_list:list[Any]|None)-> tuple[dict[str, Any], dict[str, Any]]:
    '''
    Creates a dict of JSON schemas against which a session can later check payload types comply.

        Args:
            schema_list(list[Any]|None): list of schemas defined by the user, if any

        Returns:
            A tuple of two schema dictionaries. The first dict is for builtin basic
            python types and the second for custom schemas that are sent to the API.
    '''
    
    # initialize dicts
    basic_schemas:dict[str, Any] = {}
    custom_schemas:dict[str, Any] = {}

    # first define the basic python types
    basic_schemas["int"] = TypeAdapter(int).json_schema()
    basic_schemas["float"] = TypeAdapter(float).json_schema()
    basic_schemas["bool"] = TypeAdapter(bool).json_schema()
    basic_schemas["str"] = TypeAdapter(str).json_schema()
    basic_schemas["list"] = TypeAdapter(list).json_schema()
    basic_schemas["dict"] = TypeAdapter(dict).json_schema()
    basic_schemas["tuple"] = TypeAdapter(tuple).json_schema()
    basic_schemas["none"] = TypeAdapter(None).json_schema()

    # then define the custom ones if any
    if schema_list:
        for new_schema in schema_list:
            custom_schemas[new_schema.get("title")] = new_schema # title is name of type in JSON schemas
    
    return (basic_schemas, custom_schemas)

def check_payload(msg:Any, expected:str, schema_dict:dict[str, Any]) -> bool:
    '''
    Checks if a payload is of the expected type.

        Args:
            msg(Any): payload whose type we want to check
            expected(str): name of the type the session expects the payload to be
            schema_dict(dict[str, Any]): contains all JSON schemas referenced by name

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
        print(f"Something went wrong with the type validation {e}")
        raise e