#/user/bin/dev python3

import os
p
print('Process (%s) start...' % os.getpid())
#Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('i am child process (%s) and my parent is %s.' % (os.getpid(),
                                                            os.getppid()))
else:
    print('I (%s) just created a child process(%s).' % (os.getpid(), pid))
