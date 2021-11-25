from sklearn import model_selection, preprocessing
from sklearn import linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble
import pandas, xgboost, numpy, textblob, string
import warnings
warnings.filterwarnings("ignore")

# upload dos dados
data = open('corpus.txt', encoding="utf8").read()
labels, texts = [], []
for i, line in enumerate(data.split("\n")):
    content = line.split()
    labels.append(content[0])
    texts.append(content[1:])

# construção de um dataframe usando labels e texts
train_df = pandas.DataFrame()
train_df['text'] = texts
train_df['label'] = labels


# separação entre teste e validacao
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(train_df['text'],
                                                                      train_df['label'])

# encode labels
encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
valid_y = encoder.fit_transform(valid_y)

"""
    Próximos passos:
            > Count Vectors as features
            > TF-IDF Vectors as features
                >> Word level
                >> N-Gram level
                >> Character level

            > Word Embeddings as features
            > Text / NLP based features
            > Topic Models as features
"""

"""
    Count Vector: é uma notação matricial d um dataset na qual,
                  cada linha representa um documento do corpus,
                  cada coluna representa um termo do corpus e
                  cada célula representa a freqüência de um termo
                  em particular, em um documento em particular.
"""

# criar um objeto vectorizador de contagem
count_vec = CountVectorizer(analyzer='word', token_pattern=r"\w{1,}")

count_vec.fit(train_df['text'])

# transforme os dados de treino e de validação usando o count_vec
xtrain_count = count_vec.transform(train_x)
xvalid_count = count_vec.transform(valid_x)

print(xtrain_count)


"""
    TF-idf
"""
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)
tfidf_vect.fit(train_df['text'])
xtrain_tfidf =  tfidf_vect.transform(train_x)
xvalid_tfidf =  tfidf_vect.transform(valid_x)

# ngram level tf-idf
tfidf_vect_ngram = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=5000)
tfidf_vect_ngram.fit(trainDF['text'])
xtrain_tfidf_ngram =  tfidf_vect_ngram.transform(train_x)
xvalid_tfidf_ngram =  tfidf_vect_ngram.transform(valid_x)

# characters level tf-idf
tfidf_vect_ngram_chars = TfidfVectorizer(analyzer='char', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=5000)
tfidf_vect_ngram_chars.fit(train_df['text'])
xtrain_tfidf_ngram_chars =  tfidf_vect_ngram_chars.transform(train_x)
xvalid_tfidf_ngram_chars =  tfidf_vect_ngram_chars.transform(valid_x)

