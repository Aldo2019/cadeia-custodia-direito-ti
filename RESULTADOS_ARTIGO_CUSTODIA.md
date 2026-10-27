# RESULTADOS PERICIAIS PARA O ARTIGO CIENTÍFICO (REVISTA DIREITO & TI)
**Tema:** Protocolo de Cadeia de Custódia para Evidência Digital Audiovisual  
**Aplicação Prática:** Estudo de Caso Real de Áudio Forense (Procedimento Administrativo Disciplinar)  
**Data de Extração e Auditoria:** 2026-10-27  
**Status de Integridade da Evidência Original:** 100% Preservada (SHA-256 Inalterado)

---

## 1. Identificação Formal e Tabela de Anonimização (Padrão Acadêmico)

Para publicação no artigo, todos os identificadores foram convertidos em rótulos neutros (*tokens*), preservando-se a confidencialidade das partes e instituições:

| Elemento Original | Rótulo Anonimizado no Artigo | Categoria / Descrição |
| :--- | :--- | :--- |
| `SAD 109437/2026 6º BPM` | **Procedimento Administrativo [CASO-01]** | Procedimento disciplinar de apuração |
| `CPM-PMMG` | **Órgão Correcional Central [ORGAO-01]** | Órgão correcional mantenedor |
| `6º BPM` | **Unidade Requisitante [UNIDADE-01]** | Unidade de origem da requisição |
| `Seção de Criminalística - CPM2` | **Setor Pericial Especializado [LAB-FORENSE-01]** | Laboratório de perícia audiovisual |
| `Analista da Seção de Criminalística` | **Perito Oficial Responsável [PERITO-01]** | Perito relator |
| `AUD-20260426-WA0006.mp3` | **EVIDENCIA_01.mp3** (ou `EVID-01`) | Arquivo de mídia sob exame |
| `2026-04-26` (data nominal no arquivo) | **$D_0$** | Marco temporal de origem presumida |
| `2026-09-17 15:08:11 UTC` | **$D_0 + 144$ dias, 15:08:11 UTC** | Timestamp *mtime* no sistema de arquivos |
| `2026-10-06 16:46:30 UTC` | **$D_0 + 163$ dias, 16:46:30 UTC** | Timestamp de ingresso no laboratório (*birthtime*) |
| `2026-10-06 17:22:59 UTC` | **$D_0 + 163$ dias, 17:22:59 UTC** | Formalização e autuação pericial |
| `2026-10-06 17:26:43 UTC` | **$D_0 + 163$ dias, 17:26:43 UTC** | Emissão do Laudo Pericial Oficial Final |
| `2026-10-27` | **$D_0 + 184$ dias** | Auditoria e reconstrução para o artigo |

