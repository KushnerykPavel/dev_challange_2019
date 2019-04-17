import re
from nltk.corpus import stopwords


class TextProcessor:

    def __init__(self, text):
        self.text = text

    def _text_prepare(self, text:str)->list:
        """
        Method cleanup text, remove special charters and stop words

        :param text:
        :return:
        """
        replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
        bad_symbols_re = re.compile('[^0-9A-z #+_]')
        stopwords_set = set(stopwords.words('english'))

        text = replace_by_space_re.sub(' ', text)
        text = bad_symbols_re.sub('', text)
        text = [x for x in text.split() if x and x not in stopwords_set]

        return text

    def _generate_ngram(self, text: list, n: int) -> list:
        """
        Generate n-gramm order n for splited text

        :param text:
        :param n:
        :return:
        """
        ngram = zip(*[text[i:] for i in range(n)])
        return [' '.join(ngr) for ngr in ngram]

    def generate_keywords(self) -> list:
        """
        Generate list keyword for text
        :return:
        """
        prep_text = self._text_prepare(self.text)

        keyword_ngram_amount = len(prep_text)
        keywords = []

        for ngr in range(keyword_ngram_amount + 1, 0, -1):
            keywords += self._generate_ngram(prep_text, ngr)

        return keywords
