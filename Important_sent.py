import nltk
from nltk.tokenize import RegexpTokenizer,sent_tokenize
from  nltk.stem import PorterStemmer
from nltk.corpus import stopwords

class TEXT_PROCCESS:
    def GET_BEST_SENT(self, text):
        sentences = sent_tokenize(text)  # seperate the paragraph with .
        reg_tokenizer = RegexpTokenizer('\w+')  #
        word_tokenize = reg_tokenizer.tokenize

        unique_words = set(reg_tokenizer.tokenize((text)))  # unique words
        stemmed_words = []
        # original word
        porter_stemmer = PorterStemmer()  # words that you can use instead
        for word in unique_words:
            stemmed_words.append(porter_stemmer.stem(word))  # to each word

        stemmed_words = set(stemmed_words)  # useless
        stoped_words = set(stopwords.words("english"))  # to remove ,./:';etc
        stemmed_words_delete_stop_words = []
        for word in stemmed_words:
            if not word in stoped_words:
                stemmed_words_delete_stop_words.append(word)
        temp = 0
        c = 0
        sent = dict()
        while temp < len(sentences):

            #  counter+=1
            for word in stemmed_words_delete_stop_words:  # if there is simialar words cont++
                count = 0
                for item in word_tokenize(sentences[temp]):
                    if porter_stemmer.stem(item) == word:
                        count += 1
                sent.setdefault(temp, []).append(count)


            temp += 1
            print(sent)
        doc = []
        for word in stemmed_words_delete_stop_words:
            count = 0
            for item in word_tokenize(text):
                if porter_stemmer.stem(item) == word:
                    count += 1

            doc.append(count)

        def inner_product(v1, v2):  # measuers the simuliraty
            result = 0
            index = 0
            for _ in v1:
                result += v1[index] * v2[index]
                index += 1

            return result

        c = 0
        index_max =0
        max = inner_product(sent[0], doc)
        for _ in sent:
            if (max < inner_product(sent[c], doc)):
                max = inner_product(sent[c], doc)
                index_max = c
            c += 1
        return sentences[index_max]



#text_process = TEXT_PROCCESS()

text = """
            JERUSALEM, Sunday, June 27, 2021 (WAFA) – A Palestinian husband and his wife died today and five others
            were injured in a blaze that erupted in the former’s 
            house in the occupied Jerusalem neighborhood of Beit Safafa, according to local sources.
            Mousa Elian and his wife, Mariam, were pronounced dead as a result of the blaze in their house. 
            The two are in their forties of age. The other five sustained suffocation or fainting as 
            a result of smoke inhalation."""
#print(text)
#print(text_process.GET_BEST_SENT(text))

