import pandas as pd
import requests, json, time
from datetime import datetime, timedelta

def coin_history(coin_to_get: str, change: str, start_date: str) -> pd.core.frame.DataFrame:
    """ Function that automatically gets informations from coingecko coming from a start date until today.
    coin_to_get = "bitcoin", ...
    change = "eur", "usd", ...
    start = "yyyy-mm-dd"
    """
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.today()
    list_of_days = [start_date + timedelta(days=x) for x in range((end_date - start_date).days)]
    base_url = "https://api.coingecko.com/api/v3/coins/"
    
    for day in list_of_days:
        # URL to request
        url_to_get = base_url + coin_to_get + "/history?date=" + day.strftime("%d-%m-%Y") + "&localization=fr"
        try:
            # Coin infos to get
            coin = requests.get(url_to_get).json()
            price = coin['market_data']['current_price'][change]
        except:
            # if there is an error for a specific day, the day will be added in a list
            print(f"Error: {day}")
        else:
            id_coin = coin['id']
            price = coin['market_data']['current_price'][change]
            market_cap = coin['market_data']['market_cap'][change]
            total_volume = coin['market_data']['total_volume']['usd']
            twitter_followers = coin['community_data']['twitter_followers']
            reddit_average_posts_48h = coin['community_data']['reddit_average_posts_48h']
            reddit_average_comments_48h = coin['community_data']['reddit_average_comments_48h']
            reddit_subscribers = coin['community_data']['reddit_subscribers']
            reddit_accounts_active_48h = coin['community_data']['reddit_accounts_active_48h']
            # Data that will be added into a dataframe
            line_to_append = [[day, id_coin, price, market_cap, total_volume, twitter_followers, reddit_average_posts_48h, reddit_average_comments_48h, reddit_subscribers, reddit_accounts_active_48h]]

            if day == list_of_days[0]:
                coin_informations = pd.DataFrame(line_to_append, columns=['date', 'id_coin','price', 'market_cap', 'total_volume', 'twitter_followers', 'reddit_average_posts_48h', 'reddit_average_comments_48h', 'reddit_subscribers', 'reddit_accounts_active_48h'])
            else:
                coin_informations = coin_informations.append(pd.DataFrame(line_to_append, columns=['date', 'id_coin','price', 'market_cap', 'total_volume', 'twitter_followers', 'reddit_average_posts_48h', 'reddit_average_comments_48h', 'reddit_subscribers', 'reddit_accounts_active_48h']), ignore_index=True)
            # 50 calls/minute for the CoinGecko Crypto Data API Free plan
            time.sleep(1.2)

    return coin_informations


def coin_history_with_start_and_end_date(coin_to_get: str, change: str, start_date:str, end_date:str) -> pd.core.frame.DataFrame:
    """ Function that automatically gets informations from coingecko coming from a start date until a end date.
    coin_to_get = "bitcoin", ...
    change = "eur", "usd", ...
    start_date = "yyyy-mm-dd"
    end_date = "yyyy-mm-dd"
    """
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    list_of_days = [start_date + timedelta(days=x) for x in range(0, (end_date - start_date).days + 1)]
    base_url = "https://api.coingecko.com/api/v3/coins/"
    
    for day in list_of_days:
        # URL to request
        url_to_get = base_url + coin_to_get + "/history?date=" + day.strftime("%d-%m-%Y") + "&localization=fr"
        try:
            # Coin infos to get
            coin = requests.get(url_to_get).json()
            price = coin['market_data']['current_price'][change]
        except:
            # if there is an error for a specific day, the day will be added in a list
            print(f"Error: {day}")
        else:
            id_coin = coin['id']
            price = coin['market_data']['current_price'][change]
            market_cap = coin['market_data']['market_cap'][change]
            total_volume = coin['market_data']['total_volume']['usd']
            twitter_followers = coin['community_data']['twitter_followers']
            reddit_average_posts_48h = coin['community_data']['reddit_average_posts_48h']
            reddit_average_comments_48h = coin['community_data']['reddit_average_comments_48h']
            reddit_subscribers = coin['community_data']['reddit_subscribers']
            reddit_accounts_active_48h = coin['community_data']['reddit_accounts_active_48h']
            # Data that will be added into a dataframe
            line_to_append = [[day, id_coin, price, market_cap, total_volume, twitter_followers, reddit_average_posts_48h, reddit_average_comments_48h, reddit_subscribers, reddit_accounts_active_48h]]

            if day == list_of_days[0]:
                coin_informations = pd.DataFrame(line_to_append, columns=['date', 'id_coin','price', 'market_cap', 'total_volume', 'twitter_followers', 'reddit_average_posts_48h', 'reddit_average_comments_48h', 'reddit_subscribers', 'reddit_accounts_active_48h'])
            else:
                coin_informations = coin_informations.append(pd.DataFrame(line_to_append, columns=['date', 'id_coin','price', 'market_cap', 'total_volume', 'twitter_followers', 'reddit_average_posts_48h', 'reddit_average_comments_48h', 'reddit_subscribers', 'reddit_accounts_active_48h']), ignore_index=True)
            # 50 calls/minute for the CoinGecko Crypto Data API Free plan
            time.sleep(1.2)

    return coin_informations

# Examples
bitcoin_history_2022 = coin_history("bitcoin", "usd", "2022-01-01")
bitcoin_history_2015 = coin_history_with_start_and_end_date("bitcoin", "usd", "2015-01-26", "2015-01-30")
