# coding=utf-8

from pathlib import Path
import csv
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

if __name__ == '__main__':
    current_path = Path('.')
    detail_file = current_path / '..' / 'data' / 'FRDetail_cxf.csv'

    ids = []
    details = []
    with open(str(detail_file), 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in enumerate(reader):
            if row:
                print('row', row)
                ids.append(row[1]['FRName'])
                details.append(row[1]['Description'])

    for item in enumerate(details):
        print(item)

    count_vectorizer = CountVectorizer()
    train_tc = count_vectorizer.fit_transform(details)
    print("\nDimensions of training data:", train_tc.shape)

    tfidf = TfidfTransformer()
    train_tfidf = tfidf.fit_transform(train_tc)

    for x in enumerate(train_tfidf):
        print(x[0], x[1])
