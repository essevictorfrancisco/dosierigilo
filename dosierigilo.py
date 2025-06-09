# -*- coding: utf-8 -*-
"""
Organiza fotos e vídeos em pastas 'pictures' ou 'videos',
e dentro delas por data (formato YYYYMMDD), com opção de
normalizar nomes de arquivos em snake_case ASCII.

@author: vfpresesende
"""

import shutil
import re
import unicodedata
from pathlib import Path
from datetime import datetime

# Nome das pastas principais
IMG_FOLDER = 'pictures'
VID_FOLDER = 'videos'

# Ativa a conversão dos nomes dos arquivos para snake_case ASCII
activate_snakecase = True

# Mapeamento de extensões para tipos de mídia
MEDIA_EXTENSIONS = {
    '.jpg': IMG_FOLDER, '.jpeg': IMG_FOLDER, '.png': IMG_FOLDER,
    '.gif': IMG_FOLDER, '.bmp': IMG_FOLDER, '.heic': IMG_FOLDER,
    '.webm': IMG_FOLDER,
    '.mp4': VID_FOLDER, '.mov': VID_FOLDER, '.avi': VID_FOLDER,
    '.mkv': VID_FOLDER
}


def get_modification_date(path: Path) -> datetime:
    """
    Retorna a data de modificação do arquivo.
    """
    return datetime.fromtimestamp(path.stat().st_mtime)


def create_media_date_folder(base_dir: Path, media_type: str,
                             date: datetime) -> Path:
    """
    Cria (se necessário) a pasta 'pictures' ou 'videos' e,
    dentro dela, uma subpasta com o nome da data (YYYYMMDD).
    """
    main_folder = base_dir / media_type
    main_folder.mkdir(exist_ok=True)

    date_folder = main_folder / date.strftime('%Y%m%d')
    date_folder.mkdir(exist_ok=True)

    return date_folder


def sanitize_filename(filename: str) -> str:
    """
    Converte o nome do arquivo para lowercase, substitui espaços e '-' por '_',
    remove acentos e limita aos caracteres ASCII alfanuméricos, '.' e '_'.
    """
    name = filename.lower()
    name = re.sub(r'[ \-]+', '_', name)

    # Normaliza e remove acentos
    name = unicodedata.normalize('NFKD', name)
    name = name.encode('ascii', 'ignore').decode('ascii')

    # Remove caracteres indesejados
    name = re.sub(r'[^a-z0-9._]+', '', name)

    return name


def organize_media_files(source_dir: Path) -> None:
    """
    Organiza arquivos de mídia em 'pictures' ou 'videos',
    e dentro delas em pastas nomeadas com a data de modificação.
    """
    for item in source_dir.iterdir():
        if not item.is_file():
            continue

        ext = item.suffix.lower()
        if ext not in MEDIA_EXTENSIONS:
            continue

        creation_date = get_modification_date(item)
        media_type = MEDIA_EXTENSIONS[ext]

        target_folder = create_media_date_folder(source_dir,
                                                 media_type,
                                                 creation_date)

        # Nome base do arquivo
        new_name = item.name
        if activate_snakecase:
            new_name = sanitize_filename(item.name)

        target_path = target_folder / new_name

        # Evita sobrescrever arquivos com o mesmo nome
        if target_path.exists():
            timestamp = creation_date.strftime('%H%M%S')
            new_name = f"{timestamp}_{new_name}"
            target_path = target_folder / new_name

        shutil.move(str(item), str(target_path))
        print(f"Moved: {item.name} -> {target_path.relative_to(source_dir)}")


if __name__ == '__main__':
    print('Organiza fotos e vídeos em pastas por tipo e data.\n')

    while True:
        user_input = input('Digite o caminho completo para pasta: ').strip()

        try:
            source_path = Path(user_input).expanduser().resolve()
        except Exception as e:
            print(f'Erro ao processar o caminho: {e}')
            continue

        if not source_path.is_dir():
            print(f'Erro: "{source_path}" não é uma pasta válida.\n')
        else:
            organize_media_files(source_path)
            break
