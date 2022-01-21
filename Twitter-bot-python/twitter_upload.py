



# 1. import package
import tweepy

# 2. Store credentials
apiKey = "lQtoqbP06j63jRecuzGhtIg67"
apikeySecret = "cJntAXglzg9kItO4MWlhFY4NNFELyUGi57W5ZI2Ij18x8NjiHr"

accessToken = "2864972028-QjzmelJbN2svrRRe60VKwFwPzG9GHzIATRYxYl2"
accessTokenSecret = "nsS7Hc9JSd16uHeOZ8vnfbXAOJtAdd0QvR3sao871uPXl"


# 3. Create Oauth client and set authentication and create API object
oauth = tweepy.OAuthHandler(apiKey, apikeySecret)
oauth.set_access_token(accessToken, accessTokenSecret)
print("Authentication successfully")

api = tweepy.API(oauth)


# 4. upload media
media = api.media_upload("Twitter-limitation.png")

result = api.update_status(status = "Uploaded using Tweepy python module",media_ids = [media.media_id_string])

print("Uploaded successfully")