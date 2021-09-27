import tweepy

def conn_api(): # API 연결
    api_key = ''
    api_key_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(api_key, api_key_secret) # 핸들러 생성 및 개인정보 인증 요청
    auth.set_access_token(access_token, access_token_secret) # 액세스 요청

    return tweepy.API(auth) # twitter API 생성


def get_user_tweets(api, username): # user의 tweet data 크롤링
    result = api.user_timeline(username, tweet_mode='extended') # 140자 이상 문자열까지 크롤링
    return result

def get_search_tweets(api, keyword, page): # 검색어 데이터 크롤링
    result = []
    for i in range(1, page + 1):
        tweets = api.search(keyword)
        for tweet in tweets:
            result.append(tweet) # 크롤링 결과 삽입
    return result