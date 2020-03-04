import urmarketscraper.offer as offer
from pytest import raises


TEST_DICT = {2: "456", 3: "789", 1: "123", 4: "101"}
FULL_OFFER = offer.Offer(1, TEST_DICT)


# Happy Path - No Args Init
def test_init_no_args():
    myoffer = offer.Offer()
    assert myoffer.id == 0
    assert myoffer.level_price_dict is None


# Happy Path - Init Int Id
def test_init_int_id():
    myoffer = offer.Offer(1)
    assert myoffer.id == 1


# Happy Path - Init String Id
def test_init_string_id():
    myoffer = offer.Offer("1")
    assert myoffer.id == 1


# Happy Path - Level Price Dict Sorted on Init
def test_init_level_price_dict_sorted():
    keys = list(FULL_OFFER.level_price_dict.keys())
    print(keys)
    assert FULL_OFFER._is_level_price_dict_sorted(), "Level Price Dict should be sorted on init"


# Happy Path - Level Price Dict Missing
def test_init_level_price_dict_missing():
    myoffer = offer.Offer(1)
    assert myoffer.level_price_dict is None


# Happy Path - Init Named Args Out of Order
def test_init_named_args_out_of_order():
    myoffer = offer.Offer(level_price_dict=TEST_DICT, id=1)
    assert myoffer.id == 1
    assert myoffer.level_price_dict == TEST_DICT


# Happy Path - Level Price Dict Sorted
def test_sort_level_price_dict():
    myoffer = offer.Offer()
    assert myoffer.level_price_dict is None
    myoffer.level_price_dict = TEST_DICT
    keys = list(myoffer.level_price_dict.keys())
    assert myoffer._is_level_price_dict_sorted()
    assert myoffer.level_price_dict[keys[0]] == "101", "Level Price Dict values should not be assigned to wrong key"


# Happy Path - Get Min Price
def test_min_price():
    assert FULL_OFFER.get_min_price() == "101"


# Happy Path - Get Min Level
def test_min_level():
    assert FULL_OFFER.get_min_level() == 4


# Happy Path - Get Rel Price Available Int
def test_rel_price_int():
    assert FULL_OFFER.get_rel_price(2) == "456"


# Happy Path - Get Rel Price Available String
def test_rel_price_string():
    assert FULL_OFFER.get_rel_price("2") == "456"


# Happy Path - Get Rel Price Unavailable
def test_rel_price_unavailable():
    assert FULL_OFFER.get_rel_price(5) == "101"


# Happy Path - Get Rel Level Available Int
def test_rel_level_int():
    assert FULL_OFFER.get_rel_level(4) == 4


# Happy Path - Get Rel Level Available String
def test_rel_level_string():
    assert FULL_OFFER.get_rel_level("4") == "4"


# Happy Path - Get Rel Level Unavailable
def test_rel_level_unavailable():
    assert FULL_OFFER.get_rel_level(5) == 4


# Invalid Input - Init Args Out of Order
def test_init_args_out_of_order_fails():
    with raises(TypeError):
        offer.Offer(TEST_DICT, 1)


# Invalid Input - Level Price Dict is Tuple
def test_level_price_dict_tuple_fails():
    myoffer = offer.Offer(1, {(1, 2), (3, 4)})
    assert myoffer.level_price_dict is None
