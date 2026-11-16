"""Estimativa do tempo de aplicação por secção: recolha com visita ou autorreferida, portas abertas ou fechadas.

Conta os campos de cada secção a partir do texto (grelhas, opções de resposta, campos de verificação),
marca como condicionais os quesitos que dependem de uma porta («Perguntar só se…», saltos «passar a…»),
aplica os segundos por tipo de campo de T e escreve a grelha no cabeçalho de cada secção e o total
na página «Novo formulário». Correr de novo sempre que o formulário mudar:

    python ferramentas/tempo_aplicacao.py
"""
import glob
import math
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# segundos por campo
T = {
    'visita': {'escolha': 15, 'celula': 8, 'numero': 20, 'verif_q': 45, 'verif_cel': 15, 'abertura': 30},
    'auto': {'escolha': 8, 'celula': 5, 'numero': 15, 'verif_q': 0, 'verif_cel': 0, 'abertura': 0},
}


def tira_ocultos(x):
    x = re.sub(r'^::: \{\.hhfa.*?^:::$', '', x, flags=re.S | re.M)
    x = re.sub(r'^::: \{\.nota.*?^:::$', '', x, flags=re.S | re.M)
    x = re.sub(r'^::: \{\.tempo-aplicacao.*?^:::$', '', x, flags=re.S | re.M)
    x = re.sub(r'<details.*?</details>', '', x, flags=re.S)
    return x


def caixa(b, cls):
    return re.findall(r'^::: \{\.' + cls + r'[^}]*\}\n(.*?)^:::$', b, flags=re.S | re.M)


def campos(b, verif_bloco):
    """Devolve contagens: escolha, celula, numero, verif_q, verif_cel."""
    c = dict(escolha=0, celula=0, numero=0, verif_q=0, verif_cel=0)
    corpo = b.split('\n', 1)[1] if '\n' in b else ''
    cods = set(re.findall(r'\*\*(\d+(?:\.\d+)+)\*\*', corpo))
    resp = caixa(b, 'respostas')
    num_resp = bool(resp and re.search(r'Número|número|dígitos|Texto|texto|Minutos|Quilómetros|Ano, 4|hh:mm|01 a', resp[0]))
    grelhas = caixa(b, 'grelha')
    linhas_tab = [l for g in grelhas for l in g.split('\n') if l.startswith('|')]
    if grelhas and not linhas_tab and cods:
        c['verif_cel' if verif_bloco else ('numero' if num_resp else 'celula')] += len(cods)
        return c
    if grelhas:
        for g in grelhas:
            linhas = [l for l in g.split('\n') if l.startswith('|')]
            if len(linhas) < 3:
                continue
            cab = [x.strip() for x in linhas[0].strip('|').split('|')]
            verif_cols = {i for i, h in enumerate(cab) if 'erificação' in h}
            for l in linhas[2:]:
                cel = [x.strip() for x in l.strip('|').split('|')]
                if any(x.startswith('**') for x in cel) and all(x == '' or x.startswith('**') for x in cel):
                    continue
                resp_c = [(i, x) for i, x in enumerate(cel) if i < len(cab) and cab[i] not in ('Código', 'N.º', '')]
                marcadas = [(i, x) for i, x in resp_c if '☐' in x or '\\_' in x or x == '']
                if not marcadas:
                    continue
                if any(x == '☐' for _, x in marcadas) and all(x == '☐' for _, x in marcadas if x):
                    c['verif_cel' if verif_bloco else 'celula'] += 1
                    continue
                for i, x in marcadas:
                    if verif_bloco or i in verif_cols:
                        c['verif_cel'] += 1
                    elif '☐' in x:
                        c['celula'] += 1
                    else:
                        c['numero'] += 1
        return c
    if resp:
        n = len(cods) if len(cods) > 1 else max(1, len(re.findall(r'^\*\*[^*]+:\*\*', resp[0], flags=re.M)))
        if verif_bloco:
            c['verif_q'] += n
        elif num_resp or len(cods) > 1:
            c['numero'] += n
        else:
            c['escolha'] += n
        return c
    if caixa(b, 'enunciado'):
        c['verif_q' if verif_bloco else 'numero'] += max(1, len(cods))
    return c


def chave(cod):
    return [int(x) if x.isdigit() else x for x in cod.split('.')]


