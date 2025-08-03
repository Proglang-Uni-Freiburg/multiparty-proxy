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
    def __init__(self, actor:str, alternatives: list[list[Session]], cont:Session):
        super().__init__("choice") # kind
        self.alternatives = alternatives
        self.cont = cont

    def update_conts(self):
        for item in self.alternatives:
            if not isinstance(item, Ref):
                item[-1].cont = self.cont
    

@dataclass
class Rec(Session):
    def __init__(self, actions: list[Session], cont:Session): # should Label be there? How to label?
        super().__init__("rec") # kind
        self.actions = actions
        self.cont = cont
    
    def update_conts(self):
        for i in range(0, self.actions - 2):
            if not isinstance(self.actions[i], Ref):
                self.actions[i].cont = self.actions[i+1]
        # last one's cont should be rec's cont? check later
        self.actions[-1].cont = self.cont
        
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

class ErrorInSessionDicts(Exception):
    """Raised when a lookup or addition for a label or session reference fails."""
    def __init__(self, function:str, name: str, context: str = "Unknown"):
        super().__init__(f"{function} failed for '{name}' in {context}")

# for general errors in session
class SessionError(Exception):
    pass