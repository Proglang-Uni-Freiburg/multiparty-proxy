from typing import Dict
from dataclasses import dataclass # so that @dataclass(frozen=true) can be used

# -- define session components "dir" and "label" --------------------------------------------------------------------------
class Dir:
    def __init__(self, dir: str):
        self.dir = dir # only send or recv

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
    def __init__(self, kind: str):
        self.kind = kind # options: message (would be single), choice, rec (recursive)

@dataclass
class Message(Session):
    def __init__(self, dir:Dir, name:Label, actor:str, payload:str, cont:Session):
        #!: some messages might say same name but be from/to different actors
        super().__init__("single")
        self.label = name
        self.dir = dir
        self.actor = actor # other actor with which interaction happens
        self.payload = payload
        self.cont = cont

@dataclass
class Choice(Session):
    # actor is for "choice at __" -> check if it is self
    def __init__(self, actor:str, alternatives: list[list[Session]], cont:Session, actors_involved:list[str]=[]):
        super().__init__("choice") # kind
        self.actor = actor # actor that chooses which branch to take
        self.alternatives = alternatives
        self.cont = cont
        self.actors_involved = actors_involved # initialize and will later be rewritten

    def update_conts(self):
        for item in self.alternatives:
            # blocks of actions
            for i in range(0, len(item) - 1): # all except the last one
                if not isinstance(item, Ref):
                    item[i].cont = item[i+1]
        # last item in each action block cont should be None -> that way we know we have to go back to choice, close it and go to its cont
    
    def update_actors_involved(self):
        actors = []
        for item in self.alternatives:
            for i in item:
                if isinstance(i, Choice) or isinstance(i, Message): # ref and rec don't have actor
                    if i.actor not in actors:
                        actors.append(i.actor)
        self.actors_involved = actors



@dataclass
class Rec(Session):
    def __init__(self, label, actions: list[Session], cont:Session): # should Label be there? How to label?
        super().__init__("rec") # kind
        self.label = label
        self.actions = actions
        self.cont = cont
    
    # should test that it works ok!
    def update_conts(self):
        for i in range(0, len(self.actions) - 1): # is -1 ok?
            if not isinstance(self.actions[i], Ref):
                self.actions[i].cont = self.actions[i+1]
        # last one's cont should be None -> that way we know we have to go back to rec, close it and go to its cont
    

        
@dataclass
class Ref(Session):
    def __init__(self, name: str):
        super().__init__("ref")
        self.name = name
        
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

# for general errors in session
class SessionError(Exception):
    pass