"""" get a common representation of all types of inputs"""
import re
import file_processor as fp


class TextManager:
    """converts any kind of text into common representation """

    def __init__(self, text, text_type, file_num):
        self.text = text
        self.text_type = text_type
        self.file_num = file_num
        self.common_representation = None
        self.file_processor = fp.FileManager(self.file_num)

    def select_pipeline_from_text_type(self):
        if self.text_type == 'annotation':
            self.cr_from_annotation()
        if self.text_type == 'transcription':
            print('do get_from_transcription')
        if self.text_type == 'parser':
            print('do get_from_parser')

    def cr_from_annotation(self):
        self.file_processor.write_opening('annotation', 'txt')
        prop_counter = 0
        for line in self.text:
            line = self.remove_trailing_spaces(line)
            self.ensure_enumeration(line, prop_counter)

    @staticmethod
    def remove_trailing_spaces(line):
        if re.search(r"^\t*", line):
            re.sub(r"^\t*", '', line)
        return line

    def ensure_enumeration(self, line, prop_counter):
        if re.search(r"^\d*\.", line):
            line = re.sub(r"^\d*\.", str(prop_counter), str(line))
            self.file_processor.write_content(line)
            prop_counter += 1
        else:
            self.file_processor.write_content(line)


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

    def __init__(self, text):
        self.text = text
        self.common_representation = None
        self.file_processor = fp.FileManager(self.class_text)

    def ensure_enumeration(self, line):
        # check wether line is enumerated:
        prop_counter = 0
        if re.search('^\d*\.', line):
            line = re.sub('^\d*\.', prop_counter, str(line))
            prop_counter += 1
            self.file_processor.write_content(line)
        else:
            self.file_processor.write_content(line)

    def get_common_representation_annotation(self):
        self.file_processor.write_opening('annotation', 'txt')
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
    def __init__(self, word, tag, child_prop_id, parent_prop_id):
        self.word = word
        self.tag = tag
        self.child_prop_id = child_prop_id
        self.parent_prop_id = parent_prop_id


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
        self.token_parameters = [self.id, self.form, self.lemma, self.upos, self.xpos, self.feats,
                                 self.head, self.deprel, self.deps, self.misc]
        return self.token_parameters
