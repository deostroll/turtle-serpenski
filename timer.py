from shutil import ExecError
from threading import Event, Thread

class SlidingTimer(Thread):
    def __init__(self, timeout, func, is_daemon=False):
        Thread.__init__(self, daemon=is_daemon, name="SlidingTimer")
        self._timeout = timeout
        self._func = func
        self._evt = None
        self._reset_called = False
        self._finalEvt = Event()

    def run(self):
        self._run_timer()
    
    def _run_timer(self):
        self._evt = Event()
        self._evt.wait(self._timeout)

        if self._reset_called:
            self._reset_called = False
            return self._run_timer()

        if not self._evt.is_set():
            self._evt.set()
            self._finalEvt.set()
            self._func()
        
    def reset(self):
        if self._evt is None:
            raise RuntimeError('start() not called on the timer')
        
        if self._evt.is_set():
            raise RuntimeError('timer elapsed')

        self._reset_called = True
        self._evt.set()

    def wait(self):
        self.join()
        
if __name__ == '__main__':
    import time
    timer = SlidingTimer(10, lambda: print('Timer done'))
    start_time = time.time()
    timer.start()
    time.sleep(2)        
    timer.reset()
    timer.wait()
    end_time = time.time()
    print('Elapsed:', end_time - start_time)
        


