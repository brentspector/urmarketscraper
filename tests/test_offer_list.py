import urmarketscraper.offer_list as offer_list
import urmarketscraper.offer as offer
from bs4 import BeautifulSoup
from pytest import raises

# Happy Path - Beautiful Soup
def test_html_soup(mocked_session):
    assert type(offer_list._html_to_soup(mocked_session)) == BeautifulSoup


# Happy Path - Get Offer Int Id
def test_get_offer_with_int_id():
    assert "search=14" in offer_list._get_offer_list(14, "http://sample.com?")


# Happy Path - Get Offer String Id
def test_get_offer_with_string_id():
    assert "search=14" in offer_list._get_offer_list("14", "http://sample.com?")


# Happy Path - Get Offer Base Market URL
def test_get_offer_with_url():
    assert "http://sample.com?" in offer_list._get_offer_list(14, "http://sample.com?")


# Happy Path - Find Offer
def test_find_offer(mocked_session):
    page = offer_list._html_to_soup(mocked_session)
    assert type(offer_list._find_offers(page)) == offer.Offer


# Happy Path - Get Offer Id
def test_get_offer_id(mocked_session):
    page = offer_list._html_to_soup(mocked_session)
    assert offer_list._get_offer_id(page) == 1462


# Happy Path - Create Offer Dict
def test_create_offer_dict(mocked_session):
    page = offer_list._html_to_soup(mocked_session)
    assert offer_list._create_offer_dict(page)[4] == "888"


# Invalid Type - Get Offer None Id
def test_get_offer_with_none_id_fails():
    with raises(TypeError):
        offer_list._get_offer_list(None, "http://sample.com?")


# Invalid Input - Get Offer Empty Id
def test_get_offer_with_none_id_fails():
    with raises(ValueError):
        offer_list._get_offer_list('', "http://sample.com?")