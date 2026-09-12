import pytest
from unittest.mock import patch
from datetime import date
from app.main import outdated_products


@patch("datetime.date")
def test_outdated_products(mock_today: pytest.Mock) -> None:
    mock_today.return_value = date(2022, 2, 15)
    results = outdated_products([])
    assert results == []
