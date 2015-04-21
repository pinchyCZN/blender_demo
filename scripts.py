from bge import constraints
from bge import logic
from bge import events
from bge import render

import math


def cube2anim():
	print("anim")
	cont = logic.getCurrentController()
	scene = logic.getCurrentScene()
	cube=cont.owner
#	for i in dir(cube):
#		print(i)
	name = "Cube.002Action"
	start = 1
	end = 200
	layer = 0
	priority = 0
	blendin = 0
	mode = logic.KX_ACTION_MODE_LOOP
	layerWeight = 0.0
	ipoFlags = 0
	speed = 1.0

	#cube.position[0]+=.3
	cube.playAction(name, start, end, layer, priority, blendin, mode, layerWeight, ipoFlags, speed)	

def cube2mat():
	print("mat")
	cont = logic.getCurrentController()
	cube=cont.owner
	name = "Material.001Action"
	start = 1
	end = 200
	layer = 1
	priority = 0
	blendin = 0
	mode = logic.KX_ACTION_MODE_LOOP
	layerWeight = 0.0
	ipoFlags = 0
	speed = 1.0

	cube.playAction(name, start, end, layer, priority, blendin, mode, layerWeight, ipoFlags, speed)	

