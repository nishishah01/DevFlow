from app.tools.shell import run_command


class TesterAgent:

    def run(self, state):

        result = run_command(
            "pytest -q"
        )

        passed = result["returncode"] == 0

        return {
            **state,

            "test_command": "pytest -q",

            "test_output": (
                result["stdout"]
                + "\n"
                + result["stderr"]
            ),

            "tests_passed": passed
        }
    
#coder->tester->test passed or failed->graph is provided with ans ans
#if failed, the agent can use the test output to debug and fix the code.
