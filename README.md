# IDEIAS EM REDE

Projeto de ciência de dados voltado à análise e à sumarização de textos em
língua portuguesa. O repositório usa o corpus [PublicHearingBR](https://huggingface.co/datasets/unicamp-dl/PublicHearingBR)
para explorar transcrições de audiências públicas, matérias jornalísticas e
exemplos de inferência em linguagem natural (NLI).

## Estrutura

- `src/ideias_em_rede/`: código reutilizável para configuração, download,
  carregamento e validação dos dados.
- `notebooks/01_publichearingbr_eda.ipynb`: análise exploratória do corpus LDS,
  com transcrições e matérias jornalísticas.
- `notebooks/02_publichearingbr_nli_eda.ipynb`: análise exploratória dos dados
  NLI e das verificações de possíveis alucinações.
- `data/raw/`: arquivos baixados durante a execução dos notebooks; não são
  versionados.
- `reports/figures/`: figuras e resultados gerados; não são versionados.
- `data/README.md`: descrição dos conjuntos de dados e de seus esquemas.
- `pyproject.toml`: metadados do pacote e dependências do projeto.

## Configuração do ambiente

O projeto requer Python 3.11 ou superior. Crie e ative um ambiente virtual e
instale o pacote em modo editável:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Para acessar o Hugging Face com taxas de download mais altas, basta copiar o arquivo de exemplo e preencher o token:

```bash
cp .env.example .env
```

O arquivo .env é local e não deve ser commitado. O token é opcional para
repositórios públicos, mas pode ser necessário para os limites de acesso do
Hugging Face.

## Execução

Inicie o Jupyter Lab a partir da raiz do repositório:

```bash
python -m jupyter lab
```

Execute os notebooks na ordem desejada. Na primeira execução, cada notebook
baixa automaticamente seu conjunto de dados para `data/raw/`:

- o notebook 01 baixa `PublicHearingBR_LDS.jsonl` (206 audiências);
- o notebook 02 baixa `PublicHearingBR_NLI.jsonl` (4.238 opiniões derivadas de
  206 audiências).

Os arquivos de dados e os artefatos gerados são ignorados pelo Git. Para mais
detalhes sobre organização e reprodução, consulte [`data/README.md`](data/README.md).
