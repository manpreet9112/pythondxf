from dxfwrite import DXFEngine as dxf

drawing = dxf.drawing('pythondxf.dxf')
#drawing.add_layer('CIRCLE2')
#drawing.add(dxf.circle((10), (10,5), layer='CIRCLE2'))
#drawing.add_layer('CIRCLE')
#drawing.add(dxf.circle((2), (5, 10), layer='CIRCLE'))
drawing.add_layer('RECT')
drawing.add(dxf.rectangle((5, 5) , 6, 6, bgcolor=5, layer='RECT'))
drawing.add_layer('POLY')
polyline= dxf.polyline(linetype='LINE')
polyline.add_vertices( [(7,9.5),(6,10), (10,10), (10,6), (6,6),(6,10)])
#polyline.add_vertices( [(6.5,10), (7,9.5)])
polyline.close(status=True)
drawing.add(polyline)
drawing.add_layer('CIRCLE')
drawing.add(dxf.circle((0.1), (6.5,9.5), layer='CIRCLE'))
drawing.add(dxf.circle((0.1), (9.5,9.5), layer='CIRCLE'))
drawing.add(dxf.circle((0.1), (6.5,6.5), layer='CIRCLE'))
drawing.add(dxf.circle((0.1), (9.5,6.5), layer='CIRCLE'))

drawing.save()