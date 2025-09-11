import requests # to access api



base_url = 'http://127.0.0.1:8000/'

# -- test defining meeting ----------------------------------------------------------------------------

# post meeting with wrong JSON
def test_meeting_wrong_schema():
    # example: 
    protocol = '''{
            "protocol": "Bookshop",
            "roles": [
                { "name":"Customer", "alias":"C" },
                { "name":"Shop", "alias":"S" }
            ],
            "body": [
                { "kind":"note", "name":"book", "from":"C","to":"S","payload":"str" },
                { "kind":"message", "name":"available", "from":"S","to":"C","payload":"bool" },
                { "kind":"message", "name":"price", "from":"C","to":"S","payload":"str" },
                { "kind":"message", "name":"givenprice", "from":"S","to":"C","payload":"int" },
                { "kind":"choice","at":"C","options":[
                    [ { "kind":"message","name":"ask","from":"C","to":"S","payload":"str" },
                      { "kind":"message","name":"receipt","from":"S","to":"C","payload":"str" } ],    
                    [ { "kind":"message","name":"quit","from":"C","to":"S","payload":"" },
                      { "kind":"message","name":"goodbye","from":"S","to":"C","payload":"str" } ]
                    ]
                }
            ]
            }
        '''
    resp = requests.post(base_url+"meetings", data=protocol)
    assert resp.status_code == 400

# post meeting with right JSON but wrong Scribble (i.e. wrong alias)
def test_wrong_scribble():
    protocol = '''{
            "protocol": "Bookshop",
            "roles": [
                { "name":"Customer", "alias":"C" },
                { "name":"Shop", "alias":"S" }
            ],
            "body": [
                { "kind":"message", "name":"book", "from":"Y","to":"S","payload":"str" },
                { "kind":"message", "name":"available", "from":"S","to":"C","payload":"bool" },
                { "kind":"message", "name":"price", "from":"C","to":"S","payload":"str" },
                { "kind":"message", "name":"givenprice", "from":"S","to":"C","payload":"int" },
                { "kind":"choice","at":"C","options":[
                    [ { "kind":"message","name":"buy","from":"C","to":"S","payload":"str" },
                      { "kind":"message","name":"receipt","from":"S","to":"C","payload":"str" } ],    
                    [ { "kind":"message","name":"quit","from":"C","to":"S","payload":"" },
                      { "kind":"message","name":"goodbye","from":"S","to":"C","payload":"str" } ]
                    ]
                }
            ]
            }
        '''
    resp = requests.post(base_url+"meetings/", data=protocol)
    assert resp.status_code == 400

# post meeting that should have custom type but didn't define it
def test_no_custom():
    protocol = '''{
            "protocol": "Bookshop",
            "roles": [
                { "name":"Customer", "alias":"C" },
                { "name":"Shop", "alias":"S" }
            ],
            "body": [
                { "kind":"message", "name":"ask", "from":"C","to":"S","payload":"book" },
                { "kind":"message", "name":"available", "from":"S","to":"C","payload":"bool" },
                { "kind":"message", "name":"price", "from":"C","to":"S","payload":"book" },
                { "kind":"message", "name":"givenprice", "from":"S","to":"C","payload":"int" },
                { "kind":"choice","at":"C","options":[
                    [ { "kind":"note","name":"buy","from":"C","to":"S","payload":"book" },
                      { "kind":"message","name":"receipt","from":"S","to":"C","payload":"str" } ],    
                    [ { "kind":"message","name":"quit","from":"C","to":"S","payload":"" },
                      { "kind":"message","name":"goodbye","from":"S","to":"C","payload":"str" } ]
                    ]
                }
            ]
            }
        '''
    resp = requests.post(base_url+"meetings/", data=protocol)
    assert resp.status_code == 400 # check if this is the right error code

# post meeting with custom type ok
def test_meeting_def_ok():
    schema = '''{
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title":   "book",
        "type":    "object",
        "properties": {
        "name":  { "type": "string" },
        "author": { "type": "string" },
        "published": { "type": "int" }
        },
        "required": ["name","author","published"]
        }
    '''

    protocol = '''{
        "protocol": "Bookshop",
        "roles": [
            { "name":"Customer", "alias":"C" },
            { "name":"Shop", "alias":"S" }
        ],
        "body": [
            { "kind":"message",  "name":"ask", "from":"C","to":"S","payload":"book" },
            { "kind":"message",  "name":"available", "from":"S","to":"C","payload":"bool" },
            { "kind":"message",  "name":"price", "from":"C","to":"S","payload":"book" },
            { "kind":"message",  "name":"givenprice", "from":"S","to":"C","payload":"int" },
            { "kind":"choice","at":"C","options":[
                [ { "kind":"message","name":"buy","from":"C","to":"S","payload":"book" },
                    { "kind":"message","name":"receipt","from":"S","to":"C","payload":"str" } ],    
                [ { "kind":"message","name":"quit","from":"C","to":"S","payload":"" },
                    { "kind":"message","name":"goodbye","from":"S","to":"C","payload":"str" } ]
                ]
            }
        ]
        }
    '''
    resp_schema = requests.post(base_url+"types/Bookshop/", data=schema)
    resp_proto = requests.post(base_url+"meetings", data=protocol)
    assert resp_schema.status_code == 200
    assert resp_proto.status_code == 200

# define meeting that already exists, get error
def test_exisitng_meeting_def():
    protocol = '''{
        "protocol": "Bookshop",
        "roles": [
            { "name":"Customer", "alias":"C" },
            { "name":"Shop", "alias":"S" }
        ],
        "body": [
            { "kind":"message",  "name":"ask", "from":"C","to":"S","payload":"book" },
            { "kind":"message",  "name":"available", "from":"S","to":"C","payload":"bool" },
            { "kind":"message",  "name":"price", "from":"C","to":"S","payload":"book" },
            { "kind":"message",  "name":"givenprice", "from":"S","to":"C","payload":"int" },
            { "kind":"choice","at":"C","options":[
                [ { "kind":"note","name":"buy","from":"C","to":"S","payload":"book" },
                    { "kind":"message","name":"receipt","from":"S","to":"C","payload":"str" } ],    
                [ { "kind":"message","name":"quit","from":"C","to":"S","payload":"" },
                    { "kind":"message","name":"goodbye","from":"S","to":"C","payload":"str" } ]
                ]
            }
        ]
        }
    '''
    resp = requests.post(base_url+"meetings/", data=protocol)
    assert resp.status_code == 409


# -- test getting port ----------------------------------------------------------------------------

# get port of meeting that doesn't exist, error
def test_get_port_wrong():
    resp = requests.get(base_url+"meetings/commerce/")
    assert resp.status_code == 404

# get port of meeting that does exist
def test_get_port_ok():
    resp = requests.get(base_url+"meetings/Bookshop/")
    assert isinstance(resp.json(), int) and resp.status_code == 200


# -- test delete meeting ----------------------------------------------------------------------------

# delete meeting that doesn't exist
def test_delete_wrong():
    resp = requests.delete(base_url+"meetings/commerce")
    assert resp.status_code == 404

# delete meeting and check by getting port and getting error
def test_del_meeting_ok():
    delete = requests.delete(base_url+"meetings/Bookshop")
    port = requests.get(base_url+"meetings/Bookshop/")
    assert delete.status_code == 200
    assert port.status_code == 404
