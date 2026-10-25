# Revisão do Mapa Sanitário — formulário V2

Livro Quarto que apresenta a proposta de revisão da **Ficha de Cadastramento de Unidades Sanitárias** do Mapa Sanitário de Angola (versão 19_01, GEPE/MINSA, Janeiro de 2019) na forma de formulário comentado, para circulação entre revisores.

GEPE/MINSA · OMS Angola · projecto HIIP

## Estrutura

| Ficheiro | Conteúdo |
|---|---|
| `index.qmd` | Nota de apresentação e orientações de leitura — o que é o documento, como ler um quesito, as convenções de desenho, o que ficou parqueado, as decisões em aberto, as pendências a pedir ao MINSA e como enviar comentários |
| `formulario.qmd` | Página de entrada do formulário, com a lista dos capítulos |
| `formulario/` | O formulário, um capítulo por secção (a secção 7 dividida em 7.1, 7.2 e 7.3, com 7.4 e 7.5 juntas num capítulo próprio), quesito a quesito: enunciado, opções de resposta e comentário sobre o que acontece com cada resposta |
| `_legenda.qmd` | Legenda das caixas e etiquetas, incluída no topo de cada capítulo |
| `comentar.html` | Botão «Comentar» ao lado de cada quesito, que abre o Google Forms com o quesito, o nome e o email preenchidos; o link do formulário configura-se em `FORMULARIO` |
| `_quarto.yml` | Configuração do livro |
| `estilos.css` | Estilos do documento |

## Como construir

Requer [Quarto](https://quarto.org) instalado.

```bash
quarto render        # gera o sítio em docs/
quarto preview       # pré-visualização com recarga automática
```

O resultado é escrito em `docs/`, pronto para publicação em GitHub Pages
(Settings → Pages → Source: branch `main`, pasta `/docs`).

## Fonte

O conteúdo deste documento é gerado a partir da **matriz de decisão da adaptação para V2**,
uma folha de cálculo com uma linha por quesito e as colunas: domínio, código, item original,
opções de resposta originais, item proposto, opções de resposta propostas, tipo de mudança,
nº de campos, indicador gerado, modo de recolha, explicação, comentários dos revisores,
decisão, por quem e data.

**A matriz é a fonte; este documento é a face legível dela.** Qualquer alteração deve ser
feita primeiro na matriz e só depois transcrita para aqui, para que as duas não divirjam.

## Estado

Transcritos: secções 0 a 12 (identificação da recolha, localização, propriedade e gestão,
população e referência, construção, estado físico, água e saneamento, serviços oferecidos,
recursos cama, aparelhos médico-cirúrgicos, meios de transporte, responsáveis e contactos).

Por transcrever: domínio 13 (conectividade), identificado em `formulario/13-por-transcrever.qmd`
com o respectivo volume.

## Comentários

Cada quesito tem um botão **💬 Comentar**, e cada capítulo um botão para comentários gerais.
O botão abre o Google Forms numa janela por cima do documento, que se fecha sozinha depois do
envio, com o quesito e com o nome, o email e a instituição de quem comenta
já preenchidos (estes três são pedidos uma vez e guardados no navegador). As respostas caem numa
folha de cálculo ligada ao formulário, uma linha por comentário.

Cada quesito deste documento tem o mesmo código da linha correspondente da matriz, e é por
esse código que os comentários se cruzam com a coluna «Comentários dos revisores». Por isso,
**não renumerar quesitos a meio de uma rodada de revisão**, e não apagar nem recriar os campos
Quesito, Nome e apelido, Email e Instituição do formulário, nem mudar o texto das opções de
Instituição sem o mudar também em `comentar.html` (os identificadores mudariam; ver `comentar.html`).
