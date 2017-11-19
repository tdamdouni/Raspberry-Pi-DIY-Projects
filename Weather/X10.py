
import struct
import time

# Header Byte Types
addr = 0x04
func = 0x06
fullBright = 0x7e;

funccode = {
	"All Off":	0x0,
	"All On":	0x1,
	"On":		0x2,
	"Off":		0x3,
	"Dim":		0x4,
	"Bright":	0x5,
	"All Off":	0x6,
	"ExtCode":	0x7,
	"HailReq":	0x8,
	"HailAck":	0x9,
	"Preset1":	0xA,
	"Preset2":	0xB,
	"ExtDataXfer":	0xC,
	"StatusOn":	0xD,
	"StatusOff":	0xE,
	"StatusReq":	0xF
	}


housecode = {
	"A": 0x6,
	"B": 0xE,
	"C": 0x2,
	"D": 0xA,
	"E": 0x1,
	"F": 0x9,
	"G": 0x5,
	"H": 0xD,
	"I": 0x7,
	"J": 0xF,
	"K": 0x3,
	"L": 0xB,
	"M": 0x0,
	"N": 0x8,
	"O": 0x4,
	"P": 0xC
	}

unitcode = {
	"1": 0x6,
	"2": 0xE,
	"3": 0x2,
	"4": 0xA,
	"5": 0x1,
	"6": 0x9,
	"7": 0x5,
	"8": 0xD,
	"9": 0x7,
	"10": 0xF,
	"11": 0x3,
	"12": 0xB,
	"13": 0x0,
	"14": 0x8,
	"15": 0x4,
	"16": 0xC
	}

# Given a byte string, calculate the checksum by adding all the 
# bytes and then returning the bitwise AND with 0xFF.
#==============================================================
def X10_Checksum( s ):
	sum = 0
	for c in s:
		sum = sum + ord(c)
	return sum & 0xFF


# Send a string to the X10 CM11a module.  The module replys with
# a chechsum.  On a good checksum, we send an ACK.  After the ACK,
# the module replys with a READY.  Note, the ACK value is zero and 
# the READY value is 0x55.  Also note, it make take up to two
# seconds for the module to respond on some commands.
#==============================================================
def X10_Send( ser, s ):
	ret = True	# Init return code.

	ser.flushInput()
	ser.write( s )
	c = ser.read( 1 )
	cs = X10_Checksum( s )	# Compute checksum of the bytes.

	if (len(c) == 1) and (ord(c) == cs):	# Good Checksum
		ser.write( chr(0x00) )		# Send ACK
		c = ser.read(1)			# Look for X10 ready.
		if (len(c) == 1) and (ord(c) == 0x55):
			ret = True		# All Good
		else:
			print "Err: Missing X10 ready response."
			ret = False
	else:
		print "Checksum Err / Len = %d" % len(c)
		if len(c) == 1:
			print "Checksum -> %x expecting %x" % (ord(c), cs)
		ret = False

	return ret	# Return True on Good & False on Bad



#==============================================================
def X10_On( ser, h, u ):

	ser.flushInput()
	b = struct.pack( 'BB', addr, (h << 4 ) | (u & 0x0F) )
	#print "0x%x 0x%x" % struct.unpack('BB', b)
	if X10_Send( ser, b ) == False:
		print 'X10 Error send first ON string.'
		return False
	b = struct.pack( 'BB', func, (h << 4 ) | funccode['On'] )
	#print "0x%x 0x%x" % struct.unpack('BB', b)
	if X10_Send( ser, b ) == False:
		print 'X10 Error send second ON string.'
		return False

	return True	# Everything must be OK.

#==============================================================
def X10_Off( ser, h, u ):

	ser.flushInput()
	b = struct.pack( 'BB', addr, (h << 4 ) | (u & 0x0F) )
	#print "0x%x 0x%x" % struct.unpack('BB', b)
	if X10_Send( ser, b ) == False:
		print 'X10 Error send first OFF string.'
		return False
	b = struct.pack( 'BB', func, (h << 4 ) | funccode['Off'] )
	#print "0x%x 0x%x" % struct.unpack('BB', b)
	if X10_Send( ser, b ) == False:
		print 'X10 Error send second OFF string.'
		return False

	return True	# Everything must be OK.

#==============================================================
def X10_Bright( ser, h, u ):
	ret = True
	to = ser.timeout	# Save timeout
	ser.timeout = 5
	ser.flushInput()
	b = struct.pack( 'BB', addr, (h << 4 ) | (u & 0x0F) )
	#print "0x%x 0x%x" % struct.unpack('BB', b)
	if X10_Send( ser, b ) == False:
		print 'X10 Error send first Bright string.'
		ret = False
	if ret == True:
		b = struct.pack( 'BB', fullBright, (h << 4 ) | funccode['Bright'] )
		#print "0x%x 0x%x" % struct.unpack('BB', b)
		if X10_Send( ser, b ) == False:
			print 'X10 Error send second Bright string.'
			ret = False

	ser.timeout = to	# Restore timeout to orginal value.
	return ret		# True = OK / False = Error.



# Ask the CM11A for its status.  In short order, the CM11A should
# respond with 14 bytes of status.
#==============================================================
def X10_Status( ser ):
	to = ser.timeout	# Save current timeout.
	ser.timeout = 0.1	# Status bytes should be quick.
	ret = False

	ser.flushInput()
	time.sleep( 0.1 )
	ser.write( chr(0x8b) )
	c = ser.read( 14 )	# The module should return 14 bytes of info.
	if len(c) >= 13:
		i = 0
		for a in c: 
			print "%d : %s" % ( i, hex(ord(a)) )
			i = i + 1
		print 'X10 status OK.'
		ret = True
	else:
		print 'X10 status is BAD.'
		print 'X10 string len: ' + str(len(c))
		i = 0
		for a in c: 
			print "%d : %s" % ( i, hex(ord(a)) )
			i = i + 1
		ret = False

	ser.write( chr(0x00) )	# Send an ACK.
	ser.timeout = to	# Restore timeout value.
	return (ret, c)


# The CM11A X10 will NOT do anything until its clock is set.
# The following code just sets the clock to something so the 
# interface can be used.
#==============================================================
def X10_SetClock( ser ):
	# Since I don't use the clock in the CM11A this code just
	# sets the clock to some junk so the module can start working.
	s = b"\x9b\x32\x66\x07\xf4\x04\x60"

	ser.flushInput()
	time.sleep( 0.5 )	# Wait a bit after getting a 0xA5.
	ser.flushInput()
	ser.write( s )
	print 'Reseting X10 clock.'
	c = ser.read(1)		# Readback checksum.
	cs = X10_Checksum( s[1:] )
	if (len(c) == 1) and (ord(c) == cs):
		ser.write( chr(0x00) )
		c = ser.read( 1 )
		if (len(c) == 1) and (ord(c) == 0x55):
			print 'X10 Clock set.'
		else:
			print 'X10 final 0x55 marker missing.'
	else:
		ser.write( chr(0x00) )
		print 'Bad checksum from X10 interface.'
		print 'X10 returned: ' + hex(ord(c))
		print 'Expected Checksum: ' + hex(cs)


