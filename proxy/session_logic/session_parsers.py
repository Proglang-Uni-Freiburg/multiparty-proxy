# to be able to use modules from other files
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from session_logic.session_types import *
import re # for parsing sessions
from typing import Any, Literal, Union, cast # for type definition

import json

from session_types import *

import re



#-- String <--> Session Parsers --------------------------------------------------------

def scr_into_session(path_to_scr) -> Session:
    with open(path_to_scr, 'r') as file:
        lines = file.readlines()
    '''
    '''

    # line one: module -> ignore
    # ignore all empty spaces
    # next lines: types -> for now, ignore type lines
    # next line: protocol, participants -> ignore too for now (we know our participant with keywords to/from etc) -> except when it has to make a choice! Then maybe pass on name??
    # so really, just start reading from when '{' starts
    # maybe there is a way to eliminate all empty lines?
    # message structure: func_name(payload_type) from NAME; // func_name(payload_type) to NAME;
    # we need a way to keep track of open parenthesis (to track when stuff like rec etc ends)
    # rec structure: rec NAME
    #   {
    #   .... (actions)
    #       if rec is called in any of these actions, then it should have the rec as their continue -> so when transforming to session, we have to keep track of the rec so we can reference it if we need to
    #   }
    # choice structure: choice at NAME
    #   {
    #   .... (actions)
    #   }
    #   or
    #   {
    #   .... (actions)
    #   }
    #   or
    #   .... etc
    #   so it ends when there are no more ors after a }
    #   plus at the end of each last action inside a {} (so before }) make it's continue the continue of choice, so we can keep going
    # ends in }
    # the problem is that if we ACTUALLY declar rec recursively, then we'll never escape definition :(


    # trial: list of actions
    doing:list[(Session, int)] = []
    one_ses:Session = None
    actual_ses:Session = None

    # for line in lines:
    while lines:
        line = lines[0]
        print(line) # debug
        print(one_ses) # debug
        print(actual_ses) # debug
        print(doing)

        # skip types etc for now
        if line.startswith(("type", "module", "local")):
            lines = lines[1:]
            continue

        # skip empty lines
        elif line in ['\n', '\r\n']:
            lines = lines[1:]
            continue

        # choice
        elif "at" in line:
            pattern = r"choice at (\w+)"
            match = re.match(pattern, line)
            if match:
                print("match at") # debug
                actor = match.groups()
                current_choice = Choice(actor, [], None)
                if not doing: # if not inside any rec or choice
                    if one_ses:
                        actual_ses.cont = current_choice
                        if isinstance(actual_ses, Choice):
                            actual_ses.update_conts()
                        actual_ses = actual_ses.cont
                    else:
                        one_ses = current_choice
                        actual_ses = one_ses
                elif isinstance(doing[-1][0], Rec):
                    doing[-1][0].actions.append(current_choice)
                elif isinstance(doing[-1][0], Choice):
                    choice = doing[-1][0]
                    branch = doing[-1][1]

                    # If we’ve never set alternatives at all, start with one empty branch
                    if choice.alternatives is None:
                        choice.alternatives = [[]]

                    # If this branch index is beyond current length, extend with empty lists
                    while len(choice.alternatives) <= branch:
                        choice.alternatives.append([])

                    # Now it's safe to append to the correct branch
                    choice.alternatives[branch].append(current_choice)
                doing.append((current_choice, 0))
                lines = lines[2:]

        # rec
        elif "rec" in line:
            pattern = r"rec (\w+)"
            match = re.match(pattern, line)
            if match:
                print("match rec") # debug
                name = match.groups()
                current_rec = Rec([], None)
                if not doing: # if not inside any rec or choice
                    if one_ses:
                        actual_ses.cont = current_rec
                        if isinstance(actual_ses, Choice):
                            actual_ses.update_conts()
                        actual_ses = actual_ses.cont
                    else:
                        one_ses = current_rec
                        actual_ses = one_ses
                elif isinstance(doing[-1][0], Rec):
                    doing[-1][0].actions.append(current_rec)
                elif isinstance(doing[-1][0], Choice):
                    choice = doing[-1][0]
                    branch = doing[-1][1]

                    # If we’ve never set alternatives at all, start with one empty branch
                    if choice.alternatives is None:
                        choice.alternatives = [[]]

                    # If this branch index is beyond current length, extend with empty lists
                    while len(choice.alternatives) <= branch:
                        choice.alternatives.append([])

                    # Now it's safe to append to the correct branch
                    choice.alternatives[branch].append(current_rec)
                doing.append((current_rec, 0))
                lines = lines[2:]

            """
                doing.append((current_rec, 0))
                print("appended rec") # debug
            if one_ses is None:
                one_ses = current_rec
            else:
                actual_ses.cont = current_rec
                actual_ses = current_rec
            lines = lines[2:] # skip both rec line AND first {
            """
            
        # message to
        elif "to" in line:
            pattern = r"(\w+)\(([^)]*)\) to (\w+);"
            match = re.match(pattern, line)
            if match:
                print("match to") # debug
                name, payload, actor = match.groups()
                if not doing: # if not inside any rec or choice
                    if one_ses:
                        actual_ses.cont = Message(Dir("send"), Label(name), actor, payload, None)
                        if isinstance(actual_ses, Choice):
                            actual_ses.update_conts()
                        actual_ses = actual_ses.cont
                    else:
                        one_ses = Message(Dir("send"), Label(name), actor, payload, None)
                        actual_ses = one_ses
                elif isinstance(doing[-1][0], Rec):
                    doing[-1][0].actions.append(Message(Dir("send"), Label(name), actor, payload, None))
                elif isinstance(doing[-1][0], Choice):
                    choice = doing[-1][0]
                    branch = doing[-1][1]

                    # If we’ve never set alternatives at all, start with one empty branch
                    if choice.alternatives is None:
                        choice.alternatives = [[]]

                    # If this branch index is beyond current length, extend with empty lists
                    while len(choice.alternatives) <= branch:
                        choice.alternatives.append([])

                    # Now it's safe to append to the correct branch
                    choice.alternatives[branch].append(Message(Dir("recv"), Label(name), actor, payload, None))
            lines = lines[1:]
        
        # message from
        elif "from" in line:
            pattern = r"(\w+)\(([^)]*)\) from (\w+);"
            match = re.match(pattern, line)
            if match:
                print("match from") # debug
                name, payload, actor = match.groups()
                if not doing: # if not inside any rec or choice
                    if one_ses:
                        actual_ses.cont = Message(Dir("recv"), Label(name), actor, payload, None)
                        if isinstance(actual_ses, Choice):
                            actual_ses.update_conts()
                        actual_ses = actual_ses.cont
                    else:
                        one_ses = Message(Dir("recv"), Label(name), actor, payload, None)
                        actual_ses = one_ses
                elif isinstance(doing[-1][0], Rec):
                    doing[-1][0].actions.append(Message(Dir("recv"), Label(name), actor, payload, None))
                elif isinstance(doing[-1][0], Choice):
                    print("choice from") # debug
                    choice = doing[-1][0]
                    branch = doing[-1][1]

                    # If we’ve never set alternatives at all, start with one empty branch
                    if choice.alternatives is None:
                        choice.alternatives = [[]]

                    # If this branch index is beyond current length, extend with empty lists
                    while len(choice.alternatives) <= branch:
                        choice.alternatives.append([])

                    # Now it's safe to append to the correct branch
                    choice.alternatives[branch].append(Message(Dir("recv"), Label(name), actor, payload, None))
                    print(choice.alternatives) # debug
            lines = lines[1:] 

        # ref
        elif "continue" in line:
            pattern = r"continue (\w+);"
            match = re.match(pattern, line)
            if match:
                print("match continue") # debug
                name = match.groups()
                if isinstance(doing[-1][0], Rec):
                    doing[-1][0].actions.append(Message(dir("recv"), Label(name), actor, payload, None))
                if isinstance(doing[-1][0], Choice):
                    if doing[-1][0].alternatives is not None:
                        doing[-1][0].alternatives[doing[-1][1]].append(Ref(name))
                    else:
                        doing[-1][0].alternatives = [[Ref(name)]]
            lines = lines[1:]

        # check if we move to different options in choice
        if "or" in line:
            print(f"doing: {doing}") # debug
            # find index of last occurence of choice
            for i, (sess, branch_idx) in reversed(list(enumerate(doing))):
                if isinstance(sess, Choice):
                    last_choice_index = i
                    break
            doing[last_choice_index] = (doing[last_choice_index][0], doing[last_choice_index][1] + 1)
            lines = lines[2:] # skip or and {
        
        # close the latest choice or rec
        if "}" in line:
            if len(lines) == 1:
                actual_ses.cont = End()
            elif "or" in lines[1]:
                print("line has or") # debug
                pass # because that just means we are closing one option in choice ebfore going to the next
            elif doing:
                if doing:
                    # trigger function that joins actions with cont
                    doing[-1][0].update_conts()
                    doing.pop()
                    lines = lines[1:]
                print("erased rec or choice") # debug
            # otherwise we can just skip it
            lines = lines[1:]

    return one_ses


