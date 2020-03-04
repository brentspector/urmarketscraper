import itertools
from .offer import Offer
from bs4 import BeautifulSoup
from urllib.parse import urlencode


def _html_to_soup(response):
    return BeautifulSoup(response.text, "html.parser")


def _get_offer_list(id, base_market_url):
    int_id = int(id)
    return base_market_url + urlencode({'action': 'buy', 'page': 0,
                                        'id_familly': 0, 'sortby': 'price',
                                        'orderby': 'asc', 'rarity': 'all',
                                        'group': 'all', 'id_artist': 0,
                                        'id_format': 0, 'search': int_id})


def _find_offers(page):
    return Offer(_get_offer_id(page), _create_offer_dict(page))


def _get_offer_id(page):
    return int(page.find(class_="text-character")['data-character-id'])


def _create_offer_dict(page):
    return {
        len(row.find_all(src='https://s.acdn.ur-img.com/img/v3/card/icon-star-on.png')):
            "".join(next(itertools.islice(row.stripped_strings, 2, 3)).split())
        for row in reversed(page.tbody.find_all('tr'))
    }

# TODO: Docs
