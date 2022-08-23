import vk_api
import database
import config
import requests
import random

from datetime import datetime
from time import sleep





TOKEN = config.TOKEN
login = config.login
password = config.password


vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()
working = True
posts = database.get_from_db()

def post_vk(post):
	now = datetime.now()
	current_time = now.strftime("%H:%M")
	time_to_send = "21:00"
	print(current_time)
	if current_time==time_to_send:
		print(vk.wall.post(message='Новый день', from_group = '1', owner_id = '-215521028'))
		sleep(5)
		print(vk.wall.post(message = post, from_group = '1', owner_id = '-215521028'))
	sleep(55)




while working:
	rand = random.randrange(0,len(posts))
	print(posts[rand])
	post_vk(posts[rand])
