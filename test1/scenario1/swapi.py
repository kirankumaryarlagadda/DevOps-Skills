#!/usr/bin/python3

import requests
import json
import sys

total_results = []
films_list = []

for page_num in range(1, 2):
    url = f"https://swapi.co/api/films/?format=json&page={page_num}"
    response = requests.get(url)
    data = response.json()
    total_results = total_results + data['results']
    for result in data['results']:
    	films_list.append(result['title'])

total_count = data['count']

print(f"We have {total_count} total films with the following list:")
for film_index, val in enumerate(films_list, start=1):
	print(film_index, val)

response = requests.get(url)
data = response.json()
film_chosen = input("Choose the film Index to list its starships and pilots: ")
film_index = int(film_chosen)

if(film_index < 1 or film_index > total_count):
	print("Invalid Film Selection")
	print("Please input one of the below films:")

	for index in range(0,total_count):
		print(f"Input {index+1} for title: {data['results'][index]['title']}")
	film_index = int(input("Enter:"))

if(film_index < 1 or film_index > total_count):
	print("Invalid selection again, Exited")
else:
	film = data['results'][film_index - 1]

	print("You have selected film #", film_index)
	print (f"Title: {film['title']}")

	starships = film['starships']
	num_starships = len(starships)

	for ship_index in range(0,num_starships):
		ship_url = starships[ship_index]
		ship_response = requests.get(ship_url)
		ship_data = ship_response.json()
		print(f"Starship Name: {ship_data['name']}")
		print("")
		print("Pilots: ")

		pilots = ship_data['pilots']

		num_pilots = len(pilots)
		if num_pilots == 0:
			print("[]")
		for pilot_index in range(0,num_pilots):
			pilot_url = pilots[pilot_index]
			pilot_response = requests.get(pilot_url)
			pilot_data = pilot_response.json()
			print(f"Pilot Name: {pilot_data['name']}")
			print(pilot_data)
			print("")
		print("")
