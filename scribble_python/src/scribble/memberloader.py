import sys
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.scribble import scrib_constants as constants
from src.scribble import scrib_util as util

from src.scribble.visit.context import Context as Context

from src.scribble.ast_scribble.importmodule import \
    get_full_module_name as importmodule_get_full_module_name

from src.scribble.ast_scribble.module import (
    get_moduledecl_child as module_get_moduledecl_child,
    get_importmember_children as module_get_importmember_children,
    get_importmodule_children as module_get_importmodule_children,
    get_payloadtypedecl_children as module_get_payloadtypedecl_children,
    get_globalprotocoldecl_children as module_get_globalprotocoldecl_children,
    get_localprotocoldecl_children as module_get_localprotocoldecl_children
)

from src.scribble.ast_scribble.moduledecl import (
    check_filename as moduledecl_check_file_name,
    get_full_name as moduledecl_get_full_name
)

from src.scribble.ast_scribble.payloadtypedecl import \
    get_declaration_name as payloadtypedecl_get_declaration_name

from src.scribble.ast_scribble.globel.globalprotocoldecl import \
    get_name as globalprotocoldecl_get_name

from src.scribble.ast_scribble.local.localprotocoldecl import \
    get_name as localprotocoldecl_get_name


# Section 4.2 -- dependencies of the primary module
def load_members(context_, filepath, module_):
    for fmn, module_ in list(context_.get_modules().items()):
        context_ = _add_all_members(context_, fmn, module_)
    return context_


# Same structure as visibilitybuilder.get_moduleMembers
def _add_all_members(context_, fmn, module_):
    for ptd in module_get_payloadtypedecl_children(module_):
        n = payloadtypedecl_get_declaration_name(ptd)
        f = fmn + '.' + n
        context_ = context_.add_member(f, ptd)
    for gpd in module_get_globalprotocoldecl_children(module_):
        n = globalprotocoldecl_get_name(gpd)
        f = fmn + '.' + n
        context_ = context_.add_member(f, gpd)
    for lpd in module_get_localprotocoldecl_children(module_):
        n = localprotocoldecl_get_name(lpd)
        f = fmn + '.' + n
        context_ = context_.add_member(f, lpd)
    importmembers = module_get_importmember_children(module_)
    for im in importmembers:
        # TODO: members
        util.report_error("TODO member import: " + im)
    return context_
