import re


def getLinkFromHtml(html):
    # <a href="http://m.amall.com/goods_1381.htm"
    # <a href="http://m.amall.com/overseas_list.htm?floorId=1"
    regLink = r'a.+?href="(http://m.amall.com/.+?.htm(\?.+?)?)"'
    aLink = re.compile(regLink)
    linkList = re.findall(aLink, html)
    return map(lambda x: x[0], linkList)
