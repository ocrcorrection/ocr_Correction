from pypinyin import pinyin, lazy_pinyin, Style

def to_pinyin(var_str):
    if isinstance(var_str, str):
        if var_str == "None":
            return ""
        else:
            print(lazy_pinyin(var_str, style=Style.TONE2))
            return pinyin(var_str)
    else:
        return '类型不对'
"""
        :param errors: 指定如何处理没有拼音的字符。详见 :ref:`handle_no_pinyin`

                       * ``'default'``: 保留原始字符
                       * ``'ignore'``: 忽略该字符
                       * ``'replace'``: 替换为去掉 ``\\u`` 的 unicode 编码字符串
                         (``'\\u90aa'`` => ``'90aa'``)
                       * callable 对象: 回调函数之类的可调用对象。
"""
def to_pinyin2(str_list):
    pinyin_list = []
    for c_list in str_list:
        sub_pinyin = []
        for c in c_list:
            # print(lazy_pinyin(c, style=Style.TONE8))
            str_pinyin = str(lazy_pinyin(c, style=Style.TONE2, errors='replace'))[2:-2]
            sub_pinyin.append(str_pinyin)
        pinyin_list.append(sub_pinyin)
    print(pinyin_list)
    return pinyin_list


def to_pinyinStr(var_str):
    if isinstance(var_str, str):
        if var_str == "None":
            return ""
        else:
            print(lazy_pinyin(var_str, style=Style.TONE2))
            return lazy_pinyin(var_str, style=Style.TONE2)
            # return pinyin(var_str)
    else:
        return '类型不对'

if __name__ == '__main__':
    var_str = "放假去爬山"
    chars = {'+', '%', '也', '(', '"'}
    input_text = [['您', '也', '做', '跟', '他', '们', '一', '样', '的', '行', '业', '，'],['这', '公', '司', '的', '倒', '产', '有', '没', '有', '影', '响', '到', '老', '爸', '的', '工', '作', '？']]
    # to_pinyin2(input_text)
    # to_pinyin2(list(chars))
    # to_pinyin(var_str)
    to_pinyinStr(var_str)