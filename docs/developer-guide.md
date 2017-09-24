

## Tech

### Python

Python version 2 is used at the moment

### caja-python

Home: https://github.com/mate-desktop/caja-python

Documentation: https://projects-old.gnome.org/nautilus-python/documentation/html/index.html

Examples: https://github.com/mate-desktop/caja-python/tree/master/examples

### Interface to clamtk

clamtk-gnome communicates with clamtk via the command line at the moment: `os.system('clamtk %s &' % filename)`

### Tips

#### Restarting Caja

You can use `killall caja` to close caja instances. `kill -9 pid` may sometimes have to be used (with the pid that you get from `ps aux | grep caja`)


## Social

Please keep Tord and/or Dave in the loop when updating this plugin

* tord (dot) dellsen (at) gmail (dot) com
* dave (dot) nerd (at) gmail (dot) com

Tord has a background with Python and Dave has experience with Perl
