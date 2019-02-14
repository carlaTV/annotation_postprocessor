import common_representation as cr


class Annotation():
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


class Text():
    """ This class deals with inputs."""

    def __init__(self, text_type, file_num, annotator):
        self.text_type = text_type  # transcription/annotation/parser
        self.file_num = file_num
        self.annotator = annotator
        self.annotator_initials = {'Carla':'CTV', 'Monica':'MD'}
        # self.common_representation = cr.CommonRepresentation()
        self.text_content = None
        self.initials = None

    # @property
    # def get_initials(self):
    #     self.annotator_initials.update({'Carla':'CTV'})
    #     self.annotator_initials.update({'Monica':'MD'})
    #     return self.annotator_initials

    @property
    def get_path(self):
        try:
            self.initials = self.annotator_initials[self.annotator.name]
            if self.text_type in ['transcription', 'annotation']:
                self.path = 'input/%s_%s_%s.txt' % (self.file_num, self.text_type,self.initials)
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
        cg = cr.TextManager(self.get_text, self.text_type, self.file_num, self.annotator.name)
        cg.select_pipeline_from_text_type()
        # return representation


class Annotator():
    """This class deals with annotators.
    Annotators might be humans (and have a name) or a parser (name = None)
    """

    def __init__(self, name=None):
        self.name = name
        self.counter = 0
        self.annotations = []
        if self.name is None:
            self.name = 'parser'
