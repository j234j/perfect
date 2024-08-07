import pickle

def get_vocab(corpus1, corpus2):
    """
    从两个语料库中提取唯一的词汇表。

    参数:
    corpus1 - 第一个语料库
    corpus2 - 第二个语料库

    返回:
    一个包含所有唯一词汇的集合
    """
    word_vocab = set()
    for corpus in [corpus1, corpus2]:
        for i in range(len(corpus)):
            word_vocab.update(corpus[i][1][0])
            word_vocab.update(corpus[i][1][1])
            word_vocab.update(corpus[i][2][0])
            word_vocab.update(corpus[i][3])
    print(len(word_vocab))
    return word_vocab


def load_pickle(filename):
    """
    从指定的文件路径加载数据。

    参数:
    filename - 待加载的文件路径

    返回:
    被加载的数据对象
    """
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


def vocab_processing(filepath1, filepath2, save_path):
    """
    处理词汇表,并将其保存到指定的文件中。

    参数:
    filepath1 - 第一个语料库文件路径
    filepath2 - 第二个语料库文件路径
    save_path - 保存词汇表的文件路径
    """
    with open(filepath1, 'r') as f:
        total_data1 = set(eval(f.read()))
    with open(filepath2, 'r') as f:
        total_data2 = eval(f.read())

    word_set = get_vocab(total_data2, total_data2)

    excluded_words = total_data1.intersection(word_set)
    word_set = word_set - excluded_words

    print(len(total_data1))
    print(len(word_set))

    with open(save_path, 'w') as f:
        f.write(str(word_set))


if __name__ == "__main__":
    """
    程序入口点,定义了几个文件路径并调用 vocab_processing() 函数来处理 SQL 语言的词汇表。
    """
    python_hnn = './data/python_hnn_data_teacher.txt'
    python_staqc = './data/staqc/python_staqc_data.txt'
    python_word_dict = './data/word_dict/python_word_vocab_dict.txt'

    sql_hnn = './data/sql_hnn_data_teacher.txt'
    sql_staqc = './data/staqc/sql_staqc_data.txt'
    sql_word_dict = './data/word_dict/sql_word_vocab_dict.txt'

    new_sql_staqc = './ulabel_data/staqc/sql_staqc_unlabled_data.txt'
    new_sql_large = './ulabel_data/large_corpus/multiple/sql_large_multiple_unlable.txt'
    large_word_dict_sql = './ulabel_data/sql_word_dict.txt'

    final_vocab_processing(sql_word_dict, new_sql_large, large_word_dict_sql)