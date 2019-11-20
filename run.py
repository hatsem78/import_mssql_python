import pandas as pd
from lib.class_base import ClaseBase
from model.facebook import FacebookAds
from model.google_analytics import GoogleAnalytics
from model.youtube import Youtube
import json
import pandas as pd


connection = ClaseBase()
connection.create_engine()

print('Import data Youtube')

# create table if not EXISTS
connection.create_table(Youtube)

df = pd.read_csv("csv/Youtube.csv",
                 sep=',', encoding='latin1',
                 usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                          11, 12, 13, 14, 15, 16, 17, 18, 19],
                 # nrows=3000
                 )
df['date'] = df['date'].astype('str').replace('-', '')
# Only important column
df = df.rename(
    columns={
        'date': 'date',
        'channel_name': 'channel_name',
        'channel_views': 'channel_views',
        'channel_comments': 'channel_comments',
        'channel_likes': 'channel_likes',
        'channel_dislikes': 'channel_dislikes',
        'channel_shares': 'channel_shares',
        'channel_subscribersGained': 'channel_subscribers_gained',
        'channel_subscribersLost': 'channel_subscribers_lost',
        'video_id': 'video_id',
        'video_url': 'video_url',
        'video_views': 'video_views',
        'video_comments': 'video_comments',
        'video_likes': 'video_likes',
        'video_dislikes': 'video_dislikes',
        'video_shares': 'video_shares',
        'video_subscribers_gained': 'video_subscribersGained',
        'video_subscribers_lost': 'video_subscribersLost',
        'video_estimated_minutes_watched': 'video_estimatedMinutesWatched'
    }
)

rows = df.to_json(orient='records')

rows = json.loads(rows)

# Insert data in table facebook_ads
connection.set_bulk_insert(rows, Youtube)

print('End Import data Youtube')


# ================= Import data Google Analytics =====================

print('Import data GoogleAnalytics')

# create table if not EXISTS
connection.create_table(GoogleAnalytics)

df = pd.read_csv("csv/GA.csv",
                 sep=',', encoding='latin1',
                 usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                 # nrows=3000
                 )
df['ga:date'] = df['ga:date'].astype('str')

# Only important column
df = df.rename(
    columns={
        'ga:date': 'date',
        'ga:sessions': 'sessions',
        'ga:bounceRate': 'bounce_rate',
        'ga:avgSessionDuration': 'avg_session_duration',
        'ga:pageviews': 'page_views',
        'ga:users': 'users',
        'ga:totalEvents': 'total_events',
        'ga:impressions': 'impressions',
        'ga:adClicks': 'ad_clicks',
        'ga:CPC': 'cpc',
        'ga:CTR': 'ctr',
    }
)


rows = df.to_json(orient='records')

rows = json.loads(rows)

# Insert data in table facebook_ads
connection.set_bulk_insert(rows, GoogleAnalytics)

print('End Import data GoogleAnalytics')


# ================= Import data FacebookAds =====================

print('Import data FacebookAds')

# create table if not EXISTS
connection.create_table(FacebookAds)

# Only important column
columns = ['account_currency', 'account_id', 'account_name',
           'campaign_id', 'campaign_name', 'clicks', 'cpc', 'cpm', 'ctr',
           'date_start', 'date_stop',
           'hourly_stats_aggregated_by_advertiser_time_zone', 'impressions']
df = pd.read_csv("csv/FB_Ads.csv",
                 sep=',', encoding='latin1',
                 usecols=columns,
                 # nrows=300
                 )

df['hourly_start_aggregated_by_advertiser_time_zone'] = df['hourly_stats_aggregated_by_advertiser_time_zone'].str.split(
    '-').apply(lambda x: x[0].strip())
df['hourly_end_aggregated_by_advertiser_time_zone'] = df['hourly_stats_aggregated_by_advertiser_time_zone'].str.split(
    '-').apply(lambda x: x[1].strip())

rows = df.to_json(orient='records')

rows = json.loads(rows)

# Insert data in table facebook_ads
connection.set_bulk_insert(rows, FacebookAds)

print('End Import data FacebookAds')
