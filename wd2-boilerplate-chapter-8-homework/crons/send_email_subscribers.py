import datetime
from models.user import User
from models.topic import Topic
from handlers.base import BaseHandler
from google.appengine.api import mail
import logging

class SendEmailSubscribersCron(BaseHandler):
	def get(self):
		users = User.query(User.is_subscribed==True, User.deleted == False).fetch()
		added_topics = Topic.query(Topic.deleted == False,
										Topic.created > datetime.datetime.now() - datetime.timedelta(days=1)).fetch()

		for user in users:
			mail.send_mail(subject="Topics added in last 24 hours",
											sender="klemen.plazar@gmail.com",
											to=user.email,
											body="test")
							
