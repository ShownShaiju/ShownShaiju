import requests
import json
from datetime import datetime

README_PATH = "README.md"  
BLOG_HOST = "blog.shownshaiju.me"

# Hashnode GraphQL API
API_URL = "https://gql.hashnode.com"

QUERY = """
{
  publication(host: "blog.shownshaiju.me") {
    posts(first: 6) {
      edges {
        node {
          title
          url
          publishedAt
          coverImage {
            url
          }
        }
      }
    }
  }
}
"""

response = requests.post(API_URL, json={"query": QUERY})
data = response.json()
posts = data["data"]["publication"]["posts"]["edges"]

#  markdown formatting
lines = []

for post in posts:
    node = post["node"]
    title = node["title"]
    url = node["url"]
    date_raw = node["publishedAt"]          
    cover = node.get("coverImage")

    date = datetime.strptime(date_raw, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%b %d, %Y")

    if cover and cover.get("url"):
        lines.append(f"[![{title}]({cover['url']})]({url})")
        lines.append(f"**[{title}]({url})** — {date}")
    else:
        lines.append(f"**[{title}]({url})** — {date}")
    
    lines.append("")  

new_content = "\n".join(lines)

with open(README_PATH, "r") as f:
    readme = f.read()

START_MARKER = "<!-- HASHNODE_POSTS:START -->"
END_MARKER = "<!-- HASHNODE_POSTS:END -->"

start_index = readme.index(START_MARKER) + len(START_MARKER)
end_index = readme.index(END_MARKER)

new_readme = (
    readme[:start_index] +
    "\n" + new_content + "\n" +
    readme[end_index:]
)

with open(README_PATH, "w") as f:
    f.write(new_readme)

print("README updated successfully!")
