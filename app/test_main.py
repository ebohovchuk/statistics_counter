from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_delete_statistic_by_correct_id():
    pass


def test_delete_statistic_by_incorrect_id():
    pass


def test_read_statistic_with_filter_from_date():
    pass


def test_read_statistic_with_incorrect_filter_from_date():
    pass


def test_read_statistic_with_filter_to_date():
    pass


def test_read_statistic_with_incorrect_filter_to_date():
    pass


def test_read_statistic_with_filter_from_date_and_to_date():
    pass


def test_read_statistic_with_all_filters_and_order_by():
    pass


def test_read_statistic_with_all_filters_and_incorrect_order_by():
    pass
