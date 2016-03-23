score=0
lives=3

import random
color1=(random.randrange(180,250),random.randrange(0,250),random.randrange(0,250))
color2=(random.randrange(170,250),random.randrange(0,250),random.randrange(0,250))

color4=(random.randrange(170,250),random.randrange(0,250),random.randrange(170,250))
color3=(random.randrange(0,250),random.randrange(170,250),random.randrange(170,250))
import pygame
import sys
white=(255,255,255)
yellow=(255,255,0)
fire=(226,88,34)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
orange=(255,153,0)
brown=(204,51,51)

class Person:
    def __init__(self,xpos,ypos,block_size,color):
        self.lead_x=xpos
        self.lead_y=ypos
        self.lead_x_change=0
        self.lead_y_change=0
        self.block_size=block_size
        self.color=color
        self.dir=1
        self.v1=1.5
        self.a1=0.6
        self.fallfloor=1
        self.fall_or_ladder=0
        self.fallin=0
    def getChange(self,xchange,ychange):
        self.lead_x_change=xchange
        self.lead_y_change=ychange
    def getPosition(self):
        self.lead_x+=self.lead_x_change
        self.lead_y+=self.lead_y_change
    def drawplayer(self,screen):
        pygame.draw.rect(screen,self.color,pygame.Rect( self.lead_x,self.lead_y,self.block_size,self.block_size))
class Player(Person):
    def __init__(self,xpos,ypos,life):
	size=10
        Person.__init__(self,xpos,ypos-size,size,color4)
        self.vx=3
        self.jump_vy=10
        self.jump_vx=4
        self.jump_a=1
        self.life=life
class Donkey(Person):
    def __init__(self,xpos,ypos):
        size=15
        Person.__init__(self,xpos,ypos-size,size,yellow)
        self.mov=1
        self.v_donk=5
class FireBall(Person):
    def __init__(self,xpos,ypos):
        size=13
        Person.__init__(self,xpos,ypos-size,size,red)
        self.no=0    
        self.when=300
        self.random_val=1
        self.dead=0 
        self.floor=0
        self.fallfloor=0
class Queen(Person):
    def __init__(self,xpos,ypos):
        size=20
        Person.__init__(self,xpos,ypos-size,size,green)
class Coins:
    def __init__(self,width,height,screen,temp):
        self.block_size=10
        self.randcoinx=[]
        self.randcoiny=[]
        self.start=1
        self.temp=temp#=makegrid(width,height,screen)
        self.createCoins(20,width)
    def createCoins(self,amt,width):
        inc=[]
        j=0
	i=1
        j=1
        while i<amt+1:
            if(j==self.temp.number-2):
                j=1

            start=self.temp.pos_sx[j]
            end=self.temp.pos_ex[j]-self.block_size
            x=(round(random.randrange(start,end)/10.0)*10.0)
            if x not in self.randcoinx:
                self.randcoinx.append(x)
                self.randcoiny.append(self.temp.pos_y[j]-self.block_size)
                i+=1
                j+=1
    def printcoins(self,screen):
        i=self.start
        while i<len(self.randcoinx)-1:
            pygame.draw.rect(screen,orange,pygame.Rect(self.randcoinx[i],self.randcoiny[i],self.block_size,self.block_size))
            i+=1
    def swallowcoins(self,x,y,size,screen):
        global score
        global color1
        global color2
        i=0
        while i<len(self.randcoinx):

            X1=x
            W2=self.block_size
            H2=W2
            X2=self.randcoinx[i]
            Y1=y
            Y2=self.randcoiny[i]
            H1=size
            W1=H1
    #        return 
            if(X1+W1<X2 or X2+W2<X1 or Y1+H1<Y2 or Y2+H2<Y1):
                pass
            else:
                    
                    color1=(random.randrange(180,250),random.randrange(0,250),random.randrange(0,250))
                    color2=(random.randrange(170,250),random.randrange(0,250),random.randrange(0,250))
                    
                    color3=(random.randrange(210,250),random.randrange(0,250),random.randrange(0,250))
                    screen.fill(black,rect=[X2,Y2,self.block_size,self.block_size])
                    del self.randcoinx[i]
                    del self.randcoiny[i]
                  #  self.randcoinx[self.start],self.randcoinx[i]=self.randcoinx[i],self.randcoinx[self.start]
                  #  self.randcoiny[self.start],self.randcoiny[i]=self.randcoiny[i],self.randcoiny[self.start]
                  #  self.start+=1
                    score+=5
                   # msg("Score is")
                    break
  #      print 1
            i+=1

