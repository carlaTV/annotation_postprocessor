
class FileManager:
    def __init__(self, file_num):
        self.file_num = file_num
        self.filename = None

    def write_opening(self, title, extension):
        self.filename = 'output/%s_%s.%s' % (self.file_num, title, extension)
        with open(self.filename, 'w') as f:
            f.write('')

    def write_content(self, line):
        with open(self.filename, 'a') as f:
            f.write(line)
