import json
import feedparser as fp





DATA = {}
DATA['newspapers'] = {}

with open('NewsPapers.json') as data_file:
    COMPANIES = json.load(data_file)
NEWS_FILE = open('index.html', "w")

#for key in companies:
#    print(key)
#    print(companies[key])
    #
RESULT = fp.parse(COMPANIES['bbc']['rss'])
print('<html>', "\n", file=NEWS_FILE)
print('<head>', "\n", file=NEWS_FILE)
print('<title> Parsed feed from BBC </title>', "\n", file=NEWS_FILE)
print('</head>', "\n", file=NEWS_FILE)
print('<body onload="loadDoc()">', "\n", file=NEWS_FILE)
print("<div>", RESULT.feed['title'], "</div>\n", file=NEWS_FILE)
print('<div id="demo"></div>\n', file=NEWS_FILE)

for i in RESULT.entries:
    print("<p><em>", i['published'], "</em>&nbsp; &nbsp; <strong>", i['title'], ' </strong> \
    <span style="text-decoration: underline;">', i['link'], "</span></p>\n", file=NEWS_FILE)
    print("<blockquote>", "\n", file=NEWS_FILE)
    print(i['summary'], "\n", file=NEWS_FILE)
    print("</p></blockquote>", "\n", file=NEWS_FILE)

JS_TEXT = "<script src='get_version.js'></script>"

print(JS_TEXT, "\n", file=NEWS_FILE)
print('</body>', "\n", file=NEWS_FILE)
print('</html>', "\n", file=NEWS_FILE)

NEWS_FILE.close()
data_file.close()
