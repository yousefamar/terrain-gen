import os
import noise

class TerrainGen():
	
	def __init__(self, seed=None):
		self.tiles = [[0]*256 for i in range(256)]
		self.setSeed(seed);

	def setSeed(self, seed=None):
		if seed is None:
			import time
			seed = long(time.time() * 256)
		if not isinstance(seed, (int, long)):
			seed = hash(seed)
		self.seed = seed

	def gen(self):
		for y in range(64):
			for x in range(64):
				self.tiles[y][x] = noise.perlin(self.seed, x, 0, y)