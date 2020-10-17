youtube_service = build(serviceName='youtube', version='v3', developerKey=config.youtube_api_key)
    youtube_request = youtube_service.channels().list(part='statistics', id=youtube_id)
    youtube_data = youtube_request.execute()

    youtube_view_count = youtube_data['items'][0]['statistics']['viewCount']
    youtube_video_count = youtube_data['items'][0]['statistics']['videoCount']
    youtube_subscriber_count = youtube_data['items'][0]['statistics']['subscriberCount']

    youtube_stats += [{'count': youtube_video_count, 'desc': "videos"}]
    youtube_stats += [{'count': youtube_subscriber_count, 'desc': "subs"}]
    youtube_stats += [{'count': youtube_view_count, 'desc': "views"}]
