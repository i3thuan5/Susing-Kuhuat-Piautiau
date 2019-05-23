
from http.client import HTTPConnection
import http.client
import json
from sys import argv
from urllib.parse import quote, urlencode
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器


def kiatko(hunsu):
    詞性 = susing(hunsu)
    print(詞性)
    句物件 = 拆文分析器.分詞句物件(hunsu)
    華語 = huanik(句物件)
    print(華語)
    return
    參數 = urlencode({
        'taibun': json.dumps(taiBun),
    })
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    it_conn = http.client.HTTPConnection('susing', port=5000)
    it_conn.request("POST", '/', 參數, headers)

    print('it tmpPath', tmpPath)
    ji_conn = http.client.HTTPConnection(piansik, port=5000)
    ji_conn.request("GET", tmpPath)
    print('ji',  json.loads(ji_conn.getresponse().read()))
    sam_conn = http.client.HTTPConnection(aie, port=5000)
    sam_conn.request("GET", tmpPath)
    sikan = json.loads(sam_conn.getresponse().read())
    print('sam', ''.join(sikan))
    return sikan


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
    華語句物件, _臺語句物件, _分數 = 用戶端.翻譯分析(句物件)
    return 華語句物件


if __name__ == '__main__':
    kiatko(' '.join(argv[1:]))
