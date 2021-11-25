import pandas as pd
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import os
import joblib


DATA_DIR = 'data/'


def main():
    print('lendo dados')
    df = pd.read_csv(os.path.join(DATA_DIR, 'npr.csv'))

    print('cv')
    cv = CountVectorizer(max_df=0.9,
                         min_df=2,
                         stop_words='english')

    print('dtm')
    dtm = cv.fit_transform(df['Article'])

#    print(dtm.shape)

#    print('lda model')
#    lda_model = LatentDirichletAllocation(
#            n_components=7,
#            random_state=42
#            )
#    lda_model.fit(dtm)
#    joblib.dump(lda_model, 'lda_model.pkl')
#    print('Info sobre o CV')
#    print(f'{len(cv.get_feature_names())}')
#    print(f'{cv.get_feature_names()[:5]}')

#    print('Info sobre o LDA')
#    print(f'{len(lda_model.components_)}')
#    print(f'{lda_model.components_[:5]}')


 #   for i, topico in enumerate(lda_model.components_):
 #       print([cv.get_feature_names()[index] for index in topic.argsort[-15:]])
 #       print('\n')

    print('load model')
    lda_model = joblib.load('lda_model.pkl')

    print('transform')

    topic_results = lda_model.transform(dtm)
    print(f'Prob(0): {topic_results[0].round(2)}')

    print('df update')
    df['Topic'] = topic_results.argmax(axis=1)

    print(f'{df.head(20)}')


if __name__ == '__main__':
    main()
