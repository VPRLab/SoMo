from slither.slithir.operations import Operation as SlitherIR
from slither.slithir.operations import SolidityCall, Condition



class ConditionOperationChecker:

    def is_conditional_ops(self, op: SlitherIR) -> bool:
        # "require" is the `SolidityCall`.
        if isinstance(op, SolidityCall):
            function_name = op.function.full_name
            if "require" in function_name or "assert" in function_name:
                return True

        # IF -> `Condition` call
        elif isinstance(op, Condition):
            return True

        return False
        