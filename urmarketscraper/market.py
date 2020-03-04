from .offer_list import _html_to_soup, _get_offer_list, _find_offers


#Constants
BASE_MARKET_URL = "https://www.urban-rivals.com/market/?"


def get_market_offers(session, ids, base_market_url=BASE_MARKET_URL):
    if len(ids) < 1:
        raise ValueError("Ids cannot be empty")
    if not base_market_url.endswith("?"):
        raise ValueError("URL must end with a question mark")
    market = {
        char_id:
        _html_to_soup(
            session.get(
                _get_offer_list(char_id, base_market_url)
        ))
        for char_id in map(abs, ids)
    }
    return {char_id :_find_offers(market[char_id])
            for char_id in map(abs, ids) }