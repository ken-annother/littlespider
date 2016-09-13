# coding=utf-8
from getHtml import getHtml
from getLinkFromHtml import getLinkFromHtml
import db


def start(starturl):
    html = getHtml(starturl)
    links = getLinkFromHtml(html)
    # doInsetLinks(links)
    # queryLinks()


def doInsetLinks(links):
    modifyLinks = map(lambda x: (None, x, False), links)
    db.manage.insertLinks(modifyLinks)


def queryLinks():
    links = db.manage.queryLinks()
    # print links
    map(lambda x: start(x[1]), links)
