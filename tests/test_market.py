import urmarketscraper.market as market
from requests import Session


# Happy Path - Basic usage with int
def test_list_of_ints(monkeypatch, mocked_session):
    monkeypatch.setattr(Session, "get", lambda a,b: mocked_session)
    assert market.get_market_offers(Session(), [14, 15]) == 6, "This is what happened"

# Happy Path - Basic usage with string

# Happy Path - Generator of int (range)

# Happy Path - Generator of string

# Happy Path - Tuple of int

# Happy Path - Tuple of string

# Happy Path - Tuple of mixed int and string

# Happy Path - Filters out duplicates

# Happy Path - Absolute Value

# Happy Path - Overrides Base Market URL

# Invalid Type - Float

# Invalid Type - Float as String

# Invalid Type - Dict

# Invalid Type - None

# Invalid Input - Empty ids

# Invalid Input - Bad Session

# Invalid Input - Bad Base Market URL
