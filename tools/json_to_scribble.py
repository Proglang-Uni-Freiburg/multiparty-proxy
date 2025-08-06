import json
import sys
import os

def json_to_scribble_func(proto, schemas):
    lines = []
    # Use protocol name as module name
    module_name = proto["protocol"]
    lines.append(f"module {module_name};")
    lines.append("")

     # Add builtin type declarations -> add a marker later for custom vs builtin
    builtin_types = []
    for schema in schemas:
        builtin_types.append(f'type <builtin> "{schema}" from "builtin" as {schema};')
    lines.extend(builtin_types)
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


def transform(proto, schemas, output_dir=None):
    scribble_code = json_to_scribble_func(proto, schemas)
    protocol_name = proto["protocol"]
    file_name = f"{protocol_name}.scr"
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name)
    else:
        file_path = file_name

     # Print the generated Scribble code for debugging
    print("--- Scribble code ---")
    print(scribble_code)
    print("--- End Scribble code ---")

    with open(file_path, "w") as f:
        f.write(scribble_code)
    print(f"Scribble protocol written to {file_path}")
    print("--- Scribble code ---")
    print(scribble_code)