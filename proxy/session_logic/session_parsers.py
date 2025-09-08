# to be able to use modules from other files
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# import information on sessions
from session_types import *

# for checking patterns in lines
import re

#-- Scribble Protocol scr file -> Session Parser --------------------------------------------------------

def scr_into_session(path_to_scr, error_mode:str) -> Session:
    '''
    Creates a Session object based on a projected Scribble local protocol.

        Args:
            path_to_scr(): the path to the scr file that contains the Scribble local protocol to be parsed

        Returns:
            A Session object, that might have other sessions chained by using the sessions' 'cont' property.
    '''
    try:
        # extract lines from scr file
        with open(path_to_scr, 'r') as file:
            lines = file.readlines()

        # initialize vars that will help us parse
        doing:list[tuple[Choice | Rec, int]] = [] # for open rec and choice sessions
        one_ses:Session= Session() # session we will return at end, from which the chaining of sessions with cont starts
        actual_ses:Session = Session()

        while lines:
            line = lines[0]

            # define patterns to recognize messages
            # "from" pattern for messages
            from_pattern = r"(\w+)\(([^)]*)\) from (\w+);"
            from_match = re.match(from_pattern, line)
            # "to" pattern for messages
            to_pattern = r"(\w+)\(([^)]*)\) to (\w+);"
            to_match = re.match(to_pattern, line)
    
            # possible types will be passed on as a schema from API to proxy so we don't need the type definitions here, so we skip them
            if line.startswith(("type", "module", "local")):
                lines = lines[1:]
                continue

            # skip empty lines
            elif line in ['\n', '\r\n']:
                lines = lines[1:]
                continue

            # TODO: Find a way to make code shorter, as some things are repeated a lot
            # choice
            elif line.startswith("choice"):
                pattern = r"choice at (\w+)"
                match = re.match(pattern, line)
                if match:
                    actor = match.group(1)
                    # print(f"defining actor for choice: {actor}") # debug
                    current_choice = Choice(actor, [], None)
                    if not doing: # if not inside any rec or choice
                        if one_ses.kind != "none": # if it is not the first session in the protocol
                            if isinstance(actual_ses, (Rec, Message, Choice)): # if it WILL have cont attribute
                                actual_ses.cont = current_choice
                                if isinstance(actual_ses, Choice):
                                    actual_ses.update_conts()
                                actual_ses = actual_ses.cont
                        else:
                            one_ses = current_choice
                            actual_ses = one_ses
                    elif isinstance(doing[-1][0], Rec): # if inside a rec
                        doing[-1][0].actions.append(current_choice)
                    elif isinstance(doing[-1][0], Choice): # if inside a choice
                        # TODO: better explanation of this process
                        choice = doing[-1][0]
                        branch = doing[-1][1]

                        # If we’ve never set alternatives at all, start with one empty branch
                        if choice.alternatives is None: # TODO: see if I can change this by just using [[]] when initializing choice
                            choice.alternatives = [[]]

                        # If this branch index is beyond current length, extend with empty lists
                        while len(choice.alternatives) <= branch:
                            choice.alternatives.append([])

                        # Now it's safe to append to the correct branch
                        choice.alternatives[branch].append(current_choice)
                    doing.append((current_choice, 0))
                    lines = lines[2:]

            # rec
            elif line.startswith("rec"):
                pattern = r"rec (\w+)"
                match = re.match(pattern, line)
                if match:
                    name = match.group(1)
                    current_rec = Rec(name, [], None)
                    if not doing: # if not inside any rec or choice
                        if one_ses.kind != "none":
                            actual_ses.cont = current_rec
                            if isinstance(actual_ses, Choice):
                                actual_ses.update_conts()
                            if isinstance(actual_ses, (Choice, Rec, Message)):
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
            elif to_match:
                name, payload, actor = to_match.groups()
                if not payload:
                    payload = "none"
                if not doing: # if not inside any rec or choice
                    if one_ses.kind != "none":
                        actual_ses.cont = Message(Dir("to"), Label(name), actor, payload, None)
                        if isinstance(actual_ses, Choice):
                            actual_ses.update_conts()
                        if isinstance(actual_ses, (Choice, Rec, Message)): # make sure it has cont attribute
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
            elif from_match:
                name, payload, actor = from_match.groups()
                if not payload:
                    payload = "none"
                if not doing: # if not inside any rec or choice
                    if one_ses.kind != "none":
                        actual_ses.cont = Message(Dir("from"), Label(name), actor, payload, None)
                        if isinstance(actual_ses, Choice):
                            actual_ses.update_conts()
                        if isinstance(actual_ses, (Choice, Rec, Message)):
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
            elif line.startswith("continue"):
                pattern = r"continue (\w+);"
                match = re.match(pattern, line)
                if match:
                    name = match.group(1)
                    doing_ses = doing[-1][0]
                    if isinstance(doing_ses, Rec):
                        doing_ses.actions.append(Ref(name))
                    if isinstance(doing_ses, Choice):
                        if doing_ses.alternatives is not None:
                            # -1 gets (Choice, Branch), so the [1] is to know in which Choice branch we are adding Sessions
                            doing_ses.alternatives[doing[-1][1]].append(Ref(name))
                        else:
                            doing_ses.alternatives = [[]]
                            doing_ses.alternatives[0].append(Ref(name))
                lines = lines[1:]

            # check if we move to different options in choice
            if line.strip() == "or":
                # find index of last occurence of choice
                for i, (sess, branch_idx) in reversed(list(enumerate(doing))):
                    if isinstance(sess, Choice):
                        last_choice_index = i
                        break
                else:
                    # if loop found no choice, then that means something went wrong, because the 'or'
                    #   indicated a choice should still be open
                    raise ParsingError("'or' found outside of an open 'choice'")
                doing[last_choice_index] = (doing[last_choice_index][0], doing[last_choice_index][1] + 1)
                lines = lines[2:] # skip or and {
            
            # close the latest choice or rec
            if "}" in line:
                if len(lines) == 1:
                    if isinstance(actual_ses, (Rec, Message, Choice)):
                        actual_ses.cont = End()
                elif "or" in lines[1]:
                    lines = lines[1:] # go to next line, consider the actual line as parsed
                    continue # because that just means we are closing one option in choice before going to the next
                if doing:
                    if doing:
                        doing[-1][0].update_conts() # trigger function that joins actions with cont
                        if isinstance(doing[-1][0], Choice): # for choice, add actors to list of actors mentioned in that choice
                            doing[-1][0].update_actors_involved()
                            if error_mode == "handle":
                                doing[-1][0].update_error_handling()
                        doing.pop()
                # otherwise we can just skip it
                lines = lines[1:]

        return one_ses
    except Exception as e:
        print(f"Error in scribble to session parser: {e}")
        raise ParsingError
    
    
# -- define custom exceptions for parsing errors ------------------------------------------------------------------------------------
class ParsingError(Exception):
    """Exception raised for errors in parsing"""
    def __init__(self, message:str="Parsing failed"):
        self.message = message
        super().__init__(self.message)

# for debugging
# if __name__ == "__main__":
#    print(scr_into_session(r"C:\Users\andre\Documents\Uni_Freiburg\SS_25\Bachelorarbeit\multiparty-proxy\proxy\protocols\Negotiate\Consumer.scr\Negotiate_Negotiate_Consumer.scr"))