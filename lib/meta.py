from lib.exceptions import ManagerConfigurationError


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Manager(metaclass=Singleton):
    def __init__(self, *, config=None):
        if config is None:
            raise ManagerConfigurationError("Manager config wasn't provided")
