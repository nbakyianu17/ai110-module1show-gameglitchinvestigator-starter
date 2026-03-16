from logic_utils import check_guess, parse_guess

# --- Bug fix: hint direction was reversed ---

def test_too_high_message_says_lower():
    # Guess is above secret → player should be told to go LOWER, not higher
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # was wrongly showing "HIGHER" before the fix

def test_too_low_message_says_higher():
    # Guess is below secret → player should be told to go HIGHER, not lower
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message  # was wrongly showing "LOWER" before the fix

# --- Bug fix: decimal values were silently accepted ---

def test_decimal_input_is_rejected():
    # "12.7" should not be accepted as 12 — must return an error
    ok, value, error = parse_guess("12.7")
    assert ok == False
    assert value is None
    assert error is not None  # e.g. "Please enter a whole number."

def test_decimal_zero_is_rejected():
    # "5.0" looks like a whole number but is still a decimal string
    ok, value, error = parse_guess("5.0")
    assert ok == False
    assert value is None

def test_integer_string_is_accepted():
    # Sanity check: plain integers should still work fine
    ok, value, error = parse_guess("42")
    assert ok == True
    assert value == 42
    assert error is None
