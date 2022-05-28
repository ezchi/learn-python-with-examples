import pytest






def f():
  raise SystemExit(1)


def test_raise_system_exit():
    with pytest.raises(SystemExit):

          f()
