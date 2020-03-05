#Urban Rivals Market Scraper

##Collects market offers for Urban Rivals.

####Install from https://pypi.org/project/urmarketscraper/

This is a screen scraper utility for [Urban Rivals](https://www.urban-rivals.com).

To use, call `market.get_market_offers`

The first parameter is the `requests.Session()` object which contains a logged-in
user. The second parameter is the list of `ids` for the characters in question.
The third parameter is an optional override for what what the base market address
is. Default is `https://www.urban-rivals.com/market/?`. Any url given here must end
with a `?` so that the URL encoding can complete correctly.

[Basic Usage Example](docs/market/basic-usage.rst)