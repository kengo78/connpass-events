# from github import Github

import datetime
# import pytz
# import time
import requests
import pandas as pd

URL = 'https://connpass.com/api/v1/event/'
def get_event_url(keyword, count=30):
    """
    イベント情報を取得する

    Parameters
    ----------
    keyword : string
        検索するキーワード
    count : int, default 10
        取得するイベント数
    """

    params = {
        'keyword': keyword,
        'count': count,
    }
    response = requests.get(URL, params=params)
    time.sleep(1)
    results = response.json()
    return results
if __name__ == '__main__':
    keyword = "機械学習"
    result = get_event_url(keyword)
    df = pd.json_normalize(result['events'])
    df = df[["title", "catch", "event_url", "hash_tag", "series.title","started_at"]]
    # now_info = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d')
    df.to_csv("data.csv",index=False)