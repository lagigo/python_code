import easygui

fo = ['Aoi sora:6000','Trump:10','English Tsui:-20000']

dr = ['soda:200','soodaa:2000','ssooddaa:20000']

food = easygui.choicebox('What you eat?',choices = fo)
foo = str(food.split(':')[0])
foamount = int(easygui.enterbox(foo +'數量'))

drink = easygui.choicebox('What you drink?',choices = dr)
drr = str(drink.split(':')[0])
dramount = int(easygui.enterbox(drr +'數量'))

foprice = int(food.split(':')[1])
drprice = int(drink.split(':')[1])
totalfo = str(foprice*foamount)
totaldr = str(drprice*dramount)

total = str(foprice*foamount + drprice*dramount) 

easygui.msgbox(foo + totalfo + '元'+'\n'+drr + totaldr + '元''\n'+'總共'+ total + '元')


