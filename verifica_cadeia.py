"""
SCRIPT OFICIAL DE AUDITORIA E RECALCULO DA CADEIA DE CUSTÓDIA CRIPTOGRÁFICA
Protocolo de Cadeia de Custódia Digital - Revista Direito & TI

Este script realiza a verificação formal de integridade da cadeia de custódia encadeada:
1. Carrega o registro estruturado (JSON canônico);
2. Recalcula a serialização canônica de cada entrada e_i (chaves ordenadas, sem espaços, UTF-8);
3. Recalcula h_0 = SHA-256(e_0_canonica);
4. Recalcula h_i = SHA-256(e_i_canonica || h_{i-1}_hex);
5. Compara cada hash recalculado com o hash registrado;
6. Valida a higidez dos arquivos locais referenciados na cadeia (recalculando seus SHA-256);
7. Emite relatório formal acusando qualquer divergência ou confirmando conformidade estrita.
"""

import os
import sys
import json
import hashlib

def verificar_cadeia(caminho_json=None):
    if caminho_json is None:
        caminhos_tentativa = [
            os.path.join("artigo_secao6", "registro_custodia_encadeado.json"),
            "registro_custodia_encadeado.json"
        ]
        for c in caminhos_tentativa:
            if os.path.exists(c):
                caminho_json = c
                break
                
    if not caminho_json or not os.path.exists(caminho_json):
        print(f"[ERRO CRÍTICO] Arquivo de registro de custódia não encontrado em: {caminho_json}")
        return False

    print("=" * 80)
    print("AUDITORIA CRIPTOGRÁFICA DA CADEIA DE CUSTÓDIA (PROTOCOLO DIREITO & TI)")
    print(f"Arquivo analisado: {caminho_json}")
    print("=" * 80)

    with open(caminho_json, "r", encoding="utf-8") as f:
        cadeia = json.load(f)

    total_eventos = len(cadeia)
    print(f"Total de eventos na cadeia: {total_eventos}\n")

    h_anterior_hex = None
    divergencias = []

    for i, item in enumerate(cadeia):
        indice = item["indice"]
        dados_evento = item["dados_evento"]
        hash_registrado = item["hash_encadeado_sha256"]
        hash_ant_registrado = item["hash_anterior_hex"]

        # 1. Verificar consistência do hash anterior
        if i == 0:
            if hash_ant_registrado is not None:
                divergencias.append(f"Evento e_0: hash anterior deveria ser nulo, mas contém '{hash_ant_registrado}'.")
        else:
            if hash_ant_registrado != h_anterior_hex:
                divergencias.append(
                    f"Evento e_{indice}: elo quebrado! Hash anterior registrado ({hash_ant_registrado}) "
                    f"difere do calculado para e_{indice-1} ({h_anterior_hex})."
                )

        # 2. Recalcular serialização canônica
        canon_bytes = json.dumps(dados_evento, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

        # 3. Recalcular hash encadeado
        if i == 0:
            h_calculado = hashlib.sha256(canon_bytes).hexdigest()
        else:
            conteudo = canon_bytes + h_anterior_hex.encode('utf-8')
            h_calculado = hashlib.sha256(conteudo).hexdigest()

        # 4. Comparar com o hash registrado
        if h_calculado != hash_registrado:
            divergencias.append(
                f"Evento e_{indice}: hash encadeado divergente!\n"
                f"  Registrado: {hash_registrado}\n"
                f"  Calculado:  {h_calculado}"
            )
            status_evento = "FALHA / DIVERGÊNCIA"
        else:
            status_evento = "OK"

        print(f"[{status_evento:18s}] e_{indice:02d} | Fase: {item['fase']:<32s} | Hash: {h_calculado[:24]}...")
        h_anterior_hex = h_calculado

    print("\n" + "-" * 80)
    print("VERIFICAÇÃO DE HASHES DOS ARQUIVOS FÍSICOS REFERENCIADOS:")
    print("-" * 80)
    
    arquivos_verificados = 0
    falhas_arquivos = 0

    mapeamento_caminhos = {
        "entrada/original/EVIDENCIA_01.mp3": os.path.join("entrada", "original", "AUD-20260426-WA0006.mp3")
    }

    for item in cadeia:
        for arq in item["dados_evento"].get("arquivos_envolvidos", []):
            caminho_ref = arq["caminho"]
            caminho_real = mapeamento_caminhos.get(caminho_ref, caminho_ref)
            sha_esperado = arq["sha256"]
            
            if os.path.exists(caminho_real):
                with open(caminho_real, "rb") as fa:
                    sha_real = hashlib.sha256(fa.read()).hexdigest()
                arquivos_verificados += 1
                if sha_real == sha_esperado:
                    print(f"[ARQUIVO ÍNTEGRO] {caminho_real:<55s} | SHA-256: {sha_real[:16]}... (OK)")
                else:
                    print(f"[ALERTA ADULTERAÇÃO] {caminho_real}\n  Esperado: {sha_esperado}\n  Obtido:   {sha_real}")
                    falhas_arquivos += 1
            else:
                print(f"[ARQUIVO AUSENTE] {caminho_real}")

    print("=" * 80)
    if not divergencias and falhas_arquivos == 0:
        print("RESULTADO DA AUDITORIA: CADEIA DE CUSTÓDIA 100% ÍNTEGRA E VÁLIDA!")
        print(f"Total de {total_eventos} eventos periciais encadeados matematicamente sem qualquer quebra.")
        print(f"Total de {arquivos_verificados} arquivos auditados com hashes correspondentes.")
        print("=" * 80)
        return True
    else:
        print(f"[FALHA NA AUDITORIA] Foram encontradas {len(divergencias)} divergências de encadeamento e {falhas_arquivos} falhas de arquivos:")
        for d in divergencias:
            print(f"  - {d}")
        print("=" * 80)
        return False

if __name__ == "__main__":
    caminho = sys.argv[1] if len(sys.argv) > 1 else None
    sucesso = verificar_cadeia(caminho)
    sys.exit(0 if sucesso else 1)
