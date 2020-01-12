#!/usr/bin/env python3

import requests
import json
import csv
import os
import sys
from dotenv import load_dotenv
import argparse
 
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('file', default=None, nargs='?')
args = parser.parse_args()

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_PATH = 'https://api.themoviedb.org/3/movie'

# Query params of the request
payload = {
   'api_key': API_KEY,
   'language': 'en-US'
}

def main():

    csv_file = open('dataset.csv', 'wt')
    csv_writer = csv.writer(csv_file)

    header = ['ID', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'imdb_id', 
                    'original_language', 'original_title', 'overview', 'popularity', 'poster_path', 
                    'production_companies', 'production_countries', 'release_date', 'runtime', 
                    'spoken_languages', 'status', 'tagline', 'title', 'Keywords', 'cast', 'crew', 'revenue']

    csv_writer.writerow(header)

    if (args.file):
        print('Executing from file...')
        tmdb_file = open(args.file)
        id_list = tmdb_file.readlines()
    else:
        print('Executing search...')
        max_id = requests.get(BASE_PATH + '/latest',params=payload).json()['id']
        id_list = range(1,max_id)

    internal_id = 0

    for i in id_list:

        url_movie_details = f'https://api.themoviedb.org/3/movie/{i}'

        url_casts = f'https://api.themoviedb.org/3/movie/{i}/casts'

        response_movie_details = requests.get(url_movie_details, params=payload)

        if(response_movie_details.status_code != 404 and response_movie_details.json()['revenue'] > 0):

            print(str(i).rstrip(), response_movie_details.json()['title'])

            response_casts = requests.get(url_casts, params=payload)

            row = [internal_id]

            row.append(response_movie_details.json()['belongs_to_collection'])
            row.append(response_movie_details.json()['budget'])
            row.append(response_movie_details.json()['genres'])
            row.append(response_movie_details.json()['homepage'])
            row.append(response_movie_details.json()['imdb_id'])
            row.append(response_movie_details.json()['original_language'])
            row.append(response_movie_details.json()['original_title'])
            row.append(response_movie_details.json()['overview'])
            row.append(response_movie_details.json()['popularity'])
            row.append(response_movie_details.json()['poster_path'])
            row.append(response_movie_details.json()['production_companies'])
            row.append(response_movie_details.json()['production_countries'])
            row.append(response_movie_details.json()['release_date'])
            row.append(response_movie_details.json()['runtime'])
            row.append(response_movie_details.json()['spoken_languages'])
            row.append(response_movie_details.json()['status'])
            row.append(response_movie_details.json()['tagline'])
            row.append(response_movie_details.json()['title'])
            row.append(response_movie_details.json()['Keywords'] if 'Keywords' in response_movie_details.json() else '')
            row.append(response_casts.json()['cast'] if 'cast' in response_casts.json() else '')
            row.append(response_casts.json()['crew'] if 'crew' in response_casts.json() else '')
            row.append(response_movie_details.json()['revenue'])

            csv_writer.writerow(row)
            internal_id += 1

        else:
            print(i)

if __name__== "__main__":
  main()