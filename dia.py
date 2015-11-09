from dxfwrite import DXFEngine as dxf
from dxfwrite.dimlines import dimstyles,AngularDimension
import csv

dwg=dxf.drawing('dia.dxf')
def drawcount(data):
	for i in range(len(data)-1):
		c=tuple(data[i])
		d=tuple(data[i+1])
		if i<4:
			print 'hi', i
			dwg.add(dxf.line(c,d, color=7))

		else:
			print i
f=open('coords.csv')
data=[]
for row in csv.reader(f):
	data.append(row)
	drawcount(data)


for i in range(len(data)-1):
   a=tuple(data[i])
   b=tuple(data[i+1])
   if i in range (5,9):
       print data[i]
       dwg.add(dxf.line(a, b, color=7))

for i in range(len(data)-1):
   x=tuple(data[i])
   y=tuple(data[i+1])
   if i>9:
       print data[i]
       dwg.add(dxf.line(x, y, color=7))

#arrow added 
x1=0; y1=20; x2=0;y2=30
for i in range (0,81,8):
	print 'points',x1+i
	dwg.add(dxf.line((x1+i,y1),(x2+i,y2), color=5))

text=dxf.text('P(kN)', (35,40), height=4,rotation=2)
dwg.add(text)

dwg.save()
