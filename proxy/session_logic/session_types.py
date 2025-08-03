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
        self.kind = kind # options: message (would be single), choice, rec (recursive) but idk if recursive counts?

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
    def __init__(self, actor:str, alternatives: list[list[Session]], cont:Session): # should Label be there? How to label?
        super().__init__("choice") # kind
        self.alternatives = alternatives
        self.cont = cont
    
    
    """
    def add(self, index:int, new_ses: Session):
        if self.alternatives[index]:
            self.alternatives[index].add[new_ses]
        else:
            self.alternatives.add[[new_ses]]
    """

    def update_conts(self):
        for item in self.alternatives:
            if not isinstance(item, Ref()):
                item[-1].cont = self.cont
    

@dataclass
class Rec(Session):
    def __init__(self, actions: list[Session]): # should Label be there? How to label?
        super().__init__("rec") # kind
        self.actions = actions
        # cont = self?

"""
@dataclass
class Def(Session):
    def __init__(self, name: str, cont: Session):
        super().__init__("def")
        self.name = name
        self.cont = cont
"""
        
@dataclass
class Ref(Session):
    def __init__(self, name: str):
        super().__init__("ref")
        self.name = name

        
@dataclass
class End(Session):
    def __init__(self):
        super().__init__("end")


# --- define session dictionary --------------------------------------------------------------------------------------
        
"""
# global dictionary to keep info about protocols and sessions
class GlobalDict:
    def __init__(self, records: Dict[str, Session]):
        self.dir = dir
        self.records = records
    
    def add(self, def_ses:Def):
        '''
        Adds a new protocol to the global dicitonary of protocols.

            Args:
                def_ses (Def): def session that works as protocol
            
        Returns nothing if it works.
        '''
        if def_ses.name in self.records:
            raise ErrorInSessionDicts("add protcol", def_ses.name, context="GlobalDict")
        else:
            print(f"Defining protocol {def_ses.name}...") # to track what proxy is doing at moment -> could be removed
            self.records[def_ses.name] = def_ses.cont
    
    def lookup(self, name: str) -> Session:
        '''
        Function that returns a protocol's session, usually in the form of a Choice session

            Args:
                name (Label): name of the protocol

            Returns:
                A protocol's session if found in the global dictionary or nothing otherwise.
        '''
        # print(f"Looking for label: {name} in dictionary...") # comment out to debug
        if not name in self.records:
            raise ErrorInSessionDicts("Lookup", name, "GlobalDict") # not handled as exception but could be
        else:
            return self.records[name]
"""
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