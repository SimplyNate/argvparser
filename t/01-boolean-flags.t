#!/usr/bin/env python3
import sys
sys.path.append('.')

from argvparse import check_switches
from testsimple import *

plan(tests=13)

diag('No acceptable flags, no flags passed')
args, err = check_switches(['test'], [])

ok(args == {})
ok(err is None)

diag('No acceptable flags, flags passed')
args, err = check_switches(['test', '-a'], [])

ok(args is None)
ok(err is not None)

diag('Acceptable flags, no flags passed')
args, err = check_switches(['test'], ['-a'])

ok('-a' not in args)
ok(err is None)

diag('Acceptable flags, flags passed')
args, err = check_switches(['test', '-a'], ['-a'])

ok('-a' in args)
ok(args['-a'])

diag('Acceptable flags, multiple flags passed')
args, err = check_switches(['test', '-b', '-a'], ['-a', '-b'])

ok('-b' in args)
ok('-a' in args)
ok(args['-a'])
ok(args['-b'])
ok(err is None)
