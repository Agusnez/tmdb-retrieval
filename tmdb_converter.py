#!/usr/bin/env python3

#
#   Helper script to convert a file of IMDB IDs to the correspondig TMDB ID
#   Ex: imdbs.csv -> tmbds.csv
#
#   Author: Agustín Núñez
#

import csv
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_PATH = 'https://api.themoviedb.org/3/movie'

payload = {
   'api_key': API_KEY,
   'language': 'en-US',
   'external_source': 'imdb_id'
}

def main():

    with open('imdbs.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        with open('tmdbs.csv', 'wt') as output_file:
            csv_writer = csv.writer(output_file)

            line_count = 0
            for row in csv_reader:
                print(line_count, row[0])

                url = f'https://api.themoviedb.org/3/find/{row[0]}'
                r = requests.get(url, params=payload)

                csv_writer.writerow([r.json()['movie_results'][0]['id']])

                line_count += 1
            
            print(f'Processed {line_count} lines.')

if __name__== "__main__":
  main()