from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    def __init__(self, word_file_path):
        super().__init__(word_file_path)

    def read_word_file(self, word_file_path):
        """
        expects a file at word_file_path with one word per line
        returns list of words read with new line characters and lines starting with "#" removed
        """
        word_list = []
        word_file = open(word_file_path, 'r')
        for word in word_file:
            if not word == '\n' and not word.startswith('#'):
                word_list.append(word.replace('\n',''))
        word_file.close()
        return word_list