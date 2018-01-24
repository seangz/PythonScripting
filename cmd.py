

import subprocess
import code

code = subprocess(['ls','-z'])

if code == 0:
    print('Command finished successfully')
else:
    print("failed wtih code: %i" % code)