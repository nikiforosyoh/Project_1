import os
from html5validator import Validator


def test_portfolio_html_valid():
    html_file = os.path.join(os.path.dirname(__file__), os.pardir, "nikiforos_portfolio.html")
    html_file = os.path.abspath(html_file)
    validator = Validator()
    errors = validator.validate([html_file])
    assert errors == 0, f"HTML validation failed with {errors} error(s)"
