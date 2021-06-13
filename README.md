# Flight Checklists
## Alfred Workflow
定常的な作業の確認のためのチェックリスト

## Menu
* continue: 前回のchecklistデータを読み込み、続きから再開する。
* checklists: checklistsを読み込み、初めから行う。
* make: checklistを作成する。`~/Documents/checklists`上でvimが起動する。
* clean: 実行途中のchecklistデータを削除する。

## checklistの記法
makeコマンドでは以下のテキストファイルを作成してください。
`~/Documents/checklists`上の`.txt`ファイルがchecklistsコマンドで読み込まれます。
パスが存在しない場合は、自動で作成されます。

example.txt
```
* 必須のチェック要素。
- 任意のチェック要素。
```

* 1文字目の記号は`*`と`-`の2種類です。
* 2文字目に必ずスペースを入れてください。
* 3文字目以降がチェック要素のタイトルとなります。

