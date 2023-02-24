import csv
import pickle
from random import choice

def extract_data():
    """Extracts data for the index view"""
    with open('static/data/cities.pkl', 'rb') as f:
        data = pickle.load(f)
        city = choice(data)
        return city


def package_data():
    """Extracts data for the index view"""
    with open('static/data/cities.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)[1:]
        new_data = []
        for city in data:
            new_data.append({
                'city' : city[1], 
                'state' : city[4], 
                'country' : city[7]
            })
        with open('static/data/cities.pkl', 'wb') as f:
            f.write(pickle.dumps(new_data))

if __name__ == '__main__':
    package_data()