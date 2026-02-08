# django_practice

![](https://github.com/shonan-py/django_practice/workflows/test/badge.svg)

## 必要な環境

- Python 3.10以上
- エディタまたはIDE
- Git（Gitの使い方が分からない人は[SourceTree](https://www.sourcetreeapp.com/)がオススメ）

## 開発環境構築方法

このリポジトリを`git clone`してきて、以下を実行。

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip setuptools wheel
$ pip install -r requirements/local.txt
$ python manage.py migrate
$ python manage.py runserver
```

## requirementsファイルの用途

- `requirements.txt`
  - デプロイ用
  - `requirements/production.txt`を参照している
- `requirements/production.txt`
  - 本番環境でしか使わないライブラリはここに書く
- `requirements/local.txt`
  - 開発環境でしか使わないライブラリはここに書く
- `requirements/base.txt`
  - 全環境で共通のライブラリはここに書く
