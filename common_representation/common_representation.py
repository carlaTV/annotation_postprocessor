"""" get a common representation of all types of inputs"""
import re
import file_processor as fp


class CommonReprGenerator:
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
        cr_list = []
        prop_number = ''
        self.file_processor.write_opening('annotation', 'txt')
        check_props = input('Do you want to check that the files are ok? (y/n)')
        if check_props.lower() == 'yes' or check_props.lower() == 'y':
            prop_counter = 1
            for line in self.text:
                line = self.remove_trailing_spaces(line)
                prop_counter = self.ensure_enumeration(line, prop_counter)
        else:
            for line in self.text:
                for word in line.lstrip().split(' '):
                    if re.search('\[', word) or re.search('\]', word):
                        w, tag = self.get_tag_and_word(word)
                        prop_number = prop_number
                    elif re.search('d*\.', word):
                        w = ''
                        tag = ''
                        prop_number = self.get_prop_number(word)
                    elif re.search('\n', word):
                        continue
                    elif re.search('[a-z]*', word):
                        w = self.get_plain_word(word)
                        tag = ''
                        prop_number = prop_number
                    cr = CommonRepresentation(w, tag, prop_number)
                    cr_list.append(cr)
        for element in cr_list:
            print(element.word, element.tag, element.parent_prop_id)
            to_file = element.word + element.tag + element.parent_prop_id + '\n'
            self.file_processor.write_content(to_file)

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

    def get_plain_word(self, word):
        return word

    def get_tag_and_word(self, word):
        w = ''
        tag = ''
        if re.search('\]', word):
            w_tag = re.split('\]{1}', word)
            for num, elem in enumerate(w_tag):
                if num == 0:
                    w = w_tag[num]
                else:
                    tag += w_tag[num]
            if '[' in word:
                tag = '['+tag
                w = re.sub('\[','',w)
        elif re.search('\[', word):
            tag = '[' + tag
            w = re.sub('\[', '', word)
        return w, tag

    def get_prop_number(self, word):
        prop_number = word
        return prop_number


class CommonRepresentation:
    def __init__(self, word, tag, parent_prop_id):
        self.word = word
        self.tag = tag
        # self.child_prop_id = child_prop_id
        self.parent_prop_id = parent_prop_id

