#!/usr/bin/env python
# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
from argparse import ArgumentParser
from platform import python_version_tuple
import json
import pandas as pd
import re
import requests
import time

if python_version_tuple()[0] == u'2':
    def input(prompt): return raw_input(prompt.encode('utf8')).decode('utf8')

__author__ = u'"noragami", "noragami" <yuumeikai@gmail.com>'
__version__ = '1.0'


class Scraptimus():
    def __init__(self):
        print(u"""
 ______  ______  ______  ______  ______  ______  __  __    __  __  __  ______    
/\  ___\/\  ___\/\  == \/\  __ \/\  == \/\__  _\/\ \/\ "-./  \/\ \/\ \/\  ___\   
\ \___  \ \ \___\ \  __<\ \  __ \ \  _-/\/_/\ \/\ \ \ \ \-./\ \ \ \_\ \ \___  \  
 \/\_____\ \_____\ \_\ \_\ \_\ \_\ \_\     \ \_\ \ \_\ \_\ \ \_\ \_____\/\_____\ 
  \/_____/\/_____/\/_/ /_/\/_/\/_/\/_/      \/_/  \/_/\/_/  \/_/\/_____/\/_____/ 
                                                                                 
created by {__author__}
Version: {__version__}
""".format(__author__=__author__, __version__=__version__))

    URL = 'http://www.co-optimus.com/ajax/ajax_games.php?game-title-filter=&system=&countDirection=at+least&playerCount=2&page=%d&sort=&sortDirection='

    def set_args(self):
        """ Create parser for command line arguments """
        parser = ArgumentParser(
            prog=u'python -m scraptimus',
            description='Scrape and export to a file the list of games found at Co-optimus website.\n\t\tDefault format is json.')
        parser.add_argument('-f', '--filename',
                            help=u'Override the default filename')
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            '-j', '--json', help=u'Export to a json file', action='store_true')
        group.add_argument(
            '-c', '--csv', help=u'Export to a csv file', action='store_true')
        parser.add_argument(
            '-s', '--startpage', help=u'Define where to start. Default is 1')
        parser.add_argument(
            '-e', '--endpage', help=u'Define where to end. Default is all the pages')

        return parser

    def scraper(self, start_page=None, end_page=None, records=[]):
        print('Started... please wait.')
        r = requests.get(self.URL % start_page)

        soup = BeautifulSoup(r.text, 'lxml')  # html.parser is slower
        rows = iter(soup.find('table').find_all('tr'))

        # skip first row
        next(rows)

        for row in rows:
            idx = row['id']
            cells = row.find_all('td')
            title = cells[0].strong.string
            genre = cells[0].label.string
            system = cells[1].a.string
            online = int(cells[2].string)
            couch = int(cells[3].string)
            combo = int(cells[4].string)
            features = []
            for link in cells[5].find_all('a'):
                features.extend(link['class'])
                features = [x for x in features if features.count(
                    x) == 1]  # remove duplicated
                features.remove('features-icon')  # remove unwanted
            review_score = float(
                cells[6].div.div.string) if cells[6].div else None
            user_rating = float(
                cells[7].i.string) if cells[7].i else None
            release_date = cells[8].span.string if cells[8].span else None

            records.append({'id': idx, 'title': title, 'genre': genre, 'system': system,
                            'online': online, 'couch': couch, 'combo': combo,
                            'features': ','.join(features), 'review_score': review_score,
                            'user_rating': user_rating, 'release_date': release_date})

        for tag in soup.find_all(string=re.compile("^Next$")):
            next_page = int(re.search(r'\d+', tag.parent['onclick']).group())

            if end_page is None or end_page > next_page:
                self.scraper(start_page=next_page,
                             end_page=end_page, records=records)
            else:
                break

        return records

    def export_to_csv(self, filename=None, records=None, separator='|'):
        filename = '%s.csv' % filename
        df = pd.DataFrame(records, columns=['id', 'title', 'genre', 'system', 'online',
                                            'couch', 'combo', 'features', 'review_score',
                                            'user_rating', 'release_date'])
        df.to_csv(filename, index=False, encoding='utf-8', sep=separator)

    def export_to_json(self, filename=None, records=None):
        filename = '%s.json' % filename
        with open(filename, 'w') as outfile:
            json.dump(records, outfile, indent=4)

    def scrap(self):
        parser = self.set_args()
        args = parser.parse_args()

        start_page = int(args.startpage) if args.startpage else 1
        end_page = int(args.endpage) if args.endpage else None

        records = self.scraper(
            start_page=start_page, end_page=end_page, records=[])

        filename = '%s-%d-%d' % (
            args.filename if args.filename else '%s' % time.strftime("%Y%m%d"),
            start_page,
            end_page if end_page else 0)

        if args.csv:
            self.export_to_csv(filename=filename, records=records)
        else:
            self.export_to_json(filename=filename, records=records)

        print('Finished!')


if __name__ == '__main__':
    scraptimus = Scraptimus()
    scraptimus.scrap()
