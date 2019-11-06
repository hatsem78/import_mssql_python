import sqlalchemy
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker
import pandas as pd
from lib.class_base import ClaseBase
from model.facebook import FacebookAds
import json
import pandas as pd


connection = ClaseBase()
connection.create_engine()


# ================= Import data FacebookAds =====================

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
                 nrows=300
                 )

df['hourly_start_aggregated_by_advertiser_time_zone'] = df['hourly_stats_aggregated_by_advertiser_time_zone'].str.split(
    '-').apply(lambda x: x[0].strip())
df['hourly_end_aggregated_by_advertiser_time_zone'] = df['hourly_stats_aggregated_by_advertiser_time_zone'].str.split(
    '-').apply(lambda x: x[1].strip())

rows = df.to_json(orient='records')

rows = json.loads(rows)

#Insert data in table facebook_ads
connection.set_bulk_insert(rows, FacebookAds)
