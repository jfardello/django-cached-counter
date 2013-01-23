from cached_counter.counters import virtual_factory, VirtualModelBase
from .models import Thread

ThreadForm = virtual_factory(Thread)
ThreadForm2 = virtual_factory(Thread, parent=VirtualModelBase)

