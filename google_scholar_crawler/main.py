from scholarly import scholarly
import json
from datetime import datetime
import os

print("Start...")

try:
    author = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    
    name = author['name']
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']: v for v in author['publications']}
    
    print(f"Successfully retrieved data for: {name}")
    print(json.dumps(author, indent=2))
    
    os.makedirs('results', exist_ok=True)
    with open('results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False)
        
except Exception as e:
    print(f"Error: {e}")
    raise
