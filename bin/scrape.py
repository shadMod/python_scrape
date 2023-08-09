"""
Get value by url path

__author__: ShadMod
"""

from bs4 import BeautifulSoup
from requests import get as requests_get

"""
e.g.

clean = ["<p>", "</p>"]
pathurl = []
for url in pathurl:
    scrape_text(url, "div", class_="mw-parser-output", tag="p", clean=clean)
"""


def scrape_text(
        url, content, id_=None, class_=None, name_=None, tag=None, clean=False, content_nr: int = 0,
        ret_type: str = "str",
):
    """
    content => str: tag that conțains the desired values (big container)
                    (e.g. div, span, table, ...)
    id_     => tag id
    class_  => tag class
    name_   => tag name
    tag     => str: tag to filter all html tag (detailed container)
                    (e.g. div, span, table, p, ...)
    clean   => str or list of value to be removed
    """

    # get page html by url and take soup parser
    page = requests_get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # set attrs dict
    attrs = {}
    if id_:
        attrs["id"] = id_
    if class_:
        attrs["class"] = class_
    if name_:
        attrs["name"] = name_

    if content and attrs and tag:
        # find all with params ad take tag decided like string
        soup_container = soup.findAll(content, attrs=attrs)
        soup_tag = str(getattr(soup_container[content_nr], tag))

        if clean:
            text = soup_tag
            for key_tag in clean:
                text = text.replace(key_tag, "")
            return text
        else:
            return soup_tag

    if ret_type == "str":
        return str(soup.findAll(tag, attrs=attrs))
    elif ret_type == "list":
        return list(soup.findAll(tag, attrs=attrs))
    else:
        return str(soup.findAll(tag, attrs=attrs))
