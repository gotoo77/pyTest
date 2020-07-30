import time
import sys

# nohup
dtws_out = 'C:/dev/test.txt'
watch_period = 2
continue_loop = True

print('[' + time.ctime() + "]>>> Start watching (" + dtws_out + ") <<<")


def watch_prog_return():
    global continue_loop
    with open(dtws_out) as f:
        for line in f:
            if '139' in line:
                print('\n[' + time.ctime() + "] Read ret code '" + line + "' > SEGFAULT detected!")
                continue_loop = False
                break


while continue_loop:
    sys.stdout.write('c')
    watch_prog_return()
    time.sleep(watch_period)

print('>>> End of watch.<<<')

