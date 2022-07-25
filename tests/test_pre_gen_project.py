#!/usr/bin/env python
from hooks.pre_gen_project import validate_line_length
import pytest


def test_validate_project_name():
    assert validate_line_length(88) is None
    with pytest.raises(ValueError):
        validate_line_length(1_000)

    with pytest.raises(ValueError):
        validate_line_length(-10)
