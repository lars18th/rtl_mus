'''
This file is part of RTL Multi-User Server, 
	that makes multi-user access to your DVB-T dongle used as an SDR.
Copyright (c) 2013 by Andras Retzler <retzlerandras@gmail.com>

RTL Multi-User Server is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

RTL Multi-User Server is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with RTL Multi-User Server.  If not, see <http://www.gnu.org/licenses/>.
'''

my_ip=''	# all interfaces
my_listening_port = 7373

#send_first=chr(9)+chr(0)+chr(0)+chr(0)+chr(1) # set direct sampling
send_first=""
#dongle_id = ( chr(0x52) + chr(0x54) + chr(0x4c) + chr(0x30)
#            + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x02)
#            + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x05)
#            ) # if you like to rewrite the DONGLE-ID. Required when using fake dongle.
dongle_id=""
rtl_tcp_host = 'localhost'	# set to "" (NULL) when you use the fake dongle.
rtl_tcp_port = 1234		# when you set to 0 you're enabling the fake dongle!

setuid_on_start = 0	# we normally start with root privileges and setuid() to another user
uid = 999		# determine by issuing: $ id -u username
ignore_clients_without_commands = 1	# we won't serve data to telnet sessions and things like that
					# we'll start to serve data after getting the first valid command 
freq_allowed_ranges = [[0000000,2200000000]]
# Allow from all: freq_allowed_ranges = [[24000000,2200000000]]

client_cant_set_until=0		
first_client_can_set=True	#openwebrx - spectrum thread will set things on start # no good, clients set parameters and things
buffer_size=25000000		# per client
log_file_path = "/dev/null"	# Might be set to /dev/null to turn off logging
'''
Allow any host to connect:
	use_ip_access_control=0

Allow from specific ranges:
	use_ip_access_control=1
	order_allow_deny=0 # deny and then allow
	denied_ip_ranges=() # deny from all
	allowed_ip_ranges=('192.168.','44.','127.0.0.1') # allow only from ...

Deny from specific ranges:
	use_ip_access_control=1
	order_allow_deny=0 # allow and then deny
	allowed_ip_ranges=() # allow from all
	denied_ip_ranges=('192.168.') # deny any hosts from ...
'''
use_ip_access_control=0
order_allow_deny=0
denied_ip_ranges=() 
allowed_ip_ranges=()
allow_gain_set=1

use_dsp_command=False	# you can process raw I/Q data with a custom command that starts a process that we can pipe the data into, and also pipe out of.
			# when using the fake dongle mode it's mandatory to enable the DSP
debug_dsp_command=False	# show sample rate before and after the dsp command
dsp_command=""			# when using the fake dongle mode this it's required
dsp_chunk_size=1024		# use values like '16348','1024','16384'. It's the size of READ chunks from the DSP process. Recomendation: use the same value as the command in the DSP process  
dsp_sampling_rate=250000	# when using the fake dongle it's required to resynch
dsp_resynch_loop=1		# number of reads when resynching using the fake dongle
'''
Example of fake dongle mode: reading samples from a FIFO file

# Read from fifo "/raw-fifo" in chunks of 16384 bytes
dsp_command="dd if=/raw-fifo bs=16384 status=noxfer"

# Set the sampling rate for regular 2048000 Msps
dsp_sampling_rate=2048000

# Do a resynch every 8 loops (try with 8,16,32 values) 
dsp_resynch_loop=8

Reset client values
rtl_tcp_host=""
rtl_tcp_port=0 # mandatory for fake dongle
use_dsp_command=True # mandatory for fake dongle
debug_dsp_command=True # recomended
watchdog_interval=0 # disable it

Set the Dongle-ID
dongle_id = ( chr(0x52) + chr(0x54) + chr(0x4c) + chr(0x30)
            + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x02)
            + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x05)
            ) # example for simulating a generic RTL2832U
'''

'''
Example DSP commands:
  * Compress I/Q data with FLAC:
    flac --force-raw-format --channels 2 --sample-rate=250000 --sign=unsigned --bps=8 --endian=little -o - -
  * Decompress FLAC-coded I/Q data:
    flac --force-raw-format --decode --endian=little --sign=unsigned - -
'''
watchdog_interval=1.5
reconnect_interval=10 
'''
If there's no input I/Q data after N seconds, input will be filled with zero samples, 
so that GNU Radio won't fail in openwebrx. It may reconnect rtl_tcp_tread. 
If watchdog_interval is 0, then watchdog thread is not started. 

'''
cache_full_behaviour=2
'''
	0 = drop samples
	1 = close client
	2 = openwebrx: don't care about that client until it wants samples again (gr-osmosdr bug workaround)
'''

