import requests

# response=requests.get('http://postman-echo.com/get')
# print(response.status_code)
# print(response.text)
# json_dict=response.json()
# print(json_dict['headers']['x-forwarded-port'])
# print(json_dict['headers']['x-forwarded-proto'])

response=requests.get("https://quotes.toscrape.com/")
#print(response.status_code)
html=response.text
#print(html)
#print(html.split('\n'))

# with open("quotes.txt","w") as fp:
#     for each_line in html.split('\n'):
#         if '<span class="text" itemprop="text">' in each_line:
#             each_line=each_line.replace('<span class="text" itemprop="text">“','')
#             each_line=each_line.replace('”</span>','')
#             each_line=each_line.strip()
#             print(each_line)
#             fp.write(each_line+"\n")

with open("authors.txt","w") as fp:
    for each_line in html.split('\n'):
         if '<small class="author" itemprop="author">' in each_line:
             each_line=each_line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
             each_line=each_line.strip()
             fp.write(each_line+"\n")