import os # to find file

def json_to_scribble_func(proto, schemas):
    '''
    Creates a scr file with a global Scribble protocol based on a JSON describing said protocol.

        Args:
            proto(): the JSON body that describes the protocol
            schemas(): a dict* that contains all the custom types in a session (protocol) and the JSON schemas that describe them
    '''
    lines = []
    # Use protocol name as module name
    module_name = proto["protocol"]
    lines.append(f"module {module_name};")
    lines.append("")

    # Add builtin type declarations
    all_types = []
    for schema in schemas[0].keys(): # for basic python types
        all_types.append(f'type <builtin> "{schema}" from "builtin" as {schema};')
    if schemas[1]: # there could be no custom types
        for schema in schemas[1].keys(): # for custom types
            all_types.append(f'type <custom> "{schema}" from "custom" as {schema};')
    lines.extend(all_types)
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


def transform(proto, schemas, output_dir):
    '''
    Creates a scr file with a global Scribble protocol based on a JSON describing said protocol.

        Args:
            proto(): the JSON body that describes the protocol
            schemas(): a dict* that contains all the custom types in a session (protocol) and the JSON schemas that describe them
            output_dir: where scr file we be stored at
    '''
    scribble_code = json_to_scribble_func(proto, schemas)
    protocol_name = proto["protocol"]
    file_name = f"{protocol_name}.scr"
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)
    else:
        file_path = file_name

    # debug
    with open(file_path, "w") as f:
        f.write(scribble_code)
    print(f"Scribble protocol written to {file_path}")
    print("--- Scribble code ---")
    print(scribble_code)