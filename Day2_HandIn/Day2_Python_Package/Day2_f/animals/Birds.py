class Birds:
    def __init__(self,classification='default'):
        """Constructor for this class"""
        self.category = classification
        # Create som member animals
        if self.category == 'harmless':
        #self.members = ['Sparrow','Robin','Duck']
            self.members = ['Sparrow','Robin']
        elif self.category == 'dangerous':
            self.members = ['Duck']
        else:
            self.members = ['Sparrow','Robin','Duck']

    def printmembers(self):
        print('Printing members of the Birds Class')
        for member in self.members:
            print('\t%s ' % member)

    #def harmless_birds():
    #    return ['Sparrow','Robin']
    
    #def dangerous_birds():
    #    return ['Duck']