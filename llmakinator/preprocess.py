def filter_first_k_texts(texts: list[str], k):
    """chatGPTに入れるのに長過ぎるので文字列を制限する"""
    retstr = ""
    for text_sepnewline in texts:
        for text in text_sepnewline.split("。"):
            if len(retstr + text) >= k:
                break
            else:
                retstr += ("\n" + text)
    return retstr