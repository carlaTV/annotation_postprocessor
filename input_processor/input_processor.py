""" deal with objects related with the text, such as Annotation, annotator, text content..."""

import common_representation as cr


class Annotation:
    """This class deals with annotations."""

    def __init__(self, file_num, annotator, text):
        self.id = text.file_num
        self.annotation_annotator = dict()
        self.annotator = annotator
        self.text = text

    def relate_annotation_annotator(self):
        self.annotation_annotator.update({self.annotator.name: self.text.get_text})
        return self.annotation_annotator

    def get_text_from_annotator(self):
        text = self.relate_annotation_annotator()[self.annotator.name]
        return text

    def add_annotator_info(self):
        self.annotator.counter += 1
        self.annotator.annotations.append(self.id)


class Text:
    """ This class deals with inputs."""

    def __init__(self, text_type, file_num, annotator):
        self.text_type = text_type  # transcription/annotation/parser
        self.file_num = file_num
        self.annotator = annotator
        self.annotator_initials = {'Carla': 'CTV', 'Monica': 'MD'}
        self.text_content = None
        self.initials = None

    @property
    def get_path(self):
        try:
            self.initials = self.annotator_initials[self.annotator.name]
            if self.text_type in ['transcription', 'annotation']:
                self.path = 'resources/input/%s_%s_%s.txt' % (self.file_num, self.text_type, self.initials)
            if self.text_type == 'parser':
                self.path = 'input/%s_meta_test.conllu' % (self.file_num)
            return self.path
        except AttributeError:
            print('Invalid text type. The possible types are "transcription", "annotation" and "parser".')

    @property
    def get_text(self):
        try:
            path = self.get_path
            with open(path, 'r') as f:
                self.text_content = f.readlines()
                return self.text_content
        except OSError:
            print('File not found. Review the input')

    def text_manager(self):
        cg = cr.CommonReprGenerator(self.get_text, self.text_type, self.file_num, self.annotator.name)
        cg.select_pipeline_from_text_type()  # return representation


class Annotator:
    """This class deals with annotators.
    Annotators might be humans (and have a name) or a parser (name = None)
    """

    def __init__(self, name=None):
        self.name = name
        self.counter = 0
        self.annotations = []
        if self.name is None:
            self.name = 'parser'


class ConlluFile:

    def __init__(self, tokens):
        self.tokens = tokens
        self.proposition = []
        self.file = []

    def separate_into_propositions(self):
        for num, token in enumerate(self.tokens):
            try:
                current_pos = token[num]
                next_pos = token[num + 1]
                if current_pos < next_pos:
                    self.proposition.append(token)
                else:
                    self.file.append(self.proposition)
                    del self.proposition
            except IndexError:
                pass


class ConlluToken:

    def __init__(self, line):
        # self.text = text
        self.line = line
        self.line_as_list = self.line.split('\t')
        self.id = None
        self.form = None
        self.lemma = None
        self.upos = None
        self.xpos = None
        self.feats = None
        self.head = None
        self.deprel = None
        self.deps = None
        self.misc = None
        self.token_parameters = []

    def set_token_parameters(self):
        self.id = self.line_as_list[0]
        self.form = self.line_as_list[1]
        self.lemma = self.line_as_list[2]
        self.upos = self.line_as_list[3]
        self.xpos = self.line_as_list[4]
        self.feats = self.line_as_list[5]
        self.head = self.line_as_list[6]
        self.deprel = self.line_as_list[7]
        self.deps = self.line_as_list[8]
        self.misc = self.line_as_list[9]

    @property
    def save_token_parameters(self):
        self.token_parameters = [self.id, self.form, self.lemma, self.upos, self.xpos, self.feats, self.head,
                                 self.deprel, self.deps, self.misc]
        return self.token_parameters
