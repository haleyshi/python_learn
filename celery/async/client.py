# -*- coding: utf-8 -*-

from tasks import add

# 异步任务，不会阻塞当前进程
add.delay(2, 8)

print 'hello world'