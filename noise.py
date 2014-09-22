def perlin(seed, x, y, z):
	g = 0.5#0.707106781 #Gain
	o = 4 #Octaves
	total = 0
	for i in range(o):
		f = 2**i#)/40 #Frequency
		a = g**i #Amplitude
		total += triLerpedSmoothNoise(seed, x*f, y*f, z*f)*a
	return total
	
def fBm(seed, x, y, z):
	gain = 0.5
	lacunarity = 2
	frequency = 1/40
	amplitude = 10
	octaves = 4
	total = 0
	for i in range(o):
		total += triLerpedSmoothNoise(seed, x*frequency, y*frequency, z*frequency)*amplitude
		frequency *= lacunarity
		amplitude *= gain
	return total

def triLerpedSmoothNoise(seed, x, y, z):
	muX = x-int(x)
	x = int(x)
	muY = y-int(y)
	y = int(y)
	muZ = z-int(z)
	z = int(z)
	return lerp(biLerp(smooth(seed, x, y, z), smooth(seed, x+1, y, z), smooth(seed, x, y+1, z), smooth(seed, x+1, y+1, z), muX, muY),\
			biLerp(smooth(seed, x, y, z+1), smooth(seed, x+1, y, z+1), smooth(seed, x, y+1, z+1), smooth(seed, x+1, y+1, z+1), muX, muY), muZ)

def triLerp(cs, muX, muY, muZ):
	return lerp(biLerp(cs[0][0][0], cs[1][0][0], cs[0][1][0], cs[1][1][0], muX, muY),\
			biLerp(cs[0][0][1], cs[1][0][1], cs[0][1][1], cs[1][1][1], muX, muY), muZ)

def biLerp(c00, c10, c01, c11, muX, muY):
	return lerp(lerp(c00, c10, muX), lerp(c01, c11, muX), muY)

def lerp(x0, x1, mu):
	return x0+(x1-x0)*mu

def smooth(seed, x, y, z):
	edges = (noise(seed,x-1,y-1,z)+noise(seed,x+1,y-1,z)+noise(seed,x-1,y+1,z)+noise(seed,x+1,y+1,z)\
			+noise(seed,x,y-1,z-1)+noise(seed,x-1,y,z-1)+noise(seed,x+1,y,z-1)+noise(seed,x,y+1,z-1)\
			+noise(seed,x,y-1,z+1)+noise(seed,x-1,y,z+1)+noise(seed,x+1,y,z+1)+noise(seed,x,y+1,z+1))/16
	corners = (noise(seed,x-1,y-1,z-1)+noise(seed,x+1,y-1,z-1)+noise(seed,x-1,y+1,z-1)+noise(seed,x+1,y+1,z-1)\
			+noise(seed,x-1,y-1,z+1)+noise(seed,x+1,y-1,z+1)+noise(seed,x-1,y+1,z+1)+noise(seed,x+1,y+1,z+1))/32
	sides = (noise(seed,x,y-1,z)+noise(seed,x-1,y,z)+noise(seed,x+1,y,z)+noise(seed,x,y+1,z)+noise(seed,x,y,z-1)+noise(seed,x,y,z+1))/8
	return edges + corners + sides + noise(seed,x,y,z)/4

def noise(seed, x, y, z):
	"""Generate a linearly congruent random number in the range [-1.0, 1.0) implicitly.
		Primes and generators taken from libnoise as the original large ones made patterns."""
	n = (1619*x + 31337*y + 6971*z + 1013*seed)&0x7FFFFFFF
	n = (n>>13)^n;
	return (((n*(n*n*60493+19990303)+1376312589)&0x7FFFFFFF)/1073741824.0) - 1