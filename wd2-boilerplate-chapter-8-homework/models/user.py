from google.appengine.ext import ndb

class User(ndb.Model):
	email = ndb.StringProperty()
	is_subscribed = ndb.BooleanProperty(default=False)
	created = ndb.DateTimeProperty(auto_now_add=True)
	updated = ndb.DateTimeProperty(auto_now=True)
	deleted = ndb.BooleanProperty(default=False)

	def subscribe(self):
		self.is_subscribed = True
		self.put()

	def unsubscribe(self):
		self.is_subscribed = False
		self.put()

	@classmethod
	def create(cls, email):
		users = cls.query(cls.email == email).fetch()
		if len(users) == 0:
			user = cls(email=email)
			user.put()
			return user
		
		return False