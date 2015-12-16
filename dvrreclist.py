import json
import glob
import sys, os
import unicodecsv

DVR_LOG_DIR = '/home/ckw/workspace/src/tvhreclist/dvr_log/*'
data = []    
OUT_FN = '/home/ckw/workspace/src/tvhreclist/out.csv'


for f in glob.glob(DVR_LOG_DIR):
    with open(f) as fobj:
        f_json = json.loads(fobj.read())
        title = f_json.get('title', {}).get('ger')
        subtitle = f_json.get('subtitle', {}).get('ger')
        fnames = f_json.get('files', [])
        filename = ''
        for fname in fnames:
            filename = fname.get('filename')

        data.append([title, subtitle, filename])

        print "%s - %s - %s" % (title, subtitle, filename)

with open(OUT_FN, 'w') as foutobj:
    w = unicodecsv.writer(foutobj, encoding='utf-8')
    for d in data:
        w.writerow((d[0], d[1], d[2]))


