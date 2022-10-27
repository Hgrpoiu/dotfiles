# -*- coding: utf-8 -*-
#
import subprocess
import os
import os.path

from i3pystatus import Status
import colour as color
from i3pystatus.updates import pacman, cower


status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week

status.register("updates",
    format = "Updates: {count}",
    format_no_updates = "",
    on_leftclick="termite --geometry=1200x600 --title=updates -e 'pacaur --needed --noconfirm --noedit -Syu'",
    backends = [pacman.Pacman(), cower.Cower()])

status.register("clock",
    format=" %H:%M:%S",
    color='#C678DD',
    interval=1,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("clock",
    format="  %a %d-%m-%Y ",
    color='#61AEEE',
    interval=1,)


status.register("pulseaudio",
    color_unmuted='#98C379',
    color_muted='#E06C75',
    format_muted=' [muted]',
    format=" {volume}%")

#status.register("network",
#    interface="eno1",
#    color_up="#8AE234",
#    color_down="#EF2929",
#    format_up=": {v4cidr}",
#    format_down="",)

status.register("network",
    interface="wlo1",
    color_up="#8AE234",
    color_down="#EF2929",
    format_up="  {essid}  {kbs} kbs",
    format_down="",)


status.register("mem",
    color="#999999",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format=" {avail_mem}/{total_mem} GB",
    divisor=1073741824,)

status.register("keyboard_locks",
    format='{caps} {num}',
    caps_on='Caps Lock',
    caps_off='',
    num_on='Num On',
    num_off='',
    color='#e60053',
    )

status.run()
