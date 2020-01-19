# django_practice

![](https://github.com/shonan-py/django_practice/workflows/test/badge.svg)

## 必要な環境

- Python 3.7または3.8
- エディタまたはIDE
- Git（Gitの使い方が分からない人[SourceTree](https://www.sourcetreeapp.com/)がオススメ）


## 開発環境構築方法

このリポジトリを`git clone`してきて、以下を実行。

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip setuptools wheel
$ pip install -r requirements/local.txt
$ python manage.py migrate
```
