max_chars = 140
print("*" * 50)
tweet = input("Enter your tweet! ")
tweet_len = len(tweet)

print("*" * 50)
if tweet_len < max_chars:
    print(f"That {tweet_len} char tweet will work!")

else:
    print(f"Your {tweet_len} char tweet is {tweet_len-max_chars} chars too long")
