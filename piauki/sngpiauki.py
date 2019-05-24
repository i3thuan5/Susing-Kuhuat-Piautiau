
from sys import stdin, stdout

from kiatko import susing, huanik, kuhuat, uann_tso_taigi_kuhuat


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from csv import DictWriter


def main():
    sia = DictWriter(
        stdout,
        fieldnames=['分詞', '詞性', '句法']
    )
    sia.writeheader()
    for hunsu in stdin:
        if hunsu.strip():
            詞性, tshiu = sng(hunsu.strip())
            sia.writerow({
                '分詞': hunsu,
                '詞性': 詞性,
                '句法': tshiu,
            })


def sng(hunsu):
    詞性 = susing(hunsu)

    句物件 = 拆文分析器.分詞句物件(hunsu)
    _華語句物件, 華語翻譯詞句物件 = huanik(句物件)

    句法 = kuhuat(華語翻譯詞句物件)

    tshiu = uann_tso_taigi_kuhuat(句物件, 句法)
    return 詞性, tshiu


if __name__ == '__main__':
    main()
