class Fish:
    def __init__(self):
        """Constructor for this class"""
        # Create som member animals
        self.members = ['Guppy','Shark','Pike']

    def printmembers(self):
        print('Printing memebrs of the Fish Class')
        for member in self.members:
            print('\t%s ' % member)

    def harmless_fish():
        return ['Guppy','Pike']
    
    def dangerous_fish():
        return ['Shark']