class makegrid():
    def __init__(self,width,height,screen):
        
        self.ladder_color=color3
        self.rect_color=(204,204,51)
        self.border_h=40
        self.middle_h=10
        self.middle_w=(3*width)/4
        self.number=random.randrange(6,12)
        self.number-=1
        self.pos_y=[int]*(self.number+1)
        self.pos_sx=[int]*(self.number+1)
        self.pos_ex=[int]*(self.number+1)
        self.ladder_h=[int]*(self.number+1)
        self.ladder_sx=[int]*(self.number+1)
        self.ladder_ex=[int]*(self.number+1)
        gap=int((height-2*self.border_h-(self.number-2)*self.middle_h)/(self.number-1))
        self.pos_y[0]=0
        self.pos_y[2]=int((1.6)*gap)+self.border_h
        self.pos_y[1]=int(self.pos_y[2]/2)#120-self.middle_h
        for i in range(3,self.number-1):
            self.pos_y[i]=self.pos_y[i-1]+gap+self.middle_h
        self.pos_y[self.number-1]=height-self.border_h
        i=0
        const_queen=50
        self.pos_sx[0]=self.border_h
        self.pos_ex[0]=width-self.border_h
        self.pos_sx[1]=(width/2)#for queen
        self.pos_ex[1]=self.pos_sx[1]+int((self.middle_w)/2)
        x=[2,3]
        v=random.randrange(0,2)
	for i in range(x[v],self.number-1,2):
                self.pos_sx[i]=self.border_h
                self.pos_ex[i]=self.pos_sx[i]+self.middle_w
        for i in range(x[1-v],self.number-1,2):

                self.pos_sx[i]=width-self.middle_w
                self.pos_ex[i]=width-self.border_h
        self.pos_sx[self.number-1]=self.border_h
        self.pos_ex[self.number-1]=width-self.border_h
        self.ladder_w=25
        v1_rand=random.randrange(1,5)
        v2_rand=random.randrange(v1_rand,4*v1_rand)
        start=max(self.pos_sx[1],self.pos_sx[2])
        end=min(self.pos_ex[1],self.pos_ex[2])-self.ladder_w
        self.ladder_sx[1]=int(((end-start)*(v1_rand))/(v2_rand)) +start #+const1_ladder/2
        self.ladder_ex[1]=self.ladder_sx[1]+self.ladder_w
        i=3
        while i<self.number-1:
            v1_rand=random.randrange(1,5)
            v2_rand=random.randrange(v1_rand,4*v1_rand)
            start=max(self.pos_sx[i],self.pos_sx[i+1])
            end=min(self.pos_ex[i],self.pos_ex[i+1])-self.ladder_w
            self.ladder_sx[i]=int(((end-start)*(v1_rand))/(v2_rand)) +start #+const1_ladder/2
            self.ladder_ex[i]=self.ladder_sx[i]+self.ladder_w
            i+=2
        i=2
        while i<self.number-1:
            v1_rand=random.randrange(1,5)
            v2_rand=random.randrange(v1_rand,4*v1_rand)
            start=max(self.pos_sx[i],self.pos_sx[i+1])
            end=min(self.pos_ex[i],self.pos_ex[i+1])-self.ladder_w
            self.ladder_sx[i]=int(((end-start)*(v1_rand))/(v2_rand)) +start
            self.ladder_ex[i]=self.ladder_sx[i]+self.ladder_w
            i+=2
        for i in range(2,self.number):
            self.ladder_h[i-1]=(self.pos_y[i] - self.pos_y[i-1])
    def makeladder(self,screen):
            for  i in range(1,self.number-1):
                pygame.draw.rect(screen,color3,pygame.Rect(self.ladder_sx[i],self.pos_y[i]+self.middle_h,self.ladder_w,self.ladder_h[i]-self.middle_h))
    def drawgrid(self,screen,width,height):
        global score
        pygame.draw.rect(screen,color1,pygame.Rect(self.pos_sx[1],self.pos_y[1],(self.middle_w/2),self.middle_h))
        for i in range(2,self.number-1):
            pygame.draw.rect(screen,color1,pygame.Rect(self.pos_sx[i],self.pos_y[i],self.middle_w,self.middle_h))
            self.makeladder(screen)
  #      print 1

        pygame.draw.rect(screen,color2,pygame.Rect(0,0,width,self.border_h))
        self.msg("Score is :"+str(score)+"     " +"Lives : " +str(lives),screen,width)
        pygame.draw.rect(screen,color2,pygame.Rect(0,0,self.border_h,height))
        pygame.draw.rect(screen,color2,pygame.Rect(0,height-self.border_h,width,self.border_h))
        pygame.draw.rect(screen,color2,pygame.Rect(width-self.border_h,0,self.border_h,height))

    def msg(self,mesg,screen,width):
        global red
        size=25
        clr=red
        font = pygame.font.Font("freesansbold.ttf",size)
        text = font.render(mesg,True,clr)
        screen.blit(text,(int((width*3)/8),10))
