rtl_mus
=======

**RTL Multi-User Server** is a small python script to allow multiple clients control the same RTL-SDR compatible DVB-T tuner, while also receiving I/Q samples. It has also the functionality to serve IQ samples from an external process (aka fake dongle mode).

## How does it work?
- <tt>rtl\_mus</tt> requires an instance of <tt>rtl\_tcp</tt> to connect to. 
- When it receives a command from any of its clients, <tt>rtl\_mus</tt> resends it to the <tt>rtl\_tcp</tt> server. 
- It continously reads samples from <tt>rtl\_tcp</tt>, and resends them to the clients.

## Other features

###  DSP processing

<tt>rtl\_mus</tt> can also execute a command to perform DSP processing on the I/Q stream; then the processed I/Q stream is sent to its clients. 
A sample command for FLAC processing is included in the config file. FLAC is a loseless codec originally intended for audio, but it seems to work on sampled RF, too... :smile: As of a FLAC processed I/Q stream requires about 20% less bandwidth than the original, it might help to transport I/Q signals over a low-bandwidth internet link, but as of none of the SDR software can decode FLAC right now, another instance of <tt>rtl\_mus</tt> has to be run locally, to decode the FLAC-encoded signal. 

###  DSP fake dongle mode

When configuring the tool for reading the samples from an external tool you don't need to use a real <tt>rtl\_tcp</tt> server. You can use this mode for reading the samples from a file (in RAW format) or from a FIFO (for example connected to the PIPE output of another tool that generates the samples). Then you don't need at all to have a real RTL dongle for using any RTL-SDR tool.

Inside the config file you can found and example for read the samples from a fifo file using the simple <tt>dd</tt> tool. You need to fill up the fifo using another process (for example with <tt>cat /my-file > /raw-fifo</tt>). This mode it's enabled setting the client port to 0.

### Permissions on commands
By changing the source code, one can easily allow and deny remote clients execute particular commands on the <tt>rtl\_tcp</tt> server. Commands that are not allowed are simply not forwarded by <tt>rtl\_mus</tt>.

### On rtl_tcp crash it fills clients with zeros 
It can be particularly useful to avoid your GNU Radio flowgraph hang when using an OsmoSDR Source block.

## Authors

András Retzler 
<ha7ilm@sdr.hu>
