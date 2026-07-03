# ============================================================
# tests/test_app_femi.py
# ============================================================
# WHY: Smoke test the example module to illustrate the role
# of tests in professional project workflows.
#
# Run:
#   uv run python -m pytest

from mlstudio import app_femi


def test_app_case_has_main() -> None:
    """Verify the example module exposes a main function."""
    assert callable(app_femi.main)
