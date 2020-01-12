# TMDB API: Movie information retrieval
This project consists of two Python scripts with the purpose of retrieving all
the information possible from movies in the TMBD API. Its goal is to create a comprehensive dataset for data analysis and/or machine learning.

## Requirements
- **TMDB API KEY:** You must have a developer account in [TMDB](https://www.themoviedb.org/account/signup). It's free.
- **Virtual environment: (Optional)**
```
python3 -m venv venv
source venv/bin/activate # Unix/macOS
venv\Scripts\activate.bat # Windows
```
- **Python 3:** &nbsp; `pip install -r requirements.txt`

## Usage
Very easy. We have 2 modes of retrieving:
* Brute force search of valid IDs in the API by incrementing an index.
* A more targeted alternative that consists in having a file loaded of
TMDB IDs or IMDB IDs to perform the retrieval of information of those.

```
# Brute force search
python main.py

# Retrieve from file
python main.py /path/to/file.csv
```