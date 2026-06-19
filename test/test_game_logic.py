import pytest
from logic_utils import check_guess


# --- Swapped hint messages bug ---

def test_too_low_says_go_higher():
    """Guess below secret must tell the player to go higher, not lower."""
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_too_high_says_go_lower():
    """Guess above secret must tell the player to go lower, not higher."""
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


# --- String-vs-int comparison bug (even attempts passed secret as str) ---

def test_check_guess_secret_as_string_too_low():
    """Passing secret as a string should still compare numerically."""
    outcome, message = check_guess(5, "42")
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_check_guess_secret_as_string_too_high():
    outcome, message = check_guess(99, "42")
    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_secret_as_string_win():
    outcome, _ = check_guess(42, "42")
    assert outcome == "Win"


# --- Sanity: correct numeric comparisons ---

def test_exact_match():
    outcome, message = check_guess(7, 7)
    assert outcome == "Win"
    assert "Correct" in message
