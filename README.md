# XOPSWordFrequencyList

XOPSのアドオンに出現する単語を頻度順に並べてみました。

頻度リスト: [result.csv](./result.csv)

# 処理の手順

## 生のデータ

3907件のMIFファイルおよび2126件のMSGファイル

## 完全一致するファイルを取り除く

生のデータの中には完全一致する二つ以上のファイルが含まれているので、これらの重複をなくした。

この結果、MIFファイルが3022件、MSGファイルが1445件となった。

使用したツール: [FileMany](http://codepanic.itigo.jp/)

## 文字コードによるフィルタリング

自分のアドオン管理が雑なので、日本のxopsplayerの作品と韓国のxopsplayerの作品が混ざってしまっている。
ここでは日本語テキストを対象にしているので、文字コードがShiftJISもしくはCP932のファイルを抽出した。

この結果、ファイル数は以下のようになった。

|          | MIF  | MSG  |
| :------: | :--: | :--: |
| ShiftJIS | 865  | 570  |
|  CP932   |  12  |  3   |

使用したコード: [pickup_by_encoding.py](./pickup_by_encoding.py)

## テキストの取得

MIFファイルから93841文字、MSGファイルから128053文字のテキストを取得した。

使用したコード: [concat_text.py](./concat_text.py)

## 形態素解析

[Kagome](https://github.com/ikawaha/kagome)を使用して形態素解析を行った。

使用したコード: [morph_analysis.go](./morph_analysis.go)

# 作者のコメント

最近のアドオンは解析対象に含まれていない可能性があります。

データが少ないので頻度の低い単語についてはあまり当てにならないと思います。
上位1000語くらいなら参考になるでしょうか......。

