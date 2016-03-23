columns = 70
rows = 26
blank = ""
for i in range(70):
	blank += " "
layout = [[" " for i in range(columns)] for i in range(rows)]
def AddWalls(layout,rows,columns):
	for i in range(5):
		for j in range(columns):
			if(i==0 or j==0 or i==(rows-1) or j == (columns-1)):
				layout[i][j]="X"
	for i in range(5,rows):
		for j in range(columns):
			if(i==0 or j==0 or i==(rows-1) or j == (columns-1)):
				layout[i][j]="X"
			if(i%5==0):
				layout[i][j]="X"
			
	return layout 

layout = AddWalls(layout,rows,columns)
for i in range(rows):
	for j in range(columns):
		print layout[i][j],
	print ""
# for i in layout:
# 	print i[0]
