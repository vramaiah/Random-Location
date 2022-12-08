import csv

from random import choice

def extract_data():
    """Extracts data for the index view"""
    with open('static/data/cities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)[1:]
        city = choice(data)
        return city[1], city[4], city[7]