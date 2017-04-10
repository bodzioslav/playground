#!/usr/bin/env python3

import argparse
import requests

def get_currency_rates(source_currency, target_currency):
   
   if source_currency.upper() == 'PLN': 
      source_rate = 1
   else:
      source_url = 'http://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'.format(source_currency.upper())
      source_rate = requests.get(source_url).json()['rates'][0]['mid']
   
   if target_currency.upper() == 'PLN':
      target_rate = 1
   else:
      target_url = 'http://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'.format(target_currency.upper())
      target_rate = requests.get(target_url).json()['rates'][0]['mid'] 

   return source_rate, target_rate

if __name__ == "__main__":

   parser = argparse.ArgumentParser()

   parser.add_argument("amount", help="how much you want to convert", type=float)
   parser.add_argument("source_currency", help="currency you want to convert from")
   parser.add_argument("target_currency", help="currency you want to convert to")
   parser.add_argument("-v", "--verbose", help="increase output verbosity", action = "store_true")

   args = parser.parse_args()

   source_value, target_value = get_currency_rates(args.source_currency, args.target_currency)
   result = round(args.amount * source_value / target_value, 2) 

   if args.verbose:
      print('Converted from {} to {}:'.format(args.source_currency, args.target_currency), result)
   else:
      print(result)
