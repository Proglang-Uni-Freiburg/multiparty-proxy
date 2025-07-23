import sys
from pathlib import Path
# from pathlib import Path

# Add the full absolute path to `run/parser`
# sys.path.append(str(Path(__file__).resolve().parent / "run" / "parser"))
from run.parser.ScribbleLexer import ScribbleLexer
from run.parser.ScribbleParser import ScribbleParser
from antlr3 import ANTLRFileStream, CommonTokenStream

input_file = str(Path(__file__).resolve().parent / "Negotiation1.scr")


# Create lexer and parser
char_stream = ANTLRFileStream(input_file)
lexer = ScribbleLexer(char_stream)
tokens = CommonTokenStream(lexer)
parser = ScribbleParser(tokens)

# This depends on your Scribble.g starting rule!
tree = parser.module()  # or parser.module_() if that's the top rule

print("Parsing complete.")

