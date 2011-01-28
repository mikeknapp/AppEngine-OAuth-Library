#!/usr/bin/env python

import oauth

from google.appengine.api import urlfetch

import unittest


class TestOAuth(unittest.TestCase):
  """Test our OAuth code"""

  def setUp(self):

    self.service_name = oauth.TWITTER
    self.consumer_key = "consumer_key"
    self.consumer_secret = "consumer_secret"
    self.request_url = "http://www.twitter.com/fake/request"
    self.access_url = "http://www.twitter.com/fake/access"
    self.callback_url = "http://www.twitter.com/fake/callback"

    self.client = oauth.OAuthClient(self.service_name,
                                    self.consumer_key,
                                    self.consumer_secret,
                                    self.request_url,
                                    self.access_url,
                                    self.callback_url)

  def tearDown(self):

    pass

  def test_client_factory(self):

    result = oauth.get_oauth_client(oauth.TWITTER, "key", "secret",
                                    "http://t.com/callback")

    self.assert_(isinstance(result,oauth.TwitterClient))
    self.assertEquals(result.service_name, oauth.TWITTER)
    self.assertEquals(result.consumer_key, "key")
    self.assertEquals(result.consumer_secret, "secret")
    self.assertEquals(result.callback_url, "http://t.com/callback")

  def test_initialise(self):

    self.assertEquals(self.client.service_name, self.service_name)
    self.assertEquals(self.client.consumer_key, self.consumer_key)
    self.assertEquals(self.client.consumer_secret, self.consumer_secret)
    self.assertEquals(self.client.request_url, self.request_url)
    self.assertEquals(self.client.access_url, self.access_url)

  def test_prepare_request(self):

    result = self.client.prepare_request("http://www.twitter.com/fake/request",
                                         t=123456789,
                                         nonce="jh23jk4h763u3")
    self.assertEquals(result,
      ("oauth_nonce=jh23jk4h763u3&"
      "oauth_timestamp=123456789&"
      "oauth_consumer_key=consumer_key&"
      "oauth_signature_method=HMAC-SHA1&"
      "oauth_version=1.0&"
      "oauth_signature="
      "dB1UU6FF7WChGPF4Ja5M%2FI0WRFg%3D&"
      "oauth_callback="
      "http%3A%2F%2Fwww.twitter.com%2Ffake%2Fcallback")
    )


if __name__ == "__main__":
  unittest.main()
