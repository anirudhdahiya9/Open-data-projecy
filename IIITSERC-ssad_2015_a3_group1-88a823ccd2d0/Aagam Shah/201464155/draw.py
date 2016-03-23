import pygame
import settings
import objects
import groups

settings.init()
def blitndraw():
	dheight=700
	dwidth=1000
	settings.gamedisplay.fill(settings.white)
	settings.gamedisplay.blit(settings.princessimg, (1.2*objects.B.w+10,settings.princess))
	settings.gamedisplay.blit(settings.cageimg, (1.2*objects.B.w,settings.cage))
	objects.B.brick(0,dheight*0.80)
	objects.B.brick(objects.B.w,dheight*0.80)
	objects.B.brick(2*objects.B.w,dheight*0.80)
	objects.B.brick(3*objects.B.w,dheight*0.80)
	objects.B.brick(0,dheight*0.60)
	objects.B.brick(2*objects.B.w-200,dheight*0.60)
	objects.B.brick(3*objects.B.w-230,dheight*0.60)
	objects.B.brick(0,dheight*0.40)
	objects.B.brick(objects.B.w,dheight*0.40)
	objects.B.brick(3*objects.B.w-175,dheight*0.40)
	objects.B.brick(0,objects.D.height+80)
	objects.B.brick(objects.B.w,objects.D.height+80)
	objects.B.brick(2*objects.B.w,objects.D.height+80)

	groups.block_list.draw(settings.gamedisplay)
	objects.L1.l(objects.L1.rect.x,objects.L1.rect.y)
	objects.L2.l(objects.L2.rect.x,objects.L2.rect.y)
	objects.L3.l(objects.L3.rect.x,objects.L3.rect.y)
	objects.L4.l(objects.L4.rect.x,objects.L4.rect.y)

	for bl in settings.ball:
		bl.fire(bl.rect.x,bl.rect.y)

	objects.D.villain(objects.D.rect.x,objects.D.rect.y)
	objects.A.hero(objects.A.rect.x,objects.A.rect.y)
	myfont = pygame.font.SysFont("monospace",30,True)
	label = myfont.render("Score: "+ str(settings.score), True, (0,0,0))
	settings.gamedisplay.blit(label, (dwidth-250,7))
	myfont2 = pygame.font.SysFont("monospace",30,True)
	label2 = myfont2.render("Lives: "+ str(settings.lives), True, (0,0,0))
	settings.gamedisplay.blit(label2, (dwidth-250,30))
	pygame.display.update()
	settings.clock.tick(120)
