from ..Birds import Birds as Original_class

class Birds(Original_class):                            # Inherits superclass
    def __init__(self, classification='default'):
        super().__init__(classification='harmless')     # Instigates new object with different attribute