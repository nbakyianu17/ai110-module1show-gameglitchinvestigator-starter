# logic_utils.py
# This file contains the core game logic separated from the Streamlit UI.
# Moving logic here makes the code easier to test with pytest.


def get_range_for_difficulty(difficulty: str):
    """
    Return the number range for each difficulty level.

    Easy   → smaller range
    Normal → medium range
    Hard   → large range

    Returns a tuple (low, high).
    """

    # FIX: Difficulty ranges in app.py were inconsistent
    # Hard had a smaller range than Normal.
    # We corrected it so difficulty actually increases.

    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 50
    elif difficulty == "Hard":
        return 1, 100

    # Default fallback if something unexpected happens
    return 1, 50


def parse_guess(raw: str):
    """
    Convert user input into a valid integer guess.

    Returns:
    (ok, guess_value, error_message)

    ok = True if parsing worked
    guess_value = integer guess
    error_message = message to display if input is invalid
    """

    # If user didn't type anything
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    # FIX: previous logic allowed decimals like "12.7"
    # which would silently convert to 12.
    # We now reject non-integer input.

    try:
        value = int(raw)
    except ValueError:
        return False, None, "Please enter a whole number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare the player's guess to the secret number.

    Returns:
    (outcome, message)

    outcome examples:
    "Win"
    "Too High"
    "Too Low"
    """

    # Player guessed correctly
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: In app.py the hint directions were backwards.
    # If the guess is higher than the secret,
    # the player should be told to go LOWER.

    if guess > secret:
        return "Too High", "📉 Try LOWER!"

    else:
        return "Too Low", "📈 Try HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update the player's score based on the result.

    Lower attempts = higher score.
    Winning quickly rewards more points.
    """

    # If player wins early they earn more points.
    if outcome == "Win":

        # FIX: Prevent division issues and reward faster wins
        score_gain = max(10 - attempt_number, 1)

        return current_score + score_gain

    # No score change if guess was incorrect
    return current_score
