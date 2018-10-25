import tweepy    #importing the tweepy module (used for accessing python API)
consumer_key = "78oHVqjgW5PkzPntQZL1c8eY0"  
consumer_secret="PQvmPpc9EElguXHPWYH7Xgv4vNcCNE0gqGQE6eZBjarYqrwP5x"   #details of you account
access_token="912243816-fia7iTT8YeUOUj2zEpfqgheaWv5uNNam1qsnWP0S"
access_token_secret="mgoCHgSTJC9NPeP8oK0kFbKDQ5jNdNxP8gp0L2EoI3CCL"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)	    #open standard for authentication of consumer key and consumer secret
auth.set_access_token(access_token,access_token_secret)     #authentication of access token and secrret
api=tweepy.API(auth)
api.update_status(input("Enter the tweet u want to send.."))     #update the status..
print("\n Your tweet is sent.!!")     #And the tweet is done..!!
