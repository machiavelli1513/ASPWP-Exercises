class Birds:
    def __init__(self):
        """Constructor for this class"""
        # Create som member animals
        self.members = ['Sparrow','Robin','Duck']

    def printmembers(self):
        print('Printing memebrs of the Birds Class')
        for member in self.members:
            print('\t%s ' % member)

    def harmless_birds():
        return ['Sparrow','Robin']
    
    def dangerous_birds():
        return ['Duck']