if __name__ == "__main__":
    print(scr_into_session(r"C:\Users\andre\Documents\Uni_Freiburg\SS_25\Bachelorarbeit\multiparty-proxy\proxy\protocols\Negotiate\Consumer.scr\Negotiate_Negotiate_Consumer.scr").cont.actions[0].cont)
    print("done") # debug

    


    """
    if ses_info.startswith("Session: "):
        ses_info = ses_info[9:] # split string to figure out which kind of session
        # print(f"Parsing session {ses_info}...") # comment out for debugging

        # single session
        if ses_info.startswith("Single"):
            # pattern for normal client-server proxy
            pattern = r"Single, Dir: (.*?), Payload: (.*?), Cont: (.*)"
            match = re.match(pattern, ses_info)

            # pattern for multiparty proxy
            patternMulti = r"Single, Dir: (.*?), Actor: (.*?), Payload: (.*?), Cont: (.*)"
            matchMulti = re.match(patternMulti, ses_info)

            if matchMulti:
                dir_given, actor_given, pay_given, cont_ses = matchMulti.groups()
                #return single session and parse the cont str to make it a session too
                session_changed = Single(dir=Dir(dir_given), actor=actor_given, payload=pay_given, cont=message_into_session(cont_ses, type_socket))
            elif match:
                dir_given, pay_given, cont_ses = match.groups()
                match (dir_given, type_socket):
                    case ("send", "server"):
                        dir_given = "send"
                    case ("send", "client"):
                        dir_given = "recv"
                    case ("recv", "server"):
                        dir_given = "recv"
                    case ("recv", "client"):
                        dir_given = "send"
                    case _:
                        print("Error: invalid direction given") # not handled as exception but could be
                #return single session and parse the cont str to make it a session too
                session_changed = Single(dir=Dir(dir_given), payload=pay_given, cont=message_into_session(cont_ses, type_socket))
            else:
                raise SessionError("Error parsing message into session: wrong syntax")

        # def session; uses type_socket parameter
        elif ses_info.startswith("Def"):
            pattern = r"Def, Name: (.*?), Cont: (.*)"
            match = re.match(pattern, ses_info)
            if match:
                name_given, cont_ses = match.groups()
                # print(f"Parsing protocol {name_given}") # comment put to debug
                # recursively parse choice sessions defined in protocol with "cont"
                if type_socket != "":
                    session_changed = Def(name=f"{name_given}_{type_socket}", cont=message_into_session(cont_ses, type_socket))
                else:
                    session_changed = Def(name=f"{name_given}", cont=message_into_session(cont_ses, type_socket))
            else:
                raise SessionError("Error parsing message into session: wrong syntax")

        # ref session
        elif ses_info.startswith("Ref"):
            if ses_info.startswith("Ref, Name: "):
                name_given = ses_info[11:] # references protocol name
                session_changed = Ref(name=f"{name_given}_{type_socket}")
            else:
                raise SessionError("Error parsing message into session: wrong syntax")

        # choice session
        # Idea: session would look like: Session: Choice, Dir: send, Alternatives: [{Label: append, Session: Single, }]
        elif ses_info.startswith("Choice"):
            pattern = r"Choice, Dir: (.*?), Alternatives: \[(.*)\]" # alternatives like that so it's dict
            match = re.match(pattern, ses_info)
            if match:
                dir_given, alternatives_given = match.groups()
                # parse alternatives
                alternatives_parsed = {} # to keep track of all sessions in alternatives dictionay
                alt_matches = re.findall(r"\(Label: (.*?), Session: (.*?)\)", alternatives_given) # find all things with this structure in alternatives
                for label, alt_session in alt_matches:
                    # Parse each alternative's session recursively
                    alternatives_parsed[Label(label.strip())] = message_into_session(f"Session: {alt_session.strip()}", type_socket)
                alternatives_parsed:Dict[Label, Session] # in order for the creation of Choice to be ok
                session_changed = Choice(dir=Dir(dir_given), alternatives=alternatives_parsed)
            else:
                raise SessionError("Error parsing message into session: wrong syntax")
        # end session
        elif ses_info == "End":
            session_changed = End()
        # if no cases match
        else:
            raise SessionError("Error parsing session")
        # return resulting session
        return session_changed
    else:
        raise SessionError("Error parsing session")
    """
        
