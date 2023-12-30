from pathlib import Path


home = Path.home()

pasta_busca = Path(home)

for listagem in pasta_busca.glob('**/*'):
    print(listagem)