# scribble_tools.py
import sys
from pathlib import Path
from src.scribble.main import main as _scribble_main

# adjust these to match your layout
ROOT         = Path(__file__).parent
PARSER_DIR   = ROOT / "run"    / "parser"
SCRIBBLE_SRC = ROOT / "src"    / "scribble"

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
