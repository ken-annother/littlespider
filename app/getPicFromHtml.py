import re


def getPicFromHtml(html):
    regPic = r'src="(http://pig.amall.com/upload/.+?.jpg)"'
    imgre = re.compile(regPic)
    imglist = re.findall(imgre, html)
    return imglist
