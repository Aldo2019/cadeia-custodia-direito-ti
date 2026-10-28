# Protocolo verificável de cadeia de custódia para evidência digital 

Material suplementar do artigo **"Cadeia de custódia da evidência digital: protocolo verificável da requisição pericial à defesa"**, submetido à revista *Direito & TI*.

Este repositório permite que qualquer pessoa **confira de forma independente** o registro de custódia encadeado e o manifesto de hashes do caso apresentado na Seção 6 do artigo, sem acesso à evidência original.

## Conteúdo

| Arquivo | Descrição |
|---|---|
| `verifica_cadeia.py` | Script de verificação do registro de custódia encadeado e dos hashes dos arquivos referenciados |
| `registro_custodia_encadeado.json` | Registro anonimizado dos 8 eventos de custódia do caso (e₀ a e₇) |
| `manifesto_hashes.csv` | Hashes SHA-256 da evidência e dos artefatos derivados (Quadro 5 do artigo) |
| `metadados_ffprobe.json` | Metadados técnicos extraídos com ffprobe 7.1 na reconstrução (Fase 3) |

**Não estão incluídos:** o arquivo de áudio examinado, o laudo pericial e quaisquer dados que identifiquem pessoas, unidades ou o procedimento. São materiais sigilosos, protegidos pela LGPD (Lei nº 13.709/2018).

## O registro de custódia encadeado

Cada evento de custódia eᵢ (fase, data e hora relativas, ação, responsável anonimizado, arquivos envolvidos e seus SHA-256, procedência do registro) é serializado em **JSON canônico**: chaves em ordem alfabética, UTF-8, sem espaços, `separators=(',', ':')`. Os hashes são encadeados assim:

```
h₀ = SHA-256( σ(e₀) )
hᵢ = SHA-256( σ(eᵢ) ‖ hex(hᵢ₋₁) ),   i ≥ 1
```

em que σ é a serialização canônica e ‖ é a concatenação de bytes UTF-8.

Alterar qualquer entrada anterior muda todos os valores seguintes. Basta, portanto, conferir o último valor, consignado no artigo, para verificar todo o registro:

```
h₇ = 8dea9521f869521976111eae7bce5784f4798365ea285f58c7e923e271eb5215
```

## Como verificar

Requisitos: Python 3.8 ou superior, apenas com a biblioteca padrão.

```bash
python verifica_cadeia.py registro_custodia_encadeado.json
```

O script:
1. recalcula a serialização canônica de cada evento;
2. recalcula h₀ a h₇ e os compara com os valores registrados;
3. confere se cada evento aponta para o hash correto do evento anterior;
4. recalcula o SHA-256 dos arquivos referenciados que estiverem presentes no disco.

Como a evidência e os artefatos sigilosos não são publicados, os arquivos ausentes aparecem como `[ARQUIVO AUSENTE]`. Isso é esperado e não indica falha. A verificação do encadeamento (passos 1 a 3) não depende desses arquivos.

Para conferir o artefato publicado:

```bash
sha256sum metadados_ffprobe.json
# esperado: 732a3b370dac54d99ec5cf2724e1ff044e6ba01cc7f1f2ef1e4717046369b746
```

No Windows (PowerShell): `Get-FileHash metadados_ffprobe.json -Algorithm SHA256`.

## O que esta verificação demonstra e o que não demonstra

**Demonstra:**
- que o registro publicado não foi alterado depois de sua geração;
- que os eventos estão na ordem e com o conteúdo declarados;
- que os artefatos publicados são os mesmos descritos no artigo.

**Não demonstra:**
- **a integridade da evidência antes do recebimento pelo laboratório.** O caso se enquadra no ramo C do protocolo: não havia hash de origem;
- **que os registros da época da perícia não foram alterados antes da reconstrução.** O encadeamento foi construído **retrospectivamente** (D0 + 184 dias) a partir de registros originais (D0 + 163 dias). Só um encadeamento mantido durante a própria perícia daria essa garantia;
- **a autenticidade do conteúdo** do áudio nem a autoria da gravação. O hash atesta que os bits são os mesmos, não o que eles representam.

Cada evento traz o campo de procedência (`registro original` ou `reconstruído`), que separa o que foi documentado na época do que foi calculado para a pesquisa.

## Anonimização

- Pessoas, unidades, órgãos e procedimento foram substituídos por rótulos (`CASO-01`, `PERITO-01`, `LAB-FORENSE-01` etc.).
- As datas foram convertidas em intervalos relativos a um marco D0.
- O nome original do arquivo foi substituído por `EVIDENCIA_01.mp3`.
- A tabela de correspondência é mantida apenas localmente pelos autores e não faz parte deste repositório.

