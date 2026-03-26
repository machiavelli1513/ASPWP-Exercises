class Mammals:
    def __init__(self):
        """Constructor for this class."""
        # Create som memeber animals
        self.members = ['Tiger','Elephant','Wild Cat']

    def printmembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)

    def harmless_mammals():
        return ['Wild Cat']
    
    def dangerous_fish():
        return ['Tiger','Elephant']
