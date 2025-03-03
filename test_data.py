import pytest
from data_provider import DataProvider

@pytest.mark.parametrize("username, password", DataProvider.read_csv("data.csv"))
def test_login(username, password):
    print(f"Testing login with {username} and {password}")
