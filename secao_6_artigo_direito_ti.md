# SEÇÃO 6 — ESTUDO DE CASO: APLICAÇÃO PRÁTICA DO PROTOCOLO PERICIAL DE CADEIA DE CUSTÓDIA EM EVIDÊNCIA DIGITAL 

**Autores:** [ANONIMIZADO PARA REVISÃO POR PARES]  
**Veículo Alvo:** *Revista Direito & TI*  
**Eixo Temático:** Evidências Digitais, Cadeia de Custódia e Perícia Forense Computacional  
**Referencial Normativo:** ABNT NBR ISO/IEC 27037:2014, Código de Processo Penal (Arts. 158-A a 158-F) e Diretrizes Científicas do SWGDE (*Scientific Working Group on Digital Evidence*).

---

## 6.1. Contextualização do Caso e Escopo Pericial

Para demonstrar a aplicabilidade operacional, o rigor probatório e a capacidade de auditoria do protocolo proposto neste artigo, esta seção submete um caso pericial real — oriundo de apuração administrativa de natureza disciplinar — às diretrizes estabelecidas nas Fases 0 a 7, bem como ao mecanismo criptográfico de registro encadeado de custódia.

Em observância aos imperativos éticos e regulamentares de sigilo processual, proteção de dados e integridade institucional, todos os dados identificadores originais (nomes de partes, peritos, números de processo, unidades policiais e localidades) foram estritamente substituídos por rótulos tipificados (*tokens* anonimizados), preservando-se uma tabela de correspondência sob custódia local controlada (*offline*), a qual não integra a publicação externa. Do mesmo modo, os marcos temporais absolutos foram convertidos em escala temporal relativa referenciada a $D_0$ (data nominal do arquivo examinado).

O encargo pericial foi instaurado para avaliar a **autenticidade, integridade estrutural, caracterização técnica de contêiner/codec e eventuais vestígios de edição, adulteração ou manipulação** em uma evidência digital de áudio encaminhada à autoridade correcional no âmbito do **Procedimento Administrativo [CASO-01]**, instaurado pela **Unidade Operacional Requisitante [UNIDADE-01]** e examinado pelo **Setor Pericial Especializado [LAB-FORENSE-01]** do **Órgão Correcional Central [ORGAO-01]**.

---

## 6.2. Cronologia Pericial: Análise das Fases 0 a 7 e Identificação de Lacunas

A cadeia de custódia de evidências digitais desdobra-se em oito etapas metodológicas sequenciais (Fases 0 a 7). A Tabela 6.1 sumariza a linha do tempo pericial identificada no caso concreto, discriminando documentalmente a procedência temporal de cada informação:
*   `[REGISTRO ORIGINAL]`: dado atestado por documentos formais, relatórios ou registros de sistema gerados na época do exame pericial ($D_0 + 163$ dias);
*   `[RECONSTRUÍDO EM 2026-10-27]`: metadado ou cálculo de integridade derivado no presente ciclo de auditoria acadêmica ($D_0 + 184$ dias);
*   `[NÃO DISPONÍVEL]`: informação ausente nos registros formais recebidos pela perícia.

### Tabela 6.1 — Cronologia Factual das Fases de Custódia (Fases 0 a 7)

