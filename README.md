# 関数作成

引数に計算式のリストを受け取り、各項を垂直に表示する関数を作成

## 1. 実行準備
リモートリポジトリから取得後に Python を対話モードで起動

```
$ git clone https://github.com/Makoto-Araki/boilerplate-arithmetic-formatter.git
$ cd boilerplate-arithmetic-formatter
$ python (対話モードで起動)
```

## 2. 関数実行(1)
引数に計算式のリストのみ指定

```
>>> from arithmetic_arranger import arithmetic_arranger
>>> print(arithmetic_arranger(["45 + 43", "23 - 12"]))
  45      23
+ 43    - 12
----    ----
```

## 3. 関数実行(2)
引数に True も指定して計算結果を表示

```
>>> from arithmetic_arranger import arithmetic_arranger
>>> print(arithmetic_arranger(["45 + 43", "23 - 12"], True))
  45      23
+ 43    - 12
----    ----
  88      11
```