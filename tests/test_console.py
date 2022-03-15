import click.testing
import pytest

from example_package_lth import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Test title",
        "extract": "Test extract",
    }
    return mock


def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
