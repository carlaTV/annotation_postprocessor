"""" get a common representation of all types of inputs"""
import re
import file_processor as fp


class TextManager:
    """converts any kind of text into common representation """

    def __init__(self, text, text_type, file_num, annotator_name):
        self.text = text
        self.text_type = text_type
        self.file_num = file_num
        self.common_representation = None
        self.annotator_name = annotator_name
        self.file_processor = fp.FileManager(self.file_num, self.annotator_name)

    def select_pipeline_from_text_type(self):
        if self.text_type == 'annotation':
            self.cr_from_annotation()
        if self.text_type == 'transcription':
            print('do get_from_transcription')
        if self.text_type == 'parser':
            print('do get_from_parser')

    def cr_from_annotation(self):
        self.file_processor.write_opening('annotation', 'txt')
        prop_counter = 1
        for line in self.text:
            # line = self.remove_trailing_spaces(line)
            # prop_counter = self.ensure_enumeration(line, prop_counter)
            for word in line.split(' '):
                print(word)

    @staticmethod
    def remove_trailing_spaces(line):
        if re.search(r"^\t*", line):
            line = line.lstrip()
        return line

    def ensure_enumeration(self, line, prop_counter):
        if re.search(r"^\d*\.", line):
            prop_counter += 1
            line = re.sub(r"^\d*\.", str(prop_counter), str(line))
            self.file_processor.write_content(line)
        else:
            self.file_processor.write_content(line)
        return prop_counter


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
