"""" get a common representation of all types of inputs"""
import re

class ConlluManager:
    """converts conllu to common representation """
    def __init__(self, text, common_representation):
        self.text = text
        self.common_representation = common_representation
    def get_common_representation_conllu(self):
        for line in self.text:
            for word in line.split(' '):
                print(word)

class AnnotationManager:
    """converts txt to common representation"""

    def __init__(self, text, common_representation):
        self.text = text
        self.common_representation = common_representation
        # self.class_text = ip.Text()
        # self.file_processor = ip.FileManager(self.class_text)

    def ensure_enumeration(self, line):
        #check wether line is enumerated:
        prop_counter = 0
        if re.search('^\d*\.', line):
            line = re.sub('^\d*\.', prop_counter, str(line))
            prop_counter += 1
            self.file_processor.write_content(line)
        else:
            self.file_processor.write_content(line)

    def get_common_representation_annotation(self):
        self.file_processor.write_opening('annotation','txt')
        for line in self.text:
            self.ensure_enumeration(line)
            # for word in line.split(' '):
            #     print(word)

class TranscriptionManager:
    """ Gets common representation from the transcription (bare txt)."""
    def __init__(self, text, common_representation):
        self.text = text
        self.common_representation = common_representation

    def get_common_representation_transcription(self):
        for line in self.text:
            for word in line.split(' '):
                print(word)

class CommonRepresentation:
    def __init__(self):
        self.words = []
        self.tags = []
        self.child_prop_id = []
        self.parent_prop_id = []

class Conllu:

    def __init__(self):
        self.tokens = []
        self.propositions = []

# class ConlluToken:
#
#     def __init__(self, text, line):
#         self.text = text
#         self.line = line
#         self.line_as_list = self.line.split('\t')
#         self.id = None
#         self.form = None
#         self.lemma = None
#         self.upos = None
#         self.xpos = None
#         self.feats = None
#         self.head = None
#         self.deprel = None
#         self.deps = None
#         self.misc = None
#
#     def parse_token(self):
#         for line in self.text:
#             line_as_list = line.split('\t')
#             self.id = line_as_list[0]
#             self.form = line_as_list[1]
#             self.lemma = line_as_list[2]
#             self.upos = line_as_list[3]
#             self.xpos = line_as_list[4]
#             self.feats = line_as_list[5]
#             self.head = line_as_list[6]
#             self.deprel = line_as_list[7]
#             self.deps = line_as_list[8]
#             self.misc = line_as_list[9]
#
