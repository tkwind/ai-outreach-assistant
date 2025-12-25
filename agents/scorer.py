from prompts import lead_scoring_prompt
from config import DEFAULT_SCORE, DEFAULT_PRIORITY, DEFAULT_REASON
from utils import call_llm  # if call_llm is elsewhere, adjust import


def safe_parse_score(output):
    try:
        lines = [line.strip() for line in output.splitlines() if ":" in line]

        score = int(lines[0].split(":", 1)[1].strip())
        priority = lines[1].split(":", 1)[1].strip()
        reason = lines[2].split(":", 1)[1].strip()

        if not (1 <= score <= 10):
            raise ValueError

        return score, priority, reason

    except Exception:
        return DEFAULT_SCORE, DEFAULT_PRIORITY, DEFAULT_REASON


def score_lead(lead):
    scoring_output = call_llm(lead_scoring_prompt(lead))
    return safe_parse_score(scoring_output)
