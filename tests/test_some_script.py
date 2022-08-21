#!/usr/bin/env python
from fluentqatpl.some_script import hello_world


def test_hello_world():
    assert "hello" == hello_world()
