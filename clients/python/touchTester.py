import os

from time import sleep



minX=100

maxX=850

minY=300

maxY=1450



x=minX

y=minY

cont=1



while(x<=maxX):

    y=minY

    while(y<=maxY):

        print(f"Touch number: {cont}")

        cont+=1

        print(f"touching {x},{y}")

        os.system(f"python3 client3.py --url http://127.0.0.1:8000 --light 'tap {x} {y}'")

        y+=50

    x+=50