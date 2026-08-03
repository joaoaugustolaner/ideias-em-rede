# Dados

Os dados do projeto ficam em:

- `raw/`: dados originais, sem alterações.

O notebook `notebooks/01_publichearingbr_eda.ipynb` baixa o arquivo
`PublicHearingBR_LDS.jsonl` para `raw/` a partir do repositório
`unicamp-dl/PublicHearingBR` no Hugging Face. Ele contém o corpus principal
para sumarização de documentos longos: 206 pares de transcrição de audiência
pública e matéria jornalística, com metadados estruturados.

O notebook `notebooks/02_publichearingbr_nli_eda.ipynb` baixa o arquivo
`PublicHearingBR_NLI.jsonl`. Ele contém exemplos de inferência em linguagem
natural derivados das audiências: uma opinião, quatro trechos de contexto e
anotações de verificabilidade. Os arquivos são baixados de forma independente
para evitar misturar esquemas distintos.

Os arquivos de dados não são versionados. O token de acesso deve ficar somente
na variável `HF_TOKEN` em `.env`.
