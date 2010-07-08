def s2b(msg):
	return [ord(x) for x in msg]

def b2s(msg):
	return "".join([chr(int(x)) for x in msg])

def test():
	s = chr(0xe2)+"ABCDE\0\1\2"
	b = [0xe2, 65, 66, 67, 68, 69, 0, 1, 2]
	assert(b == s2b(s))
	assert(s == b2s(b))
	assert(b == s2b(b2s(b)))
	assert(s == b2s(s2b(s)))
	print "Test ok"

if __name__ == '__main__':
	test()
