import requests
import os
import json

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
OUTPUT_PATH = os.environ["OUTPUT_PATH"]
LABEL = os.environ["ISSUE_LABEL"]

MARP_PREFIX = """---
marp: true
size: 4:3
paginate: true
style: |
  section {
    font-size: 12px; /* Adjust font size to fit content */
    margin: 0;
    padding: 20px 40px;
  }
  h2 {
    margin: 0;
    padding: 0;
  }
  p {
    margin: 0;
    padding: 0;
  }
---
"""

MARKDOWN_TEMPLATE = """
# {title}

{body}
"""


def fetch_issues() -> list[dict]:
    url = f"https://api.github.com/repos/{REPO}/issues?state=open&labels={LABEL}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(url, headers=headers)
    issues = response.json()
    assert isinstance(issues, list)
    return issues


def convert_issue_to_markdown(issue: dict) -> str | None:
    if "title" not in issue:
        return None
    if "body" not in issue:
        return None
    return MARKDOWN_TEMPLATE.format(title=issue["title"], body=issue["body"])


def main():
    issues = fetch_issues()
    markdown_contents: list[str] = []
    for issue in issues:
        md = convert_issue_to_markdown(issue)
        if md is not None:
            markdown_contents.append(md)
    # Geerate the final output file
    with open(OUTPUT_PATH, "w") as f:
        f.write(MARP_PREFIX)
        for md in markdown_contents:
            f.write(md)
            f.write("\n---\n")


if __name__ == "__main__":
    main()
