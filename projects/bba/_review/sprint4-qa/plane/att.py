import json,os,sys,urllib.request,urllib.error
K=open(os.environ['KF']).read().strip().splitlines()[-1].split(',')[-1].strip()
B='https://plane.bba.dotb.vn/api/v1/workspaces/bba/projects/b3a74ce6-a01c-4d94-8287-7d03dd13e84e'
I=sys.argv[1]; out=sys.argv[2]; os.makedirs(out,exist_ok=True)
class NoRedir(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*a,**k): return None
def req(u,redir=True):
    r=urllib.request.Request(u,headers={'X-API-Key':K})
    op=urllib.request.build_opener() if redir else urllib.request.build_opener(NoRedir)
    return op.open(r,timeout=60)
try:
    a=json.load(req(f'{B}/issues/{I}/issue-attachments/'))
except urllib.error.HTTPError as e:
    print('list err',e.code,e.read()[:300]); sys.exit()
a=a.get('results',a) if isinstance(a,dict) else a
for x in a:
    meta={k:x.get(k) for k in ('id','attributes','asset','asset_url','is_uploaded')}
    print(json.dumps(meta,ensure_ascii=False)[:300])
    name=(x.get('attributes') or {}).get('name') or x['id']
    for u in [f"{B}/issues/{I}/issue-attachments/{x['id']}/"]:
        try:
            r=req(u,redir=False); data=r.read(); print(' got',len(data), r.headers.get('content-type'))
            if r.headers.get('content-type','').startswith('application/json'):
                print(' json',data[:300])
            else: open(f'{out}/{name}','wb').write(data)
        except urllib.error.HTTPError as e:
            loc=e.headers.get('Location'); print(' http',e.code,'redirect' if loc else '')
            if loc:
                d=urllib.request.urlopen(loc,timeout=120).read(); open(f'{out}/{name}','wb').write(d); print(' saved',name,len(d))