| Fase Metodológica | Marco Temporal Relativo | Ação / Evento Registrado | Agente Responsável | Origem Probatória do Registro |
| :--- | :--- | :--- | :--- | :--- |
| **Fase 0: Admissão do Encargo** | $D_0 + 163$ dias, 17:22:59 UTC | Formalização e autuação do procedimento pericial no sistema correcional. Fixação do escopo do encargo. | Perito Oficial [PERITO-01] | `[REGISTRO ORIGINAL]` *(termo pericial e log formal)* |
| **Fase 1: Recebimento** | $D_0 + 163$ dias, 16:46:30 UTC | Depósito do arquivo digital no armazenamento pericial (*ctime/birthtime* no sistema NTFS). | Setor [LAB-FORENSE-01] | `[REGISTRO ORIGINAL]` *(metadados de sistema de arquivos)* |
| | $D_0 + 163$ dias, 17:23:01 UTC | Cálculo dos hashes criptográficos de custódia de entrada (MD5, SHA-1, SHA-256, SHA-512). | Perito Oficial [PERITO-01] | `[REGISTRO ORIGINAL]` *(registro em hashes.json)* |
| **Fase 2: Preservação** | $D_0 + 163$ dias, 17:23:06 UTC | Fixação do original em modo somente-leitura. Geração de cópia de trabalho decodificada em PCM Linear 16-bit. | Perito Oficial [PERITO-01] | `[REGISTRO ORIGINAL]` *(registro em filesystem_metadata.json e log.txt)* |
| **Fase 3: Processamento** | $D_0 + 163$ dias, 17:23:13 UTC | Extração atomizada de contêiner, codecs e fluxos temporais via FFprobe 7.1 e MediaInfo 26.05. | Perito Oficial [PERITO-01] | `[REGISTRO ORIGINAL]` *(ffprobe_summary.json e container_codec.json)* |
| | $D_0 + 184$ dias, 11:09:42 UTC | Extração padronizada de metadados FFprobe sobre cópia de trabalho autenticada para auditoria da Seção 6. | Equipe de Pesquisa | `[RECONSTRUÍDO EM 2026-10-27]` *(metadados_ffprobe.json)* |
| **Fase 4: Análise** | $D_0 + 163$ dias, 17:24:01 UTC | Inspeção acústica (RMS, FFT, STFT, cutoff em 15.996 Hz, ENF 60 Hz, VAD e diarização em 2 grupos vocais). | Perito Oficial [PERITO-01] | `[REGISTRO ORIGINAL]` *(laudos parciais das etapas 08 a 22)* |
| **Fase 5: Documentação** | $D_0 + 163$ dias, 17:26:43 UTC | Emissão e assinatura do Laudo Pericial Oficial Conclusivo (20 Capítulos) e Matriz de 8 Quesitos. | Perito Oficial [PERITO-01] | `[REGISTRO ORIGINAL]` *(relatorio_final.md e matriz_quesitos.json)* |
| **Fase 6: Entrega** | *Não disponível nos autos eletrônicos* | Remessa formal do laudo pericial à autoridade requisitante. | Setor [LAB-FORENSE-01] | `[NÃO DISPONÍVEL]` *(lacuna de protocolo externo)* |
| **Fase 7: Guarda e Descarte** | *Em andamento (contínua)* | Arquivamento do repositório em cofre digital de custódia institucional. | Órgão [ORGAO-01] | `[REGISTRO ORIGINAL]` *(política de custódia corporativa)* |

### Apontamento Crítico de Lacunas Temporais e Probatórias
A análise cronológica formal revela **duas lacunas de custódia relevantes**:
1.  **Lacuna Pré-Laboratorial ($D_0$ até $D_0 + 163$ dias):** O nome do arquivo ostenta a sequência `20260426` ($D_0$), ao passo que o *mtime* no sistema de arquivos registra $D_0 + 144$ dias e a gravação física no armazenamento pericial ocorreu em $D_0 + 163$ dias. O intervalo de 163 dias entre a suposta produção do áudio e seu ingresso no laboratório pericial é desprovido de logs de transmissão, recibos de servidores ou registros de posse intermediária.
2.  **Lacuna de Entrega Formal (Fase 6):** Não constam no repositório digital os recibos de protocolo físico ou transmissão assinada digitalmente do memorando de entrega dos autos à autoridade requisitante, subsistindo apenas a data/hora exata de emissão interna do laudo ($D_0 + 163$ dias, 17:26:43 UTC).

---

## 6.3. Fase de Recebimento: Aplicação da Árvore de Decisão e Classificação no Ramo C

O protocolo estabelece quatro ramos decisórios no ato do recebimento da evidência digital em ambiente laboratorial:
*   **Ramo A:** Hash de origem prévio registrado e coincidente com o calculado no ato do recebimento;
*   **Ramo B:** Hash de origem registrado, porém divergente (impondo investigação obrigatória de causas não adulterantes, tais como divergência de algoritmo, cálculo sobre envelope e erro de transcrição);
*   **Ramo C:** Hash de origem inexistente (o hash apurado no laboratório constitui o marco inicial; declaração obrigatória de que a integridade prévia é inverificável);
*   **Ramo D:** Lacre físico violado, ausente ou divergente.

### Enquadramento Técnico e Justificativa Documental
No caso em apreço, o arquivo `EVIDENCIA_01.mp3` foi encaminhado ao laboratório pericial sem que a autoridade requisitante houvesse documentado previamente em ofício, termo de apreensão ou auto de arrecadação o seu respectivo valor *hash* de origem. Conforme expressamente registrado no exame pericial de transmissão (Etapa 22 — `22_Email/resultados/email_metadata.json`):

