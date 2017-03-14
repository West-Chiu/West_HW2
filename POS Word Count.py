file = open('')
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

from collections import defaultdict, Counter
PwordsCount = defaultdict(Counter)

for line in file:
    Twords = word_tokenize(line)
    Pwords = nltk.pos_tag(Twords)
    for word, pos in Pwords:
        PwordsCount[pos][word] += 1
        
for pos, counter in PwordsCount.items():
    print(pos, ':', end=' ')
    for word, count in counter.most_common(5):
        print(word, '/', count, end=' ')
    print()