class Board(Coins,Player,makegrid):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.initpygame()
        self.makescreen()
        self.Grid=makegrid(self.width,self.height,self.screen)
        self.Grid.drawgrid(self.screen,self.width,self.height)
        self.User=Player(self.Grid.border_h+20,self.height-self.Grid.border_h,3)
        self.Coin=Coins(self.width,self.height,self.screen,self.Grid)
        self.donk=Donkey(self.Grid.pos_sx[2]+20,self.Grid.pos_y[2])
        self.Ball=[]
        self.queen=Queen(int(self.Grid.pos_sx[1]+self.Grid.pos_ex[1])/2,self.Grid.pos_y[1])
        self.tempball=FireBall(0,0)
        self.play()
    

    def CheckWall(self,temp,val):
        if temp.lead_x>=(self.width-temp.block_size-self.Grid.border_h):
                temp.lead_x=(self.width-temp.block_size-self.Grid.border_h)
                return -val
        elif(temp.lead_x<=self.Grid.border_h):
                temp.lead_x=self.Grid.border_h
                return -val
        if temp.lead_y>(self.height-temp.block_size-self.Grid.border_h):
            temp.lead_y=self.height-temp.block_size-self.Grid.border_h
        elif(temp.lead_y<self.Grid.border_h):
            temp.lead_y=self.Grid.border_h
        return val
    def checkfloor(self,temp,val):
        for i in range(1,self.Grid.number):
                
            if(temp.lead_y==self.Grid.pos_y[i]-temp.block_size  and temp.lead_x<=self.Grid.pos_ex[i]-temp.block_size-val and
            temp.lead_x>=self.Grid.pos_sx[i]+val):
                
                return i
        return 0
    def checkladder(self,temp):
        for i in range(2,self.Grid.number):
            if(temp.lead_y<=self.Grid.pos_y[i]-temp.block_size and temp.lead_x>=self.Grid.ladder_sx[i-1] 
                and temp.lead_x<=self.Grid.ladder_ex[i-1]-temp.block_size
                and temp.lead_y>=self.Grid.pos_y[i-1]-temp.block_size):
                return i-1
        return 0
    def onfloor_1(self,temp):
        for i in range(1,self.Grid.number):
            if(temp.lead_y<self.Grid.pos_y[i]-temp.block_size):
                temp.lead_y=self.Grid.pos_y[i]-temp.block_size
                break
    
    def onfloor_2(self,temp):
        for i in range(self.Grid.number-1,0,-1):
            if(temp.lead_y>self.Grid.pos_y[i]-temp.block_size):
                temp.lead_y=self.Grid.pos_y[i]-temp.block_size
                break
        
    def fall(self,temp,a_inc,v_inc,x_inc):
        if(temp.fallin==0):
            
                
            temp.dir=1
            floor=0

            for i in range(1,self.Grid.number):
                if((temp.lead_x<self.Grid.pos_sx[i] or temp.lead_x>self.Grid.pos_ex[i]-temp.block_size )

                #-temp.block_size) 
                        and temp.lead_y==self.Grid.pos_y[i]-temp.block_size):
                
                    print "woah"
                    temp.fallin=1
                    temp.fall_or_ladder=0
                   # if(i==1 and  temp.lead_x >self.Grid.pos_ex[1]-temp.block_size):
                    #    temp.fallfloor=i+2
                    
                    #else:  
                    temp.fallfloor=i+1
                    print "floor is" 
                 #   print temp.fallfloor

                    if temp.lead_x<self.Grid.pos_sx[i]:
                        temp.dir=-1
                    

                        self.getChange(3*temp.dir,0)#temp.lead_x+=x_inc*temp.dir
                    
                    break
        if(temp.fallin==1):
            temp.lead_y+=v_inc*temp.v1
            temp.lead_x+=x_inc*temp.dir
            temp.v1+=a_inc*temp.a1
            #print floor
            flag=0
            if((temp.lead_x<self.Grid.pos_sx[temp.fallfloor] or temp.lead_x>self.Grid.pos_ex[temp.fallfloor]) and flag==0):
                

                temp.fallfloor+=1
                flag=1
            print temp.fallfloor
            if(temp.lead_y>=self.Grid.pos_y[temp.fallfloor]-temp.block_size):
                temp.lead_y=self.Grid.pos_y[temp.fallfloor]-temp.block_size
                temp.v1=2
                temp.fallin=0
                print "brea"
    def setclock(self):
        clock=pygame.time.Clock()
    def setFPS(self,val):
        clock=pygame.time.Clock()
        FPS=val
        clock.tick(FPS)
    def initpygame(self):  
        pygame.init()
    def checkdonk(self):
        if(self.checkfloor(self.donk,20)!=0 and self.donk.mov==1):
                self.donk.getChange(self.donk.v_donk,0)
                self.donk.getPosition()
        elif(self.checkfloor(self.donk,20)==0 and self.donk.mov==1):
                self.donk.getChange(-self.donk.v_donk*2,0)
                self.donk.getPosition()
                self.donk.mov=-1
        elif(self.checkfloor(self.donk,20)!=0 and self.donk.mov==-1):
                self.donk.getChange(-self.donk.v_donk,0)
                self.donk.getPosition()
        elif(self.checkfloor(self.donk,20)==0 and self.donk.mov==-1):
                self.donk.getChange(2*self.donk.v_donk,0)
                self.donk.getPosition()
                self.donk.mov=1
    def makescreen(self):
        self.screen=pygame.display.set_mode((self.width,self.height))
    def prnt(self):
        pygame.display.update()
        pygame.display.set_caption("Donkey Kong")
    def findfloor(self):
        if((self.checkladder(self.User)!=0) and self.checkfloor(self.User,0)!=self.checkladder(self.User)):
            self.User.jump_vy=0
            floor=self.checkladder(self.User)+1
        elif(self.checkfloor(self.User,0)!=0):
            floor=self.checkfloor(self.User,0)
        return floor
    def jump_h(self,sign):
        self.jumping(sign)
    def jumping(self,sign):  
        flag=0
        bf=0
        floor=self.findfloor()
        if(self.User.jump_vy==0):
            self.User.lead_x+=3*self.User.jump_vx*sign
        #print floor
        while(bf!=1):
            flag=0
            self.User.lead_y-=self.User.jump_vy
            self.User.jump_vy-=self.User.jump_a
            self.User.lead_x+=self.User.jump_vx*sign
            self.CheckWall(self.User,0)
            if((self.User.lead_x<self.Grid.pos_sx[floor] or self.User.lead_x>self.Grid.pos_ex[floor]) and flag==0):

                floor+=1
                flag=1
            if(self.checkladder(self.User)!=0):
                bf=1
                self.User.jump_vy=0
            #print self.User.lead_y
            if(self.User.lead_y>=self.Grid.pos_y[floor]-self.User.block_size):
                self.User.lead_y=self.Grid.pos_y[floor]-self.User.block_size
                bf=1   
                self.User.jump_vy=10
            self.screen.fill((0,0,0))
            self.Grid.drawgrid(self.screen,self.width,self.height)
            self.makeplay()
            self.prnt()
            self.setFPS(50)
    def jump(self):
        if( self.checkladder(self.User)!=0 and self.checkfloor(self.User,0)==0):
            return
        flag=0
        #print "yes"
        self.jumping(0)
    def movfireball(self):

        ar=[1,-1]
        length=len(self.Ball)
        cnt=0
        j=0
        k=[]
        floor=0
        while cnt<length:
 

                if( self.checkladder(self.Ball[cnt])!=0 and self.checkfloor(self.Ball[cnt],0)!=0 and 
                    self.checkladder(self.Ball[cnt])==self.checkfloor(self.Ball[cnt],0)):
                    
                    self.Ball[cnt].fall_or_ladder=1
                    #print "yes"
                    self.Ball[cnt].floor=self.checkfloor(self.Ball[cnt],0)     
                    #print("floor is %d and ladder is %d" %(self.checkfloor(self.Ball[cnt],0),self.checkladder(self.Ball[cnt])))
                  #  print "floor is "
                  #  print floor
                    
                    v=random.randrange(0,2)
                   # ind=random.randint(0,1)
                   # self.Ball[cnt].random_val=ar[ind]
                    if(v==0):
                        self.Ball[cnt].getChange(0,5)
                    else:

                       # if(self.Ball[cnt].floor!=1):
                        self.Ball[cnt].getChange(4*self.Ball[cnt].random_val,0)
                            
                
                elif( self.checkfloor(self.Ball[cnt],0)!=0):
                    #print "what the fuck"
                    
                    self.Ball[cnt].getChange(4*self.Ball[cnt].random_val,0)
                elif(self.checkladder(self.Ball[cnt])!=0):
                    self.Ball[cnt].getChange(0,5)

                   # v=random.randint(0,1)
                    ind=random.randint(0,1)
                    self.Ball[cnt].random_val=ar[ind]
                    #print "chutiya"
                    
       

                self.Ball[cnt].getPosition()
                if(self.Ball[cnt].fall_or_ladder==1):

                   # print("floor is %d and ladder is %d" %(self.checkfloor(self.Ball[cnt],0),self.checkladder(self.Ball[cnt])))
                #    print "floor is"
                 #   print floor

                    if(self.Ball[cnt].lead_y>self.Grid.pos_y[self.Ball[cnt].floor+1]-self.Ball[cnt].block_size):

                        self.Ball[cnt].lead_y=self.Grid.pos_y[self.Ball[cnt].floor+1]-self.Ball[cnt].block_size
                    #    print "man"
                        self.Ball[cnt].fall_or_ladder=0
                self.Ball[cnt].random_val=self.CheckWall(self.Ball[cnt],self.Ball[cnt].random_val)
                self.fall(self.Ball[cnt],1,1.1,0.8)
                if (self.Ball[cnt].lead_x==self.Grid.border_h and
                        self.Ball[cnt].lead_y==self.height-self.Ball[cnt].block_size-self.Grid.border_h):

                    self.tempball.dead+=1
                    k.append(cnt)
                cnt+=1
        for i in k:
            del self.Ball[i]
            
    def play(self):
        gameExit=False
        self.setclock()
        self.prnt()
        print "A"
        check="none"
        while not gameExit:
            if(self.User.fallin==0):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:#event type can be any event like keypress mouse movement screen active or not and quit etc.
                        pygame.quit()
                        quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN: #key is pressed,#only change is an event continous doesnt work
                        if event.key== pygame.K_a:#left arrow is pressed
                            if(check=="space"):
                                self.jump_h(-1)
                            check="left"
                        elif event.key ==pygame.K_d:
                            if(check=="space"):
                                self.jump_h(1)
                            check="right"
                        elif event.key== pygame.K_w:#left arrow is pressed
                            check="up"
                        elif event.key ==pygame.K_q :
                            pygame.quit()
                            quit
                        elif event.key==pygame.K_s:
                            check="down"
                        elif event.key==pygame.K_SPACE:
                            if(check=="right"):
                               self.jump_h(1)
                            elif(check=="left"):
                               self.jump_h(-1)
                            else:
                                self.jump()
                            check="space"
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a or event.key==pygame.K_d:#to stop when we release the arrow key
                            check="none"
                        if event.key ==pygame.K_w or event.key==pygame.K_s:
                            check="none"
                        if event.key==pygame.K_SPACE:
                            check="none"
            if self.User.fallin!=0:
                check="none"
            if(check=="left"):
                if(self.checkfloor(self.User,0)!=0):  
                    self.User.getChange(-self.User.block_size,0)
                else:
                    self.User.getChange(0,0)
            elif(check=="right"):
                if(self.checkfloor(self.User,0)!=0): 
                    self.User.getChange(self.User.block_size,0)
                else:
                    self.User.getChange(0,0)
            elif(check=="down"):
                if(self.checkladder(self.User)!=0 and( self.checkladder(self.User)-self.checkfloor(self.User,0)!=-1)): 
                    self.User.getChange(0,self.User.block_size)
                else:
                    self.User.getChange(0,0)
            elif(check=="up"):
                if(self.checkladder(self.User)!=0 and self.checkfloor(self.User,0) !=self.checkladder(self.User)):
                    self.User.getChange(0,-self.User.block_size)
                else:
                    self.User.getChange(0,0)
            else:
                self.User.getChange(0,0)

            self.User.getPosition()
            
            if(self.checkladder(self.User)==0 and self.checkfloor(self.User,0)==0 and check=="up"):

                self.onfloor_1(self.User)
            elif(self.checkladder(self.User)==0 and check=="down" and self.checkfloor(self.User,0)==0):

                self.onfloor_2(self.User)
            
            self.CheckWall(self.User,0)
            self.fall(self.User,1,1.3,1.1)
            self.screen.fill((0,0,0))
            self.Grid.drawgrid(self.screen,self.width,self.height)     
            if (self.User.lead_x==0 and self.User.lead_y==0):
    
                gameExit=True
            else:
                self.makeplay()
                self.prnt()
                self.setFPS(50)
    def checkcollision(self,temp,flag):
            global lives
            global score
            X1=self.User.lead_x
            W2=temp.block_size
            H2=W2
            X2=temp.lead_x
            Y1=self.User.lead_y
            Y2=temp.lead_y
            H1=self.User.block_size
            W1=H1
    #        return 
            if(X1+W1<X2 or X2+W2<X1 or Y1+H1<Y2 or Y2+H2<Y1):
                return
    #        self.User.life-=1
            if(flag==0): 
                if(lives==1 ):
                    self.msg("GameOver",self.screen,self.width)
                    pygame.quit()
                    quit()
                else:
    
                    lives-=1
                    score-=25
            else:
                score+=25
                main()
            self.User.color=(0,0,0)
            self.User.drawplayer(self.screen)
            self.User=Player(self.Grid.border_h+20,self.height-self.Grid.border_h,self.User.life-1)
            self.User.drawplayer(self.screen)
    def makeplay(self):
        self.User.drawplayer(self.screen)
        self.queen.drawplayer(self.screen)
        self.checkdonk()
        self.donk.drawplayer(self.screen)
        if((self.tempball.when)%300==0):
            self.Ball.append(FireBall(self.donk.lead_x,self.Grid.pos_y[2]))
        self.tempball.when=(self.tempball.when+1)%300
        self.movfireball()
        cnt=0
        length=len(self.Ball)
        for i in range(0,length):
            self.checkcollision(self.Ball[i],0)
            self.Ball[i].drawplayer(self.screen)
        
        self.checkcollision(self.donk,0)
        self.checkcollision(self.queen,1)
        self.Coin.printcoins(self.screen)
        self.Coin.swallowcoins(self.User.lead_x,self.User.lead_y,self.User.block_size,self.screen)
def reset():

    global red
    size=25
    clr=red
    mesg="Do you want to continue press Y/Q"

    font = pygame.font.Font("freesansbold.ttf",size)
    text = font.render(mesg,True,clr)
    
def main():
    gameover=False
    while not gameover:
        a=Board(840,640)
        del a
    pygame.quit()#uninitialize everything
    quit()#quits python
if __name__ == "__main__":
    main()


