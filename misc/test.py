def dict_test():
    d = {'a': '1', 'b': '2'}
    try:
        print(d['c'])
    except KeyError:
        print('Invalid Key. The possible keys are "transcription", "annotation" and "parser".')


def conllu_parser():
    line = '10	much	much	JJ	JJ	_	12	NMOD	12:NMOD	spos=JJ	'
    print(line.split('\t'))


class ConlluToken:

    # def __init__(self, text, line, id, form, lemma, upos, xpos, feats, head, deprel, deps, misc):
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
        self.save_token_parameters()

    def save_token_parameters(self):
        self.token_parameters = [self.id, self.form, self.lemma, self.upos, self.xpos, self.feats,
                                 self.head, self.deprel, self.deps, self.misc]
        return self.token_parameters


def main():
    tokens = []
    with open('input/0192_meta_test_CTV.conllu', 'r') as f:
        text = f.readlines()
        for num, line in enumerate(text):
            if num == 10:
                break
            else:
                token = ConlluToken(line)
                try:
                    token.set_token_parameters()
                    tokens.append(token.save_token_parameters())
                except:
                    pass
    print(tokens)


if __name__ == '__main__':
    main()