> *"Status: NÃO APLICÁVEL / NÃO DISPONIBILIZADO. Não foram disponibilizados arquivos de e-mail para exame pericial de transferência... Sem arquivos de e-mail brutos com cabeçalhos RFC 822/MIME, não é possível rastrear servidores de transmissão ou comparar hashes de anexos."*

Adicionalmente, na resposta oficial ao **Quesito nº 2 da Matriz Pericial** (`24_Matriz_Quesitos/resultados/matriz_quesitos.json`), assentou o perito relator:

> *"A integridade física do arquivo foi fixada no momento inicial por meio do hash criptográfico SHA-256 (`526cee63cc98221a84a0f9578fa12b02a0350cd5a6ae9c4352caf039e374766d`)... Limitações: Hashes garantem a não alteração a partir do recebimento formal; não provam a cadeia prévia anterior ao depósito."*

Por conseguinte, o caso enquadra-se inequivocamente no **Ramo C (Hash de origem inexistente)**:
1.  **Marco Inicial:** O hash `SHA-256: 526cee63cc98221a84a0f9578fa12b02a0350cd5a6ae9c4352caf039e374766d` calculado em $D_0 + 163$ dias (17:23:01 UTC) fixa o início da custódia forense rastreável e auditável;
2.  **Ressalva Probatória Obrigatória:** É tecnicamente vedado presumir ou afirmar a intangibilidade da evidência entre a sua captação pelo microfone em $D_0$ e o seu depósito formal no laboratório pericial em $D_0 + 163$ dias, cabendo ao julgador valorar o elemento probatório sob a reserva da quebra da cadeia antecedente (Art. 158-B, incisos I a III do CPP).

---

## 6.4. Processamento e Extração Padronizada de Metadados

Em cumprimento estrito às exigências de transparência metodológica da norma ABNT NBR ISO/IEC 27037:2014, a extração de metadados foi executada sobre uma **cópia de trabalho bit-a-bit autenticada** (`trabalho/copia_trabalho_artigo.mp3`), sem qualquer interação de leitura direta com o arquivo original sob custódia.

### Parâmetros da Execução Controlada
*   **Ferramenta Utilizada:** `ffprobe` (suíte FFmpeg 7.1, *built with clang 19.1.0*);
*   **Sistema Operacional:** Windows 11 Enterprise AMD64 (Compilação 10.0.26200);
*   **Comando Executado:**  
    `ffprobe -v quiet -print_format json -show_format -show_streams trabalho/copia_trabalho_artigo.mp3`
*   **Artefato Gerado:** `artigo_secao6/metadados_ffprobe.json` (tamanho: 2.293 bytes);
*   **Hash SHA-256 do JSON de Saída:** `732a3b370dac54d99ec5cf2724e1ff044e6ba01cc7f1f2ef1e4717046369b746`.

### Tabela 6.2 — Parâmetros Estruturais Extraídos da Mídia sob Exame

| Atributo Técnico | Valor Identificado | Significado Pericial |
| :--- | :--- | :--- |
| **Nome do Contêiner (`format_name`)** | `mov,mp4,m4a,3gp,3g2,mj2` | Contêiner ISO Base Media File Format (MPEG-4 Part 14) |
| **Pontuação de Confiança (`probe_score`)** | `100` (Confiabilidade Máxima) | Ausência de ambiguidade no cabeçalho do arquivo |
| **Átomos de Marcação (`tags`)** | `major_brand=mp42`, `compatible_brands=mp42isom` | Assinatura nativa de mídia MP4/M4A moderna |
| **Codec de Áudio (`codec_name`)** | `aac` (`profile="LC"`, `codec_tag="mp4a"`) | Advanced Audio Coding — Low Complexity |
| **Disposição de Canais (`channels` / `layout`)** | `1 canal` / `mono` | Fluxo de áudio monofônico |
| **Taxa de Amostragem (`sample_rate`)** | `48.000 Hz` | Frequência de amostragem padrão de telefonia/vídeo |
| **Base Temporal e Taxa de Quadros** | `time_base="1/48000"`, `r_frame_rate="48000/1024"` | Mediana constante de 21,33 ms por pacote AAC |
| **Duração Exata (`duration`)** | `218.602667 segundos` (03 min 38 s 602 ms) | Duração total idêntica nos cabeçalhos e no sinal |
| **Ponto Inicial (`start_time`)** | `0.000000` | Início em zero absoluto, sem atraso de apresentação |
| **Total de Quadros / Pacotes (`nb_frames`)** | `10.247 quadros` | Continuidade integral dos índices PTS de apresentação |
| **Taxa de Bits Nominal Total** | `68.860 bps` (~68,8 kbps - VBR) | Compressão acústica típica de mensagens móveis |

