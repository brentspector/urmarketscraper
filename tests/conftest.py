import pickle, os
from pytest import fixture

# Optional markers
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "create_file(file_name): name of file that will be created in resources folder"
    )


# Location of Test Resource files
@fixture(scope="session")
def test_resource_dir():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'resources',
        )


@fixture(scope="module")
def mocked_session(test_resource_dir):
    file_location = os.path.join(test_resource_dir, "market_session.txt")
    with open(file_location, "rb") as f:
            return pickle.load(f)


@fixture
def create_file(request, test_resource_dir):
    content_list = []
    yield content_list
    for mark in request.node.iter_markers("create_file"):
        for file, content in zip(mark.args, content_list):
            file_location = os.path.join(test_resource_dir, file)
            with open(file_location, "wb") as f:
                pickle.dump(content, f)