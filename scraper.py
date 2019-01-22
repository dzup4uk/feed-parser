import json
import feedparser as fp





data = {}
data['newspapers'] = {}

with open('NewsPapers.json') as data_file:
    companies = json.load(data_file)
news_file = open('index.html', "w")

#for key in companies:
#    print(key)
#    print(companies[key])
    #
result = fp.parse(companies['bbc']['rss'])
print('<html>', "\n", file=news_file)
print('<head>', "\n", file=news_file)
print('<title> Parsed feed from BBC </title>', "\n", file=news_file)
print('</head>', "\n", file=news_file)
print('<body onload="loadDoc()">', "\n", file=news_file)
print("<div>", result.feed['title'], "</div>\n", file=news_file)
print('<div id="demo"></div>\n', file=news_file)

for i in result.entries:
    print("<p><em>", i['published'], "</em>&nbsp; &nbsp; <strong>", i['title'], ' </strong> <span style="text-decoration: underline;">', i['link'],  "</span></p>\n", file=news_file)
    print("<blockquote>", "\n", file=news_file)
    print(i['summary'], "\n", file=news_file)
    print("</p></blockquote>", "\n", file=news_file)

js_text = "<script src='get_version.js'></script>"

print(js_text, "\n", file=news_file)
print('</body>', "\n", file=news_file)
print('</html>', "\n", file=news_file)

news_file.close()
data_file.close()