res = {}
for f in sorted(glob.glob('formulario/[012][0-9]-*.qmd')):
    sec = int(os.path.basename(f)[:2])
    x = tira_ocultos(open(f, encoding='utf-8').read().replace('\r\n', '\n'))
    blocos = re.split(r'(?=^#{2,3} \d)', x, flags=re.M)[1:]
    qs = []
    for b in blocos:
        cod = re.match(r'#{2,3} (\d+(?:\.\d+)*)', b).group(1)
        tit = b.split('\n')[0]
        instr = ' '.join(caixa(b, 'instrucao'))
        verif = 'só na recolha com visita' in tit or 'Campo de verificação' in b or 'Pergunta de verificação' in b
        cond = bool(re.search(r'Perguntar só|Fazer só se|— Só se|Só na recolha presencial|Perguntar apenas|só nas colunas', instr))
        saltos = re.findall(r'(?:saltar|passar)(?: para| a| à)? ?(?:a )?(secção \d+|\d+(?:\.\d+)*)', instr)
        fim = bool(re.search(r'terminar a secção', instr, flags=re.I))
        qs.append(dict(cod=cod, cond=cond, saltos=saltos, fim=fim, c=campos(b, verif)))
    # portas: o que fica entre a porta e o destino do salto é condicional
    for i, q in enumerate(qs):
        for alvo in q['saltos'] + (['secção'] if q['fim'] else []):
            if alvo.startswith('secção'):
                j = len(qs)
            else:
                j = next((k for k in range(i + 1, len(qs)) if qs[k]['cod'] == alvo or qs[k]['cod'].startswith(alvo + '.') or chave(qs[k]['cod']) >= chave(alvo)), len(qs))
            for k in range(i + 1, j):
                qs[k]['cond'] = True
    tot = {}
    for modo in ('visita', 'auto'):
        for portas in ('abertas', 'fechadas'):
            s = T[modo]['abertura']
            for q in qs:
                if portas == 'fechadas' and q['cond']:
                    continue
                for k, n in q['c'].items():
                    s += n * T[modo][k]
            tot[f'{modo}_{portas}'] = max(1, math.ceil(s / 60))
    res[sec] = tot
    print(f"{sec:2d} | visita {tot['visita_abertas']:4d} / {tot['visita_fechadas']:3d} | autorreferida {tot['auto_abertas']:4d} / {tot['auto_fechadas']:3d}")
soma = {k: sum(r[k] for r in res.values()) for k in ('visita_abertas', 'visita_fechadas', 'auto_abertas', 'auto_fechadas')}
print('TOTAL', soma)


def tabela(r, horas=False):
    def v(k):
        if not horas:
            return str(r[k])
        return f'{r[k]} (cerca de {r[k] / 60:.1f} horas)'.replace('.', ',')
    return ('| Forma de recolha | Todas as portas abertas | Todas as portas fechadas |\n'
            '|---|:-:|:-:|\n'
            f"| Com visita (presencial, com inquiridor) | {v('visita_abertas')} | {v('visita_fechadas')} |\n"
            f"| Autorreferida | {v('auto_abertas')} | {v('auto_fechadas')} |\n")


ANTIGA = re.compile(r'^::: \{\.tempo-aplicacao\}\n.*?^:::\n\n', flags=re.S | re.M)
for f in sorted(glob.glob('formulario/[012][0-9]-*.qmd')):
    sec = int(os.path.basename(f)[:2])
    b = open(f, 'rb').read().decode('utf-8')
    nl = '\r\n' if '\r\n' in b else '\n'
    x = ANTIGA.sub('', b.replace('\r\n', '\n'))
    m = re.search(r'^<details class="medir-seccao">', x, flags=re.M) or re.search(r'^## ', x, flags=re.M)
    bloco = '::: {.tempo-aplicacao}\n**Tempo estimado de aplicação, em minutos**\n\n' + tabela(res[sec]) + ':::\n\n'
    x = x[:m.start()] + bloco + x[m.start():]
    open(f, 'wb').write(x.replace('\n', nl).encode('utf-8'))

p = 'formulario.qmd'
b = open(p, 'rb').read().decode('utf-8')
nl = '\r\n' if '\r\n' in b else '\n'
x = re.sub(r'^## Tempo de aplicação\n.*?(?=^## |\Z)', '', b.replace('\r\n', '\n'), flags=re.S | re.M).rstrip('\n') + '\n'
x += ('\n## Tempo de aplicação\n\n'
      'Estimativa do tempo de aplicação do formulário inteiro, em minutos. Cada secção mostra a sua no cabeçalho.\n\n'
      '::: {.tempo-aplicacao}\n' + tabela(soma, horas=True) + ':::\n\n'
      '**Como se calcula.** Contam-se os campos de cada secção e aplica-se um tempo por tipo de campo. '
      'Na recolha com visita: 15 segundos por pergunta de escolha, 8 por linha ou caixa de grelha, 20 por número ou texto, '
      '45 por pergunta de verificação e 15 por caixa de verificação numa grelha, mais 30 segundos de abertura por secção. '
      'Na recolha autorreferida: 8, 5 e 15 segundos, sem verificação. '
      '«Portas abertas» é a unidade que responde «Sim» a todas as perguntas que abrem outras; «portas fechadas», a que responde «Não» a todas e salta tudo o que delas depende. '
      'Uma unidade real fica entre os dois valores. Não se conta o tempo de deslocação entre serviços nem o de procurar registos.\n')
open(p, 'wb').write(x.replace('\n', nl).encode('utf-8'))
print('grelhas escritas')
