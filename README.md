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
cat 結案/ithuan-igua.txt | time docker-compose run -T piauki python sngpiauki.py > ithuan-igua.csv
cat 結案/例句150.txt | time docker-compose run -T piauki python sngpiauki
.py > leku150.csv
cat 結案/散文5 | time docker-compose run -T piauki python sngpiauki.py > suannbun.csv
cat 結案/kautian-leku.txt | head -n 1000 | time docker-compose run -T piauki python sngpiauki.py > kautian-leku.csv
cat 結案/kautian.txt | time docker-compose run -T piauki python sngpiauki.py > kautian.csv
cat 結案/kautian.txt | time docker-compose run -T piauki python sngpiantiau.py > kautian2.csv
```
