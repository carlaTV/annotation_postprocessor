
def dict_test():
    d = {'a':'1','b':'2'}
    try:
        print(d['c'])
    except KeyError:
        print('Invalid Key. The possible keys are "transcription", "annotation" and "parser".')

def conllu_parser():
    line = '10	much	much	JJ	JJ	_	12	NMOD	12:NMOD	spos=JJ	'
    print(line.split('\t'))


def main():
    conllu_parser()

if __name__ == '__main__':
    main()