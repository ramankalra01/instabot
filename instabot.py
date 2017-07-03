import requests

APP_ACCESS_TOKEN = '4392741281.7788e8d.25fc02bdcc8d4d28bb8749bba860571e'
#access token for self info

BASE_URL = 'https://api.instagram.com/v1/'


def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()
  #convert json into py

  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'User does not exist!'
        #no user found
  else:
    print 'Status code other than 200 received!'

self_info()