from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

x = 100
y = 100
z = 100

pos = mc.player.getTilePos()

playerX = pos.x
playerY = pos.y
playerZ = pos.z

time.sleep(3)

#mc.player.setTilePos(x,y,z)

blockType = 171, 14

mc.setBlock(playerX,(playerY-1),playerZ, blockType)

mc.setBlock(x,y,z, blockType)

i = 0

while i < 100:
    #mc.setBlock(x,y,z, blockType)
    #time.sleep(0.1)
    #mc.player.setTilePos(x,y,z)
    #y = y + 1
    i = i + 1
