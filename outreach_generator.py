import pandas as pd

from agents.scorer import score_lead
from agents.messenger import generate_outreach
from config import MIN_SCORE_FOR_OUTREACH
from utils import call_llm  # used internally if needed


def main():
    leads = pd.read_csv("data\\leads.csv")

    scores, priorities, reasons, messages, decision_traces = [], [], [], [], []

    for _, row in leads.iterrows():
        lead = row.to_dict()

        #Decision Agent
        score, priority, reason = score_lead(lead)

        print(f"\nScored {lead['name']} → {score}/10 ({priority})")
        print(f"Reason: {reason}")

        decision_trace = f"Score {score}/10 ({priority}) because {reason.lower()}. "

        # Execution Agent
        if score >= MIN_SCORE_FOR_OUTREACH:
            message = generate_outreach(lead)
            decision_trace += "Outreach generated."
        else:
            message = "Skipped (below score threshold)"
            decision_trace += f"Skipped because score below threshold ({MIN_SCORE_FOR_OUTREACH})."

        scores.append(score)
        priorities.append(priority)
        reasons.append(reason)
        messages.append(message)
        decision_traces.append(decision_trace)

        print("-" * 50)

    leads["lead_score"] = scores
    leads["priority"] = priorities
    leads["score_reason"] = reasons
    leads["decision_trace"] = decision_traces
    leads["outreach_message"] = messages

    leads.to_csv("data\\output_messages.csv", index=False)
    print("\n Agentic workflow completed and saved.")


if __name__ == "__main__":
    main()
