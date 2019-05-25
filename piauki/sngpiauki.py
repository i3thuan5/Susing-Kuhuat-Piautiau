
from csv import DictWriter
from sys import stdin, stdout

from kiatko import susing, huanik, kuhuat, uann_tso_taigi_kuhuat, pian_jitshuan


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成.閩南語音韻.變調判斷 import 變調判斷
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def main():
    sia = DictWriter(
        stdout,
        fieldnames=['分詞', '詞性', '句法', '變調']
    )
    sia.writeheader()
    for hunsu in stdin:
        if hunsu.strip():
            詞性, tshiu, 變調名 = sng(hunsu.strip())
            sia.writerow({
                '分詞': hunsu,
                '詞性': 詞性,
                '句法': tshiu,
                '變調': 變調名,
            })


def sng(hunsu):
    詞性 = susing(hunsu)

    句物件 = 拆文分析器.分詞句物件(hunsu)
    _華語句物件, 華語翻譯詞句物件 = huanik(句物件)

    句法 = kuhuat(華語翻譯詞句物件)

    tshiu = uann_tso_taigi_kuhuat(句物件, 句法)

    變調 = 變調判斷.判斷(句物件.轉音(臺灣閩南語羅馬字拼音, '音值'))
    變調名 = pian_jitshuan(變調)
    return 詞性, tshiu, 變調名


if __name__ == '__main__':
    main()
