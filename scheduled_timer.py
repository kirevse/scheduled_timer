import enum
import threading

class ScheduledTimer:

    class IntervalType(enum.Enum):
        DELAY = 1
        RATE = 2

    def __init__(self, interval, function, args=None, kwargs=None, interval_type = IntervalType.DELAY, initial_delay = 0):
        self.interval = interval
        self.function = function
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.interval_type = interval_type

        self.timer = threading.Timer(initial_delay, self.__invoke, args, kwargs)

    def start(self):
        self.timer.start()

    def cancel(self):
        self.timer.cancel()

    def __invoke(self):
        self.timer = threading.Timer(self.interval, self.__invoke)
        if self.interval_type == ScheduledTimer.IntervalType.RATE:
            self.timer.start()
        self.function(*self.args, **self.kwargs)
        if self.interval_type == ScheduledTimer.IntervalType.DELAY:
            self.timer.start()
