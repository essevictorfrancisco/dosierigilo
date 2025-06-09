# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 14:35:38 2025

@author: vfpresesende
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# Extensões consideradas como fotos e vídeos
MEDIA_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.heic',
    '.mp4', '.mov', '.avi', '.mkv', '.webm'
}


def get_creation_date(path: Path) -> datetime:
    """
    Retorna a data de criação do arquivo. Em sistemas Unix, pode usar
    a data de modificação como fallback.
    """
    try:
        timestamp = path.stat().st_ctime
    except AttributeError:
        timestamp = path.stat().st_mtime
    return datetime.fromtimestamp(timestamp)


def create_date_folder(base_dir: Path, date: datetime) -> Path:
    """
    Cria (caso não exista) e retorna o caminho da pasta no formato YYYYMMDD.
    """
    folder_name = date.strftime('%Y%m%d')
    target_dir = base_dir / folder_name
    target_dir.mkdir(exist_ok=True)
    return target_dir


def organize_media_files(source_dir: Path) -> None:
    """
    Organiza arquivos de mídia em pastas nomeadas com a data de criação.
    """
    for item in source_dir.iterdir():
        if not item.is_file():
            continue

        if item.suffix.lower() not in MEDIA_EXTENSIONS:
            continue

        creation_date = get_creation_date(item)
        target_folder = create_date_folder(source_dir, creation_date)
        target_path = target_folder / item.name

        # Evita sobrescrever arquivos com o mesmo nome
        if target_path.exists():
            new_name = f"{creation_date.strftime('%H%M%S')}_{item.name}"
            target_path = target_folder / new_name

        shutil.move(str(item), str(target_path))
        print(f"Moved: {item.name} -> {target_path.relative_to(source_dir)}")


if __name__ == '__main__':
    print('Organiza fotos e vídeos em pastas por data de criação.\n')
    print('Caminho da pasta com os arquivos a organizar')
    
    is_dir = False

    while not is_dir:
        source_path = input('digite aqui: ')

    if not source_path.is_dir():
        print(f'Erro: {source_path} não é uma pasta válida.')
    else:
        organize_media_files(source_path)
        is_dir = True
