from common_representation import ConlluManager, TxtManager


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
        self.text_type = text_type  # transcription/annotation/parser
        self.file_num = file_num
        self.annotator = annotator

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

    def conllu_manager(self):
        cg = ConlluManager()
        repr = cg.convert_from_conllu()
        # return repr

    def txt_manager(self):
        tm = TxtManager()
        repr = tm.convert_from_txt()
        # return repr


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


def main():
    file_num = input('Which file do you want to process?\nEnter a number: ')
    annotator1 = Annotator('Carla')
    text1 = Text('annotation', file_num, annotator1)
    text1.txt_manager()
    # annotation1 = Annotation(file_num, annotator1, text1)
    # annotation1.add_annotator_info()
    # text1 = annotation1.get_text_from_annotator()


if __name__ == '__main__':
    main()
