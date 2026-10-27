# INVENTÁRIO TÉCNICO FORENSE E REGISTRO DE INTEGRIDADE
**Projeto de Pesquisa: Protocolo de Cadeia de Custódia para Evidências Digitais**  
*Revista Direito & TI — Artigo Acadêmico / Seção 6*  
**Data de Emissão da Auditoria:** 2026-10-27  

---

### 1. Evidência Original sob Custódia Estrita
| Arquivo Real | Rótulo Anonimizado no Artigo | Tamanho (Bytes) | Extensão Declarada | SHA-256 (Identificador Primário Mestre) | MD5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AUD-20260426-WA0006.mp3` | `EVIDENCIA_01.mp3` | 1.881.640 | `.mp3` | `526cee63cc98221a84a0f9578fa12b02a0350cd5a6ae9c4352caf039e374766d` | `aebf5c6ae0fdddde84acf13bce02cce5` |

*Nota de Preservação:* Armazenado em diretório de custódia original com atributo somente-leitura. O hash SHA-256 foi auditado antes e após todas as rotinas laboratoriais, permanecendo estritamente idêntico.

---

### 2. Cópias de Trabalho Autenticadas
| Arquivo | Finalidade | Tamanho (Bytes) | SHA-256 | Relação com o Original |
| :--- | :--- | :--- | :--- | :--- |
| `trabalho/copia_trabalho_artigo.mp3` | Execução de rotinas atomizadas de metadados FFprobe para a Seção 6 | 1.881.640 | `526cee63cc98221a84a0f9578fa12b02a0350cd5a6ae9c4352caf039e374766d` | **Coincidente (Bit-a-Bit)** |
| `trabalho/amostra_trabalho.wav` | Amostra decodificada em PCM Linear 16-bit 48 kHz para análise acústica não destrutiva | 20.985.934 | `78d6b4aac076594166854f9ffca444b5dcbdd678172c40cb60c5b911e5cd2bda` | Decodificação linear sem alteração da evidência fonte |

---

### 3. Documentos do Caso e Artefatos Processuais de Custódia
| Etapa / Local | Arquivo | Categoria Pericial | SHA-256 | MD5 |
| :--- | :--- | :--- | :--- | :--- |
| `00_Caso/resultados/` | `caso.json` | Termo de autuação do procedimento e especificação de ambiente | `1c07b2e69fbe70a664258dafbbcc218eea331b8f15a853ad34819716da7fba2c` | `bec9a48922db003b9148a49df70d6fe5` |
| `01_Hashes/resultados/` | `hashes.json` | Certificação de custódia inicial (MD5, SHA-1, SHA-256, SHA-512) | `fff3f59a0955ba46946e000950829e91fc069abff31c3d2e1240a6edf64f548d` | `bf09d270ebd0e7932168907703b95649` |
| `02_Filesystem_Metadata/resultados/` | `filesystem_metadata.json` | Metadados temporais MACB e parâmetros NTFS | `0791f6637214f01812d30a58e133ed3c197b27f5b16f925b7a1d3f1f434937bf` | `8a20c070abe1b444eece596571d709a4` |
| `22_Email/resultados/` | `email_metadata.json` | Registro de cadeia de transmissão e canais de recebimento | `536ff937d7a16ecb2ff5c30adbc557fe9dc03c8c6d1d287bc5e679093aa9a823` | `a901844b2f4c9c118742b8744573177f` |
| `24_Matriz_Quesitos/resultados/` | `matriz_quesitos.json` | Matriz oficial de resposta aos 8 quesitos periciais | `9eb89e5aac4f97bff39df95e61e4d0dd8253564bde2c162427337cf8b0d44989` | `28f5c0df5d4ba00f72ff53ebfdd1897f` |
| `25_Relatorio_Final/resultados/` | `relatorio_final.md` | Laudo Pericial Oficial Conclusivo (20 Capítulos) | `662b0d87843804e0e432545a2f00235b4379261955a5f6ced176109dc550ba6b` | `301d5d059024833eae3ae0ac0ef80f2d` |
| `logs/` | `pipeline.log` | Log cronológico auditável de execução do laboratório | `432c25df7f4dc47833a6b5790be9dffc3ba2b3b7e4ef46062f6ce83c07e0c4cb` | `5c6aa1b504938634591f868df32f17ec` |

---

### 4. Artefatos de Inspeção Técnica e Metadados
| Etapa / Local | Arquivo | Finalidade Analítica | SHA-256 |
| :--- | :--- | :--- | :--- |
| `03_Assinatura_Arquivo/resultados/` | `file_signature.json` | Magic bytes (ftyp) e detecção de spoofing de extensão | `192f155990266dafa9745b46d7fa02f5db811807667a4e8d356c9a3dbe88825f` |
| `04_FFprobe/resultados/` | `ffprobe_summary.json` | Parâmetros de container, streams, taxas e codecs | `49918f3b061911a7bbfac373d6d6fce099cec4b3485ddaa758ed06fe2ca27b67` |
| `05_MediaInfo/resultados/` | `mediainfo.json` | Atomização de metadados MediaInfo CLI 26.05 | `2785642841bcfa2520c4f8eaecda3e4811a43d99fae5361097e32402947f6cf6` |
| `06_Container_Codec/resultados/` | `container_codec.json` | Confronto técnico entre contêiner e formato de codec | `98f894f46ff2cd6a966d819fe7aa61da767afc23ee466a008fa34597b57296de` |
| `07_Packets_Frames/resultados/` | `temporal_structure.json` | Cadência PTS/DTS dos 10.247 quadros e gaps | `17988e882e28351f153b1c31d006eaa11a97ee610e1482148d5990ead6d98157` |
| `11_Compressao_Transcodificacao/resultados/` | `compression_analysis.json` | Corte espectral psicoacústico em 15.996 Hz | `6589e64fa73e8532cb2edde0eceee2672aa6ab7f2180ab1ea270a4f2c0b97abf` |
| `12_Descontinuidades_Edicao/resultados/` | `editing_indicators.json` | Detectores de descontinuidade RMS, ZCR e fluxo espectral | `58a7a6da434aca3a3d51cb73ef8758e0f7dd6b1b5d4b8cd817f5f9f09ba7f635` |
| `13_ENF/resultados/` | `enf_analysis.json` | Rastreamento da frequência da rede elétrica (60 Hz) | `391f799f69266ae813d5fed0bb551de4ce3f50747bd650df3deda898fddbc2c1` |
| `16_Diarizacao/resultados/` | `diarization.json` | Agrupamento de turnos vocais por locutor | `5b4bb1c71b9fbd50f6314a4dddde9c79a3ce22f1ef3d0317b69c7e3b3832afea` |
| `21_Proveniencia/resultados/` | `provenance_assessment.json` | Rastreabilidade da proveniência técnica do arquivo | `b3341b53e878e35cf8db6612df54db38980b1e4a6435ca1d07931f6d3f3f50c0` |
| `artigo_secao6/` | `metadados_ffprobe.json` | Extração reprodutível FFprobe 7.1 para a Seção 6 | `732a3b370dac54d99ec5cf2724e1ff044e6ba01cc7f1f2ef1e4717046369b746` |
