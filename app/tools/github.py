import os
import requests
class GitHubClient:
    def __init__(self):
        self.token = os.environ["GITHUB_TOKEN"]
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    def get_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int
    ):

        url = (
            f"{self.base_url}/repos/"
            f"{owner}/{repo}/issues/{issue_number}"
        )
        response = requests.get(
            url,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_repo_tree(
        self,
        owner: str,
        repo: str
    ):

        url = (
            f"{self.base_url}/repos/"
            f"{owner}/{repo}/git/trees/main"
            "?recursive=1"
        )

        response = requests.get(
            url,
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()

    def create_branch(
        self,
        owner,
        repo,
        branch_name,
        sha
    ):

        url = (
            f"{self.base_url}/repos/"
            f"{owner}/{repo}/git/refs"
        )

        payload = {
            "ref": f"refs/heads/{branch_name}",
            "sha": sha,
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        response.raise_for_status()

        return response.json()

    def create_pull_request(
        self,
        owner,
        repo,
        title,
        body,
        head,
        base="main"
    ):

        url = (
            f"{self.base_url}/repos/"
            f"{owner}/{repo}/pulls"
        )

        payload = {
            "title": title,
            "body": body,
            "head": head,
            "base": base,
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        response.raise_for_status()

        return response.json()

