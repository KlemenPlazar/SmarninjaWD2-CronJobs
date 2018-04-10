#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.comments import CommentAdd
from handlers.topics import TopicAdd, TopicDetails, TopicDelete
from workers.email_new_comment import EmailNewCommentWorker
from crons.delete_topics import DeleteTopicsCron
from crons.send_email_subscribers import SendEmailSubscribersCron

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),

    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetails, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAdd, name="comment-add"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDelete, name="topic-delete"),

    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker, name="task-email-new-comment"),
    webapp2.Route('/cron/delete-topics', DeleteTopicsCron, name="cron-delete-topics"),
    webapp2.Route('/cron/send-email', SendEmailSubscribersCron, name="cron-send-email"),
], debug=True)
