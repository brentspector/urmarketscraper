.. urmarketscraper documentation master file, created by
   sphinx-quickstart on Tue Mar  3 16:25:22 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Full Documentation
==================
A basic example can be found at :ref:`basic-usage`

Example
-------
>>> from urmarketscraper import market
>>> market.get_market_offers(session, ["1462", "1463"])
Returns:
    {"1462": {"_Offer__id": 1462, "_Offer__level_price_dict": {"1": "799", "4": "799"}}, "1463": {"_Offer__id": 1463,
 "_Offer__level_price_dict": {"2": "27887"}}}

Market Module
-------------
.. automodule:: urmarketscraper.market
   :members:

Offer Object
------------
.. autoclass:: urmarketscraper.offer.Offer
   :members:
   :noindex:

urmarketscraper Documentation TOC
===========================================

.. toctree::
   :maxdepth: 0
   :caption: Contents:

   offer/offer
   market/basic-usage
   market/advanced-usage

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`