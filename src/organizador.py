import os
import shutil

def organizar_arquivos_por_camera_e_view(pasta_base='dataset'):
    arquivos = os.listdir(pasta_base)

    for nome_arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta_base, nome_arquivo)

        if not os.path.isfile(caminho_arquivo):
            continue

        partes = nome_arquivo.split('_')
        if len(partes) < 2:
            continue

        view = partes[1]
        camera = 'Nuance_EX' if 'GDBICP' in nome_arquivo else 'Specim_IQ'

        # Caminho final: camera/view/
        pasta_destino = os.path.join(camera, view)
        os.makedirs(pasta_destino, exist_ok=True)

        novo_caminho = os.path.join(pasta_destino, nome_arquivo)
        shutil.copy2(caminho_arquivo, novo_caminho)
