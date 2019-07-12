import os
import logging
import argparse
from collections import Counter

import pandas as pd
import inflect


_CATEGRORIES = [
    'Mini Briefs',
    'Advances & Business',
    'Concerns & Hype',
    'Analysis & Policy',
    'Expert Opinions & Discussion within the field',
    'Explainers'
]


_LINK_TEMPLATE = '[{}]({})'


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--template_file', '-tf', type=str, default='digest_template')
    parser.add_argument('--digest_number', '-n', type=int, required=True)
    parser.add_argument('--input_csv', '-i', type=str, required=True)
    parser.add_argument('--output_md', '-o', type=str, required=True)
    parser.add_argument('--force_overwrite', '-f', action='store_true')
    args = parser.parse_args()

    n = args.digest_number
    p = inflect.engine()
    n_english = p.number_to_words(p.ordinal(n))
    logging.info('Parsing for the {} digest'.format(n_english))

    logging.info('Will save result to {}'.format(args.output_md))
    if os.path.isfile(args.output_md):
        if not args.force_overwrite:
            raise ValueError('Cannot overwrite existing output file!')

    logging.info('Reading {}'.format(args.input_csv))
    articles_map = {c : [] for c in _CATEGRORIES}
    csv = pd.read_csv(args.input_csv)
    for row_num, row in csv.iterrows():
        print('To which category does this article belong?')
        print(row['Name'])
        
        for i, c in enumerate(_CATEGRORIES):
            print('{}) {}'.format(i, c))
        while True:
            try:
                c_idx = int(input('Category Number: '))
                c = _CATEGRORIES[c_idx]
                break
            except:
                print('Please enter a valid category!')
        print()

        articles_map[c].append(row)

    import IPython; IPython.embed(); exit(0)
