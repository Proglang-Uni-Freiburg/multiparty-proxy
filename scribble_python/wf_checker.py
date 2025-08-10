# to access other files in the project
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scribble_python" / "src"
PARSER_DIR = SRC / "run" / "parser"
SCRIBBLE_SRC = SRC / "scribble"
sys.path.insert(0, str(SRC))

from scribble.main import main as _scribble_main


def check_well_formedness(scr_path: str) -> None:
    '''
    Checks a Scribble protocol is written correctly by using the official Scribble well-formedness checker code.

        Args:
            scr_path(): where the scr file of the protocol we want to check can be found
    '''
    old_argv = sys.argv.copy()
    try:
        argv = ["scribblec",
                "-ip", str(PARSER_DIR),
                "-ip", str(SCRIBBLE_SRC),
               ]
        argv += [str(scr_path)]
        sys.argv[:] = argv
        try:
            _scribble_main(sys.argv)
        except SystemExit as e:
            raise WellFormednessError("Protocol is not well-formed") from e
    finally:
        sys.argv[:] = old_argv

def project_protocol(
    scr_path: str,
    full_global: str,
    role: str,
    output_dir: str
) -> None:
    '''
    Using the official Scribble code to project a protocol and create a scr file with the local protocol corresponding to a specific actor.

        Args:
            scr_path(): where the scr file of the global protocol can be found
            full_global(): name of the protocol we will write on the file, according to Scribble specifications
            role(): name of the role of the actor for which we want to make a local protocol
            output_dir(): where to write the scr file with the protocol to
    '''
    old_argv = sys.argv.copy()
    try:
        argv = ["scribblec",
                "-ip", str(PARSER_DIR),
                "-ip", str(SCRIBBLE_SRC),
               ]
        argv += [str(scr_path),
                 "-project", full_global, role,
                 "-o", output_dir]
        sys.argv[:] = argv
        _scribble_main(sys.argv)
    finally:
        sys.argv[:] = old_argv


class WellFormednessError(Exception): # TODO: write properly
    """Raised when a Scribble protocol is not well-formed."""
    pass
