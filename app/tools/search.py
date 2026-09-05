import os
import subprocess


class CodeSearch:

    def search(self, query: str):

        workspace = os.environ.get(
            "DEVFLOW_WORKSPACE",
            "./workspace"
        )

        result = subprocess.run(
            [
                "grep",
                "-R",
                "-n",
                query,
                workspace
            ],
            capture_output=True,
            text=True
        )

        return result.stdout[:15000]

#Its job is to let an agent search the downloaded GitHub repository for a particular piece of code/text.