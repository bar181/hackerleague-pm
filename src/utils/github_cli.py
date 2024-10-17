import subprocess
import json
from ..config import settings

def run_github_cli_command(command: list[str]) -> dict:
    result = subprocess.run(
        [settings.GITHUB_CLI_PATH] + command,
        capture_output=True,
        text=True,
        env={"GITHUB_TOKEN": settings.GITHUB_TOKEN}
    )
    if result.returncode != 0:
        raise Exception(f"GitHub CLI command failed: {result.stderr}")
    return json.loads(result.stdout)

def create_github_project(name: str, description: str) -> dict:
    return run_github_cli_command(["project", "create", name, "--description", description, "--format", "json"])

def create_github_issue(project_id: str, title: str, body: str) -> dict:
    return run_github_cli_command(["issue", "create", "--project", project_id, "--title", title, "--body", body, "--format", "json"])

# Implement other GitHub CLI wrapper functions