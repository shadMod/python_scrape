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
