import pytest
from phases.phase_12_reliability_recovery.recovery import retry_with_limit


def test_retry_succeeds_after_transient_timeout():
    calls = {"count": 0}

    def operation():
        calls["count"] += 1
        if calls["count"] < 3:
            raise TimeoutError("temporary")
        return "ok"

    assert retry_with_limit(operation, max_attempts=3) == "ok"
    assert calls["count"] == 3


def test_retry_stops_at_limit():
    calls = {"count": 0}

    def operation():
        calls["count"] += 1
        raise ConnectionError("offline")

    with pytest.raises(RuntimeError):
        retry_with_limit(operation, max_attempts=2)
    assert calls["count"] == 2
