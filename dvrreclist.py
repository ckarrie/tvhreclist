import json
import glob
import sys, os
import unicodecsv

DVR_LOG_DIR = '/home/ckw/workspace/src/tvhreclist/dvr_log/*'
data = []    
OUT_FN = '/home/ckw/workspace/src/tvhreclist/out.csv'
LANG_CODE = 'ger'


for f in glob.glob(DVR_LOG_DIR):
    with open(f) as fobj:
        f_json = json.loads(fobj.read())
        title = f_json.get('title', {}).get(LANG_CODE)
        subtitle = f_json.get('subtitle', {}).get(LANG_CODE)
        fnames = f_json.get('files', [])
        filename = ''
        for fname in fnames:
            _fname = fname.get('filename')
            if _fname:
                filename = _fname

        data.append([f, title, subtitle, filename])

        print "%s = %s - %s - %s" % (f, title, subtitle, filename)
        if len(fnames) > 1:
            print " --> Duplicate Recording Files", fnames

with open(OUT_FN, 'w') as foutobj:
    w = unicodecsv.writer(foutobj, encoding='utf-8')
    # add header col
    w.writerow(['Rec Log File', 'Title', 'Subtitle', 'Filename'])
    for d in data:
        w.writerow((d[0], d[1], d[2], d[3]))


