import click.testing
import pytest
import requests

from example_package_lth import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_print_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_use_en_wikipedia_org(runner, mock_requests_get):
    result = runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fail_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception("Failed")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output
