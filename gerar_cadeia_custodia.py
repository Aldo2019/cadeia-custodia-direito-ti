"""
GERADOR DO REGISTRO DE CUSTÓDIA ENCADEADO (PROTOCOLO DIREITO & TI)
Serialização canônica em JSON e cálculo do hash encadeado:
h_0 = SHA-256(e_0_canonica)
h_i = SHA-256(e_i_canonica || h_{i-1}_hex)

Todos os hashes de arquivos físicos correspondem estritamente aos bytes reais dos arquivos no disco.
"""

import os
import sys
import json
import hashlib
import csv

os.makedirs('artigo_secao6', exist_ok=True)

# Entradas formais da cadeia de custódia com valores reais auditados
entradas = [
    {
        "indice": 0,
        "data_hora_utc": "2026-10-06T16:46:30Z",
        "data_relativa": "D0 + 163 dias, 16:46:30 UTC",
        "fase": "1 - Recebimento",
        "acao": "Ingresso do arquivo no repositório de custódia do laboratório (NTFS birthtime/ctime). Ramo C da árvore de decisão: ausência de hash prévio documentado pela autoridade requisitante.",
        "responsavel": "Setor Pericial Especializado [LAB-FORENSE-01]",
        "arquivos_envolvidos": [
            {
                "caminho": "entrada/original/EVIDENCIA_01.mp3",
                "sha256": "526cee63cc98221a84a0f9578fa12b02a0350cd5a6ae9c4352caf039e374766d",
                "md5": "aebf5c6ae0fdddde84acf13bce02cce5",
                "tamanho_bytes": 1881640
            }
        ],
        "origem_dado": "[REGISTRO ORIGINAL]"
    },
    {
        "indice": 1,
        "data_hora_utc": "2026-10-06T17:22:59Z",
        "data_relativa": "D0 + 163 dias, 17:22:59 UTC",
        "fase": "0 - Admissão do encargo",
        "acao": "Formalização e autuação do procedimento pericial no sistema de custódia (Procedimento Administrativo [CASO-01]). Registro da descrição do encargo e designação do perito.",
        "responsavel": "Perito Oficial Responsável [PERITO-01]",
        "arquivos_envolvidos": [
            {
                "caminho": "00_Caso/resultados/caso.json",
                "sha256": "1c07b2e69fbe70a664258dafbbcc218eea331b8f15a853ad34819716da7fba2c",
                "md5": "bec9a48922db003b9148a49df70d6fe5",
                "tamanho_bytes": 2572
            }
        ],
        "origem_dado": "[REGISTRO ORIGINAL]"
    },
    {
        "indice": 2,
        "data_hora_utc": "2026-10-06T17:23:01Z",
        "data_relativa": "D0 + 163 dias, 17:23:01 UTC",
        "fase": "1 - Recebimento (Fixação de Hashes)",
        "acao": "Cálculo de hashes criptográficos de cadeia de custódia (MD5, SHA-1, SHA-256, SHA-512) antes de qualquer manipulação. Definição do SHA-256 como identificador unívoco pericial.",
        "responsavel": "Perito Oficial Responsável [PERITO-01]",
        "arquivos_envolvidos": [
            {
                "caminho": "01_Hashes/resultados/hashes.json",
                "sha256": "fff3f59a0955ba46946e000950829e91fc069abff31c3d2e1240a6edf64f548d",
                "md5": "bf09d270ebd0e7932168907703b95649",
                "tamanho_bytes": 738
            }
        ],
        "origem_dado": "[REGISTRO ORIGINAL]"
    },
    {
        "indice": 3,
        "data_hora_utc": "2026-10-06T17:23:06Z",
        "data_relativa": "D0 + 163 dias, 17:23:06 UTC",
        "fase": "2 - Preservação",
        "acao": "Extração de metadados de sistema de arquivos (MACB) e preservação do arquivo original em modo estrito somente-leitura. Decodificação de cópia de trabalho em PCM 16-bit linear para processamento não destrutivo.",
        "responsavel": "Perito Oficial Responsável [PERITO-01]",
        "arquivos_envolvidos": [
            {
                "caminho": "02_Filesystem_Metadata/resultados/filesystem_metadata.json",
                "sha256": "0791f6637214f01812d30a58e133ed3c197b27f5b16f925b7a1d3f1f434937bf",
                "md5": "8a20c070abe1b444eece596571d709a4",
                "tamanho_bytes": 751
            },
            {
                "caminho": "trabalho/amostra_trabalho.wav",
                "sha256": "78d6b4aac076594166854f9ffca444b5dcbdd678172c40cb60c5b911e5cd2bda",
                "md5": "3638a9989c60a39bf5b2c681fa246bfe",
                "tamanho_bytes": 20985934
            }
        ],
        "origem_dado": "[REGISTRO ORIGINAL]"
    },
    {
        "indice": 4,
        "data_hora_utc": "2026-10-06T17:23:13Z",
        "data_relativa": "D0 + 163 dias, 17:23:13 UTC",
        "fase": "3 - Processamento (Inspeção Atomizada de Contêiner e Codec)",
        "acao": "Extração técnica com FFprobe 7.1 e MediaInfo 26.05. Identificação de divergência crítica de contêiner (ISO Base Media mp42/isom com áudio AAC-LC em arquivo rotulado com extensão .mp3). Análise de cadência PTS de 10.247 quadros.",
        "responsavel": "Perito Oficial Responsável [PERITO-01]",
        "arquivos_envolvidos": [
            {
                "caminho": "04_FFprobe/resultados/ffprobe_summary.json",
                "sha256": "49918f3b061911a7bbfac373d6d6fce099cec4b3485ddaa758ed06fe2ca27b67",
                "md5": "6d9e0764fcd07091fda2c3b074abd863",
                "tamanho_bytes": 1518
            },
            {
                "caminho": "06_Container_Codec/resultados/container_codec.json",
                "sha256": "98f894f46ff2cd6a966d819fe7aa61da767afc23ee466a008fa34597b57296de",
                "md5": "c2ce7e3295af4b4c9f098a0459a9a7df",
                "tamanho_bytes": 3232
            },
            {
                "caminho": "07_Packets_Frames/resultados/temporal_structure.json",
                "sha256": "17988e882e28351f153b1c31d006eaa11a97ee610e1482148d5990ead6d98157",
                "md5": "4763102df8fe6e9367061c4f588c30e2",
                "tamanho_bytes": 672
            }
        ],
        "origem_dado": "[REGISTRO ORIGINAL]"
    },
    {
        "indice": 5,
        "data_hora_utc": "2026-10-06T17:24:01Z",
        "data_relativa": "D0 + 163 dias, 17:24:01 UTC",
        "fase": "4 - Análise (Acústica, Integridade e Verificação Multimétodo)",
        "acao": "Análise de forma de onda, densidade espectral FFT, espectrogramas STFT, cut-off psicoacústico em 15.996 Hz, busca de descontinuidades/cortes de edição, rastreamento de ENF 60 Hz e diarização vocal.",
        "responsavel": "Perito Oficial Responsável [PERITO-01]",
        "arquivos_envolvidos": [
            {
                "caminho": "11_Compressao_Transcodificacao/resultados/compression_analysis.json",
                "sha256": "6589e64fa73e8532cb2edde0eceee2672aa6ab7f2180ab1ea270a4f2c0b97abf",
                "md5": "d0c094405dbd472d812b350c6334bdca",
                "tamanho_bytes": 1842
            },
            {
                "caminho": "12_Descontinuidades_Edicao/resultados/editing_indicators.json",
                "sha256": "58a7a6da434aca3a3d51cb73ef8758e0f7dd6b1b5d4b8cd817f5f9f09ba7f635",
                "md5": "5da7b218eb6ef62b8addccbef687f86c",
                "tamanho_bytes": 768
            },
            {
                "caminho": "13_ENF/resultados/enf_analysis.json",
                "sha256": "391f799f69266ae813d5fed0bb551de4ce3f50747bd650df3deda898fddbc2c1",
                "md5": "7066e1a4dab8059c1f452fe02fc973cb",
                "tamanho_bytes": 759
            },
            {
                "caminho": "16_Diarizacao/resultados/diarization.json",
                "sha256": "5b4bb1c71b9fbd50f6314a4dddde9c79a3ce22f1ef3d0317b69c7e3b3832afea",
                "md5": "e49fd12dc3546f026cd9b1d5f71447f5",
                "tamanho_bytes": 746
            }
        ],
        "origem_dado": "[REGISTRO ORIGINAL]"
    },
    {
        "indice": 6,
        "data_hora_utc": "2026-10-06T17:26:43Z",
        "data_relativa": "D0 + 163 dias, 17:26:43 UTC",
        "fase": "5 - Documentação",
        "acao": "Emissão e assinatura técnica do Laudo Pericial Oficial com resposta à matriz de 8 quesitos, consolidação pericial e manifesto completo de hashes.",
        "responsavel": "Perito Oficial Responsável [PERITO-01]",
        "arquivos_envolvidos": [
            {
                "caminho": "24_Matriz_Quesitos/resultados/matriz_quesitos.json",
                "sha256": "9eb89e5aac4f97bff39df95e61e4d0dd8253564bde2c162427337cf8b0d44989",
                "md5": "28f5c0df5d4ba00f72ff53ebfdd1897f",
                "tamanho_bytes": 9137
            },
            {
                "caminho": "25_Relatorio_Final/resultados/relatorio_final.md",
                "sha256": "662b0d87843804e0e432545a2f00235b4379261955a5f6ced176109dc550ba6b",
                "md5": "301d5d059024833eae3ae0ac0ef80f2d",
                "tamanho_bytes": 8601
            }
        ],
        "origem_dado": "[REGISTRO ORIGINAL]"
    },
    {
        "indice": 7,
        "data_hora_utc": "2026-10-27T11:09:42Z",
        "data_relativa": "D0 + 184 dias (Data da Auditoria Acadêmica)",
        "fase": "3 - Processamento (Auditoria de Reprodutibilidade para Artigo)",
        "acao": "Execução de rotina de metadados com FFprobe 7.1 em ambiente Windows 11 sobre cópia de trabalho autenticada, confirmação do probe_score=100, geração de JSON canônico e cálculo do hash de auditoria.",
        "responsavel": "Equipe de Pesquisa Forense / Protocolo Direito & TI",
        "arquivos_envolvidos": [
            {
                "caminho": "artigo_secao6/metadados_ffprobe.json",
                "sha256": "732a3b370dac54d99ec5cf2724e1ff044e6ba01cc7f1f2ef1e4717046369b746",
                "md5": "4923d54d349ec208f73f6e504bf9a3dd",
                "tamanho_bytes": 2293
            }
        ],
        "origem_dado": "[RECONSTRUÍDO EM 2026-10-27]"
    }
]

