"""" get a common representation of all types of inputs"""
import re
import file_processor as fp
from stack import stack as st

class CommonReprGenerator:
    """converts any kind of text into common representation """

    def __init__(self, text, text_type, file_num, annotator_name):
        self.text = text
        self.text_type = text_type
        self.file_num = file_num
        self.common_representation = None
        self.annotator_name = annotator_name
        self.file_processor = fp.FileManager(self.text_type, self.file_num, self.annotator_name)

    def select_pipeline_from_text_type(self):
        if self.text_type == 'annotation':
            self.cr_from_annotation()
        if self.text_type == 'transcription':
            print('do get_from_transcription')
        if self.text_type == 'parser':
            print('do get_from_parser')

    def cr_from_annotation(self):
        proposition = Proposition()
        prop_open = False
        cr_list = []
        prop_number = ''
        check_props = input('Do you want to check that the files are ok? (y/n)')
        if check_props.lower() == 'yes' or check_props.lower() == 'y':
            self.file_processor.write_opening('input', 'annotation', 'txt')
            prop_counter = 1
            for line in self.text:
                line = self.remove_trailing_spaces(line)
                prop_counter = self.ensure_enumeration(line, prop_counter)
        else:
            complete_sentence = ''
            sentence_list = []
            stack = st.Stack()
            for num, line in enumerate(self.text):
                if re.search(r'^\d', line):
                    sentence_list.append(complete_sentence)
                    complete_sentence = ''
                    complete_sentence += line.strip() + ' '
                else:
                    complete_sentence += line.strip() + ' '
            sentence_list.remove("")
            for num, line in enumerate(sentence_list):
                sent = Sentence(line.rstrip())
                sent.get_sent_id()
                sent.get_sent_text()
                # print(sent.sent_text, '-->', sent.sent_id)
                for n, word in enumerate(sent.sent_text.split(' ')):
                    for char in word:
                        if char == '{':
                            if stack.isEmpty():
                                proposition.get_open_position(n, word)
                            stack.push('{')
                        if char == '}':
                            stack.pop()
                            if stack.isEmpty():
                                proposition.get_closing_position(n, word)
                                proposition.get_prop_tag(word)
                                print(proposition.open_word, '--->', proposition.close_word, 'tag: ', proposition.prop_tag)
                    # if re.search('{', word) and prop_open == False:
                    #     proposition.get_open_position(n, word)
                    #     prop_open = True
                    # if re.search('}', word):
                    #     proposition.get_prop_tag(word)
                    #     proposition.get_closing_position(num, word)
                    #     proposition.get_words_in_proposition(word)
                    #     prop_open = False
                    #     proposition.reset_words_included()
                    # if prop_open == True:
                    #     proposition.get_words_in_proposition(word)
        #             if re.search('\[', word) or re.search('\]', word):
        #                 w, tag = self.get_tag_and_word(word)
        #                 prop_number = prop_number
        #             elif re.search('}P\d', word):
        #                 w = ''
        #                 tag = ''
        #                 prop_number = self.get_prop_number(word)
        #             elif re.search('\n', word) or re.search('d*\.', word):
        #                 continue
        #             elif re.search('[a-z]*', word):
        #                 w = self.get_plain_word(word)
        #                 tag = ''
        #                 prop_number = prop_number
        #             cr = CommonRepresentation(w, tag, prop_number)
        #             cr_list.append(cr)
        # for num, element in enumerate(cr_list):
        #     if num < 20:
        #         # print(element.word, element.tag, element.parent_prop_id)
        #         to_file = element.word + element.tag + element.parent_prop_id + '\n'
        #         self.file_processor.write_content(to_file)

    @staticmethod
    def remove_trailing_spaces(line):
        if re.search(r"^\t*", line):
            line = line.lstrip()
            line = re.sub('^\n', ' ', line)
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
                tag = '[' + tag
                w = re.sub('\[', '', w)
        elif re.search('\[', word):
            tag = '[' + tag
            w = re.sub('\[', '', word)
        return w, tag

    def get_prop_number(self, word):
        word_prop_number = re.split('}', word)
        prop_number = word_prop_number[1]
        w = word_prop_number[0]
        return prop_number


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.sent_id = None
        self.sent_text = None

    def get_sent_id(self):
        try:
            self.sent_id = re.search(r'^\d* ', self.sentence).group()
        except:
            pass
        return self.sent_id

    def get_sent_text(self):
        try:
            self.sent_text = re.sub(self.sent_id, '', self.sentence)
            if re.search('^{', self.sent_text):
                pass
            else:
                self.sent_text = '{' + self.sent_text + '}P1'
        except:
            self.sent_text = None
        return self.sent_text


class Proposition:
    def __init__(self):
        self.open_position = None
        self.close_position = None
        self.open_word = None
        self.close_word = None
        self.words_included = []
        self.prop_tag = None
        self.range_prop = None

    def get_open_position(self, num, word):
        self.open_position = num
        self.open_word = word

    def get_closing_position(self, num, word):
        self.close_position = num
        self.close_word = word

    def get_prop_tag(self, word):
        if re.search('}', word):
            word_tag = re.split('}', word)
            self.prop_tag = word_tag[len(word_tag) - 1]
        else:
            self.prop_tag = 'P1'

    def get_words_in_proposition(self, word):
        self.words_included.append(word)

    def reset_words_included(self):
        self.words_included = []


class CommonRepresentation:
    def __init__(self, word, tag, parent_prop_id):
        self.word = word
        self.tag = tag
        # self.child_prop_id = child_prop_id
        self.parent_prop_id = parent_prop_id
