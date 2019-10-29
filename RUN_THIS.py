''''Use this program to generate all references needed to run a spectra sensor validation.'''

import ADC
import time

try:
    s = ADC.DataQ_DI145(comm_port='COM4')
    s.scan()
    s.live_data()
except:
    pass

time.sleep(20)
s.sts()
