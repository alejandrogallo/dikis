"""Tests for `dikis` package."""

import pytest
from pkg_resources import parse_version

import dikis


def test_valid_version():
    """Check that the package defines a valid __version__"""
    assert parse_version(dikis.__version__) >= parse_version("0.1.0")
