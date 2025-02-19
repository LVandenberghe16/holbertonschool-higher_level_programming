#!/usr/bin/python3
"""
Module for fetching and saving posts from a RESTful API.
"""


import requests
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to retrieve posts.")

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        csv_filename = 'posts.csv'
        posts_data = ([{'id': post['id'], 'title': post['title'],
                        'body': post['body']} for post in posts])
        with open(csv_filename, mode='w', newline='',
                  encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
        print(f'Data successfully saved to {csv_filename}')
    else:
        print("Failed to retrieve posts.")
