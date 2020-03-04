import urmarketscraper.market as market
from requests import Session
from unittest import mock
from pytest import raises


# Happy Path - Basic usage
def test_list_of_ints(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_session)
    offer = market.get_market_offers(Session(), [14, 15])
    for k in offer:
        print(k)
        for k,v in offer[k].__dict__.items():
            print("Key is ", k, " and value is ", v)
    # Since session is immutable from file, id given and found are different
    assert offer[14].id == 1462
    assert offer[15].id == 1462


# Happy Path - Generator
def test_generator_of_ints(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_session)
    offer = market.get_market_offers(Session(), range(14, 16))
    for k in offer:
        print(k)
        for k,v in offer[k].__dict__.items():
            print("Key is ", k, " and value is ", v)
    # Since session is immutable from file, id given and found are different
    assert offer[14].id == 1462
    assert offer[15].id == 1462


# Happy Path - Tuple
def test_tuple_of_ints(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_session)
    offer = market.get_market_offers(Session(), (14,15,))
    for k in offer:
        print(k)
        for k,v in offer[k].__dict__.items():
            print("Key is ", k, " and value is ", v)
    # Since session is immutable from file, id given and found are different
    assert offer[14].id == 1462
    assert offer[15].id == 1462


# Happy Path - Dict
def test_dict_uses_keys(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_session)
    offer = market.get_market_offers(Session(), {14: "a", 15: "b"})
    for k in offer:
        print(k)
        for k,v in offer[k].__dict__.items():
            print("Key is ", k, " and value is ", v)
    # Since session is immutable from file, id given and found are different
    assert offer[14].id == 1462
    assert offer[15].id == 1462


# Happy Path - Absolute Value
def test_absolute_value_of_ints(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_session)
    offer = market.get_market_offers(Session(), [-14, -15])
    for k in offer:
        print(k)
        for k,v in offer[k].__dict__.items():
            print("Key is ", k, " and value is ", v)
    # Since session is immutable from file, id given and found are different
    assert offer[14].id == 1462
    assert offer[15].id == 1462


# Happy Path - Uses Base URL by Default
def test_base_market_url_provided(monkeypatch, mocked_session):
    m = mock.Mock()
    m.return_value = mocked_session
    monkeypatch.setattr(Session, "get", m)
    offer = market.get_market_offers(Session(), [14])
    print(m.call_args.args)
    assert market.BASE_MARKET_URL in m.call_args.args[0]


# Happy Path - Overrides Base Market URL
def test_overrides_base_market_url(monkeypatch, mocked_session):
    override_url = "http://sample.com?"
    m = mock.Mock()
    m.return_value = mocked_session
    monkeypatch.setattr(Session, "get", m)
    offer = market.get_market_offers(Session(), [14], override_url)
    print(m.call_args.args)
    assert override_url in m.call_args.args[0]


# Invalid Type - None
def test_none_fails(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_session)
    with raises(TypeError):
        market.get_market_offers(Session(), None)


# Invalid Input - Empty ids
def test_empty_ids_fails(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_session)
    with raises(ValueError):
        market.get_market_offers(Session(), [])

# Invalid Input - Base URL Missing '?'
def test_bad_url(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_session)
    with raises(ValueError):
        market.get_market_offers(Session(), [], "http://sample.com")