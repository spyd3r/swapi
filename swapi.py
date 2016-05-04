#!/usr/bin/env python
import requests

'''
Obtain a list of starships and their 
previous owners from the Star Wars API
project (swapi.co)
'''

#return a list of people
def list_people():
  people = requests.get('http://swapi.co/api/people/')
  return people.json()

def get_person_name(url):
  person = requests.get(url)
  name = ''
  if person.status_code == 200:
    name = person.json()['name']
  if name:
    return name
  else:
    return False

def get_person_name_by_id(person_id):
  person = requests.get('http://swapi.co/api/people/{0}'.format(person_id))
  name = ''
  if person.status_code == 200:
    name = person.json()['name']
  if name:
    return name
  else:
    return False

#return a list of starships for a given person
def get_starships(person_id):
  r = requests.get('http://swapi.co/api/people/{0}'.format(person_id))
  starships = r.json()['starships']
  return starships

#return the name of a given starship id
def get_starship_name(starship_id):
  r = requests.get('http://swapi.co/api/starships/{0}'.format(starship_id))
  name = ''
  if r.status_code == 200:
    name = r.json()['name']
  return name

def get_starship_pilots(starship_id):
  r = requests.get('http://swapi.co/api/starships/{0}'.format(starship_id))
  pilots = []
  pilot_names = []
  if r.status_code == 200:
    pilots = r.json()['pilots']
    for pilot in pilots:
      pilot_names.append(get_person_name(pilot))
  return pilot_names

def show_person_starships():
  #There are 87 people from the list_people method
  for x in range(1,88):
    info = {}
    info['owner'] = get_person_name_by_id(x)
    if info['owner']:
      starships = get_starships(x)
    info['starships'] = []
    for ship in starships:
      details = requests.get(ship)
      info['starships'].append(details.json()['name'])
    #print '{0} was the owner of {1}'.format(info['owner'], info['starships'])
    if info['owner']:
      if not info['starships']:
        print '{0} didn\'t own any ships'.format(info['owner'].encode('utf-8'))
      else:
        print '{0} owned \n\t{1}'.format(info['owner'].encode('utf-8'), "\n\t".join([ x.encode('utf-8') for x in info['starships']]))

def show_starship_pilots():
  for x in range(1,38):
    starship_name = get_starship_name(x)
    pilots = get_starship_pilots(x)
    if starship_name:
      print '{0} was piloted by:\n\t{1}'.format(starship_name.encode('utf-8'), "\n\t".join([ y.encode('utf-8') for y in pilots]))

if __name__ == "__main__":
  show_starship_pilots()
  #show_person_starships()
