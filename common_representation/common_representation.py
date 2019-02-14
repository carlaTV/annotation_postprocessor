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
        self.file_processor.write_opening('annotation', 'txt')
        check_props = input('Do you want to check that the files are ok? (y/n)')
        if check_props.lower() == 'yes' or check_props.lower() == 'y':
            prop_counter = 1
            for line in self.text:
                line = self.remove_trailing_spaces(line)
                prop_counter = self.ensure_enumeration(line, prop_counter)
        else:
            for line in self.text:
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
