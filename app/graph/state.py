from typing import TypedDict, List, Dict, Optional

class DevFlowState(TypedDict, total=False):

    # GitHub
    owner: str
    repo: str
    issue_number: int

    issue_title: str
    issue_body: str

    # Triage
    issue_type: str
    complexity: str
    triage_reason: str  

    # Context
    repository_tree: str
    relevant_files: List[str]
    file_contents: Dict[str, str]

    # Planning
    implementation_plan: str
    affected_files: List[str]

    # Coding
    changed_files: List[str]
    patch: str

    # Testing
    test_command: str
    test_output: str
    tests_passed: bool
    retry_count: int

    # Review
    review_status: str
    review_comments: List[str]

    # Human approval
    human_approved: bool

    # GitHub
    branch_name: str
    pull_request_url: Optional[str]

    # Error handling
    errors: List[str]

#every agent reads from and writes to this state object.
# This allows for a single source of truth for the entire workflow,
# and makes it easy to debug and understand the state of the system at any point in time.

