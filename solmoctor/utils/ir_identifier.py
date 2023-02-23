from slither.core.cfg.node import Node as SlitherNode


class IRIdentifier:
    
    @staticmethod
    def has_ssa_irs(node: SlitherNode) -> bool:
        if node.irs_ssa:
            return True
        else:
            return False
    