### Entendendo a Escala Temporal Relativa ($D_0$) e a Constante de 163 Dias

Para proteger o sigilo do processo original sem perder o rigor cronológico da perícia, todas as datas reais do caso foram convertidas em uma **escala de tempo relativa**, tendo como ponto de partida o marco **$D_0$**. 

Ao longo dos documentos deste repositório, a referência recorrente a **$D_0 + 163\text{ dias}$** representa o exato momento em que a evidência deu entrada no laboratório pericial, encerrando um período de **163 dias sem custódia formal documentada** (a chamada *Lacuna Pré-Laboratorial*).

#### 1. Como foi calculado o intervalo de 163 dias?
O cálculo decorre da diferença em dias corridos entre a data nominal gravada no nome do arquivo original e a data de seu recebimento oficial no laboratório:

| Marco Relativo | Data Real de Referência | Evento Cronológico na Cadeia de Custódia |
| :--- | :---: | :--- |
| **$D_0$** | `26/04/2026` | **Data nominal da mídia:** extraída da nomenclatura original do arquivo (`AUD-20260426-WA0006.mp3`, padrão `AAAAMMDD` do WhatsApp). |
| **$D_0 + 144\text{ dias}$** | `17/09/2026` | **Última modificação externa (`mtime`):** data de modificação registrada no sistema de arquivos antes do envio à perícia (`15:08:11 UTC`). |
| **$D_0 + 163\text{ dias}$** | `06/10/2026` | **Ingresso no laboratório e exame pericial:** data em que o arquivo foi recebido no armazenamento pericial (`16:46:30 UTC`), teve seu hash inicial fixado (`17:23:01 UTC`), passou pela análise acústica e resultou na emissão do laudo oficial (`17:26:43 UTC`). |
| **$D_0 + 184\text{ dias}$** | `27/10/2026` | **Auditoria acadêmica:** data da extração reprodutível de metadados e validação criptográfica para o artigo científico. |

**Memória de cálculo dos dias corridos (`26/04/2026` a `06/10/2026`):**
* **Abril:** 4 dias restantes (26 a 30/04)
* **Maio:** 31 dias
* **Junho:** 30 dias
* **Julho:** 31 dias
* **Agosto:** 31 dias
* **Setembro:** 30 dias
* **Outubro:** 6 dias (01 a 06/10)
* **Total:** `4 + 31 + 30 + 31 + 31 + 30 + 6 = 163 dias`

#### 2. Qual é a importância pericial e jurídica desses 163 dias?
No estudo de caso ([secao_6_artigo_direito_ti.md](secao_6_artigo_direito_ti.md)), esse intervalo cumpre duas funções essenciais:

1. **Preservação do Sigilo com Precisão Analítica:** Permite que o leitor audite a exata duração de cada etapa pericial sem expor o calendário civil sensível do procedimento disciplinar.
2. **Demonstração Prática da Quebra da Cadeia Antecedente (Ramo C da Árvore de Decisão):** Evidencia que o arquivo circulou por **163 dias** entre sua suposta criação ($D_0$) e sua apresentação oficial ao Estado ($D_0 + 163\text{ dias}$) sem termo de coleta, sem logs de transmissão e sem código hash de origem. Como consequência técnica e jurídica, **a integridade física da mídia só pode ser matematicamente garantida a partir do 163º dia**, cabendo ao perito declarar formalmente que a integridade histórica prévia ao ingresso no laboratório é inverificável.

## Uso do protocolo em outros casos

O script serve para qualquer registro que siga a mesma estrutura:

```json
[
  {
    "indice": 0,
    "fase": "1 - Recebimento",
    "dados_evento": {
      "data_hora_relativa": "D0+163d 16:46:30 UTC",
      "acao": "...",
      "responsavel": "PERITO-01",
      "procedencia": "registro original",
      "arquivos_envolvidos": [
        { "caminho": "entrada/EVIDENCIA_01.mp3", "sha256": "..." }
      ]
    },
    "hash_anterior_hex": null,
    "hash_encadeado_sha256": "..."
  }
]
```

Recomenda-se gerar e encadear cada entrada **no momento** em que o evento ocorre, e não depois, e consignar o último valor no laudo ou parecer assinado.

## Como citar

> [AUTORES]. Cadeia de custódia da evidência audiovisual: protocolo verificável da requisição pericial à defesa. **Direito & TI**, Porto Alegre, [v.], [n.], [p.], [ano]. DOI: [a definir].

## Licença

- Código (`verifica_cadeia.py`): MIT.
- Dados anonimizados e documentação: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
