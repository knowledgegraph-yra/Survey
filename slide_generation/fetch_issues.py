import requests
import re
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

MD_IMAGE_PATTERN = r'!\[(?P<description>.+)\]\((?P<url>.+)\)'


def fetch_issues() -> list[dict]:
    # I don't implement pagenation here
    # Implement pagenation if you have more than 100 issues per label
    url = f"https://api.github.com/repos/{REPO}/issues?state=open&labels={LABEL}&per_page=100"
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
    print(f"Found {len(issues)} issues")
    markdown_contents: list[str] = []
    for issue in issues:
        md = convert_issue_to_markdown(issue)
        if md is None:
            issue_id = issue['id']
            print(f"Failed to convert issue to markdown. Issue ID: {issue_id}")
            continue
        # detect images
        image_mds: list[str] = []
        for image_match_obj in re.finditer(MD_IMAGE_PATTERN, md):
            image_mds.append(image_match_obj.group(0))
        # remove images from the original page
        md = re.sub(MD_IMAGE_PATTERN, "", md)

        markdown_contents.append(md)
        markdown_contents.extend(image_mds)
    # Geerate the final output file
    with open(OUTPUT_PATH, "w") as f:
        f.write(MARP_PREFIX)
        for md in markdown_contents:
            f.write(md)
            f.write("\n---\n")


if __name__ == "__main__":
    main()
