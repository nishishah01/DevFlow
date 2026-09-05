from fastapi import FastAPI

from app.api.schemas import IssueRequest

app = FastAPI(
    title="DevFlow",
    description="Agentic Software Engineering Platform"
)


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/run")
def run_issue(
    request: IssueRequest
):

    return {
        "message": "Workflow started",
        "owner": request.owner,
        "repo": request.repo,
        "issue": request.issue_number
    }