---

## 6.5. Matriz de Achados Fatuais, Interpretação Pericial e Hipóteses Alternativas

Um dos pilares metodológicos do protocolo em discussão é a **distinção categórica entre achado factual (dado objetivo da natureza ou do sinal), interpretação pericial (inferência teórica fundamentada) e hipóteses alternativas viáveis**. Essa separação impede que conclusões subjetivas sejam travestidas de fatos técnicos indiscutíveis.

### Tabela 6.3 — Matriz Pericial Comparativa de Achados e Hipóteses

| Dimensão Pericial | 1. Achado Factual (Evidência Física) | 2. Interpretação Pericial Fundamentada | 3. Hipóteses Alternativas Avaliadas e Descarte |
| :--- | :--- | :--- | :--- |
| **A. Relação Extensão vs. Contêiner** | O arquivo possui nome com extensão `.mp3`. A leitura de seus *magic bytes* iniciais revela átomos `ftypmp42`, e o decodificador atesta contêiner ISO Media com codec `mp4a-40-2` (AAC-LC). Não há fluxo MP3 no arquivo. | **Incompatibilidade Declarada / Spoofing de Extensão.** O arquivo foi renomeado no sistema de arquivos ou foi encapsulado por rotina de exportação de mensageria móvel que designa incorretamente `.mp3` para facilitar compatibilidade. | **H1:** Renomeação voluntária por usuário leigo para reprodução local *(Plausível)*.<br>**H2:** Exportação por cliente WhatsApp Web/Desktop *(Altamente Provável)*.<br>**H3:** Adulteração fraudulenta de conteúdo *(Descartada: integridade estrutural interna íntegra)*. |
| **B. Perfil Espectral e Compressão** | Densidade espectral FFT com corte vertical abrupto (*cutoff*) em **15.996 Hz**, seguido por decaimento de **61,9 dB** até o piso de ruído digital em 24 kHz. | **Compressão Lossy Agressiva.** A frequência de corte a 16 kHz com forte atenuação é o padrão de fábrica do codificador psicoacústico AAC-LC em baixa taxa de bits (~64 kbps). | **H1:** Limitação de resposta analógica do microfone *(Refutada: microfones perdem energia gradualmente, sem degraus de 61 dB)*.<br>**H2:** Transcodificação por aplicativo de mensagens *(Confirmada como hipótese de máxima aderência)*. |
| **C. Cadência Temporal de Pacotes** | 10.247 pacotes analisados sequencialmente. Intervalo mediano constante de **21,33 ms** (1.024 amostras a 48 kHz). Gaps = 0, Overlaps = 0. Detectores Delta RMS, ZCR e Spectral Flux sem picos anômalos. | **Continuidade da Amostra.** O contêiner e o sinal de áudio não exibem vestígios físicos de cortes, montagens, emendas ou eliminação de segmentos ao longo dos 218,6 segundos. | **H1:** Edição perfeita em DAW profissional reexportada *(Improvável: haveria bitolação de quantização dupla e quebra na fase de ruído ambiente e de ENF)*.<br>**H2:** Gravação contínua sem intervenção editorial *(Altamente Provável)*. |
| **D. Rede Elétrica (ENF) e Datação** | Sinal exibe componente senoidal induzido na faixa de 60 Hz com média de **59,9422 Hz** (desvio padrão: 0,7615 Hz; SNR médio: 69,13 dB). | **Ambiente Eletrificado Brasileiro.** O áudio foi capturado nas proximidades de instalação elétrica de 60 Hz. Não é possível determinar data/hora absoluta da gravação por ENF. | **H1:** Datação objetiva da gravação *(Impossível: ausência de banco sincrofasorial histórico correlato)*.<br>**H2:** Flutuações pontuais de frequência como prova de corte *(Refutada: em aparelhos celulares, oscilações térmicas geram dispersão natural)*. |
| **E. Atividade Vocal e Diarização** | Duração de fala ativa de **106,44 s** (48,69% do tempo total). VAD isolou 101 segmentos válidos. Diarização espectral agrupou os turnos em **2 locutores acústicos**. | **Estrutura Dialogal Bipessoal.** Gravação contendo diálogo alternado entre duas vozes distintas em ambiente acústico estável. | **H1:** Identificação civil ou criminal de indivíduos *(Vedada: Princípio Pericial 21 veda identificação sem padrão vocal contemporâneo autêntico)*.<br>**H2:** Presença de terceiros silenciosos *(Inverificável acusticamente)*. |

