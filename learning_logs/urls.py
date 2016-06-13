from django.conf.urls import url
from .views import index, topics, topic, new_topic, new_entry, edit_entry


urlpatterns = [
    # Main page
    url(r'^$', index, name='index'),
    # Show all topics
    url(r'^topics/$', topics, name='topics'),
    # Detail topics
    url(r'^topic/(?P<topic_id>\d+)/$', topic, name='topic'),
    # Add a new topic
    url(r'^new_topic/$', new_topic, name='new_topic'),
    # Edit topic
    url(r'^edit_topic/$', new_topic, name='new_topic'),
    # Add a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', new_entry, name='new_entry'),
    # Edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', edit_entry, name='edit_entry'),
]
