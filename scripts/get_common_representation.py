"""" get a common representation of all types of inputs"""


class ConlluManager():
    """converts conllu to common representation """
    def __init__(self, text, common_representation):
        self.text = text
        self.common_representation = common_representation
    def convert_from_conllu(self):
        for line in self.text:
            for word in line.split(' '):
                print(word)

class TxtManager():
    """converts txt to common representation"""
    def __init__(self):
        self.text = None
    def convert_from_txt(self):
        print('Function %s is still being built. Sorry :)' % (self.convert_from_txt.__name__))

class CommonRepresentation():
    def __init__(self):
        self.words = []
        self.tags = []
        self.child_prop_id = []
        self.parent_prop_id = []