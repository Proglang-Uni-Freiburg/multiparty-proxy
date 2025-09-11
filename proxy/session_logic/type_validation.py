# json imports
import json
import jsonschema

# for getting json schemas of basic python types
from pydantic import TypeAdapter
from typing import Any

# JSON defined as Any as there is no proper definition in Python
def create_type_checker(schema_list:list[Any]|None)-> tuple[dict[str, Any], dict[str, Any]]:
    '''
    Creates a dict of JSON schemas (type_name: json_schema) against which a session can check payload types comply.

        Args:
            schema_list(): list of schemas defined by the user, if any

        Returns:
            A tuple of type :schema dicts. The first dict is for builtin basic python types and the seconf for custom schemas that are sent to the API.
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
            msg(): payload whose type we want to check
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
        print(f"Something went wrong with the type validation {e}")
        raise e

def check_json_protocol(proto:Any, proto_schema:Any)->bool:
    try:
        jsonschema.validate(instance=proto, schema=proto_schema)
        return True
    except jsonschema.ValidationError:
        return False


# schema of protocol definition
protocol_schema = json.loads(r'''{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://something.com/scribble.protocol.schema.json",
  "title": "Protocol",
  "description": "A Scribble protocol described as a JSON object",
  "type": "object",
  "properties": {
     "protocol": { "type": "string" },
	   "roles": {
		   "type": "array",
       "items": {
			   "type": "object",
	        "required": ["name", "alias"],
	        "properties": {
	          "name":  { "type": "string" },
	          "alias": { "type": "string" }
	        }
	      }
	   },
     "error": {
			"type": "string",
			"enum": ["fatal", "ignore", "handle"]
		 },
     "timeout": { "type": "integer" },
     "body": {
	     "type": "array",
       "items": { "$ref": "#/$defs/session" }
	   }
  },  
  "required": [ "roles", "body" ],
  "additionalProperties": false,
  "$defs": {
  "forbiddenNames": { "enum": ["timeout", "error", "wrongPayload", "wrongLabel"] },

  "session": {
    "type": "object",
    "oneOf": [
      { "$ref": "#/$defs/message" },
      { "$ref": "#/$defs/rec" },
      { "$ref": "#/$defs/continue" },
      { "$ref": "#/$defs/choice" }
    ]
  },

  "message": {
    "type": "object",
    "properties": {
      "kind": { "const": "message" },
      "name": { "type": "string", "not": { "$ref": "#/$defs/forbiddenNames" } },
      "from": { "type": "string" },
      "to":   { "type": "string" },
      "payload": { "type": "string" }
    },
    "required": ["kind", "name", "from", "to", "payload"],
    "additionalProperties": false
  },

  "choice": {
    "type": "object",
    "properties": {
      "kind": { "const": "choice" },
      "at": { "type": "string" },
      "options": {
        "type": "array",
        "items": {
          "type": "array",
          "items": { "$ref": "#/$defs/session" }
        }
      }
    },
    "required": ["kind", "at", "options"],
    "additionalProperties": false
  },

  "rec": {
    "type": "object",
    "properties": {
      "kind": { "const": "rec" },
      "name": { "type": "string", "not": { "$ref": "#/$defs/forbiddenNames" } },
      "body": {
        "type": "array",
        "items": { "$ref": "#/$defs/session" }
      }
    },
    "required": ["kind", "name", "body"],
    "additionalProperties": false
  },

  "continue": {
    "type": "object",
    "properties": {
      "kind": { "const": "continue" },
      "name": { "type": "string" }
    },
    "required": ["kind", "name"],
    "additionalProperties": false
  }
}

}
''')

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