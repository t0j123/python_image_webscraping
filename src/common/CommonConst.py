# coding: utf-8
import _const
import os
import os.path

# プロキシを使用する場合は設定する
# {
#     'http': 'http://proxy.sample.com:8080',
#     'https': 'https://proxy.sample.com:8080'
# }
PROXIES = {}
# connect timeout / read timeout
CONNECT_TIMEOUT = (3.0, 3.0)
SEARCH_URL = {
    'google':'https://www.google.co.jp/search',
    'bing':'https://bing.com/images/search'
}
UA = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
IMG_EXT = ['jpeg', 'jpg', 'png', 'gif', 'bmp', 'tiff']
# WindowsとUnixでセパレータが異なるため、/で統一する
DATA_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '../../../download/image').replace('\\', '/')
INFO_MESSAGE = {
    'common_info_001':'画像URLの収集を開始します',
    'common_info_002':'画像URLの収集が完了しました',
    'common_info_003':'ダウンロードを開始します',
    'common_info_004':'ダウンロードが完了しました'
}
ERROR_MESSAGE = {
    'common_err_001':'画像以外のファイルです',
    'common_err_002':'同じ画像が既に存在します',
    'common_err_003':'タイムアウトしました',
    'common_err_004':'対象外の検索サイトが指定されたため、Googleで検索を行います',
    'common_err_005':'サイトに接続できませんでした',
    'common_err_006':'検索結果が0件でした',
    'common_err_007':'パラメータが不足しています [検索サイト(google or bing)] [検索キーワード] [取得枚数]',
    'common_err_999':'エラーが発生しました'
}