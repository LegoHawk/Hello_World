tweet_limit = 280
tweet_string = "Blah" * 50
#diff = tweet_limit - len(tweet_string)
#if diff >=0:
#    print("A fitting tweet")
#else:
#    print("Went over by,", abs(diff))
if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
