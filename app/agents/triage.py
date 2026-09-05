from app.llm.gemini import GeminiClient
class TriageAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def run(self, state):

        issue = f"""
Title:
{state["issue_title"]}

Description:
{state["issue_body"]}
"""
        prompt = f"""
You are a software engineering issue triage agent.
Analyze the GitHub issue below.
{issue}
Return:

TYPE: one of
- bug
- feature
- refactor
- documentation
- test
COMPLEXITY: one of
- low
- medium
- high
REASON:
Explain why.
Do not propose code yet.
"""

        result = self.llm.generate(prompt)

        lines = result.splitlines()

        issue_type = "unknown"
        complexity = "unknown"

        for line in lines:

            if line.startswith("TYPE:"):
                issue_type = line.split(":", 1)[1].strip()

            if line.startswith("COMPLEXITY:"):
                complexity = line.split(":", 1)[1].strip()

        return {
            **state,
            "issue_type": issue_type,
            "complexity": complexity,
            "triage_reason": result
        }
#github issue->agent answer(type,complexity, reason)->graph is provided with ans ans

