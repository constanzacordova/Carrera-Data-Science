import re, sys

feed_document = sys.stdin


for line_in_document in feed_document:
    line_in_document = re.sub(r'^\W+|\W+$', '', line_in_document)
    words_in_line = re.split(r'\W+',line_in_document)
    
    for word in words_in_line:
        print(word.lower() + '\t1')
