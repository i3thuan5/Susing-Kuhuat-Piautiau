# Susing-Kuhuat-Piautiau

## Kuhuat
先去[句法專案](https://github.com/i3thuan5/Stanford_Hua5gi2_NLP)build image
```
docker-compose build
```

## 才閣轉來執行
```
docker-compose up -d --build
docker-compose run --rm piauki python kiatko.py 逐-家｜tak8-ke1 做-伙｜tso3-hue2 來｜lai5 𨑨-迌｜tshit4-tho5 ！｜!
cat 結案/ithuan.txt | time docker-compose run -T piauki python sngpiauki.py > ithuan.csv
```
