# Revisão do Mapa Sanitário — formulário V2

Livro Quarto que apresenta a proposta de revisão da **Ficha de Cadastramento de Unidades Sanitárias** do Mapa Sanitário de Angola (versão 19_01, GEPE/MINSA, Janeiro de 2019) na forma de formulário comentado, para circulação entre revisores.

GEPE/MINSA · OMS Angola · projecto HIIP

## Estrutura

| Ficheiro | Conteúdo |
|---|---|
| `index.qmd` | Nota de apresentação e orientações de leitura — o que é o documento, como ler um quesito, as convenções de desenho, o que ficou parqueado, as decisões em aberto, as pendências a pedir ao MINSA e como enviar comentários |
| `formulario.qmd` | Página de entrada do formulário, com a lista dos capítulos |
| `formulario/` | O formulário em 18 secções, por tema, quesito a quesito: enunciado, opções de resposta e comentário |
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

Todas as secções estão transcritas e organizadas em 18 secções por tema. Os quesitos foram renumerados.
A correspondência com os códigos da versão anterior (usados na matriz de decisão) está em `notas/correspondencia-codigos.md`, fora do livro.

## Orientações para o guião do inquiridor (a escrever)

Regras de recolha já decididas, que o guião do inquiridor deve desenvolver na parte inicial
(como perguntar, como ouvir, como anotar). Os quesitos do livro já as aplicam, salvo indicação em contrário.

**Como perguntar**

- Ler a pergunta tal como está escrita na caixa «Pergunta · ler ao respondente», sem a resumir
  nem a reformular. As opções de resposta só se lêem quando a pergunta o pede.
- As caixas «Instrução ao inquiridor (não ler para o respondente)» nunca se lêem em voz alta.
- Os campos «preenchido pelo inquiridor» e «registado pelo sistema digital» não se perguntam
  (localização pré-carregada da lista prévia, coordenadas, hora). «Confirmar com o respondente»
  quer dizer mostrar o valor pré-carregado e pedir confirmação.
- Uma pergunta de cada vez, uma resposta de cada vez.

**Quem responde: procurar quem sabe**

- Se o respondente não souber a resposta com certeza, o inquiridor pergunta quem na unidade pode
  responder e faz-lhe a pergunta, ou consulta os registos da unidade. Não se aceita um palpite.
- A opção «Não sabe» passa a **«Ninguém na unidade sabe responder»** (código 98, que se mantém;
  decidido a 27/10/2026, ainda por aplicar nas listas e grelhas do livro). É opção só do inquiridor: **não se lê ao respondente** e só se marca depois de
  procurar quem sabe. O próprio rótulo lembra essa regra.
- No sistema digital, marcar 98 abre um campo obrigatório «Quem foi consultado?».
- A proporção de respostas 98 por inquiridor e por unidade é um indicador de qualidade da
  recolha a acompanhar na supervisão. Na análise, o 98 lê-se como falha de informação na gestão
  da unidade, e não como dado em falta.

**Como anotar**

- Quando a pergunta diz «posso ver?», distinguir o que foi observado do que foi apenas referido
  (as opções separam os dois casos).
- «Outro (especificar)» exige o texto. Os números escrevem-se com os dígitos indicados no campo.
- Os saltos indicados nas instruções são obrigatórios. No sistema digital são automáticos.

## Comentários

Cada quesito tem um botão **💬 Comentar**, e cada capítulo um botão para comentários gerais.
O botão abre o Google Forms numa janela por cima do documento, que se fecha sozinha depois do
envio, com o quesito e com o nome, o email e a instituição de quem comenta
já preenchidos (estes três são pedidos uma vez e guardados no navegador). As respostas caem numa
folha de cálculo ligada ao formulário, uma linha por comentário.

Os comentários usam os códigos novos; `notas/correspondencia-codigos.md` permite ligá-los às linhas da matriz, e é por
esse código que os comentários se cruzam com a coluna «Comentários dos revisores». Por isso,
**não renumerar quesitos a meio de uma rodada de revisão**, e não apagar nem recriar os campos
Quesito, Nome e apelido, Email e Instituição do formulário, nem mudar o texto das opções de
Instituição sem o mudar também em `comentar.html` (os identificadores mudariam; ver `comentar.html`).
