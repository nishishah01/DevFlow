from pydantic import BaseModel


class IssueRequest(BaseModel):

    owner: str
    repo: str
    issue_number: int