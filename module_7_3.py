class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, "r", encoding='utf-8') as file:
                content = file.read().lower()
                for i in punctuation:
                    content = content.replace(i, '')
                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word_positions = {}
        for name, words in all_words.items():
            word = word.lower()
            if word in words:
                word_positions[name] = words.index(word)+1
        return word_positions

    def count(self, word):
        all_words = self.get_all_words()
        word_counts = {}
        for name, words in all_words.items():
            word = word.lower()
            word_counts[name] = words.count(word)
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
