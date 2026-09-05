from app.llm.gemini import GeminiClient


class PlannerAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def run(self, state):

        files = state.get(
            "file_contents",
            {}
        )

        prompt = f"""
You are a senior software engineer.

GitHub issue:

{state["issue_title"]}

{state["issue_body"]}

Relevant source files:

{files}

Create an implementation plan.

Your plan must include:

1. Root cause
2. Files to modify
3. Changes required
4. Tests that should be added or modified
5. Potential edge cases

Do NOT write implementation code.
"""

        plan = self.llm.generate(prompt)

        return {
            **state,
            "implementation_plan": plan
        } 

#gets the relevant code, does not edit anything
