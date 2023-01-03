#!/usr/bin/env python
"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest


@pytest.fixture
def some_fixture():
    return


class Test{{ cookiecutter.project_slug|title }}:
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def test_000_something(self, some_fixture):
        """Test something."""
        assert False


