import random
import math

sampleMax = 10000000
insideSamples = 0
sampleCount = 0
samples = []
avg = 0

def Average(list):
    return sum(list) / len(list)

def sampleDistance(x,y):
    return(math.sqrt((x - 0)**2 + (y - 0)**2))

while(avg < 10):
    insideSamples = 0
    sampleCount = 0
    random.seed()
    while(sampleCount < sampleMax): 
        rx = random.random()
        ry = random.random()
        dist = sampleDistance(rx,ry)
        if(dist <= 1):
            insideSamples = insideSamples + 1
        sampleCount = sampleCount + 1

    print(insideSamples/sampleMax*100 , "% of points are inside")
    pi = insideSamples/sampleMax*4
    print("this might say pi:", pi)
    samples.append(pi)
    avg = avg + 1
answer = Average(samples)
print(answer)
print(answer - math.pi)

input("Press enter to quit")