from logic_utils import check_guess, update_score


def test_winning_guess_outcome_and_message():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high_outcome_and_hint_direction():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low_outcome_and_hint_direction():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_score_first_try_win_is_100():
    score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert score == 100


def test_score_wrong_guess_penalty_is_consistent():
    score_after_high = update_score(current_score=50, outcome="Too High", attempt_number=2)
    score_after_low = update_score(current_score=50, outcome="Too Low", attempt_number=2)
    assert score_after_high == 45
    assert score_after_low == 45


def test_win_score_has_minimum_floor_of_10():
    # Very late wins should still award at least 10 points.
    score = update_score(current_score=0, outcome="Win", attempt_number=20)
    assert score == 10


def _initialize_secret_if_missing(state, low, high, randint_fn):
    """Mirror the app's fixed secret initialization behavior for regression testing."""
    if "secret" not in state:
        state["secret"] = randint_fn(low, high)
    return state["secret"]


def test_secret_stays_stable_across_reruns_once_initialized():
    calls = []

    def fake_randint(low, high):
        calls.append((low, high))
        return 42 if len(calls) == 1 else 99

    state = {}
    first_secret = _initialize_secret_if_missing(state, 1, 100, fake_randint)
    second_secret = _initialize_secret_if_missing(state, 1, 100, fake_randint)

    assert first_secret == 42
    assert second_secret == 42
    assert state["secret"] == 42
    assert len(calls) == 1
