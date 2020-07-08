import redis
import os
import telebot

target = os.environ['TARGET']
stoploss = os.environ['STOPLOSS']


yolodice_privkey = os.environ['YOLODICE_PRIVKEY']
yolodice_currency = is.environ['YOLODICE_CURRENCY']

r = redis.from_url(os.environ.get("REDIS_URL"))
