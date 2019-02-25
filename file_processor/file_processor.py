
class FileManager:
    def __init__(self, file_num, annotator_name):
        self.file_num = file_num
        self.annotator_name = annotator_name
        self.filename = None

    def write_opening(self, title, extension):
        self.filename = 'resources/output/%s_%s_%s.%s' % (self.file_num ,title, self.annotator_name, extension)
        print('Saving results to %s' % self.filename)
        with open(self.filename, 'w') as f:
            f.write('')

    def write_content(self, line):
        with open(self.filename, 'a') as f:
            f.write(line)
