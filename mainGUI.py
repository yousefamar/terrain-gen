# perlin.py
# (c)Yousef Amar

import sys
import random
import math
import pygame
import time
import terrainGen
from pygame.locals import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((256,256))
	pygame.display.set_caption("Yousef'sche Noise Visualiser")
	imgsur = pygame.Surface((256,256))
	terraGen = terrainGen.TerrainGen();

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				maxe = 0
				mine = 1
				#set seed
				imgsur.fill((0,0,0))
				terraGen.setSeed()
				terraGen.gen()
				for y in range(256):
					for x in range(256):
						h = int((terraGen.tiles[y][x]*256))&0xFF
				#		if h>maxe:
				#			maxe = h
				#		if h<mine:
				#			mine = h
						imgsur.set_at((x,y),(h,h,h))
				#print "maxe = "+str(maxe)+" mine = "+str(mine)
			elif event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit(0)
		screen.blit(imgsur,(0,0))
		pygame.display.flip()

if __name__ == '__main__':
	print "Starting Yousef'sche Noise Visualiser"
	main()