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

def get_person_name(person_id):
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
  name = r.json()['name']


if __name__ == "__main__":
  #There are 87 people from the list_people method
  for x in range(1,88):
    info = {}
    info['owner'] = get_person_name(x)
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
