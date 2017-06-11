import urllib.request

def read_text():
    file = open("/Users/alantran/Documents/Studying/summer2017/foundation_with_python/text.txt")
    check_profanity(file.read())
    file.close()

def check_profanity(text):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    print(connection.read())
    
read_text()
