import pandas as pd
import spacy
import os


DATA_DIR = 'data/'


def main():
    df = pd.read_csv(os.path.join(DATA_DIR, 'npr.csv'))
    
    sample = df['Article'][0]
#    print(f'{sample}')

    model = spacy.load('en_core_web_sm')
    doc = model(sample)
    tokens = [token for token in doc]
    tokens_no_punct = [token for token in tokens if token.is_punct is False]
    print(tokens[:10])
    print(tokens_no_punct[:10])


if __name__ == '__main__':
    main()
