import json

def json_to_scribble(proto):
    lines = []
    lines.append(f"module Example;")
    lines.append("")
    roles = ", ".join([f'role {r["name"]} as {r["alias"]}' for r in proto["roles"]])
    lines.append(f'global protocol {proto["protocol"]}({roles})')
    lines.append("{")
    lines += walk_body(proto["body"], indent=1)
    lines.append("}")
    return "\n".join(lines)

def walk_body(body, indent=1):
    lines = []
    ind = "\t" * indent
    for item in body:
        kind = item["kind"]
        if kind == "message":
            payload = f'({item["payload"]})' if item["payload"] else "()"
            lines.append(f'{ind}{item["name"]}{payload} from {item["from"]} to {item["to"]};')
        elif kind == "rec":
            lines.append(f'{ind}rec {item["label"]} {{')
            lines += walk_body(item["body"], indent+1)
            lines.append(f'{ind}}}')
        elif kind == "choice":
            lines.append(f'{ind}choice at {item["at"]}')
            lines.append(f'{ind}' + "{")
            for idx, option in enumerate(item["options"]):
                lines += walk_body(option, indent+1)
                if idx < len(item["options"])-1:
                    lines.append(f'{ind}}} or {{')
            lines.append(f'{ind}}}')
        elif kind == "continue":
            lines.append(f'{ind}continue {item["label"]};')
    return lines

# Example usage with a Python dict:
if __name__ == "__main__":
    proto = {
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
    scribble_code = json_to_scribble(proto)
    with open("output.scr", "w") as f:
        f.write(scribble_code)
    print("Scribble protocol written to output.scr")
    print("--- Scribble code ---")
    print(scribble_code)