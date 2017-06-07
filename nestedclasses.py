import sys


class nestedclasses(object):

    def __init__(self):
        self.old = sys.gettrace()
        sys.settrace(self.tracer)

    def tracer(self, frame, event, arg):
        if event == 'call':
            for key, value in frame.f_back.f_locals.items():
                if key not in frame.f_locals:
                    # Python 3.3 fix:
                    if '__locals__' in frame.f_locals:
                        frame.f_locals['__locals__'][key] = value
                    else:
                        frame.f_locals[key] = value
        return self.tracer

    def __call__(self, cls):
        sys.settrace(self.old)
        return cls
