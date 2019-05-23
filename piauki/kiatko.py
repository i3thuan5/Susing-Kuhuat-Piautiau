
from http.client import HTTPConnection
import json
from sys import argv
from urllib.parse import quote

from nltk.tree import Tree
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器


def kiatko(hunsu):
    詞性 = susing(hunsu)
    print(詞性)
    句物件 = 拆文分析器.分詞句物件(hunsu)
    華語句物件, 華語翻譯詞句物件 = huanik(句物件)
    print(華語句物件, 華語翻譯詞句物件)
    句法 = kuhuat(華語翻譯詞句物件)
    print(句法)
    tshiu = uann_tso_taigi_kuhuat(句物件, 句法)
    tshiu.pretty_print()


def susing(hunsu):
    conn = HTTPConnection('susing', port=5000)
    conn.request(
        "GET",
        '/{}'.format(
            quote(hunsu),
        )
    )
    r1 = conn.getresponse()
    if r1.status != 200:
        print(r1.status, r1.reason)
        raise RuntimeError()
    詞性結果 = []
    for _分詞, 詞性 in json.loads(r1.read().decode('utf-8')):
        詞性結果.append(詞性)
    return 詞性結果


def huanik(句物件):
    用戶端 = 摩西用戶端(
        編碼器=語句編碼器,
        位址='huanik', 埠='8080',
    )
    華語句物件, 臺語句物件, _分數 = 用戶端.翻譯分析(句物件)
    huagisu = []
    for 詞物件 in 臺語句物件.網出詞物件():
        huagisu.append(詞物件.翻譯目標詞陣列[-1].看型())
    return 華語句物件, 拆文分析器.建立句物件(' '.join(huagisu))


def kuhuat(華語句物件):
    kuhuat_tree = _kuhuat_mng(華語句物件.看型('', ' '))
    while True:
        tsiu = Tree.fromstring(kuhuat_tree)
        if len(tsiu.leaves()) == len(華語句物件.網出詞物件()):
            return kuhuat_tree
        華語句物件, kuhuat_tree = _kuhuat_uannsine(華語句物件, kuhuat_tree)


def _kuhuat_uannsine(華語句物件, kuhuat_tree):
    tsiu = Tree.fromstring(kuhuat_tree)
    huaniksu = []
    斷詞 = tsiu.leaves()
    斷詞所在 = 0
    liaptsik = ''
    for su in 華語句物件.網出詞物件():
        while True:
            liaptsik += 斷詞[斷詞所在]
            if len(liaptsik) == len(su.看型()):
                huaniksu.append(斷詞[斷詞所在])
                斷詞所在 += 1
                liaptsik = ''
                break
            斷詞所在 += 1
    return 拆文分析器.建立句物件(' '.join(huaniksu)), _kuhuat_mng(' '.join(huaniksu))


def _kuhuat_mng(華語hunsu):
    conn = HTTPConnection('kuhuat', port=5000)
    conn.request(
        "GET",
        '/{}'.format(
            quote(華語hunsu),
        )
    )
    r1 = conn.getresponse()
    if r1.status != 200:
        print(r1.status, r1.reason)
        raise RuntimeError()
    return json.loads(r1.read().decode('utf-8'))


def uann_tso_taigi_kuhuat(句物件, 句法):
    su = []
    for 詞物件 in 句物件.網出詞物件():
        su.append(詞物件.看分詞())
    tshiu = Tree.fromstring(句法)
    return uann_tshiu(su[::-1], tshiu)


def uann_tshiu(su, tshiu):
    kiann = []
    for child in tshiu:
        if isinstance(child, Tree):
            kiann.append(uann_tshiu(su, child))
        else:
            kiann.append(su.pop())
    return Tree(tshiu.label(), kiann)


if __name__ == '__main__':
    kiatko(' '.join(argv[1:]))
