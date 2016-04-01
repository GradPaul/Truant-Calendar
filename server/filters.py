import re


def content_chopper(s, offset, limit):
    return re.sub(r'<.*?>|&.*?;', '', s)[offset:offset+limit]


def completeProtocal(url):
    if url[:4] == "http":
        return url
    else:
        return "http://" + url
