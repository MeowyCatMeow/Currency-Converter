"""currency converter
https://hyperskill.org/projects/157?track=2
https://imgur.com/a/t0oPVli
"""
import requests
import json
'''
switcher = {
    'RUB': 2.98,
    'ARS': 0.82,
    'HNL': 0.17,
    'AUD': 1.9622,
    'MAD': 0.208
}
li = [print(f'I will get {switcher[x] * num} {x} from the sale of {num} conicoins.') for x in switcher]
'''
choice = input().lower()
if choice == '':
    exit()
r = requests.get(f'http://www.floatrates.com/daily/{choice}.json')
_dict = json.loads(r.text)
# print(_dict)
# print(_dict['usd'])
# print(_dict['eur'])
cache_dict = {}
if choice == 'usd':
    cache_dict['eur'] = _dict['eur']
elif choice == 'eur':
    cache_dict['usd'] = _dict['usd']
else:
    cache_dict = {'usd': _dict['usd'], 'eur': _dict['eur']}
# print(cache_dict)
# print(_dict['usd'])
# print(_dict['eur'])

while True:
    goal_currency = input().lower()
    if goal_currency == '':
        break
    money = input()
    if money == '':
        break
    else:
        money = float(money)
    print('Checking the cache...')
    if goal_currency in cache_dict:
        print('Oh! It is in the cache!')
        rate = cache_dict[goal_currency]['rate']
        print(f'You received {round(rate * money, 2)} {goal_currency.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        cache_dict[goal_currency] = _dict[goal_currency]
        rate = cache_dict[goal_currency]['rate']
        print(f'You received {round(rate * money, 2)} {goal_currency.upper()}.')
