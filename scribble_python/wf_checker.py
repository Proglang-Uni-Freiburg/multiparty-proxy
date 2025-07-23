# scribble_tools.py
import sys
from pathlib import Path

# Set project root as two levels up from this file

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scribble_python" / "src"
PARSER_DIR = SRC / "run" / "parser"
SCRIBBLE_SRC = SRC / "scribble"

# Add src to sys.path so you can import scribble.main
sys.path.insert(0, str(SRC))

from scribble.main import main as _scribble_main

# Add src to sys.path so you can import scribble.main
sys.path.insert(0, str(SRC))

def check_well_formedness(scr_path: str, extra_import_paths=None) -> None:
    """
    Raise SystemExit if scr_path isn’t well-formed (incl. reachability).
    Mirrors `scribblec -ip … scr_path`.
    """
    old_argv = sys.argv.copy()
    try:
        argv = ["scribblec",
                "-ip", str(PARSER_DIR),
                "-ip", str(SCRIBBLE_SRC),
               ]
        if extra_import_paths:
            for p in extra_import_paths:
                argv += ["-ip", str(p)]
        argv += [str(scr_path)]
        sys.argv[:] = argv
        _scribble_main(sys.argv)
    finally:
        sys.argv[:] = old_argv

def project_protocol(
    scr_path: str,
    full_global: str,
    role: str,
    output_dir: str,
    extra_import_paths=None
) -> None:
    """
    Run full pipeline *including* projection.
    Mirrors:
      scribblec -ip … scr_path -project full_global role -o output_dir
    """
    old_argv = sys.argv.copy()
    try:
        argv = ["scribblec",
                "-ip", str(PARSER_DIR),
                "-ip", str(SCRIBBLE_SRC),
               ]
        if extra_import_paths:
            for p in extra_import_paths:
                argv += ["-ip", str(p)]
        argv += [str(scr_path),
                 "-project", full_global, role,
                 "-o", output_dir]
        sys.argv[:] = argv
        _scribble_main(sys.argv)
    finally:
        sys.argv[:] = old_argv
