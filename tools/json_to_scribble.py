from typing import Any # for type annotation

def json_to_scribble_func(path:str, proto:Any, schemas:tuple[dict[str, Any], dict[str, Any]]):
    '''
    Creates a scr file with a global Scribble protocol based on a JSON describing said protocol.

        Args:
            path(str): path to protocols folder in proxy
            proto(Any): the JSON body that describes the protocol
            schemas(tuple[dict[str, Any]): a tuple of dicts that contain the schemas of the built in and custom schema types
    '''

    # create file and write to it
    with open(f"{path}/{proto['protocol']}.scr", "w") as scr_file:
        scr_file.write(f"module {proto['protocol']};\n\n") # module name
        # write types
        for a in schemas[0].keys(): # first default types
            scr_file.write(f'type <builtin> "{a}" from "builtin" as {a};\n')
        if (len(schemas) > 1): # then custom types, if any
            for a in schemas[1].keys(): # first default types
                scr_file.write(f'type <custom> "{a}" from "custom" as {a};\n')
        scr_file.write('\n')
        roles_str = ", ".join(f"role {r['name']} as {r['alias']}" for r in proto["roles"])
        scr_file.write(f"global protocol {proto['protocol']}({roles_str})\n")
        scr_file.write('{\n')

        tabs = 3 # increase
        def define_body(tabs:int, body:Any):
            for b in body:
                if b["kind"] == "message":
                    scr_file.write(f'{" "*tabs}{b["name"]}({b["payload"]}) from {b["from"]} to {b["to"]};\n')
                elif b["kind"] == "choice":
                    scr_file.write(f'{" "*tabs}choice at {b["at"]}\n')
                    scr_file.write(f'{" "*tabs}' + '{\n')
                    tabs += 3
                    options = b["options"]
                    for i, opt in enumerate(options):
                        if i:
                            scr_file.write(f'{" "*(tabs - 3)}' + '} or {\n') # only or if it's not alst one; -3 because lined up with choice word
                        define_body(tabs, opt)
                    tabs -= 3
                    scr_file.write(f'{" "*tabs}' + '}\n')
                elif b["kind"] == "rec":
                    scr_file.write(f'{" "*tabs}rec {b["label"]}' + ' {\n')
                    tabs += 3
                    define_body(tabs, b["body"])
                    tabs -= 3
                    scr_file.write(f'{" "*tabs}' + '}\n')
                elif b["kind"] == "continue":
                    scr_file.write(f'{" "*tabs}continue {b["label"]};\n')
                
        # recursively define the scr
        define_body(tabs, proto["body"])
        scr_file.write('}')