---

## 6.6. Registro Encadeado de Custódia e Verificação Criptográfica

Para assegurar a não repudiação, a integridade matemática retroativa e a auditabilidade de ponta a ponta dos atos periciais, o protocolo implementa um modelo de **Registro de Custódia Encadeado (*Hash Chaining*)**, inspirado em estruturas de livros-razão criptográficos imutáveis (*hash-linked ledgers*).

### Especificação Matemática do Algoritmo
Cada entrada de custódia $e_i$ ($i \in \{0, 1, \dots, n\}$) é modelada como uma tupla contendo:
*   Índice sequencial $i$;
*   Data e hora em UTC e sua equivalência relativa;
*   Fase metodológica do protocolo (0 a 7);
*   Descrição circunstanciada da ação pericial;
*   Identificador anonimizado do responsável técnico;
*   Relação de arquivos físicos vinculados com seus respectivos hashes SHA-256 e tamanhos;
*   Origem probatória do dado (`[REGISTRO ORIGINAL]` ou `[RECONSTRUÍDO]`).

A garantia de imutabilidade assenta-se em duas regras de cálculo:
1.  **Serialização Canônica:** A tupla $e_i$ é serializada em formato JSON canônico ($\sigma(e_i)$), com ordenação lexicográfica estrita de chaves, codificação UTF-8 e supressão de espaços em branco separadores (`sort_keys=True, separators=(',', ':')`);
2.  **Encadeamento Criptográfico:**  
    $$h_0 = \text{SHA-256}(\sigma(e_0))$$  
    $$h_i = \text{SHA-256}(\sigma(e_i) \mathbin{\Vert} \text{hex}(h_{i-1})), \quad \forall i \ge 1$$  
    onde $\mathbin{\Vert}$ denota a concatenação de bytes binários UTF-8.

Qualquer alteração em um único caractere de uma entrada histórica $e_j$ ou a adulteração de qualquer arquivo referenciado corrompe imediatamente todos os hashes subsequentes $h_k$ ($k \ge j$), denunciando quebra instantânea da cadeia de custódia.

### Tabela 6.4 — Registro de Custódia Criptográfica Encadeada do Caso Real

| Índice ($e_i$) | Fase do Protocolo | Data Relativa | Responsável Técnico | Origem Probatória | Hash Anterior ($h_{i-1}$) | Hash Encadeado ($h_i$) [SHA-256] |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **$e_0$** | 1 - Recebimento | $D_0 + 163$ d, 16:46 UTC | Setor [LAB-FORENSE-01] | `[ORIGINAL]` | *Nenhum (Gênese)* | `7b7cd952b033b5685db1943c2ddae7be5332f913d8d5df8f5f1c9fcbbd1d7bb3` |
| **$e_1$** | 0 - Admissão | $D_0 + 163$ d, 17:22 UTC | Perito [PERITO-01] | `[ORIGINAL]` | `7b7cd952b033...` | `7fafb43579211386dfba867d718b53297a7da933ae3da3975a5e381ebf399d94` |
| **$e_2$** | 1 - Fixação Hashes | $D_0 + 163$ d, 17:23 UTC | Perito [PERITO-01] | `[ORIGINAL]` | `7fafb4357921...` | `c1d532a58062af7400e86aea8151b72e90c4fb6ca18fdf92ae17983c27ae3464` |
| **$e_3$** | 2 - Preservação | $D_0 + 163$ d, 17:23 UTC | Perito [PERITO-01] | `[ORIGINAL]` | `c1d532a58062...` | `16253ae2a9a9db05ef0f185310fa2fc339199d79905fa86fb0e4130086ff503d` |
| **$e_4$** | 3 - Processamento | $D_0 + 163$ d, 17:23 UTC | Perito [PERITO-01] | `[ORIGINAL]` | `16253ae2a9a9...` | `40ae7881c96f70c2cad0119e2c6087b7a1197775c947cf29653139fcb903ec9a` |
| **$e_5$** | 4 - Análise Acústica| $D_0 + 163$ d, 17:24 UTC | Perito [PERITO-01] | `[ORIGINAL]` | `40ae7881c96f...` | `280c7aca8d1bbc4279daeb621b44ecb3f742299a9cf4e8f7fa0c7c34b82fc60f` |
| **$e_6$** | 5 - Documentação | $D_0 + 163$ d, 17:26 UTC | Perito [PERITO-01] | `[ORIGINAL]` | `280c7aca8d1b...` | `53401cdaf5c15e7f409ca280f58eb80083ae8e6ce9389e830e9dcf477611dc82` |
| **$e_7$** | 3 - Auditoria Artigo | $D_0 + 184$ d, 11:09 UTC | Equipe de Pesquisa | `[RECONSTRUÍDO]`| `53401cdaf5c1...` | `8dea9521f869521976111eae7bce5784f4798365ea285f58c7e923e271eb5215` |

