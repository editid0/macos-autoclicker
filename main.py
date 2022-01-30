import re, time
from humanfriendly import format_timespan
from pynput.mouse import Button, Controller

mouse = Controller()

with open('config.txt', 'r') as f:
    lines = f.readlines()
    clicks = None
    gap = None
    side = None
    dual = None
    for line in lines:
        clicks_regex = re.compile(r'clicks=(-?(\d|,)+)')
        gap_regex = re.compile(r'gap=((\d|((\d))?\.(\d+)?)+)')
        side_regex = re.compile(r'side=(left|right)')
        dual_regex = re.compile(r'dual=(yes|no)')
        clicks_ = re.search(clicks_regex, line)
        gap_ = re.search(gap_regex, line)
        side_ = re.search(side_regex, line)
        dual_ = re.search(dual_regex, line)
        if clicks_:
            clicks = clicks_.group(1)
            clicks = clicks.replace(',', '')
            clicks = int(clicks)
            continue
        if gap_:
            gap = gap_.group(1)
            gap = gap.replace(',', '')
            gap = float(gap)
            continue
        if side_:
            side = side_.group(1)
            continue
        if dual_:
            dual = dual_.group(1)
            continue
    if not all([clicks, gap, side, dual]):
        print('No clicks, gap, side, or dual found in config.txt')
        exit()
    else:
        print('Clicking in 5 seconds.')
        print(f'This will take about {format_timespan(gap * clicks)} to finish.')
        time.sleep(5)
        print('Clicking {} times with a gap of {} and using the {} mouse button.'.format(clicks, gap, side))

for _ in range(clicks):
    if side == 'left':
        if dual == 'yes':
            mouse.click(Button.left, 1)
        mouse.click(Button.left, 1)
        time.sleep(gap)
    elif side == 'right':
        if dual == 'yes':
            mouse.click(Button.right, 1)
        mouse.click(Button.right, 1)
        time.sleep(gap)
    else:
        print('Invalid mouse button side')
        exit()
