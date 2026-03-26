class Mammals:
    def __init__(self,classification='default'):
        """Constructor for this class."""
        self.category = classification
        # Create som memeber animals
        if self.category == 'harmless':
            self.members = ['Wild Cat']
        elif self.category == 'dangerous':
            self.members = ['Tiger','Elephant']
        else:
            self.members = ['Tiger','Elephant','Wild Cat']

    def printmembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)

    #def harmless_mammals():
    #    return ['Wild Cat']
    
    #def dangerous_fish():
    #    return ['Tiger','Elephant']