### Script de Auditoria Automatizada (`verifica_cadeia.py`)
Para viabilizar a verificação independente por defensores, magistrados, auditores ou comitês editoriais, o protocolo disponibiliza o script autônomo `verifica_cadeia.py`. Executado diretamente sobre os artefatos do caso, o script recalcula a serialização canônica de cada elo e audita os blocos binários dos arquivos referenciados no disco. 

A saída padronizada do auditor confirma a integridade plena do sistema:

```text
================================================================================
AUDITORIA CRIPTOGRÁFICA DA CADEIA DE CUSTÓDIA (PROTOCOLO DIREITO & TI)
Arquivo analisado: artigo_secao6/registro_custodia_encadeado.json
================================================================================
Total de eventos na cadeia: 8

[OK                ] e_00 | Fase: 1 - Recebimento                  | Hash: 7b7cd952b033b5685db1943c...
[OK                ] e_01 | Fase: 0 - Admissão do encargo          | Hash: 7fafb43579211386dfba867d...
[OK                ] e_02 | Fase: 1 - Recebimento (Fixação Hashes) | Hash: c1d532a58062af7400e86aea...
[OK                ] e_03 | Fase: 2 - Preservação                  | Hash: 16253ae2a9a9db05ef0f1853...
[OK                ] e_04 | Fase: 3 - Processamento (Contêiner)    | Hash: 40ae7881c96f70c2cad0119e...
[OK                ] e_05 | Fase: 4 - Análise (Acústica e VAD)     | Hash: 280c7aca8d1bbc4279daeb62...
[OK                ] e_06 | Fase: 5 - Documentação (Laudo Final)   | Hash: 53401cdaf5c15e7f409ca280...
[OK                ] e_07 | Fase: 3 - Auditoria Artigo (FFprobe)   | Hash: 8dea9521f869521976111eae...

--------------------------------------------------------------------------------
VERIFICAÇÃO DE HASHES DOS ARQUIVOS FÍSICOS REFERENCIADOS:
--------------------------------------------------------------------------------
[ARQUIVO ÍNTEGRO] entrada/original/AUD-20260426-WA0006.mp3                | SHA-256: 526cee63cc98221a... (OK)
[ARQUIVO ÍNTEGRO] 00_Caso/resultados/caso.json                            | SHA-256: 1c07b2e69fbe70a6... (OK)
[ARQUIVO ÍNTEGRO] 01_Hashes/resultados/hashes.json                        | SHA-256: fff3f59a0955ba46... (OK)
[ARQUIVO ÍNTEGRO] 02_Filesystem_Metadata/resultados/filesystem_metadata.json | SHA-256: 0791f6637214f018... (OK)
[ARQUIVO ÍNTEGRO] trabalho/amostra_trabalho.wav                           | SHA-256: 78d6b4aac0765941... (OK)
[ARQUIVO ÍNTEGRO] 04_FFprobe/resultados/ffprobe_summary.json              | SHA-256: 49918f3b061911a7... (OK)
[ARQUIVO ÍNTEGRO] 06_Container_Codec/resultados/container_codec.json      | SHA-256: 98f894f46ff2cd6a... (OK)
[ARQUIVO ÍNTEGRO] 07_Packets_Frames/resultados/temporal_structure.json    | SHA-256: 17988e882e28351f... (OK)
[ARQUIVO ÍNTEGRO] 11_Compressao_Transcodificacao/resultados/compression_analysis.json | SHA-256: 6589e64fa73e8532... (OK)
[ARQUIVO ÍNTEGRO] 12_Descontinuidades_Edicao/resultados/editing_indicators.json | SHA-256: 58a7a6da434aca3a... (OK)
[ARQUIVO ÍNTEGRO] 13_ENF/resultados/enf_analysis.json                     | SHA-256: 391f799f69266ae8... (OK)
[ARQUIVO ÍNTEGRO] 16_Diarizacao/resultados/diarization.json               | SHA-256: 5b4bb1c71b9fbd50... (OK)
[ARQUIVO ÍNTEGRO] 24_Matriz_Quesitos/resultados/matriz_quesitos.json      | SHA-256: 9eb89e5aac4f97bf... (OK)
[ARQUIVO ÍNTEGRO] 25_Relatorio_Final/resultados/relatorio_final.md        | SHA-256: 662b0d87843804e0... (OK)
[ARQUIVO ÍNTEGRO] artigo_secao6/metadados_ffprobe.json                    | SHA-256: 732a3b370dac54d9... (OK)
================================================================================
RESULTADO DA AUDITORIA: CADEIA DE CUSTÓDIA 100% ÍNTEGRA E VÁLIDA!
Total de 8 eventos periciais encadeados matematicamente sem qualquer quebra.
Total de 15 arquivos auditados com hashes correspondentes.
================================================================================
```

