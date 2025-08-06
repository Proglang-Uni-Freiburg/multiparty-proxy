# to be able to use modules from other files
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from session_logic.session_types import *
import re # for parsing sessions

from session_types import *

import re



#-- String <--> Session Parsers --------------------------------------------------------

def scr_into_session(path_to_scr) -> Session:
    with open(path_to_scr, 'r') as file:
        lines = file.readlines()


    doing:list[(Session, int)] = []
    one_ses:Session = None
    actual_ses:Session = None

    # for line in lines:
    while lines:
        line = lines[0]
 
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
                actor = match.group(1)
                # print(f"defining actor for choice: {actor}") # debug
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
                name = match.group(1)
                current_rec = Rec(name, [], None)
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
            
        # message to
        elif "to" in line:
            pattern = r"(\w+)\(([^)]*)\) to (\w+);"
            match = re.match(pattern, line)
            if match:
                name, payload, actor = match.groups()
                if not doing: # if not inside any rec or choice
                    if one_ses:
                        actual_ses.cont = Message(Dir("to"), Label(name), actor, payload, None)
                        if isinstance(actual_ses, Choice):
                            actual_ses.update_conts()
                        actual_ses = actual_ses.cont
                    else:
                        one_ses = Message(Dir("to"), Label(name), actor, payload, None)
                        actual_ses = one_ses
                elif isinstance(doing[-1][0], Rec):
                    doing[-1][0].actions.append(Message(Dir("to"), Label(name), actor, payload, None))
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
                    choice.alternatives[branch].append(Message(Dir("to"), Label(name), actor, payload, None))
            lines = lines[1:]
        
        # message from
        elif "from" in line:
            pattern = r"(\w+)\(([^)]*)\) from (\w+);"
            match = re.match(pattern, line)
            if match:
                name, payload, actor = match.groups()
                if not doing: # if not inside any rec or choice
                    if one_ses:
                        actual_ses.cont = Message(Dir("from"), Label(name), actor, payload, None)
                        if isinstance(actual_ses, Choice):
                            actual_ses.update_conts()
                        actual_ses = actual_ses.cont
                    else:
                        one_ses = Message(Dir("from"), Label(name), actor, payload, None)
                        actual_ses = one_ses
                elif isinstance(doing[-1][0], Rec):
                    doing[-1][0].actions.append(Message(Dir("from"), Label(name), actor, payload, None))
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
                    choice.alternatives[branch].append(Message(Dir("from"), Label(name), actor, payload, None))
            lines = lines[1:] 

        # ref
        elif "continue" in line:
            pattern = r"continue (\w+);"
            match = re.match(pattern, line)
            if match:
                name = match.group(1)
                if isinstance(doing[-1][0], Rec):
                    doing[-1][0].actions.append(Ref(name))
                if isinstance(doing[-1][0], Choice):
                    if doing[-1][0].alternatives is not None:
                        doing[-1][0].alternatives[doing[-1][1]].append(Ref(name))
                    else:
                        doing[-1][0].alternatives = [[Ref(name)]]
            lines = lines[1:]

        # check if we move to different options in choice
        if "or" in line:
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
                lines = lines[1:]
                continue # because that just means we are closing one option in choice before going to the next
            if doing:
                if doing:
                    # trigger function that joins actions with cont
                    doing[-1][0].update_conts()
                    if isinstance(doing[-1][0], Choice):
                        doing[-1][0].update_actors_involved()
                    doing.pop()
            # otherwise we can just skip it
            lines = lines[1:]

    return one_ses
    
    
# define custom exceptions for parsing errors
class ParsingError(Exception):
    """Exception raised for errors in parsing"""
    def __init__(self, message:str="Parsing failed"):
        self.message = message
        super().__init__(self.message)

# for debugging
# if __name__ == "__main__":
#    print(scr_into_session(r"C:\Users\andre\Documents\Uni_Freiburg\SS_25\Bachelorarbeit\multiparty-proxy\proxy\protocols\Negotiate\Consumer.scr\Negotiate_Negotiate_Consumer.scr"))