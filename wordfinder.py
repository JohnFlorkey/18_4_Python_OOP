from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, word_file_path):
        """
        word_list: list of words read in from file at word_file_path, new line characters are removed
        """
        self.word_list = self.read_word_file(word_file_path)
        print(f"{len(self.word_list)} words read")

    def read_word_file(self, word_file_path):
        """
        expects a file at word_file_path with one word per line
        returns list of words read with new line characters removed
        """
        word_list = []
        word_file = open(word_file_path, 'r')
        for word in word_file:
            word_list.append(word.replace('\n',''))
        word_file.close()
        return word_list

    def random(self):
        """returns a random word from word_list"""
        return choice(self.word_list)