# IDEIAS EM REDE

Projeto de ciência de dados voltado à sumarização de textos em língua
portuguesa.

## Estrutura

- `src/ideias_em_rede/`: código reutilizável do projeto.
- `notebooks/`: análises exploratórias e experimentos documentados.
- `data/raw/`: dados originais do projeto.
- `reports/`: figuras e resultados gerados.

## Ambiente

Ative o ambiente virtual e instale o projeto com `pip`:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m jupyter lab
```

Caso ainda não exista um ambiente virtual local, crie-o antes da instalação:

```bash
python -m venv .venv
source .venv/bin/activate
```

Defina `HF_TOKEN` em `.env`. O notebook baixa somente o corpus LDS do
PublicHearingBR; os dados não são versionados. Consulte `data/README.md` para
as instruções de organização e reprodução.
