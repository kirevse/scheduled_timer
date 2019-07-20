import datetime
import unittest
import time
import scheduled_timer

class TestScheduled(unittest.TestCase):

    def runTest(self):
        func = lambda: (
            print('{}'.format(datetime.datetime.now())),
            time.sleep(5))
        func()
        scheduled_timer.ScheduledTimer(initial_delay=2, function=func, interval=5, interval_type = scheduled_timer.ScheduledTimer.IntervalType.RATE).start()

if __name__ == '__main__':
    unittest.main()   
