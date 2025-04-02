from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

confluence = Confluence(
    url=os.getenv("CONFLUENCE_DOMAIN"),
    username=os.getenv("CONFLUENCE_EMAIL"),
    password=os.getenv("CONFLUENCE_API_TOKEN")
)

space_key = os.getenv("CONFLUENCE_SPACE_KEY")

def get_all_pages(space):
    results = []
    start = 0
    limit = 50
    while True:
        pages = confluence.get_all_pages_from_space(space, start=start, limit=limit)
        if not pages:
            break
        results.extend(pages)
        start += limit
    return results

def extract_content(page_id):
    page = confluence.get_page_by_id(page_id, expand='body.storage')
    soup = BeautifulSoup(page['body']['storage']['value'], 'html.parser')
    return soup.get_text(separator=' ', strip=True)

pages = get_all_pages(space_key)
data = []

for page in pages:
    content = extract_content(page['id'])
    data.append({
        'title': page['title'],
        'content': content,
        'url': f"{confluence.url}/wiki{page['_links']['webui']}"
    })

df = pd.DataFrame(data)
df.to_csv("confluence_pages.csv", index=False)
print("✅ Extracted pages saved to confluence_pages.csv")