> *A correspondência unívoca completa e confidencial está armazenada localmente em [artigo_secao6/tabela_correspondencia_anonimizacao.json](file:///c:/Users/PMMG/Desktop/Direito&TI/Analise_de_Vídeo/artigo_secao6/tabela_correspondencia_anonimizacao.json).*

---

## 2. Garantia de Preservação e Verificação de Integridade dos Originais

Em estrita obediência à norma ABNT NBR ISO/IEC 27037:2014, o arquivo original permaneceu em modo estrito somente-leitura. Os hashes foram verificados antes e após todo o ciclo analítico:

| Arquivo de Evidência | Algoritmo | Hash Inicial (Recebimento) | Hash Final (Pós-Auditoria) | Veredito |
| :--- | :--- | :--- | :--- | :---: |
| `EVIDENCIA_01.mp3` | **SHA-256** | `526cee63cc98221a84a0f9578fa12b02a0350cd5a6ae9c4352caf039e374766d` | `526cee63cc98221a84a0f9578fa12b02a0350cd5a6ae9c4352caf039e374766d` | **INALTERADO** |
| `EVIDENCIA_01.mp3` | **MD5** | `aebf5c6ae0fdddde84acf13bce02cce5` | `aebf5c6ae0fdddde84acf13bce02cce5` | **INALTERADO** |
| `EVIDENCIA_01.mp3` | **SHA-1** | `2a27583eca82932b9903c81f4751a491911981fa` | `2a27583eca82932b9903c81f4751a491911981fa` | **INALTERADO** |
| `EVIDENCIA_01.mp3` | **SHA-512** | `1d948f6c46e62df057c71382d2c5a69154e30efdb50feb78a482b502d7c9600c...` | `1d948f6c46e62df057c71382d2c5a69154e30efdb50feb78a482b502d7c9600c...` | **INALTERADO** |

---

## 3. Linha do Tempo Factual e Identificação de Lacunas Probatórias (Fases 0 a 7)

Cada registro possui indicação categórica de sua procedência temporal:
*   `[REGISTRO ORIGINAL]`: documento ou log lavrado na época da perícia ($D_0 + 163$ dias);
*   `[RECONSTRUÍDO EM 2026-10-27]`: cálculo derivado na auditoria acadêmica ($D_0 + 184$ dias);
*   `[NÃO DISPONÍVEL]`: dado não documentado pela autoridade ou remetente.

### Tabela 3.1 — Cronologia das Fases de Custódia

| Fase do Protocolo | Data / Hora Relativa | Ação Pericial Realizada | Responsável | Procedência do Registro |
| :--- | :--- | :--- | :--- | :---: |
| **Fase 0: Admissão** | $D_0 + 163$ d, 17:22:59 UTC | Autuação e fixação do encargo no sistema de custódia. | [PERITO-01] | `[REGISTRO ORIGINAL]` |
| **Fase 1: Recebimento** | $D_0 + 163$ d, 16:46:30 UTC | Gravação no repositório (*birthtime* do sistema de arquivos). | [LAB-FORENSE-01] | `[REGISTRO ORIGINAL]` |
| | $D_0 + 163$ d, 17:23:01 UTC | Fixação dos hashes de custódia de entrada (SHA-256). | [PERITO-01] | `[REGISTRO ORIGINAL]` |
| **Fase 2: Preservação** | $D_0 + 163$ d, 17:23:06 UTC | Bloqueio do original e decodificação para PCM linear 16-bit. | [PERITO-01] | `[REGISTRO ORIGINAL]` |
| **Fase 3: Processamento** | $D_0 + 163$ d, 17:23:13 UTC | Extração atomizada via FFprobe 7.1 e MediaInfo 26.05. | [PERITO-01] | `[REGISTRO ORIGINAL]` |
| | $D_0 + 184$ d, 11:09:42 UTC | Extração padronizada de metadados FFprobe para a Seção 6. | Pesquisa | `[RECONSTRUÍDO EM 2026-10-27]` |
| **Fase 4: Análise** | $D_0 + 163$ d, 17:24:01 UTC | Análise espectral, cutoff 16 kHz, cadência PTS, ENF 60 Hz e VAD. | [PERITO-01] | `[REGISTRO ORIGINAL]` |
| **Fase 5: Documentação**| $D_0 + 163$ d, 17:26:43 UTC | Emissão do Laudo Oficial e resposta aos 8 quesitos periciais. | [PERITO-01] | `[REGISTRO ORIGINAL]` |
| **Fase 6: Entrega** | *Não disponível nos autos* | Remessa formal do laudo à autoridade requisitante. | [LAB-FORENSE-01] | `[NÃO DISPONÍVEL]` |
| **Fase 7: Guarda/Descarte**| *Em andamento (contínua)* | Arquivamento em cofre digital de custódia corporativa. | [ORGAO-01] | `[REGISTRO ORIGINAL]` |

### Lacunas Probatórias Apontadas
1.  **Lacuna Antecedente / Pré-Laboratorial (163 dias):** Inexistência de registros de custódia entre $D_0$ (data nominal do áudio) e $D_0 + 163$ dias (ingresso no laboratório). Não foram disponibilizados logs de servidores de e-mail, termos de apreensão de smartphone ou comprovantes de custódia prévia.
2.  **Lacuna de Entrega Externa (Fase 6):** Não consta dos registros técnicos o protocolo de entrega física ou recibo eletrônico de remessa à autoridade requisitante.

---

## 4. Classificação na Árvore de Decisão: Ramo C (Hash Inexistente)

*   **Enquadramento:** **Ramo C** (Hash de origem inexistente / ausência de registro formal antecedente).
*   **Condição do Lacre:** "Não aplicável / Não disponibilizado" (mídia remetida por meio digital desprovida de invólucro ou lacre físico numerado).
*   **Fundamentação Documental Literal:**
    *   *Etapa 22 (Email Metadata):* `"Status: NÃO APLICÁVEL / NÃO DISPONIBILIZADO... Sem arquivos de e-mail brutos com cabeçalhos RFC 822/MIME, não é possível rastrear servidores de transmissão ou comparar hashes de anexos."`
    *   *Matriz de Quesitos (Quesito nº 2):* `"Hashes garantem a não alteração a partir do recebimento formal; não provam a cadeia prévia anterior ao depósito."`
*   **Efeito Pericial e Jurídico:** O valor `SHA-256: 526cee63cc98221a84a0f9578fa12b02a0350cd5a6ae9c4352caf039e374766d` calculado em $D_0 + 163$ dias é o **marco inicial da custódia auditável**. É tecnicamente vedado declarar higidez prévia ao depósito em laboratório.

---

## 5. Metadados Técnicos Extraídos via FFprobe (Fase 3)

*   **Ferramenta:** `ffprobe version 7.1 Copyright (c) 2007-2024 the FFmpeg developers (built with clang 19.1.0)`
*   **Sistema Operacional:** `Windows 11 Enterprise AMD64 (10.0.26200)`
*   **Comando Executado:**  
    `ffprobe -v quiet -print_format json -show_format -show_streams trabalho/copia_trabalho_artigo.mp3`
*   **Artefato Gerado:** [artigo_secao6/metadados_ffprobe.json](file:///c:/Users/PMMG/Desktop/Direito&TI/Analise_de_Vídeo/artigo_secao6/metadados_ffprobe.json)
*   **SHA-256 do JSON de Saída:** `732a3b370dac54d99ec5cf2724e1ff044e6ba01cc7f1f2ef1e4717046369b746`

### Tabela 5.1 — Atributos Técnicos Consolidados da Mídia

| Parâmetro FFprobe | Valor Identificado | Significado Pericial |
| :--- | :--- | :--- |
| `format_name` | `mov,mp4,m4a,3gp,3g2,mj2` | Contêiner ISO Base Media File Format (MP4) |
| `probe_score` | `100` | Máxima certeza estrutural de decodificação |
| `tags.major_brand` | `mp42` | Família ISO/IEC 14496-14 (MPEG-4 Part 14) |
| `tags.compatible_brands` | `mp42isom` | Compatibilidade com reprodutores MP4/M4A |
| `codec_name` | `aac` (`profile="LC"`) | Advanced Audio Coding — Low Complexity |
| `codec_tag_string` | `mp4a` | IdentificadorFourCC de áudio MPEG-4 |
| `channels` / `channel_layout` | `1` / `mono` | Áudio monofônico |
| `sample_rate` | `48.000 Hz` | Taxa de amostragem padrão de áudio móvel |
| `r_frame_rate` | `48000/1024` (~46,875 fps) | Taxa constante de quadros AAC (1.024 amostras/bloco) |
| `duration` | `218.602667 s` (03m 38s 602ms) | Duração exata do contêiner e do fluxo de áudio |
| `start_time` | `0.000000` | Início em zero absoluto, sem atraso de apresentação |
| `nb_frames` | `10.247` quadros | Cadência temporal uniforme e contínua |
| `bit_rate` | `68.860 bps` (~68,8 kbps) | Taxa de bits variável (VBR) típica de mensageria |

---

## 6. Matriz de Achados Fatuais, Interpretação Técnica e Hipóteses Alternativas (Fase 4)

| Dimensão Analítica | 1. Achado Factual (Dado Objetivo) | 2. Interpretação Pericial Fundamentada | 3. Hipóteses Alternativas e Veredito |
| :--- | :--- | :--- | :--- |
| **Extensão vs. Contêiner** | Extensão declarada `.mp3`, contudo os magic bytes revelam átomos `ftypmp42` e codec AAC-LC (`mp4a-40-2`). Inexiste fluxo MP3. | **Incompatibilidade / Spoofing de Extensão.** Mídia renomeada ou derivada de rotina de exportação móvel (ex: WhatsApp Web). | **H1:** Renomeação por usuário leigo (Plausível).<br>**H2:** Exportação por mensageria móvel (Altamente Provável).<br>**H3:** Fraude deliberada (Descartada: fluxo intacto). |
| **Corte Espectral Psicoacústico** | Queda abrupta de energia em **15.996 Hz** com atenuação vertical de **61,9 dB** até o piso de ruído digital em 24 kHz. | **Compressão Lossy Severa.** Corte matemático característico do filtro passa-baixas psicoacústico do codec AAC em baixa taxa de bits (~64 kbps). | **H1:** Resposta analógica de microfone (Refutada: decaimento analógico é suave).<br>**H2:** Transcodificação por mensageria (Confirmada). |
| **Cadência Temporal de Pacotes** | 10.247 pacotes. Intervalo mediano constante de **21,33 ms**. Gaps = 0, Overlaps = 0. Detectores RMS, ZCR e Spectral Flux sem picos anômalos. | **Continuidade da Amostra.** Inexistência de quebras de fase, saltos de energia ou cortes no ruído de fundo. Mídia gravada em sessão contínua. | **H1:** Edição avançada reexportada em DAW (Improvável: quebraria ruído e ENF).<br>**H2:** Gravação contínua sem emendas (Altamente Provável). |
| **Rede Elétrica (ENF)** | Componente em 60 Hz detectado: média **59,9422 Hz**, desvio de **0,7615 Hz**, SNR de **69,13 dB**. | Captação em ambiente brasileiro sob rede elétrica (60 Hz). Impossibilidade de datação objetiva por falta de banco sincrofasorial. | **H1:** Datação objetiva da gravação (Impossível nos autos).<br>**H2:** Flutuações locais como indício de corte (Refutada: variação térmica normal de celular). |
| **Atividade Vocal e Diarização** | Duração de fala de **106,44 s** (48,69%). VAD isolou 101 turnos. Diarização espectral agrupou as falas em **2 locutores acústicos**. | Diálogo alternado entre duas vozes em ambiente com ruído constante. Vedada atribuição de identidade sem padrão autêntico de confronto. | **H1:** Identificação civil de investigado (Vedada pelo Princípio 21).<br>**H2:** Presença de terceiros silenciosos (Inverificável). |

---

## 7. Registro de Custódia Criptográfica Encadeada (*Hash Chaining*)

Algoritmo de encadeamento com serialização JSON canônica (UTF-8, chaves ordenadas, sem espaços):
$$h_0 = \text{SHA-256}(\sigma(e_0)) \quad \text{e} \quad h_i = \text{SHA-256}(\sigma(e_i) \mathbin{\Vert} \text{hex}(h_{i-1})), \quad \forall i \ge 1$$

### Tabela 7.1 — Entradas Encadeadas e Hashes Verificados

| $e_i$ | Fase do Protocolo | Marco Relativo | Responsável | Origem | Hash Anterior ($h_{i-1}$) | Hash Encadeado ($h_i$) |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **$e_0$** | 1 - Recebimento | $D_0 + 163$ d, 16:46 UTC | [LAB-FORENSE-01] | `[ORIGINAL]` | *Gênese (Nenhum)* | `7b7cd952b033b5685db1943c2ddae7be5332f913d8d5df8f5f1c9fcbbd1d7bb3` |
| **$e_1$** | 0 - Admissão | $D_0 + 163$ d, 17:22 UTC | [PERITO-01] | `[ORIGINAL]` | `7b7cd952b033...` | `7fafb43579211386dfba867d718b53297a7da933ae3da3975a5e381ebf399d94` |
| **$e_2$** | 1 - Fixação Hashes | $D_0 + 163$ d, 17:23 UTC | [PERITO-01] | `[ORIGINAL]` | `7fafb4357921...` | `c1d532a58062af7400e86aea8151b72e90c4fb6ca18fdf92ae17983c27ae3464` |
| **$e_3$** | 2 - Preservação | $D_0 + 163$ d, 17:23 UTC | [PERITO-01] | `[ORIGINAL]` | `c1d532a58062...` | `16253ae2a9a9db05ef0f185310fa2fc339199d79905fa86fb0e4130086ff503d` |
| **$e_4$** | 3 - Processamento | $D_0 + 163$ d, 17:23 UTC | [PERITO-01] | `[ORIGINAL]` | `16253ae2a9a9...` | `40ae7881c96f70c2cad0119e2c6087b7a1197775c947cf29653139fcb903ec9a` |
| **$e_5$** | 4 - Análise Acústica| $D_0 + 163$ d, 17:24 UTC | [PERITO-01] | `[ORIGINAL]` | `40ae7881c96f...` | `280c7aca8d1bbc4279daeb621b44ecb3f742299a9cf4e8f7fa0c7c34b82fc60f` |
| **$e_6$** | 5 - Documentação | $D_0 + 163$ d, 17:26 UTC | [PERITO-01] | `[ORIGINAL]` | `280c7aca8d1b...` | `53401cdaf5c15e7f409ca280f58eb80083ae8e6ce9389e830e9dcf477611dc82` |
| **$e_7$** | 3 - Auditoria Artigo | $D_0 + 184$ d, 11:09 UTC | Pesquisa | `[RECONSTRUÍDO]`| `53401cdaf5c1...` | `8dea9521f869521976111eae7bce5784f4798365ea285f58c7e923e271eb5215` |

---

## 8. Validação e Auditoria Independente (`verifica_cadeia.py`)

Para auditabilidade por terceiros, o script [verifica_cadeia.py](file:///c:/Users/PMMG/Desktop/Direito&TI/Analise_de_Vídeo/verifica_cadeia.py) valida automaticamente o encadeamento e confere os hashes dos arquivos no disco.

**Comando de Execução:**
```bash
python verifica_cadeia.py
```

**Resultado Auditado:**
```text
================================================================================
AUDITORIA CRIPTOGRÁFICA DA CADEIA DE CUSTÓDIA (PROTOCOLO DIREITO & TI)
Arquivo analisado: artigo_secao6/registro_custodia_encadeado.json
================================================================================
Total de eventos na cadeia: 8

[OK] e_00 | Fase: 1 - Recebimento                  | Hash: 7b7cd952b033b568...
[OK] e_01 | Fase: 0 - Admissão do encargo          | Hash: 7fafb43579211386...
[OK] e_02 | Fase: 1 - Recebimento (Fixação Hashes) | Hash: c1d532a58062af74...
[OK] e_03 | Fase: 2 - Preservação                  | Hash: 16253ae2a9a9db05...
[OK] e_04 | Fase: 3 - Processamento (Contêiner)    | Hash: 40ae7881c96f70c2...
[OK] e_05 | Fase: 4 - Análise (Acústica e VAD)     | Hash: 280c7aca8d1bbc42...
[OK] e_06 | Fase: 5 - Documentação (Laudo Final)   | Hash: 53401cdaf5c15e7f...
[OK] e_07 | Fase: 3 - Processamento (FFprobe Art.) | Hash: 8dea9521f8695219...

--------------------------------------------------------------------------------
VERIFICAÇÃO DE HASHES DOS ARQUIVOS FÍSICOS REFERENCIADOS:
--------------------------------------------------------------------------------
[ARQUIVO ÍNTEGRO] entrada/original/AUD-20260426-WA0006.mp3 (OK)
[ARQUIVO ÍNTEGRO] 00_Caso/resultados/caso.json (OK)
[ARQUIVO ÍNTEGRO] 01_Hashes/resultados/hashes.json (OK)
[ARQUIVO ÍNTEGRO] 02_Filesystem_Metadata/resultados/filesystem_metadata.json (OK)
[ARQUIVO ÍNTEGRO] trabalho/amostra_trabalho.wav (OK)
[ARQUIVO ÍNTEGRO] 04_FFprobe/resultados/ffprobe_summary.json (OK)
[ARQUIVO ÍNTEGRO] 06_Container_Codec/resultados/container_codec.json (OK)
[ARQUIVO ÍNTEGRO] 07_Packets_Frames/resultados/temporal_structure.json (OK)
[ARQUIVO ÍNTEGRO] 11_Compressao_Transcodificacao/resultados/compression_analysis.json (OK)
[ARQUIVO ÍNTEGRO] 12_Descontinuidades_Edicao/resultados/editing_indicators.json (OK)
[ARQUIVO ÍNTEGRO] 13_ENF/resultados/enf_analysis.json (OK)
[ARQUIVO ÍNTEGRO] 16_Diarizacao/resultados/diarization.json (OK)
[ARQUIVO ÍNTEGRO] 24_Matriz_Quesitos/resultados/matriz_quesitos.json (OK)
[ARQUIVO ÍNTEGRO] 25_Relatorio_Final/resultados/relatorio_final.md (OK)
[ARQUIVO ÍNTEGRO] artigo_secao6/metadados_ffprobe.json (OK)
================================================================================
RESULTADO DA AUDITORIA: CADEIA DE CUSTÓDIA 100% ÍNTEGRA E VÁLIDA!
Total de 8 eventos encadeados sem qualquer quebra.
Total de 15 arquivos auditados com hashes correspondentes.
================================================================================
```

---

## 9. Síntese Dogmático-Jurídica para o Artigo (CPP e STJ)

1.  **Diferenciação Epistemológica:** A integridade *física* em laboratório restou matematicamente provada ($100\%$ íntegra). Todavia, a integridade *histórica de origem* é tecnicamente inverificável em razão do enquadramento no Ramo C (ausência de hash prévio da autoridade remetente e lacuna de 163 dias).
2.  **Valoração Probatória (*Probative Weight*):** Conforme jurisprudência do Superior Tribunal de Justiça (RHC 143.169/RJ e HC 653.515/RJ), a fragilidade da cadeia de custódia antecedente não gera nulidade absoluta automática na ausência de adulteração interna comprovada, mas atenua a força persuasiva da prova digital, que não pode fundamentar isoladamente um juízo condenatório sem corroboração extrínseca.
