from app.llm.gemini import GeminiClient


class ContextAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def run(self, state):

        tree = state["repository_tree"]

        prompt = f"""
You are a software repository analysis agent.
GitHub issue:
TITLE:
{state["issue_title"]}
DESCRIPTION:
{state["issue_body"]}
Repository tree:
{tree}
Identify the files most likely relevant to this issue.
Return:
FILES:
- file1
- file2
- file3

REASONING:
Explain why these files are relevant.

Do not write code.
"""

        result = self.llm.generate(prompt)

        files = []

        collecting = False

        for line in result.splitlines():

            if line.strip() == "FILES:":
                collecting = True
                continue

            if line.strip() == "REASONING:":
                collecting = False

            if collecting and line.strip().startswith("-"):
                files.append(
                    line.strip()[1:].strip()
                )

        return {
            **state,
            "relevant_files": files
        }