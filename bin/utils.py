from urllib.parse import unquote


def unquote_try(value: str):
    try:
        return unquote(value, errors='strict')
    except UnicodeDecodeError:
        return unquote(value, encoding='latin-1')


def get_url_href(link: str):
    # get first link href in <a>
    for text in link.split(" "):
        if "href" in text:
            return text.replace("href=", "").replace("'", "").replace('"', "")


def clean_text(text: str):
    clean_txt = ["[", "]", "'"]
    for char in clean_txt:
        text = text.replace(char, "")
    return text


def clean_a_href(text: str, capo: bool = False):
    """
    draft method to clean html a href in text
    """
    # first clean
    text = text.replace("</a>", "")

    # init txt_clean
    txt_clean = []
    # split href and clean
    for x in text.split("<"):
        for y in x.split(">"):
            if 'href' not in y:
                txt_clean.append(y)

    if capo:
        # return clean text capitalize
        return "".join(txt_clean).capitalize()
    # return clean text
    return "".join(txt_clean)


def get_html_text(value: str, tag: str, clean_a: bool = False):
    """
    Support tag:
        - `<a href=""></a>`
        - `<b></b>`

    :result:    res
    :rtype:     str
    """
    for text in value.split("><"):
        if tag == "href" and tag in text:
            res = clean_a_href(text).replace("/a", "") if clean_a else text
            return res
        if tag == "<b>" and tag in text:
            pass

    return ""
