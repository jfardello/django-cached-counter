from django.utils import unittest
from .models import Thread, Message


class CounterTest(unittest.TestCase):
    def setUp(self):
        thread = Thread.objects.create()

        for i in range(10):
            Message.objects.create(thread=thread)

        self.thread = thread

    def tearDown(self):
        self.thread.messages_counter_from_prop.clear_cache
        self.thread.messages_counter_from_method.clear_cache()
        self.thread = None

    def test_count(self):
        self.assertEqual(self.thread.message_set.count(), 10)

    def test_wrapped_counters(self):
        self.assertEqual(self.thread.messages_count_prop, 10)
        self.assertEqual(self.thread.messages_count_method(), 10)

    def test_prop_cached_counter(self):
        self.assertEqual(int(self.thread.messages_counter_from_prop), 10)

    def test_method_cached_counter(self):
        self.assertEqual(int(self.thread.messages_counter_from_method), 10)

    def test_atomic_increment(self):
        # Forcing counter to fetch it's value from the DB
        int(self.thread.messages_counter_from_prop)

        # Incrementing the counter without actually adding elements
        self.thread.messages_counter_from_prop += 42
        self.assertEqual(int(self.thread.messages_counter_from_prop), 52)

        # Cache is resetted after calling assertEqual,
        # so counter gets it's actual value
        thread = Thread.objects.all()[0]
        thread.messages_counter_from_prop.clear_cache()
        self.assertEqual(int(thread.messages_counter_from_prop), 10)

    def test_atomic_decrement(self):
        # Forcing counter to fetch it's value from the DB
        int(self.thread.messages_counter_from_prop)

        # Incrementing the counter without actually adding elements
        self.thread.messages_counter_from_prop -= 2
        value = int(self.thread.messages_counter_from_prop)
        self.assertEqual(value, 8)

    def test_without_instance_cache(self):
        counter = self.thread.messages_counter_without_local_cache

        # Forcing counter to fetch it's value from the DB
        int(counter)

        from django.core.cache import cache
        cache.incr(counter.cache_key, 5)

        self.assertEqual(int(counter), 15)
