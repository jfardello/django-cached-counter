from django.db import models
from cached_counter.counters import Counter


class Thread(models.Model):
    messages_counter_from_prop = Counter("messages_count_prop")
    messages_counter_from_method = Counter("messages_count_method")
    messages_counter_without_local_cache = Counter("messages_count_prop", use_instance_cache=False)

    @property
    def messages_count_prop(self):
        return self.message_set.count()

    def messages_count_method(self):
        return self.messages_count_prop


class Message(models.Model):
    thread = models.ForeignKey(Thread)
