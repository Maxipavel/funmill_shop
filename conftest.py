import pytest as pytest


@pytest.fixture()
def set_up():
    print("START TEST")
    yield
    print("\nFINISH TEST")