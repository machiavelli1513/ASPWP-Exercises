class Fish:
    def __init__(self,classification='default'):
        """Constructor for this class"""
        self.category = classification
        # Create som member animals
        if self.category == 'harmless':
            self.members = ['Guppy','Pike']
        elif self.category == 'dangerous':
            self.members = ['Shark']
        else:
            self.members = ['Guppy','Shark','Pike']

    def printmembers(self):
        print('Printing memebrs of the Fish Class')
        for member in self.members:
            print('\t%s ' % member)

    #def harmless_fish():
    #    return ['Guppy','Pike']
    
    #def dangerous_fish():
    #    return ['Shark']