from time import sleep
from progress.bar import Bar

with Bar('Lendo...', max=100) as bar:
    for i in range(100):
        sleep(0.02)
        bar.next()