---

## 6.7. Discussão Jurídico-Pericial: Efeitos Probatórios da Quebra de Cadeia Antecedente

O caso examinado exemplifica com precisão o drama epistemológico frequente na justiça criminal e administrativa contemporânea: **a presença de evidência tecnicamente íntegra no laboratório, mas circundada por fragilidades ou quebras formais em sua fase pré-processual**.

1.  **Diferenciação entre Integridade Física e Integridade Histórica:**
    *   A integridade *física* do arquivo a partir de seu depósito em laboratório ($D_0 + 163$ dias) restou matematicamente blindada via SHA-256 e encadeamento criptográfico.
    *   Por outro lado, a integridade *histórica* ou *de origem* (entre $D_0$ e $D_0 + 163$ dias) jamais pôde ser atestada. O enquadramento compulsório no **Ramo C da Árvore de Decisão** estabelece como imperativo de honestidade científica que o perito declare que a evidência pode ter sofrido edições prévias antes de sua apresentação ao Estado, especialmente porque a codificação lossy AAC-LC atenua microdetalhes analógicos que denunciariam montagens amadoras.
2.  **Valoração Jurídica da Prova Digital:**
    À luz da jurisprudência do Superior Tribunal de Justiça (STJ) nos precedentes de quebra da cadeia de custódia (RHC 143.169/RJ e HC 653.515/RJ), a ausência de registro formal de lacre e hash de origem não conduz à automática nulidade processual quando inexistir demonstração de adulteração material interna no sinal. Todavia, impõe redução substantiva no **peso probatório (*probative weight*)** da gravação. 
    A evidência não pode, isoladamente, fundamentar condenação criminal ou demissão funcional se desacompanhada de elementos colaterais de corroboração (depoimentos testemunhais autônomos, registros de antenas ERB ou quebras telemáticas judiciais).

---

## 6.8. Síntese dos Resultados e Conclusão da Demonstração Prática

A aplicação do protocolo proposto sobre a evidência pericial real evidenciou resultados contundentes:
1.  **Imutabilidade Comprovada:** Todos os 8 eventos periciais e os 15 artefatos do repositório mantiveram estrita convergência criptográfica encadeada, garantindo auditabilidade pública e reprodutibilidade integral por script de código aberto (`verifica_cadeia.py`);
2.  **Transparência Metodológica:** A distinção formal entre fatos técnicos objetivos (contêiner MP4, áudio AAC-LC, cutoff a 16 kHz) e inferências (aplicativo WhatsApp como proveniência provável) forneceu balizas seguras para o contraditório jurisdicional;
3.  **Segurança Ética e Legal:** A segregação rígida entre dados históricos (`[REGISTRO ORIGINAL]`) e reconstruções posteriores (`[RECONSTRUÍDO]`), somada ao protocolo de anonimização com tabela de correspondência sob custódia local, assegurou pleno sigilo e preservação da cadeia probatória, atendendo aos mais rigorosos padrões da perícia criminal e das diretrizes editoriais da *Revista Direito & TI*.
