from prompts import outreach_prompt
from utils import call_llm  # adjust if needed


def generate_outreach(lead):
    return call_llm(outreach_prompt(lead))
