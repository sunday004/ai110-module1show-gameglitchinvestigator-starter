from logic_utils import check_guess, update_high_score, update_score


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


def test_high_score_updates_when_score_is_higher():
    assert update_high_score(current_high_score=80, current_score=100) == 100


def test_high_score_does_not_change_when_score_is_lower():
    assert update_high_score(current_high_score=100, current_score=90) == 100


def _apply_new_game_reset_without_touching_high_score(state):
    """Mirror app new-game logic where high score is intentionally preserved."""
    state["attempts"] = 0
    state["score"] = 0
    state["status"] = "playing"
    state["history"] = []


def test_high_score_is_not_reset_by_new_game_logic():
    state = {
        "attempts": 4,
        "score": 70,
        "high_score": 120,
        "status": "won",
        "history": [11, 22, 33, 44],
    }

    _apply_new_game_reset_without_touching_high_score(state)

    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    assert state["high_score"] == 120
