import common_representation as cr


class FileManager:
    def __init__(self, text):
        self.file_num = text.file_num
        self.filename = None

    def write_opening(self, title, extension):
        self.filename = 'output/%s_%s.%s' % (self.file_num, title, extension)
        with open(self.filename, 'w') as f:
            f.write('')

    def write_content(self, line):
        with open(self.filename, 'a') as f:
            f.write(line)


class Annotation():
    """This class deals with annotations."""

    def __init__(self, file_num, annotator, text):
        self.id = text.file_num
        self.annotation_annotator = dict()
        self.annotator = annotator
        self.text = text

    def relate_annotation_annotator(self):
        self.annotation_annotator.update({self.annotator.name: self.text.get_text()})
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
        self.text_type = text_type # transcription/annotation/parser
        self.file_num = file_num
        self.annotator = annotator
        self.common_representation = cr.CommonRepresentation()

    # def get_text_type(self, text_type):
    #     self.text_type = text_type
    #     return self.text_type
    #
    # def get_file_num(self, file_num):
    #     self.file_num = file_num
    #     return self.file_num
    #
    # def get_annotator(self, annotator):
    #     self.annotator = annotator
    #     return self.annotator

    def get_path(self):
        try:
            if self.text_type in ['transcription', 'annotation']:
                self.path = 'input/%s_%s.txt' % (self.file_num, self.text_type)
            if self.text_type == 'parser':
                self.path = 'input/%s_meta_test.conllu' % (self.file_num)
            return self.path
        except AttributeError:
            print('Invalid text type. The possible types are "transcription", "annotation" and "parser".')

    def get_text(self):
        try:
            path = self.get_path()
            with open(path, 'r') as f:
                self.text_content = f.readlines()
                return self.text_content
        except OSError:
            print('File not found. Review the input')

    def text_manager(self):
        if self.text_type == 'parser':
            cg = cr.ConlluManager(self.get_text(), self.common_representation)
            repr = cg.get_common_representation_conllu()
            return repr
        if self.text_type == 'annotation':
            cg = cr.AnnotationManager(self.get_text(), self.common_representation)
            repr = cg.get_common_representation_annotation()
            return repr
        if self.text_type == 'transcription':
            cg = cr.TranscriptionManager(self.get_text(), self.common_representation)
            repr = cg.get_common_representation_transcription()
            return repr


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

