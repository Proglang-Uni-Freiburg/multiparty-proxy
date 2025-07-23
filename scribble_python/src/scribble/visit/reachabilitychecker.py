"""from ast_scribble.importmodule import (
    check_reachability_enter as importmodule_check_reachability_enter,
    check_reachability_visit as importmodule_check_reachability_visit,
    check_reachability_leave as importmodule_check_reachability_leave
)

# TODO: import members

from ast_scribble.module import ( 
    check_reachability_enter as module_check_reachability_enter,
    check_reachability_visit as module_check_reachability_visit,
    check_reachability_leave as module_check_reachability_leave
)

from ast_scribble.moduledecl import (
    check_reachability_enter as moduledecl_check_reachability_enter,
    check_reachability_visit as moduledecl_check_reachability_visit,
    check_reachability_leave as moduledecl_check_reachability_leave
)

from ast_scribble.parameterdecllist import ( 
    check_reachability_enter as parameterdecllist_check_reachability_enter,
    check_reachability_visit as parameterdecllist_check_reachability_visit,
    check_reachability_leave as parameterdecllist_check_reachability_leave
)

from ast_scribble.payloadtypedecl import ( 
    check_reachability_enter as payloadtypedecl_check_reachability_enter,
    check_reachability_visit as payloadtypedecl_check_reachability_visit,
    check_reachability_leave as payloadtypedecl_check_reachability_leave
)

from ast_scribble.roledecllist import ( 
    check_reachability_enter as roledecllist_check_reachability_enter,
    check_reachability_visit as roledecllist_check_reachability_visit,
    check_reachability_leave as roledecllist_check_reachability_leave
)

from ast_scribble.local.localprotocoldecl import ( 
    check_reachability_enter as localprotocoldecl_check_reachability_enter,
    check_reachability_visit as localprotocoldecl_check_reachability_visit,
    check_reachability_leave as localprotocoldecl_check_reachability_leave
)

from ast_scribble.local.localprotocoldef import ( 
    check_reachability_enter as localprotocoldef_check_reachability_enter,
    check_reachability_visit as localprotocoldef_check_reachability_visit,
    check_reachability_leave as localprotocoldef_check_reachability_leave
)"""

"""from ast_scribble.local.localprotocolblock import ( 
    check_reachability_enter as \
        localprotocolblock_check_reachability_enter,
    check_reachability_visit as \
        localprotocolblock_check_reachability_visit,
    check_reachability_leave as \
        localprotocolblock_check_reachability_leave
)

from ast_scribble.local.localinteractionsequence import ( 
    check_reachability_enter as 
        localinteractionsequence_check_reachability_enter,
    check_reachability_visit as \
        localinteractionsequence_check_reachability_visit,
    check_reachability_leave as \
        localinteractionsequence_check_reachability_leave
)

from ast_scribble.local.localsend import ( 
    check_reachability_enter as localsend_check_reachability_enter,
    check_reachability_visit as localsend_check_reachability_visit,
    check_reachability_leave as localsend_check_reachability_leave
)

from ast_scribble.local.localreceive import ( 
    check_reachability_enter as localreceive_check_reachability_enter,
    check_reachability_visit as localreceive_check_reachability_visit,
    check_reachability_leave as localreceive_check_reachability_leave
)"""

"""from ast_scribble.local.localchoice import ( 
    check_reachability_enter as localchoice_check_reachability_enter,
    check_reachability_visit as localchoice_check_reachability_visit,
    check_reachability_leave as localchoice_check_reachability_leave
)

from ast_scribble.local.localrecursion import ( 
    check_reachability_enter as localrecursion_check_reachability_enter,
    check_reachability_visit as localrecursion_check_reachability_visit,
    check_reachability_leave as localrecursion_check_reachability_leave
)

from ast_scribble.local.localcontinue import ( 
    check_reachability_enter as localcontinue_check_reachability_enter,
    check_reachability_visit as localcontinue_check_reachability_visit,
    check_reachability_leave as localcontinue_check_reachability_leave
)

from ast_scribble.local.localparallel import ( 
    check_reachability_enter as localparallel_check_reachability_enter,
    check_reachability_visit as localparallel_check_reachability_visit,
    check_reachability_leave as localparallel_check_reachability_leave
)

from ast_scribble.local.localinterruptible import ( 
    check_reachability_enter as \
        localinterruptible_check_reachability_enter,
    check_reachability_visit as \
        localinterruptible_check_reachability_visit,
    check_reachability_leave as \
        localinterruptible_check_reachability_leave
)

from ast_scribble.local.localdo import ( 
    check_reachability_enter as localdo_check_reachability_enter,
    check_reachability_visit as localdo_check_reachability_visit,
    check_reachability_leave as localdo_check_reachability_leave
)"""

from src.scribble.ast_scribble.nodefactory import NodeFactory as NodeFactory


# Following WellformednessChecker
# TODO: factor out "LocalContextVisitor" aspects
class ReachabilityChecker(object):
    nf = NodeFactory()

    def __init__(self, context_):
        super(ReachabilityChecker, self).__init__()
        self._context = context_
           # Generic ContextVisitor enter/leave that simply uses the default Context

    def check_reachability(self, node_):
        return self.visit(node_)

    def enter(self, node_):
        context = self._context.push(node_)
        self._context = context

    def leave(self, node_):
        self._context = self._context.pop() 

    def get_context(self):
        return self._context

    def set_context(self, context):
        self._context = context
    
    def clone(self):
        clone = self._context.clone()
        return ReachabilityChecker(clone)

    def visit(self, node_):
        node_.check_reachability_enter(self)
        visited = node_.check_reachability_visit(self)
        node_.check_reachability_leave(self)
        return visited
