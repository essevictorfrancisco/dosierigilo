# DOSIERIGILO - Organize Media by Date

Este script Python organiza automaticamente fotos e vídeos em subpastas com base
no tipo de mídia (`pictures` ou `videos`) e na data de modificação do arquivo
(`YYYYMMDD`). Ideal para manter grandes coleções de mídia organizadas de forma
limpa e consistente.

---

## Funcionalidades

- Classifica fotos e vídeos em pastas separadas
- Cria subpastas por data de modificação (YYYYMMDD)
- Renomeia arquivos para snake_case ASCII (opcional)
- Evita sobrescrever arquivos duplicados
- Compatível com Windows, Linux e macOS
- Sem dependências externas (somente bibliotecas padrão)

## Exemplo de organização

**Antes:**
```
/midia/
├── IMG_2023-01-01 12-15-01.JPG
├── Vídeo Final - Edição.mp4
```

**Depois:**
```
/midia/
├── pictures/
│ └── 20230101/
│ └── img_2023_01_01_12_15_01.jpg
└── videos/
└── 20230101/
└── video_final_edicao.mp4
```

## 🚀 Como usar

1. Clone este repositório:

Execute o script:

```bash
python dosierigilo.py
```

Digite o caminho completo da pasta que contém os arquivos:

```bash
    Digite o caminho completo para pasta: /caminho/para/sua/pasta
```

### Configuração

No início do script, você pode ativar ou desativar a normalização dos nomes
dos arquivos com a variável activate_snakecase:

```bash
activate_snakecase = True  # Ativa a conversão para snake_case ASCII
```

### Requisitos

O script utiliza apenas bibliotecas da biblioteca padrão do Python 3.6 ou superior.
