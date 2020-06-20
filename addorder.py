#!/usr/bin/env python

# This file is part of krakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# Add order to buy 1 BTC at 1€

import krakenex

def main():
    kraken = krakenex.API()
    kraken.load_key('kraken.key')

    response = kraken.query_private('AddOrder',
                                    {'pair': 'XXBTZEUR',
                                     'type': 'buy',
                                     'ordertype': 'limit',
                                     'price': '1',
                                     'volume': '1',
                                     })
    return response

if __name__ == '__main__':
    ret = main()
    print(ret)