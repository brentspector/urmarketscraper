from .offer_list import _html_to_soup, _get_offer_list, _find_offers, BASE_MARKET_URL


def get_market_offers(session, ids, base_market_url=BASE_MARKET_URL):
    market = [
        _html_to_soup(
            session.get(
            _get_offer_list(id)
        ))
        for id in ids
    ]

    return _find_offers(market)