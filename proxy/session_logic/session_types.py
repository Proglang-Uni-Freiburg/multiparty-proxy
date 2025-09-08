from dataclasses import dataclass # so that @dataclass(frozen=true) can be used

# -- define session components "dir" and "label" --------------------------------------------------------------------------
class Dir:
    def __init__(self, dir: str):
        self.dir = dir # TODO: make only "to" and "from"

    # to make it work with session to string parser
    def __str__(self):
        return self.dir

    def __repr__(self):
        return self.dir

@dataclass(frozen=True)
class Label:
    label: str


# -- define session and session types ---------------------------------------------------------------------------------
class Session:
    def __init__(self, kind:str="none"):
        self.kind = kind # options: message (would be single), choice, rec (recursive), ref (reference to a recursive one)

@dataclass
class Message(Session):
    def __init__(self, dir:Dir, name:Label, actor:str, payload:str, cont:Session|None):
        #!: some messages might have the same name but be from/to different actors amd have different payloads
        super().__init__("message")
        self.label = name
        self.dir = dir
        self.actor = actor # other actor with which interaction happens
        self.payload = payload
        self.cont = cont

@dataclass
class Choice(Session):
    # actor is for "choice at __"
    def __init__(self, actor:str, alternatives: list[list[Session]], cont:Session|None, actors_involved:list[str]=[], errors:list[str]=[]):
        super().__init__("choice") # kind
        self.actor = actor # actor that chooses which branch to take
        self.alternatives = alternatives
        self.cont = cont
        self.actors_involved = actors_involved # initialize and will later be rewritten
        self.errors = errors

    def update_conts(self):
        """
        Joins all sessions in a choice alternatives 'set' together by defining their 'conts'.

        This does not apply to the last one, that need to remain as a None; that way we know we have to go back to choice,
        close it and go to its cont.
        """
        for item in self.alternatives:
            # blocks of actions
            for i in range(0, len(item) - 1): # all except the last one in each "set" of options
                if not isinstance(item, Ref):
                    item_indexed = item[i]
                    if isinstance (item_indexed, (Rec, Choice, Message)): # so type checker makes sure it'll have attribute cont
                        item_indexed.cont = item[i+1]
    
    def update_actors_involved(self):
        actors:list[str] = []
        for item in self.alternatives:
            for i in item:
                if isinstance(i, Choice) or isinstance(i, Message): # ref and rec don't have actor
                    if i.actor not in actors:
                        actors.append(i.actor)
        self.actors_involved = actors

    def update_error_handling(self):
        errors_handled:list[str] = []
        for item in self.alternatives:
            elem = item[0]
            if isinstance(elem, Message):
                if elem.label.label == "timeout":
                    errors_handled.append("timeout")
                elif elem.label.label == "wrongPayload":
                    errors_handled.append("wrongPayload")
                elif elem.label.label == "wrongPayload":
                    errors_handled.append("wrongLabel")
                elif elem.label.label == "error":
                    errors_handled.append("error")
        self.errors = errors_handled


@dataclass
class Rec(Session):
    def __init__(self, label:Label, actions: list[Session], cont:Session|None): # should Label be there? How to label?
        super().__init__("rec") # kind
        self.label = label
        self.actions = actions
        self.cont = cont
    
    def update_conts(self):
        """
        Joins all sessions in the session's actions element together by defining their 'conts'.

        This does not apply to the last one, that need to remain as a None; that way we know we have to go back to
        close the Rec session and go to its cont.
        """
        for i in range(0, len(self.actions) - 1): # is -1 ok?
            elem = self.actions[i]
            if isinstance(elem, (Rec, Message, Choice)): # so if not Ref or End
                elem.cont = self.actions[i+1]
        
@dataclass
class Ref(Session):
    def __init__(self, name: str):
        super().__init__("ref")
        self.name = name # name of Rec session we are referencing
        
@dataclass
class End(Session):
    def __init__(self):
        super().__init__("end")


# --- define errors and exceptions  --------------------------------------------------------------------------------------

class SchemaValidationError(Exception):
    """Exception raised for errors in schema validation."""
    def __init__(self, message:str="Schema validation failed"):
        self.message = message
        super().__init__(self.message)
    
class WrongLabelError(Exception):
    """Exception raised for when the name given for the message does not coincide with that of the session."""
    def __init__(self, message:str="Wrong message label"):
        self.message = message
        super().__init__(self.message)

class Timeout(Exception):
    """Exception raised when a client has exceeded the timeout limit"""
    def __init__(self, message:str="Client has timed out"):
        self.message = message
        super().__init__(self.message)

# for general errors in session
class SessionError(Exception):
    pass