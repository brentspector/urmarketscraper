.. _advanced-usage:

Advanced Usages
===============

Generator
---------
:Note: Using `Range` is not recommended as it will \
    generate hits for each number. To reduce network traffic, \
    use a generator function with only ids you are interested in.

>>> import urmarketscraper.market as market
>>> market.get_market_offers(session, range(1400,1420))
Returns:
    {1400: Offer, 1401: Offer, ... , 1419: Offer}

>>> import urmarketscraper.market as market
>>> def gen_func(max):
...     n = 800
...     while n < max:
...         yield n
...         n += 3
>>> market.get_market_offers(session, gen_func(806))
Returns:
    {800: Offer, 803: Offer, 806: Offer}


Tuple
-----
>>> import urmarketscraper.market as market
>>> market.get_market_offers(session, (1203,1320,))
Returns:
    {1203: Offer, 1320: Offer}

Dict
----
>>> import urmarketscraper.market as market
>>> market.get_market_offers(session, {1522: 'whatever', 1623: ["maybe a random list"]})
Returns:
    {1522: Offer, 1623: Offer}

Proxy URL
---------
:Note: If you desire more control over where the request is going, you can submit your own \
    URL which can be used for proxy routing. Ideally a VPN would accomplish this for you, \
    but if you need more control, this is for you.

>>> import urmarketscraper.market as market
>>> market.get_market_offers(session, [1234, 1235], "http://secreturl.com?")
Returns:
    {1234: Offer, 1235: Offer}