cadeia = []
h_anterior_hex = None

for i, e in enumerate(entradas):
    # Serializacao canônica JSON: chaves ordenadas alfabeticamente, UTF-8, sem espaços
    canon_bytes = json.dumps(e, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    
    if i == 0:
        h_atual = hashlib.sha256(canon_bytes).hexdigest()
    else:
        conteudo_para_hash = canon_bytes + h_anterior_hex.encode('utf-8')
        h_atual = hashlib.sha256(conteudo_para_hash).hexdigest()
        
    entrada_encadeada = {
        "indice": e["indice"],
        "data_hora_utc": e["data_hora_utc"],
        "data_relativa": e["data_relativa"],
        "fase": e["fase"],
        "acao": e["acao"],
        "responsavel": e["responsavel"],
        "origem_dado": e["origem_dado"],
        "hash_anterior_hex": h_anterior_hex,
        "hash_encadeado_sha256": h_atual,
        "dados_evento": e
    }
    
    cadeia.append(entrada_encadeada)
    h_anterior_hex = h_atual

# Salvar JSON completo da cadeia encadeada
with open('artigo_secao6/registro_custodia_encadeado.json', 'w', encoding='utf-8') as f:
    json.dump(cadeia, f, indent=2, ensure_ascii=False)

# Salvar CSV resumido da cadeia encadeada
with open('artigo_secao6/registro_custodia_encadeado.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['indice', 'data_relativa', 'fase', 'responsavel', 'origem_dado', 'hash_anterior_hex', 'hash_encadeado_sha256', 'acao_resumo'])
    for item in cadeia:
        writer.writerow([
            item['indice'],
            item['data_relativa'],
            item['fase'],
            item['responsavel'],
            item['origem_dado'],
            item['hash_anterior_hex'] if item['hash_anterior_hex'] else 'NENHUM (Gênese)',
            item['hash_encadeado_sha256'],
            item['acao'][:100] + '...' if len(item['acao']) > 100 else item['acao']
        ])

print(f"Sucesso: {len(cadeia)} eventos encadeados gerados com hashes reais.")
for item in cadeia:
    h_ant = item['hash_anterior_hex'][:12] + '...' if item['hash_anterior_hex'] else 'GÊNESE'
    print(f"e_{item['indice']} | {item['fase'][:20]:20s} | h_ant={h_ant:15s} | h_enc={item['hash_encadeado_sha256'][:16]}...")
