import random
from random import choice

def ReadFile(filename,method):
        with open(filename,method) as f:
            content = [line.strip('\n') for line in f]
            return content

def GetRandomUserAgent():
        useragents = ReadFile('modules/useragents.txt','r')
        return choice(useragents)
