'''
This is a script for converting subtitles with a timeline to no-timeline.
'''

import re, sys,os

file_path = os.path.abspath(sys.argv[1])

f = open(file_path, encoding='utf-8')
subtitle = f.read().replace('\n', ' ')
f.close()
p = re.compile(r'\d+:\d{2}:\d{2},\d+\s-->\s\d{2}:\d{2}:\d{2},\d+')
newsubtitle = p.sub(' ', subtitle)
p2 = re.compile(r'\d+\s+')
newsubtitle = p2.sub('', newsubtitle)
file_dest = file_path.replace('.srt', '.txt')
with open(file_dest, 'w', encoding='utf-8') as f:
    f.write(newsubtitle)
