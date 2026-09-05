class CoderAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def run(self, state):

        prompt = f"""
You are the implementation agent.

GitHub issue:
{state["issue_title"]}

Issue:
{state["issue_body"]}

Implementation plan:
{state["implementation_plan"]}

Relevant files:
{state["file_contents"]}

Implement the planned change.

Rules:

1. Modify only necessary files.
2. Preserve existing architecture.
3. Do not introduce unnecessary dependencies.
4. Add or update tests.
5. Do not change unrelated code.
6. Explain every modification.
"""

        result = self.llm.generate(prompt)

        return {
            **state,
            "patch": result
        }


# For the real project, we'll replace this with a tool-enabled agent that can:
# read_file
# search
# write_file
# run_tests
# git_diff
# That's one of the sections I'd build with you after the architecture is working.