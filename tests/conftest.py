import pickle, os
from pytest import fixture


# Location of Test Resource files
@fixture(scope="session")
def test_resource_dir():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'resources',
        )


@fixture(scope="module")
def mocked_session(request, test_resource_dir):
    file_location = os.path.join(test_resource_dir, 'market_session.txt')
    with open(file_location, "rb") as f:
            return pickle.load(f)