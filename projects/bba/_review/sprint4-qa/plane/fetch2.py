import json,os,sys,time,re,html,urllib.request,urllib.error
D=sys.argv[1]
K=open(os.environ['KF']).read().strip().splitlines()[-1].split(',')[-1].strip()
B='https://plane.bba.dotb.vn/api/v1/workspaces/bba/projects/b3a74ce6-a01c-4d94-8287-7d03dd13e84e'
def get(u):
    for i in range(6):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'X-API-Key':K}),timeout=60))
        except urllib.error.HTTPError as e:
            if e.code==429: time.sleep(5*(i+1)); continue
            raise
def txt(h):
    h=re.sub(r'<(br|/p|/li|/h\d|/tr)[^>]*>','\n',h or ''); h=re.sub(r'<li[^>]*>','• ',h); h=re.sub(r'<td[^>]*>',' | ',h)
    return re.sub(r'\n{3,}','\n\n',html.unescape(re.sub(r'<[^>]+>','',h))).strip()
res=json.load(open(f'{D}/done.json'))
for r in res:
    i=get(f"{B}/issues/{r['id']}/"); r['desc']=txt(i.get('description_html'))
    c=get(f"{B}/issues/{r['id']}/comments/"); c=c.get('results',c) if isinstance(c,dict) else c
    r['comments']=[txt(x.get('comment_html')) for x in c]
    time.sleep(0.3)
json.dump(res,open(f'{D}/done.json','w'),ensure_ascii=False,indent=1)
with open(f'{D}/done.md','w') as f:
    for r in res:
        f.write(f"\n## BBA-{r['seq']} {r['name']}\n\n### Description\n{r['desc']}\n")
        for k,c in enumerate(r['comments'],1): f.write(f"\n### Comment {k}\n{c}\n")
print({r['seq']:(len(r['desc']),sum(len(c) for c in r['comments'])) for r in res})
