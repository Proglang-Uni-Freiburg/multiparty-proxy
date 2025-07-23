import json
import json_to_scribble

json_str = '''
{
  "protocol": "Negotiate",
  "roles": [
    { "name":"Consumer", "alias":"C" },
    { "name":"Producer", "alias":"P" }
  ],
  "body": [
    { "kind":"message",  "name":"propose", "from":"C","to":"P","payload":"int" },
    {
      "kind":"rec", "label":"X", "body":[
        {
          "kind":"choice","at":"P","options":[
            [ { "kind":"message","name":"accept","from":"P","to":"C","payload":"" },
              { "kind":"message","name":"confirm","from":"C","to":"P","payload":"" } ],
            [ { "kind":"message","name":"reject","from":"P","to":"C","payload":"" } ],
            [ { "kind":"message","name":"propose","from":"P","to":"C","payload":"int" },
              {
                "kind":"choice","at":"C","options":[
                  [ { "kind":"message","name":"accept","from":"C","to":"P","payload":"" },
                    { "kind":"message","name":"confirm","from":"P","to":"C","payload":"" } ],
                  [ { "kind":"message","name":"reject","from":"C","to":"P","payload":"" } ],
                  [ { "kind":"message","name":"propose","from":"C","to":"P","payload":"" },
                    { "kind":"continue","label":"X" } ]
                ]
              }
            ]
          ]
        }
      ]
    }
  ]
}
'''

proto = json.loads(json_str)
scribble_code = json_to_scribble(proto)
print(scribble_code)