# Chèn lại comment của reviewer vào file Word mới. Usage: add_comments.py <docx> <json>
import json, sys
from docx import Document
doc = Document(sys.argv[1]); items = json.load(open(sys.argv[2], encoding='utf-8'))
def paras(d):
    for p in d.paragraphs: yield p
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs: yield p
ok = 0
for it in items:
    hit = next((p for p in paras(doc) if it['anchor'] in p.text and p.runs), None)
    if not hit: print('KHÔNG THẤY:', it['anchor']); continue
    text = it['text'] + f"\n— {it['author']}, {it['date']} (chuyển từ file cũ; {it['where']})"
    doc.add_comment(hit.runs, text=text, author=it['author'], initials='MH'); ok += 1
doc.save(sys.argv[1]); print(f'{sys.argv[1]}: {ok}/{len(items)} comment')
