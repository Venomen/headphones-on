# headphones-on
Live checking if you are in focus-mode-on and letting your team know that.

## Warning. This script is Mac Only.
...but offcourse you can make it work in any OS you want in like 5min. :-)

## Requirements.
python3, bash, bluetooth headphones

## How it works?
- checking if you are @ work by ip.rz1.pl (you may use some other tool)
- gathering hardware info from <i>system_profiler</i>
- parsing this with your config & sending notifications.

## Install Me
1. git clone it to your scripts folder 
2. edit <i>config.ini</i> and <i>com.deregowski.net.headphones-on.plist</i> with your <b>work IP</b>, <b>local dirs</b>, <b>headphones names</b> and some other stuff
3. <b>./run.sh</b>

### [extra-install-stuff]
4. copy <i>com.deregowski.net.headphones-on.plist</i> to <i>~/Library/LaunchAgents/</i> [to make it permanent]
5. <i>launchctl load com.deregowski.net.headphones-on.plist</i> [to make it autostart]