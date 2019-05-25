
from csv import DictWriter
from sys import stdin, stdout, stderr

from kiatko import susing, huanik, kuhuat, uann_tso_taigi_kuhuat, pian_jitshuan


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成.閩南語音韻.變調判斷 import 變調判斷
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def main():
    sia = DictWriter(
        stdout,
        fieldnames=['分詞', '變調']
    )
    sia.writeheader()
    for hunsu in stdin:
        if hunsu.strip():
            try:
                變調名 = sng(hunsu.strip())
            except RuntimeError as tshogoo:
                print(tshogoo, file=stderr)
            except IndexError as tshogoo:
                print(tshogoo, hunsu.strip(), file=stderr)
            sia.writerow({
                '分詞': hunsu,
                '變調': 變調名,
            })


def sng(hunsu):
    句物件 = 拆文分析器.分詞句物件(hunsu)

    變調 = 變調判斷.判斷(句物件.轉音(臺灣閩南語羅馬字拼音, '音值'))
    變調名 = pian_jitshuan(變調)
    return 變調名


if __name__ == '__main__':
    main()
