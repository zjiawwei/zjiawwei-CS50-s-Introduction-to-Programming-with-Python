import pytest
from datetime import date
from unittest.mock import patch
from seasons import Time

Fixed_today = date(2026,3,22)

def test_valid_dates():
    with patch('seasons.date') as mock_date:
        mock_date.today.return_value  = Fixed_today
        mock_date.fromisoformat = date.fromisoformat

        time_obj = Time(date(2026,3,22))
        assert time_obj.calculate_minutes() == 0

        time_obj = Time(date(2026,3,21))
        assert time_obj.calculate_minutes() == 1440

def test_fruture_dates():
    with patch('seasons.date') as mock_date:
        mock_date.today.return_value = Fixed_today
        
        time_obj = Time(date(2026,3,23))
        with pytest.raises(ValueError):
            time_obj.calculate_minutes()