# do i actually need a session into scr? I find that probably unnecessary
"""
def session_into_message(session: Session) -> str:
    '''
    Serializes a Session object into a string.
    
        Args:
            session (Session): the session object to serialize
        
        Returns:
            str: string representation of the session
    '''
    if isinstance(session, Single):
        if session.actor:
            return (
                f"Session: Single, Dir: {session.dir}, Actor: {session.actor}, Payload: {session.payload}, "
                f"Cont: {session_into_message(session.cont)}"
            )
        else:
            return (
                f"Session: Single, Dir: {session.dir}, Payload: {session.payload}, "
                f"Cont: {session_into_message(session.cont)}"
            )
    
    elif isinstance(session, Def):
        return (
            f"Session: Def, Name: {session.name}, Cont: {session_into_message(session.cont)}"
        )
    
    elif isinstance(session, Ref):
        return f"Session: Ref, Name: {session.name}"
    
    elif isinstance(session, Choice):
        alternatives: list[str] = []
        for label_given, alt_session in session.alternatives.items():
            alt_str = (
                f"(Label: {label_given.label}, Session: {session_into_message(alt_session)[9:]})"
            )
            alternatives.append(alt_str)
        return (
            f"Session: Choice, Dir: {session.dir}, Alternatives: [{', '.join(alternatives)}]"
        )
    
    elif isinstance(session, End):
        return "Session: End"
    
    else:
        raise ValueError("Unknown session type")


#-- Create payload string easier --------------------------------------------------------

# Literals for allowed parameter strings
AllTypes = Literal["bool", "string", "none", "number", "array", "tuple", "union", "def", "record"]
PayloadTypes = Union[AllTypes, list[AllTypes], None]

def payload_to_string(type_str:AllTypes, payload:PayloadTypes=None) -> str:
    '''
    Create a string that represents a payload that can be given to session declarations.

    Note:
    - AllTypes type is any of these strings: "bool", "string", "none", "number", "array", "tuple", "union", "def", "record"
    - PayloadTypes is any of the AllTypes string or a list containing any of them
        
        Args:
            type_str (AllTypes): string saying which allowed payload type will be created
            payload (PayloadTypes=None): optional string or list of strings describing extra payloads (for tupless, arrays, unions and records)
        
        Returns:
            str: string representation of the payload
    '''
    match type_str:
        case "bool":
            return '{ type: "bool" }'
        case "string":
            return '{ type: "string" }'
        case "none":
            return '{ type: "null" }'
        case "number":
            return '{ type: "number" }'
        case "array":
            if isinstance(payload, str): # checking array only accepts ONE payload type
                return f'{{ type: "array", payload: {payload_to_string(type_str=payload)} }}'
            else:
                raise ParsingError("Array payload can only be of one type")
        case ("tuple" | "union" | "record"):
            if isinstance(payload, list):
                elements = [payload_to_string(i) for i in payload] # get all types of payloads inside
                if type_str == "union": # check no types are repeated for unions
                    elements = list(dict.fromkeys(elements)) # removes duplicates in list while preserving order
                return f'{{ type: "{type_str}", payload: [' + ", ".join(elements) + '] }'
            else:
                raise ParsingError("Payload has to be given as a list")
        case "def":
            if isinstance(payload, str): # checking array only accepts ONE payload type
                return f'{{ type: "def", name: {{ type: "string" }}, payload: {payload_to_string(type_str=payload)} }}'
            else:
                raise ParsingError("Def payload has to be given as a string")
        case _:
            raise ParsingError("This payload couldn't be turned into a string")
"""

    
# define custom exceptions for parsing errors
class ParsingError(Exception):
    """Exception raised for errors in parsing"""
    def __init__(self, message:str="Parsing failed"):
        self.message = message
        super().__init__(self.message)