
def dict_test():
    d = {'a':'1','b':'2'}
    try:
        print(d['c'])
    except KeyError:
        print('Invalid Key. The possible keys are "transcription", "annotation" and "parser".')


def main():
    print(dict_test.__name__)

if __name__ == '__main__':
    main()