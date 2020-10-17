#from googleapiclient.discovery import build
import json
# importing instagram  libraries
from bs4 import BeautifulSoup
from . import config
import requests
import humanfriendly
import google

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


# to search

# facebook page stats
def get_facebook_stats(page_id, url):
    community_page = requests.get(url)
    document = BeautifulSoup(community_page.text, 'html.parser')
    page_likes = humanfriendly.parse_size(document.find(text='Total Likes').parent.previous.replace(',', ''))
    total_follows = humanfriendly.parse_size(document.find(text='Total Follows').parent.previous.replace(',', ''))
    return page_likes, total_follows


def get_facebook_data(facebook_id, url):
    facebook_pagelikes, facebook_total_follows = get_facebook_stats(facebook_id, url)
    facebook_stats = []
    facebook_stats += [{'count': facebook_pagelikes, 'desc': "likes"}]
    facebook_stats += [{'count': facebook_total_follows, 'desc': "follows"}]
    return (facebook_stats)


# youtube stats
def get_youtube_stats(youtube_id):
    youtube_stats = []
    #youtube_service = build(serviceName='youtube', version='v3', developerKey=config.youtube_api_key)
    ##youtube_request = youtube_service.channels().list(part='statistics', id=youtube_id)
    #youtube_data = youtube_request.execute()

    #youtube_view_count = youtube_data['items'][0]['statistics']['viewCount']
    #youtube_video_count = youtube_data['items'][0]['statistics']['videoCount']
    #youtube_subscriber_count = youtube_data['items'][0]['statistics']['subscriberCount']

    #youtube_stats += [{'count': youtube_video_count, 'desc': "videos"}]
    #youtube_stats += [{'count': youtube_subscriber_count, 'desc': "subs"}]
    #youtube_stats += [{'count': youtube_view_count, 'desc': "views"}]

    return (youtube_stats)


# Instagram
# Instagram parse function
def parse_data(s):
    # creating a dictionary
    data = {}

    # splitting the content
    # then taking the first part
    s = s.split("-")[0]

    # again splitting the content
    s = s.split(" ")

    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    print ('parse', data)
    # returning the dictionary
    return data


def scrape_data(username, url):
    # getting the request from url

    r = requests.get(url)
    print('r=')
    print(r)
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
    print ('s=')
    print(BeautifulSoup)
    # finding meta info
    meta = s.find("meta", property="og:description")
    print('met ffffffffffffffffffffffffffa')
    print(meta)
    print (type(meta))

 #   if len(meta.attrs) > 0:
 #       result = parse_data(meta.attrs['content'])
 #   else:
    result=[]


    return (result)
 #   return parse_data(lookup['content'])


def get_instagram_data(instagram_id, url):
    instagram_data = scrape_data(instagram_id, url)
    instagram_stats = []
    #instagram_stats += [{'count': instagram_data['Posts'], 'desc': "posts"}]
    #instagram_stats += [{'count': instagram_data['Followers'], 'desc': "followers"}]
    #instagram_stats += [{'count': instagram_data['Following'], 'desc': "following"}]

    return (instagram_stats)

def get_site_stats(sitename, url, username):
    site_stats = []
    if sitename == 'YOUTUBE':
        site_stats = get_youtube_stats(username)
    # instagram
    if sitename == 'INSTAGRAM':
        site_stats = get_instagram_data(username, url)
    # facebook
    if sitename == 'FACEBOOK':
        site_stats = get_facebook_data(username, url)

    return (site_stats)
