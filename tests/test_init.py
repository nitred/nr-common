# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test modules."""


def test_init(hello_world):
    """Run a test."""
    import nr_common

    # Test __init__
    assert hasattr(nr_common, '__version__')

    # Test pytest fixtures
    assert(hello_world == "Hello World!")
