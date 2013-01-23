CachedCounter is used to cache counters such as photo number in an album.

It uses django.core.cache as backend. CachedCounter acts as a model field and supports atomic increments.

You can use signals to update counter after adding or deleting instances.

Usage
--

models.py

    from django.db import models
    from cached_counter.counters import Counter

    class Album(models.Model):
        photo_count = Counter("get_photo_count")

        def get_photo_count(self):
            return self.photo_set.count()

getting and updating the counter

    # get counter value
    print long(album.photo_count)

    # atomic increment
    album.photo_count += 1

    # set the value
    album.photo_count = 10

    # using counter in django templates
    {{ album.photo_count }}

ModelForm helper, that works on virtual fields, useful on perdurable cache backeds, such as django-redis.


    from cached_counter.counters import virtual_factory

    AlbumForm = virtual_factory(Album)
