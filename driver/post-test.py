#!/usr/lib/python2.7
#coding:utf-8

import urllib2
import urllib

host = 'http://101.201.78.139:8080'

source = '/phone/yidong/capcha'



params = {
            'phone_no' : '18811157152',
            'token' : 'APIXIDCARDAUTHTOKEN20150202'
         }

print urllib2.urlopen(host+source, urllib.urlencode(params)).read()


