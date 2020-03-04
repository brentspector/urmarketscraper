.. _basic-usage:

Basic Usage
===========

Setting Up
----------
#. Install the `urmarketscraper` module

    ::

        pip install urmarketscraper

    :Note: Alternatively, use a dependency manager like Poetry_.

    .. _Poetry: https://python-poetry.org/

    ::

        poetry add urmarketscraper

#. Import into your code::

    >>> import urmarketscraper.market as market
    >>> from urllib.parse import urlencode

:Note: `urlencode` is my recommendation for appending query elements
    to a base URL. You can choose anything so long as you get the
    correct output.

Usage
-----
#. Authenticate with Urban Rivals

    :Note: Replace `your_username` and `your_password` with the correct values
        for your account. If you are not comfortable putting your password in
        code, you can search for examples for extracting values during runtime,
        such as environment variables or password storage APIs.

    ::

        >>> URL = 'https://www.urban-rivals.com/ajax/player/account/'
        >>> FORM_DATA = {
        ...     'login': 'your_username',
        ...    'password': 'your_password',
        ...    'action': 'signin',
        ...    'frompage': ''
        ... }
        >>> AUTH_URL = URL + '?' + urlencode(FORM_DATA)
        >>> with requests.Session() as session:
        ...     auth = session.get(AUTH_URL)

#. Run the function

    ::

        >>> if "redirect" in auth.text:
        ...     list = offer_list.get_market_offers(session, [1200, 1233])
        Returns:
            {1200: Offer, 1233: Offer}

        ...     list = offer_list.get_market_offers(session, ["1200", "1233"])
        Returns:
            {"1200": Offer, "1233": Offer}

    :Note: The list `[1200, 1233]` can be replaced with a number of things.
        Please read :ref:`advanced-usage` for more examples.