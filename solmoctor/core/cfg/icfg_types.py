import typing as T
from slither.core.cfg.node import Node as SlitherNode
from .defined_node import StateVariableWrapper, EntryPoint, ExitPoint
from slither.slithir.variables import *
from slither.slithir.operations import *
from slither.slithir.operations.operation import Operation as SlitherIR


# All the nodes union in the ICFG
GeneralNode: T.TypeAlias = T.Union[SlitherNode, SlitherIR]
ICFGNode: T.TypeAlias = T.Union[SlitherNode, SlitherIR, StateVariableWrapper, EntryPoint, ExitPoint]

# All the edges used in the networkx graph
FunctionCallEdge: T.TypeAlias = T.Tuple[SlitherIR, EntryPoint]
CallReturnEdge: T.TypeAlias = T.Tuple[ExitPoint, SlitherIR]
GeneralEdge: T.TypeAlias = T.Tuple[GeneralNode, GeneralNode]

ICFGEdge: T.TypeAlias = T.Union[FunctionCallEdge, CallReturnEdge, GeneralEdge]

# Used for the mdg building and contract analysis
ModifierSinkNode: T.TypeAlias = T.Union[SlitherNode, SlitherIR]

# The IR operations that could write to the state variables
SlitherLValue: T.TypeAlias = T.Union[StateIRVariable, LocalIRVariable, TemporaryVariableSSA, ReferenceVariableSSA, TupleVariableSSA]

# The possible operations in the function that can write to the state variables.
FunctionSinkNode: T.TypeAlias = T.Union[Assignment, Binary, Index]
