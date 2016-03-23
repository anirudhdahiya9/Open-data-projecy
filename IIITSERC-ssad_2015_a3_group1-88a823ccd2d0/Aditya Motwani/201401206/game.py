import pygame
import random , sys
import time
from pygame.locals import *
from player import Player
from gorilla import Gorilla
from coins import Coins
from ladders import Ladders
from fireball import Fireball
from misc import Redheart,Whiteheart,life
from princess import Princess


turns = 3
score = 0
def main(turns,score):
	pygame.init()
	pygame.display.set_caption('Donkey Kong')
	swidth=800
	sheight=620
	clock = pygame.time.Clock()
	disp=pygame.display.set_mode([swidth,sheight],0,32)

	BLACK = (0,0,0)
	class Gameline(pygame.sprite.Sprite) :
		def __init__(self,color,length):

			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.Surface([length,4])
			self.image.fill(color)
			self.rect=self.image.get_rect()
	class Vertline(pygame.sprite.Sprite) :
		def __init__(self):

			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.Surface([4,45])
			self.image.fill(BLACK)
			self.rect=self.image.get_rect()
			self.rect.y = 10

	line1 = Vertline()
	line1.rect.x = 250
	line2 = Vertline()
	line2.rect.x = 450
	list_obj=pygame.sprite.Group()
	pl_list=pygame.sprite.Group()
	coin_list=pygame.sprite.Group()
	ladder_list=pygame.sprite.Group()
	fire_list=pygame.sprite.Group()
	gor_list=pygame.sprite.Group()
	heart=pygame.sprite.Group()
	ps_list=pygame.sprite.Group()
	list_obj.add(line1)
	list_obj.add(line2)

	for i in range(3):
		line = Gameline(BLACK,600)
		line.rect.x = -10
		line.rect.y = 100+i*200
		list_obj.add(line)
	for i in range(2):
		line = Gameline(BLACK,600)
		line.rect.x = 230
		line.rect.y = 200+i*200
		list_obj.add(line)

	line = Gameline(BLACK,810)
	line.rect.x = -10
	line.rect.y = 600
	list_obj.add(line)

	line = Gameline(BLACK,200)
	line.rect.x = 250
	line.rect.y = 50
	list_obj.add(line)

	mario = Player()
	pl_list.add(mario)

	gor=Gorilla()
	gor_list.add(gor)

	ps=Princess()
	ps_list.add(ps)


	ladxy =[520,298,550,498,300,398,300,198,540,98]
	for i in range(0,10,2):
		lad=Ladders(ladxy[i],ladxy[i+1])
		ladder_list.add(lad)
		

	for i in range(12) :
		c = Coins()
		c.cd(1)
		coin_list.add(c)
	for i in range(12) :
		c=Coins()
		c.cd(2)
		coin_list.add(c)
	c=50

	while True :
			heart.empty()
			life(turns,heart)

			font = pygame.font.Font(None, 36)
			text = font.render("Score = "+ str(score), 1, (10, 10, 10))
			for event in pygame.event.get() : 
				if event.type == QUIT :
					pygame.quit()
					sys.exit()
			s=pygame.sprite.groupcollide(pl_list,coin_list,False,True)
			score += (len(s)*5)
			if score >= 50 :
				list_obj.remove(line1)
				list_obj.remove(line2)
			flag = pygame.sprite.groupcollide(pl_list,ladder_list,False,False)
			if len(flag) > 0 :
				for i in ladder_list :
					if flag.values()[0][0] == i :
						i.move(mario) 
			else :
				mario.move() 
				mario.rect.y=mario.checkmove(list_obj)
			keys=pygame.key.get_pressed()
			if keys[K_q] :
			 	pygame.quit()
			 	sys.exit()
			if keys[K_SPACE] :
				flag = 1
				v = -50
			if flag == 1 :
				mario.rect.y += v
				v += 10
				if v == 40 :
					flag = 0	
			if c % 100 == 0 :
				f=Fireball(gor,fire_list)
				c=850
			else :
				c += 1
			for qw in fire_list :
				ladcol=pygame.sprite.spritecollideany(qw,ladder_list,collided = None)
				plcol=pygame.sprite.spritecollideany(qw,pl_list,collided = None)
				gorcol=pygame.sprite.groupcollide(gor_list,pl_list,False,False)
				"""if ladcol != None :
					r=random.randrange(0,2)
					print r
					if r == 1 :
						qw.state = 1
						qw.h += 20
						if qw.state == 1 :
							qw.rect.y += qw.h
							qw.h += 1
						if qw.h == 23 :
							qw.state = 0
							qw.h = 0
				else :	
				"""
				if plcol != None or len(gorcol) < 0 :
					turns -= 1
					if turns == 0 :
						font = pygame.font.Font(None, 72)
						text = font.render("GAME OVER ", 1, (10, 10, 10))
						disp.blit(text,(150,300))
						pygame.display.update()
						time.sleep(2)
						pygame.quit()
						sys.exit()
					main(turns,score)
				qw.move(pl_list,list_obj,fire_list)
			gor.move(500,20)
			ps.move(410,260)
			if mario.rect.x >= 260 and mario.rect.x <=400 and mario.rect.y >= 00 and mario.rect.y <= 30 :
				font = pygame.font.Font(None, 72)
				text = font.render("YOU WIN SCORE = "+ str(score), 1, (10, 10, 10))
				disp.blit(text,(150,300))
				pygame.display.update()
				time.sleep(2)
				pygame.quit()
				sys.exit()
			bgimg = pygame.image.load('background.png')
			#bgimg.rect = pygame.get_rect()
			disp.blit(bgimg,(0,0))
			disp.blit(text,(650,70))
			pl_list.draw(disp)
			coin_list.draw(disp)
			ladder_list.draw(disp)
			heart.draw(disp)
			gor_list.draw(disp)
			list_obj.draw(disp)
			fire_list.draw(disp)
			ps_list.draw(disp)
			pygame.display.update()
			clock.tick(20)
main(turns,score)
