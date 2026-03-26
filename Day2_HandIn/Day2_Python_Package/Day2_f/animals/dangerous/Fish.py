from ..Fish import Fish as Original_Fish_class

class Fish(Original_Fish_class):                            # Inherits superclass
    def __init__(self, classification='default'):
        super().__init__(classification='dangerous')     # Instigates new object with different attribute