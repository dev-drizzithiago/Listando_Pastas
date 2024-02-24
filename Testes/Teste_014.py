import os
import random
import re


def contar_itens(pasta):
    subpastas = 0
    arquivos = 0

    for item in os.listdir(pasta):
        caminho_item = os.path.join(pasta, item)
        if os.path.isdir(caminho_item):
            subpastas += 1
        else:
            arquivos += 1

    return subpastas, arquivos


def gerar_relatorio(pasta):
    pasta_inicial = pasta

    html = "<html>\n<head>\n<title>Relatório de Pastas</title>\n"
    html += "<link rel='stylesheet' href='https://fonts.googleapis.com/icon?family=Material+Icons'>"
    html += "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'>"
    html += "</head>\n<body>\n"

    html += "<div class='container'>"
    html += modal

    for root, dirs, files in os.walk(pasta):
        for diretorio in dirs:
            caminho_diretorio = os.path.join(root, diretorio)
            subpastas, arquivos = contar_itens(caminho_diretorio)
            pasta_inicial_formatada = " - ".join(pasta_inicial.split(os.sep))
            caminho_formatado = " - ".join(caminho_diretorio.split(os.sep)).replace(pasta_inicial_formatada + " -", "")
            print("Caminho formatado: {}".format(caminho_formatado).encode('UTF-8'))

            if subpastas >= 30:
                html += "<div class='card blue-grey darken-1'>\n"
                html += "<div class='card-content white-text'>\n"
                html += "<span class='card-title'>{}</span>\n".format(caminho_formatado)
                html += "<p><small>{}</small></p>\n".format(caminho_diretorio).replace(user_path, '%userprofile%')
                html += "<ul>\n"
                html += "<li><i class='material-icons'>folder</i> Quantidade de subpastas: {}</li>\n".format(subpastas)
                html += "<li><i class='material-icons'>description</i> Quantidade de arquivos: {}</li>\n".format(
                    arquivos)
                html += "</ul>\n"
                html += "<a href='javascript:void(0);' onclick=\"copyToClipboard('{}')\"><i class='material-icons'>content_copy</i> Copiar Caminho</a>\n".format(
                    caminho_diretorio).replace(user_path, '%userprofile%').replace('\\', '\\\\')
                html += "</div>\n"
                html += "</div>\n"

    html += "</div>"
    html += "<script src='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js'></script>"
    html += "</body>\n</html>"
    html += js_copy_to_clipboard

    return html


js_copy_to_clipboard = """
<script>
function copyToClipboard(text) {
    var tempInput = document.createElement('input');
    tempInput.value = text;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    alert('Caminho copiado para o clipboard!');
}
</script>
"""

modal = """
<div id="modal" class="modal">
    <div class="modal-content">
        <h4>Atalho para visualização da pasta no explorer</h4>
        <p>
        Dentro do Explorer do Windows, você pode exibir o documento 
        referenciado em um relatório utilizando a opção 'Copiar Caminho'. 
        Com essa opção, você pode facilmente copiar o caminho do arquivo e, 
        em seguida, utilizar os atalhos Win + R e Ctrl + V para colar o caminho.
        </p>
    </div>
    <div class="modal-footer">
        <a href="#!" class="modal-close waves-effect waves-green btn-flat"><i class='material-icons'>close</i> Fechar</a>
    </div>
</div>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            var elems = document.querySelectorAll('.modal');
            var instances = M.Modal.init(elems);
            var modalInstance = M.Modal.getInstance(elems[0]);
            modalInstance.open();
        }, 0800);
    });
</script>
"""

user_path = os.getenv('USERPROFILE')
pasta_inicial = os.path.join(user_path, 'vBox', 'Team Shares',
                             'MKT - NOVA REDE BITTENCOURT')  # vBox/Team Shares/MKT - NOVA REDE BITTENCOURT
relatorio = gerar_relatorio(pasta_inicial)

nome_arquivo = "relatorio-{}.html".format(random.randrange(1, 999))
with open(nome_arquivo, "w", encoding="utf-8") as file:
    file.write(relatorio)

print("Relatório gerado com sucesso em {}".format(nome_arquivo))
