from internetSpeedTwitterBot import InternetSpeedTwitterBot


post = InternetSpeedTwitterBot()

speeds = post.get_internet_speed()
post.tweet_at_provider(speedDown=speeds[0],speedUp=speeds[1])