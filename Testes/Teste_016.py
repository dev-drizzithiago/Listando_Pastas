from time import sleep
from progress.bar import Bar

from tqdm import tqdm

with Bar('Lendo...', max=100) as bar:
    for i in range(100):
        sleep(0.02)
        bar.start()
        bar.next()

for i in tqdm(range(101), desc='Lendo...', ascii=False, ncols=75):
    sleep(0.01)

print('completo..!')
