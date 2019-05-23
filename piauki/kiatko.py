
from http.client import HTTPConnection
import json
from sys import argv
from urllib.parse import quote

from nltk.tree import Tree
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.斷詞.國教院斷詞用戶端 import 國教院斷詞用戶端


def kiatko(hunsu):
    詞性 = susing(hunsu)
    print(詞性)
    句物件 = 拆文分析器.分詞句物件(hunsu)
    華語句物件, huagi_hunsu = huanik(句物件)
    print(華語句物件, huagi_hunsu)
    句法 = kuhuat(huagi_hunsu)
    print(句法)
    tsiu = Tree.fromstring(句法)
    tsiu.pretty_print()


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
    return 華語句物件, ' '.join(huagisu)


def kuhuat(華語hunsu):
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


if __name__ == '__main__':
    kiatko(' '.join(argv[1:]))
