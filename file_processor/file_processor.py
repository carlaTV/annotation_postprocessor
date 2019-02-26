import input_processor


class FileManager:
    def __init__(self, text_type, file_num, annotator_name):
        self.file_num = file_num
        self.text_type = text_type
        # self.annotator_name = annotator_name
        self.annotator_id = input_processor.Text(text_type, file_num, annotator_name).annotator_initials[annotator_name]
        self.filename = None

    def write_opening(self, folder, title, extension):
        self.filename = 'resources/%s/%s_%s_%s.%s' % (folder, self.file_num, title, self.annotator_id, extension)
        print('Saving results to %s' % self.filename)
        with open(self.filename, 'w') as f:
            f.write('')

    def write_content(self, line):
        with open(self.filename, 'a') as f:
            f.write(line)
