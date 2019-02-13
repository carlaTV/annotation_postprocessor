import common_representation as cr
import input_processor as ip

def main():
    # initialize setup
    file_num = input('Which file do you want to process?\nEnter a number: ')
    if file_num == "":
        file_num = '0192'
    file_type = input('Select a file type to process:\n 1: "transcription", 2: "parser", 3: "annotation".\n')
    file_type_dict = {'1': 'transcription', '2': 'parser', '3': 'annotation'}
    annotator1 = ip.Annotator('Carla')
    file_to_open = file_type_dict[file_type]
    #
    # text.get_text_type(file_to_open)
    # text.get_file_num(file_num)
    # text.get_annotator(annotator1)

    # work with files
    # 1. get text
    text = ip.Text(file_to_open, file_num, annotator1)
    text.text_manager()
    # annotation1 = Annotation(file_num, annotator1, text1)
    # annotation1.add_annotator_info()
    # text1 = annotation1.get_text_from_annotator()


if __name__ == '__main__':
    main()