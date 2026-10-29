# Notas por quesito

Notas de justificação de cada quesito (porque mudou, de onde vem, para que serve), retiradas do texto dos revisores a 27/10/2026. No livro continuam presentes mas escondidas; aparecem com `?hhfa=1`. Atenção: a 27/10/2026 criou-se a secção 11 (doenças crónicas não transmissíveis) e as secções 11 a 19 passaram a 12 a 18; os códigos 10.B, 10.C e 10.D deste arquivo correspondem hoje a 11.1 a 11.9 (ver `correspondencia-codigos.md`).

## Secção 1 — Identificação e finalização da recolha

### 1.1 Data desta recolha

**Porque mudou.** As três caixas e os códigos mantêm-se. O enunciado passa a dizer que a data é a desta recolha; a data da visita anterior, que o Guião também prevê (folha 2), passa para 1.6.

**Verificação a programar.** A data não pode ser posterior à data de carregamento no sistema.

### 1.2 Hora de início

**Para que serve.** Dá a duração do preenchimento, por tipo de unidade e por forma de recolha, para planear as rondas seguintes e assinalar fichas preenchidas em tempo demasiado curto.

### 1.3 Hora de fim

**Verificação a programar.** A hora de fim não pode ser anterior à hora de início.

### 1.4 Forma de recolha

**É o campo que faz funcionar toda a arquitectura da proposta.** A grelha de verificação da secção 9 e as colunas «a funcionar» das secções 8 e 9 aplicam-se apenas às unidades visitadas. Sem este campo não é possível saber, na análise, se uma célula vazia significa «não tem» ou «não foi verificado».

**Consequência analítica.** Permite calcular os indicadores com o denominador correcto — apenas as unidades em que a verificação foi efectivamente possível — em vez de misturar observação e declaração numa mesma percentagem. Uma caixa resolve isto para todo o instrumento.

### 1.6 Data da visita anterior

**Para que serve.** Cruzada com 1.1, dá o intervalo entre visitas, e identifica as unidades que nunca foram visitadas. O Guião já prevê esta informação (folha 2).

**Verificação a programar.** Se 1.6.4 estiver marcada, 1.6.1 a 1.6.3 ficam vazias, e vice-versa.

### 1.7 Quem recolheu os dados

**Para que serve.** Permite devolver dúvidas a quem recolheu os dados e ler a qualidade dos dados por equipa de recolha.

### 1.8 Responsável da unidade sanitária

**Para que serve.** Identifica quem responde pela unidade: é a pessoa a contactar quando uma dúvida diz respeito ao conjunto dos dados e não a um quesito, e pode não ser quem respondeu ao inquérito. Passa a ser o primeiro quesito da secção.

### 1.9 Pessoas que responderam ao inquérito

**Porque mudou.** As cinco linhas e as quatro colunas da Ficha mantêm-se. O código passa de 1.8 para 1.9, para que o responsável da unidade abra a secção. A quinta coluna é nova: quando um valor precisar de ser confirmado, diz a quem telefonar e sobre que parte da ficha. O Guião já distingue «as pessoas que preencheram ou comunicaram os dados» (folha 20).

### 1.10 Responsável do preenchimento

Mantém-se exactamente como está, incluindo o título e os códigos. Enquanto 1.9 nomeia todas as pessoas que responderam, até cinco, 1.10 identifica a pessoa que responde pela ficha no seu todo.

### Pendência desta secção

**Lista de categorias profissionais (1.8.3).** A lista fechada deve seguir a nomenclatura nacional das carreiras da saúde. A mesma lista servirá também o futuro bloco sobre o pessoal da unidade, pelo que convém defini-la uma só vez com o GEPE e usá-la nos dois lugares.

## Secção 2 — Localização

### 2.1 a 2.5 Localização administrativa e nome da unidade

**O que muda.** Os campos mantêm-se. Com a lista prévia carregada no sistema, deixam de ser escritos de novo em cada ronda: confirmam-se e corrigem-se. As unidades encontradas no terreno que não constam da lista entram como unidades novas.

### 2.7 Categoria da unidade

É o estratificador principal de toda a análise: é por esta caixa que todos os indicadores se leem por tipo de unidade. Mantém-se exactamente como está. A categoria não decide nenhum salto do formulário.

### 2.8 e 2.9 Coordenadas

**Porque mudou.** As duas caixas mantêm-se. Ao formato que o Guião fixa — «em graus decimais» — acrescenta-se um protocolo de leitura: o local onde se faz a leitura e o tempo de estabilização do aparelho. Sem protocolo, a mesma unidade pode ficar a 200 metros de si mesma entre duas rondas, e os cálculos de distância e de acesso geográfico deixam de ser comparáveis.

### 2.10 Precisão da leitura

Uma caixa que qualifica a leitura anterior. Uma coordenada com precisão de 4 metros e uma com precisão de 300 metros não servem para o mesmo, e esta caixa permite distingui-las no ficheiro.

### 2.11 Zona urbana, rural ou periurbana

**Para que serve.** Uma caixa própria dispensa inferir esta informação da localização administrativa, o que é difícil nas periferias das capitais provinciais, e permite desagregar por urbano e rural todos os indicadores do formulário.

## Secção 3 — População e sistema de referência

### 3.1 População adstrita

**Porque mudou.** A caixa é a mesma. O que se acrescenta é a palavra «directa» e a instrução que a explica, porque sem elas a mesma população é contada várias vezes ao longo da árvore de referência — o hospital municipal declara a população do município, e cada centro de saúde do município declara a sua. Somando as fichas, a população do país aparece duas ou três vezes. O código 999998 para «não dispõe de estimativa» evita que a ausência de dado seja registada como zero.

**Consequência.** É o denominador de 27 indicadores, incluindo as 20 densidades de pessoal por habitante.

### 3.1.1 Origem da estimativa

**Para que serve.** Duas caixas que qualificam o denominador de 27 indicadores. Uma densidade de enfermeiros por habitante calculada sobre uma projecção do INE de 2024 e outra calculada sobre um recenseamento feito pela unidade em 2016 não são comparáveis, e estas duas caixas permitem distingui-las.

### 3.1.3 Unidades que referem para esta

É o total de controlo da árvore de referência: permite confrontar o que cada unidade declara receber com o que as outras declaram enviar. Divergências entre os dois lados são informação sobre o funcionamento real da rede, não erros a corrigir.

### 3.2.1 a 3.2.3 Nó superior da referência

**Porque mudou.** A Ficha oferece duas filas para duas unidades de referência. A proposta dá a cada uma um papel próprio e separa o nó superior, que é obrigatório e único, da referência lateral de 3.3, que é opcional e definida por grupo de doentes. O acrescento com mais consequência é **3.2.3, o código**: com ele, a árvore de referência nacional passa a ser reconstruível a partir das fichas, sem depender da grafia com que cada unidade escreve o nome do hospital de destino.

### 3.2.4 Meio de transporte ao nó superior

**O meio de transporte** (3.2.4) é novo e pergunta pelo que de facto se usa, não pelo que deveria usar-se. A opção 5, transporte pago pelo doente, e a opção 6, a pé ou em maca, são respostas frequentes no terreno, que passam a ter opção própria.

### 3.2.5 Distância total ao nó superior

**Porque mudou.** Os quatro campos da Ficha mantêm-se no essencial e ganham precisões. A decomposição em asfalto e picada, já pedida pelo Guião, mantém-se; acrescenta-se a instrução de que a distância é pela estrada e não em linha recta, para que os números sejam comparáveis entre unidades.

### 3.2.7 Quilómetros em estrada de terra ou picada

**Verificação a programar.** A soma de 3.2.6 e 3.2.7 deve ser igual a 3.2.5.

### 3.2.9 Tempo ao nó superior na época das chuvas

**O acrescento decisivo é a época das chuvas** (3.2.9): numa boa parte do país a referência que leva 40 minutos em Agosto leva três horas em Fevereiro, ou não é possível — e é essa a situação que um plano de investimentos precisa de ver. O código 997 regista a intransitabilidade sem a confundir com um tempo muito longo.

### 3.3.1 Grupo de doentes com referência lateral

**Porque mudou.** A segunda fila da Ficha passa a ser uma referência qualificada: além de saber para onde, passa a saber-se **para quem**. O próprio Guião dá o exemplo — o envio das grávidas ao Centro Materno Infantil —, e a proposta passa a recolher o motivo, para que a segunda unidade de referência possa ser interpretada.

### 3.3.5 Distância à referência lateral

**Regra de desenho.** Se o motivo indicado em 3.3.1 for obstetrícia e maternidade, aplica-se o protocolo completo de distância, como no nó superior — asfalto, picada e época das chuvas. É a referência em que o tempo decide o desfecho.

### 3.4 a 3.9 Funcionamento do sistema de referência

Fica para o bloco de gestão o funcionamento do sistema de referência: se existe sistema estabelecido, se há normas de referência e de contrarreferência, se as referências feitas são registadas e se há informação de retorno. O quesito 3.9, sobre o acesso a viatura em condições de funcionamento e a motorista 24 horas, obtém-se também dos quesitos 20.1 e 20.1.1, nos serviços gerais.

São cinco medidas sobre o funcionamento da referência. Duas são declaradas — a existência do sistema e a informação de retorno —, e três pedem para ver o documento: as normas de referência, as normas de contrarreferência e o registo das referências feitas. Em recolha sem visita, estes três ficam vazios para a unidade. É candidato natural a entrar nesta ronda, se a revisão o considerar.

## Secção 4 — Construção e estado físico

### 4.1 Número de edifícios da unidade

**Porque mudou.** Mantém-se a regra do Guião — «sem contar as Residências dos Trabalhadores» — e acrescenta-se a regra para dois casos frequentes no terreno: os edifícios de apoio contam, as ruínas não contam. Assim, duas unidades iguais dão o mesmo número.

### 4.3 Residências dos trabalhadores

**Porque mudou.** Acrescenta-se «ou sob a sua responsabilidade», porque há unidades com residências fora do recinto que são, para todos os efeitos, suas. É informação com peso directo na retenção de pessoal em zonas rurais.

### 4.4 Superfície coberta das residências

**A mesma medida nos dois quesitos.** A Ficha pede a «superfície» dos edifícios da unidade em 4.2 e a «superfície útil» das residências em 4.4, que são medidas diferentes — área coberta e área interior utilizável. A proposta usa a área coberta nos dois, dita na própria pergunta, para que 4.2 e 4.4 sejam comparáveis entre si e com a soma dos metros quadrados de 4.9. *Decisão aprovada a 15/10.*

### 4.5 Ano de construção

No ano (4.5) acrescenta-se a instrução sobre reconstrução, que decide o caso dos edifícios coloniais reabilitados, e o código 9998, porque o campo é «não obrigatório» e fica em branco com frequência — e um branco não se distingue de um desconhecimento.

### 4.6 Período de construção

As cinco categorias do período (4.6) mantêm-se sem alteração: correspondem a ciclos reconhecíveis da história e do investimento público angolanos, e mudá-las quebraria a série das quatro edições. Acrescenta-se apenas o código 98.

### 4.7 Material de construção

**Porque mudou.** A opção «tijolo – bloco» desdobra-se em duas, porque são materiais com durabilidade, comportamento térmico e custo de reabilitação diferentes. As cinco categorias passam a seis, e a conversão para a série histórica é directa: as novas 3 e 4 juntam-se na antiga 3. A instrução de predominância resolve o caso do edifício com paredes de materiais diferentes. *Decisão aprovada a 15/10.*

### 4.8 Estado físico do edifício principal

As quatro categorias mantêm-se com a redacção da Ficha. O que muda é o enunciado, que nomeia os sete elementos a considerar, para que todos os inquiridores apliquem os critérios do Guião aos mesmos elementos.

### 4.8.1 a 4.8.7 Estado por elemento construtivo

**O que acontece com estas respostas.** Sete caixas que transformam o juízo de 4.8 em dado. A caixa de 4.8 continua a ser respondida, e passa a poder ser confrontada com os sete elementos que a definem. Mais importante para o planeamento: **uma unidade classificada globalmente como «reabilitação ligeira» pode ter a cobertura a precisar de reconstrução** — e é essa a informação que decide uma ordem de trabalhos, não a classificação global.

**Nota de fronteira.** Um levantamento de defeitos sala a sala seria um exercício diferente e muito mais pesado. Não é comparável e não foi adoptado.

### 4.9 Superfície por estado

**Origem.** É literalmente o que o Guião manda fazer no campo 4.9: «especificar o nº de m2 em bom estado, de reabilitação ligeira, de reabilitação pesada e de reconstrução. A especificação dos m2 serve para calcular os custos da reabilitação/manutenção necessários». A proposta dá a cada uma das quatro parcelas uma caixa numérica própria, para que os metros quadrados se possam somar.

**Consequência.** Com quatro caixas numéricas, a estimativa de custo de reabilitação da rede passa a ser calculável directamente a partir do Mapa Sanitário. É provavelmente o ganho mais directo de toda a proposta para o plano de investimentos.

**Verificação a programar.** A soma de 4.9.1 a 4.9.4 deve ser igual a 4.2.

## Secção 5 — Água, energia, saneamento e resíduos

### 5.1 Fonte de água

**Porque mudou.** As cinco categorias da Ficha desdobram-se na lista internacional de fontes de água, que distingue situações reunidas na Ficha em «furo ou poço»: um poço protegido é fonte melhorada, um poço não protegido não é. É esta distinção que permite calcular o indicador de fonte melhorada. A estrutura Principal + Outras da Ficha é integralmente conservada.

### 5.1.3 Água disponível no recinto

**O que acontece com cada resposta.** O indicador de água melhorada cumpre-se quando a categoria de 5.1 é melhorada **e** a resposta aqui é 1 ou 2. As respostas 3 e 4 não o cumprem: uma unidade com furo no papel e sem água na torneira não tem água.

**Porque é necessário.** É a diferença entre ter uma fonte e ter água. Uma caixa separa as duas coisas.

### 5.2 Fonte de electricidade

As categorias mantêm-se — são adequadas e correspondem às da classificação internacional. A estrutura Principal + Outras mantém-se e é aqui especialmente útil: a combinação «rede geral como principal, gerador e solar como reserva» é a situação real de muitas unidades e hoje já é captada.

### 5.2.3 Disponibilidade de electricidade nos últimos 7 dias

**O que acontece com cada resposta.** O indicador de unidades com electricidade cumpre-se quando 5.2 é diferente de «não tem» **e** a resposta aqui é 1 ou 2. A resposta 3 não o cumpre.

**Porque é necessário.** Pela mesma razão da água: ter ligação à rede não é ter electricidade. E este campo articula-se com a cadeia de frio do PAV — uma unidade com geleira e com interrupções de mais de duas horas por dia tem um problema de conservação de vacinas que nenhum inventário de equipamento revela.

### 5.3 Saneamento

**Porque mudou.** As quatro categorias da Ficha são casa de banho, latrina, latrina melhorada e outra. A lista nova é a internacional e traz a definição dentro da própria opção, para que a distinção entre «latrina» e «latrina melhorada» se faça da mesma maneira em todas as unidades. O indicador de saneamento melhorado cumpre-se com as categorias 1, 2 ou 4. As definições das oito categorias serão escritas no Guião revisto. *Decisão aprovada a 15/10.*

### 5.4 Recolha de resíduos comuns

Categorias mantidas. Acrescenta-se apenas o código 00, para que a ausência de recolha organizada seja uma resposta e não um branco.

### 5.5 Destino final dos resíduos comuns

Categorias mantidas.

### 5.6 Destino final dos resíduos hospitalares

Categorias mantidas. O quesito 5.6 é o único da secção 5 sem coluna «Outros», e assim permanece.

### 5.5.3 O meio de tratamento funciona

**O que acontece com cada resposta.** O destino adequado dos resíduos cortantes e dos resíduos infecciosos só conta para o indicador **se** o meio de tratamento estiver a funcionar e tiver combustível. Um incinerador parado por falta de gasóleo é, na prática, queima ao ar livre — e é essa a situação que estas duas caixas tornam visível.

### 5.5.5 Normas de gestão de resíduos

Duas caixas, dois indicadores, e a ligação ao bloco de prevenção e controlo de infecções — que fica parqueado, mas de que estas duas perguntas são a parte que se responde por declaração.

### 5.7.1 Tratamento de águas residuais

Os dois campos mantêm-se. A codificação passa a ser Sim = 1 e Não = 2 nas duas perguntas, para que a mesma resposta tenha sempre o mesmo código; na conversão para a série histórica, recorde-se que na Ficha 5.7.1 usa Não = 1 e Sim = 2.

### 5.7.2 Funcionamento do tratamento de águas residuais

Mantém-se a especificação da causa, que o Guião já pede. Acrescenta-se o período de referência — «nos últimos 30 dias» — porque «funciona» sem período não é verificável.

## Secção 6 — Conectividade e meios informáticos

### 6.1.1 Cobertura de rede móvel

**Porque vem primeiro.** A cobertura não depende da unidade. Perguntada antes da internet, separa a falta de sinal — que se resolve com infra-estrutura de telecomunicações — da falta de contrato ou de equipamento, que se resolve com o orçamento da unidade. Serve também o canal de voz: a chamada para a unidade de referência depende de sinal, não de internet.

### 6.1.2 Meio de ligação à internet

**Para que serve.** A opção 3 mostra as unidades em que a ligação depende do telemóvel pessoal dos profissionais.

### 6.1.3 Acesso à internet

**De onde vem.** A caixa «Comunicação» dos serviços gerais (20.7) passa para esta secção, desdobrada nesta pergunta e em 6.1.4.

### 6.1.4 Custo da ligação à internet

**Para que serve.** O custo pago pela gestão distingue a ligação institucional da ligação paga pelo próprio profissional.

### 6.1.5 Disponibilidade da ligação nos últimos 7 dias

**Para que serve.** Ter ligação não é o mesmo que ter ligação quando se precisa. A escala é a mesma usada para a electricidade em 5.2.3.

### 6.2.1 a 6.2.6 Equipamento informático e telefone

**Para que serve.** Segue a lógica usada para os veículos na secção 7: quantos existem e quantos funcionam. A bateria de apoio entra porque, com os cortes de energia medidos em 5.2.3, é ela que decide se um registo em curso se perde.

### 6.3.2 Tipos de informação em base de dados

**A decidir.** É a informação que muda mais depressa em todo o formulário — muda com cada projecto que instala um sistema. Falta decidir se entra já ou se fica para as recolhas com visita. Sem esta grelha, a secção passa de 36 para 24 campos.

### 6.3.4 Cópias de segurança

**Para que serve.** Onde a energia falha, a falta de cópia de segurança arrisca a perda definitiva de processos clínicos. Lê-se com a bateria de apoio (6.2.5) e com os cortes de energia (5.2.3).

### 6.3.5 Formato do reporte de rotina

**Para que serve.** Lido com a cobertura de rede (6.1.1) e com a disponibilidade da ligação (6.1.5), distingue a unidade que reporta em papel por falta de meios da que o faz por hábito.

### 6.3.6 Plataforma de registo e reporte

**Para que serve.** Acompanha a transição para o DHIS2. A lista de opções deve ser validada pelo GEPE e pela área de informática do MINSA.

### 6.4.1 Pessoa designada para a gestão dos dados

**Para que serve.** Lidas ao lado do equipamento e dos sistemas, 6.4.1 e 6.4.2 mostram as unidades que têm meios informáticos mas ninguém designado para os usar.

## Secção 8 — Camas e equipamentos de exame

### 8.0.1 Internamento — porta

**Porque é necessária.** A porta antecede a contagem de camas: com ela, uma unidade sem internamento salta as perguntas sobre camas de internamento e responde apenas às que se aplicam a todas as unidades.

### 8.1.1 Camas de internamento de adulto

**Porque mudou.** Mantém-se a definição do Guião. Acrescenta-se apenas «de tamanho adulto», para separar estas camas das pediátricas, contadas em 8.1.2.

### 8.1.2 Camas pediátricas e berços de lactentes

**Porque é necessária.** As camas pediátricas passam a ter contagem própria. Aqui contam-se pelo tamanho da cama; em 8.2 contam-se também pela enfermaria. As duas leituras servem fins diferentes e ambas ficam disponíveis.

### 8.1.3 Berços para recém-nascidos

**Porque mudou.** O quesito já existe. Acrescenta-se o momento de referência — o dia da visita — e a distinção face aos berços de lactentes de 8.1.2, para que a mesma criança não seja contada duas vezes.

### 8.1.4 Camas autorizadas

**Para que serve.** A distância entre as camas autorizadas e as instaladas é informação de planeamento que passa a ficar disponível.

**Verificação a programar.** Assinalar quando 8.1.1 for maior que 8.1.4.

### 8.2 Camas por enfermaria ou serviço

**Porque é necessária.** Ao total de camas da Ficha acrescenta-se a distribuição por enfermaria, que mostra que serviços de internamento cada unidade tem de facto e com que dimensão.

**Verificações a programar.** A soma das linhas de adulto não pode exceder 8.1.1; a linha 11 não pode exceder 8.1.2; a linha 12 não pode exceder 8.1.3.

### 8.2b Camas de adulto por sexo da enfermaria

**Porque é necessária.** A mesma cama é classificada por enfermaria ou serviço em 8.2 e por sexo da enfermaria aqui, em duas perguntas separadas sobre o mesmo total. Assim cada caixa tem uma resposta única, sem obrigar a cruzar os dois critérios numa só grelha.

**Verificação a programar.** A soma das três linhas deve ser igual a 8.1.1.

### 8.3.1 Camas de observação

**Porque mudou.** O Guião já distingue a observação até 24 horas da curta estadia até 72 horas; a proposta segue essa distinção e dá uma caixa a cada uma.

### 8.3.3 Camas de observação com pernoita

**Para que serve.** O Guião exclui as camas de observação das camas de internamento. Com este campo ficam disponíveis as duas leituras: a nacional, que mantém a série das edições anteriores, e a que soma às camas de internamento as camas de observação em que os doentes pernoitam.

### 8.4 Macas, marquesas e cadeiras de estomatologia

**Porque mudou.** As marquesas de parto e as cadeiras de estomatologia, que a Ficha conta junto das camas, passam a ter pergunta própria: a cama é lugar de estadia, a maca é lugar de exame. Acrescentam-se a maca para exame físico e a maca ou mesa para exame ginecológico, e a coluna «a funcionar» estende a todos os equipamentos a indicação do Guião sobre o estado de funcionamento da cadeira de estomatologia.

### 8.5 Camas em armazém ou fora de uso

**Porque é necessária.** Como o Guião prevê, as camas guardadas em armazém registam-se «aparte»: passam a ter caixa própria, que evita que entrem na contagem de 8.1.1.

### 8.6 Outros recursos de estadia ou de exame

**Porque mudou.** As cinco linhas abertas da Ficha passam a uma: com as camas por enfermaria e por sexo, a observação, a curta estadia e os equipamentos de exame em perguntas próprias, uma linha aberta é suficiente.

## Secção 9 — Aparelhos médico-cirúrgicos

### 9.1.1 a 9.1.15 Número de aparelhos

**Porque mudou.** Os 15 tipos de aparelho mantêm-se, com os mesmos códigos. O enunciado passa a dizer o que se conta: os aparelhos em condições de utilização no último mês.

**Remissões.** O esterilizador, o aparelho de raios X e o ecógrafo contam-se aqui como equipamento; a oferta dos serviços correspondentes — esterilização, imagiologia — está na secção 12.

### 9.1.16 a 9.1.23 Verificação do equipamento básico

**Porque é necessária.** A contagem de 9.1.1 a 9.1.15 diz quantos aparelhos existem; esta grelha verifica se estão presentes e a funcionar na área de atendimento. As duas servem decisões diferentes — a contagem orienta a distribuição de equipamento, a verificação mostra onde estão as falhas —, e por isso os quatro aparelhos que entram nas duas conservam a sua caixa de quantidade.

**Códigos.** Os oito itens novos continuam a numeração da Ficha, de 9.1.16 a 9.1.23, para que nada do que já existe mude de número. A balança de criança (graduação de 250 g) é distinta da balança de bebé (graduação de 100 g), que se mantém.

### Pendência desta secção

**Âmbito da secção.** Hoje a secção aplica-se apenas a centros e postos de saúde. O Guião (folha 17) justifica a restrição: nos hospitais, a informação sobre aparelhos está incluída nos dados das provas diagnósticas e de tratamento. Falta decidir se a secção passa a aplicar-se a todas as unidades sanitárias. Com a restrição, a contagem e a verificação do equipamento básico ficam disponíveis só para centros e postos de saúde. Como a verificação se faz apenas nas unidades visitadas, o custo de alargar a secção depende do número de visitas e não do total de unidades.

## Secção 7 — Meios de transporte

### 7.1.1 a 7.1.7 Veículos por tipo e estado

**Porque mudou.** Os sete tipos de veículo mantêm-se. As duas colunas da Ficha — funcionantes e não funcionantes — passam a três. A definição de funcional do Guião (folha 18) fica preservada e passa a estar escrita na pergunta: um veículo é funcional se está em funcionamento ou tem uma avaria que a unidade pode resolver com os seus recursos. A soma das colunas 1 e 2 corresponde aos «funcionantes» da Ficha e a coluna 3 aos «não funcionantes».

### 7.1.8 a 7.1.10 Outros meios de transporte

**Porque mudou.** As três linhas abertas mantêm-se, com a terceira coluna acrescentada, como em 7.1.1 a 7.1.7.

### 7.3.1 Plano de manutenção dos veículos

**Porque é necessária.** A opção «A unidade não tem veículos» evita que uma unidade sem frota seja contada como unidade sem plano de manutenção.

**Verificação a programar.** Se a contagem de 7.1.1 a 7.1.10 for zero em todas as colunas, 7.3.1 tem de ser 5.

### Pendência desta secção

**Nível a que se regista a frota.** A secção conta apenas os veículos da própria unidade. Para a maioria das unidades de cuidados primários, o que decide a evacuação de um doente é haver uma viatura disponível no município ou na região. A capacidade de chamar um veículo de outro local já está nos quesitos 20.1 e 20.1.1 (transporte de emergência) e 14.6 (transporte para referir doentes de urgência). Falta decidir onde se regista a frota ao nível municipal: num quesito à unidade sobre a frota a que tem acesso através do município, ou num instrumento próprio dirigido à Direcção Municipal de Saúde, fora da ficha da unidade.

## Secção 10 — Serviços clínicos e cirúrgicos

### 10.A · Especialidades clínicas (10.1 a 10.28)

**Porque mudou.** A pergunta da Ficha — se há atendimento em cada especialidade — mantém-se e ganha a companhia de outras três, para que se possa distinguir um centro de saúde onde o clínico geral acompanha hipertensos uma manhã por semana de um hospital com três cardiologistas em consulta diária. As quatro perguntas separam a **existência** da oferta, a sua **dimensão** — especialistas e turnos de atendimento — e a **forma de acesso**. O número de especialistas, com o código 00, conserva a distinção entre atendimento por especialista e por outro profissional.

**O enunciado fixa o critério** de atendimento regular — dias marcados na semana, não suspenso há mais de 3 meses —, para que todas as unidades respondam com a mesma régua.

**Verificação a programar.** O número de especialistas declarado aqui deverá ser coerente com o quadro de pessoal da unidade, quando o bloco de pessoal for desenhado.

*Proposta desta revisão, ainda por registar na matriz de decisão.*

### 10.B · Doenças não transmissíveis — funções por condição

**Diferença em relação a 10.A.** Em 10.A pergunta-se pela disponibilidade de atendimento em cada especialidade. Aqui pergunta-se se a unidade consegue realizar funções específicas no cuidado a doentes com hipertensão e outras doenças cardiovasculares, diabetes e doença respiratória crónica — diagnosticar, iniciar e ajustar o tratamento, seguir regularmente os doentes e aconselhá-los para o autocuidado —, haja ou não especialista na unidade.

Com estas respostas é possível medir a densidade da disponibilidade e da prontidão para o cuidado a doentes com estas condições na área de abrangência da unidade.

### 10.B.1 · Procura activa de faltosos — doenças crónicas não transmissíveis

**Porque entra.** A continuidade dos cuidados depende de a unidade saber quem faltou e ir procurá-lo. A mesma pergunta repete-se em cada linha de cuidado com consultas marcadas e, no fim, em 18.4.2, como função dos ADECOS.

**Verificação a programar.** Na resposta 1, pedir para ver a lista ou o livro de faltosos do último mês.

### 10.C.1 · Saúde mental

Duas caixas, dois indicadores. Mesma lógica de 10.B: a psiquiatria e a psicologia são especialidades que quase nenhuma unidade de cuidados primários tem, enquanto o atendimento a transtornos mentais comuns e o seguimento de doentes com epilepsia acontecem em centros de saúde sem qualquer especialista.

### 10.C.2 · Doenças neurológicas

**A epilepsia é nomeada de propósito** no enunciado, porque é a condição neurológica cujo seguimento mais depende dos cuidados primários e cuja ruptura de medicamento tem consequência imediata.

### 10.D.1 a 10.D.4 · Cancro, por localização

Cinco caixas, cinco indicadores. O cancro do colo do útero é o que mais interessa à rede de cuidados primários, porque o rastreio por inspecção visual com ácido acético é factível num centro de saúde — e já temos a maca de exame ginecológico na secção 8 e o espéculo na secção 9. **Cruzando os três, passa a ser possível ver quais as unidades que têm a condição material para rastrear e não rastreiam** — que é uma lacuna de organização e não de investimento, e portanto barata de corrigir.

### 10.E.0 · Sobreviventes de violência — porta

**Reserva registada.** Uma resposta afirmativa a este bloco cria expectativa de confidencialidade, de protocolo escrito e de articulação com a polícia e o sistema judicial. Perguntar sem que exista essa capacidade pode produzir um dado que sobrestima a resposta disponível. Está pedida ao MINSA a norma nacional sobre atendimento a sobreviventes de violência sexual, para ancorar o enunciado.

### 10.E.3 · Prestações oferecidas aos sobreviventes

**A profilaxia pós-exposição ao VIH (PEP) dos sobreviventes de violência é recolhida aqui** — a linha 3 de 10.E.3. A profilaxia pós-exposição ao VIH (PEP) fora do contexto da violência está no quesito 17.3 e não se repete aqui.

**Duas notas que importam à recolha.** A primeira é de prazo: a profilaxia pós-exposição ao VIH (PEP) só é eficaz nas primeiras 72 horas, pelo que a oferta declarada aqui deve ler-se ao lado do horário de funcionamento da unidade e da disponibilidade de antirretrovirais. A segunda é de enquadramento: **as linhas 7 e 8, sobre interrupção da gravidez, devem ser confirmadas com o GEPE contra o quadro legal angolano antes de irem a terreno.** Se a prestação não for legalmente possível, as duas linhas saem.

### 10.E.4 · Profissional do mesmo sexo para o exame

**10.E.4** é o único quesito do bloco que não mede uma prestação clínica mas uma condição de acesso: determina se a pessoa chega a ser examinada. Numa rede onde muitas unidades têm um único profissional de turno, é uma restrição real.

### 10.29.1 · Pequena cirurgia

**Porque mudou.** A Ficha divide a cirurgia geral em urgência, electiva e pequena; o instrumento internacional divide em pequena e grande, pelo critério da anestesia e do bloco operatório. A proposta adopta o critério internacional, que é o verificável, e conserva a distinção urgência/electiva como informação própria dentro da grande cirurgia. As definições do Guião (folha 10) para as três caixas da Ficha mantêm-se válidas.

### 10.29.4 · Procedimentos de referência nos últimos 12 meses

**Os três procedimentos de 10.29.4** são os procedimentos de referência: medem capacidade cirúrgica essencial **efectiva** e não declarada, porque perguntam o que foi feito nos últimos 12 meses e não o que a unidade poderia fazer.

**Cruzam-se** com o número de blocos operatórios (12.D.5) e com a anestesia (12.D.2).

### 10.30 a 10.34 · Cirurgia de especialidade

**Fecho da secção 10.** Decisão de fundo a registar: nesta secção adopta-se o olhar internacional, que é o mais adequado ao objecto, **sem retirar a lista de especialidades da Ficha**. As duas convivem porque respondem a perguntas diferentes — a especialidade diz como a unidade está organizada e serve a gestão da rede; a condição diz o que a unidade consegue resolver e serve o planeamento do cuidado. É o mesmo desenho usado nas comissões de 19.2, onde o órgão e a actividade convivem.

[**52 indicadores do HHFA** nesta secção.]{.hhfa}

## Secção 12 — Diagnóstico e serviços de apoio

### 12.C.0 · Testes rápidos de diagnóstico

**Porque não tem porta, e porque vem primeiro.** É exactamente aquilo que um posto de saúde faz, e é por aqui que um posto que só tem teste rápido de malária cumpre o indicador de capacidade de diagnóstico de malária. Colocá-lo antes da porta do laboratório — como faz o instrumento internacional — garante que nenhuma unidade perde estas onze linhas por responder «não» a uma pergunta sobre laboratório.

**A escala é de sim ou não, e não de três níveis**, por uma razão de desenho: a opção «amostra enviada para fora» é impossível num teste de ponto de atendimento, que por definição é feito ali.

### 12.1 · Porta geral do laboratório

**É a porta dos quatro blocos de exames.** Segue a regra transversal de que a porta é a actividade e não o órgão: se fosse «tem laboratório», a unidade que não faz exames mas encaminha doentes ficaria de fora — e é precisamente dela que queremos saber. A caixa do laboratório como **serviço** mantém-se, em paralelo, na lista dos serviços de apoio.

**A definição do Guião deixa de ser um critério implícito de marcação e passa a ser verificável item a item.** O Guião exige, para marcar «Laboratório», no mínimo gota espessa, hemoglobina ou hematócrito e análises simples de fezes e urina (folha 15): a gota espessa está em 12.C.IV, a hemoglobina em 12.C.I, e as análises de fezes e urina em 12.C.IV.

### 12.C.I a 12.C.IV · Os quatro blocos de exames

A porta de grupo é a do próprio instrumento internacional e salta os sete itens seguintes quando a unidade não faz nenhum exame de glóbulos. A **electroforese de hemoglobina** e a **pesquisa de hemoglobina S** são acrescento próprio: justificam-se num país com prevalência de drepanocitose e nenhum instrumento internacional as recolhe. O eritrograma foi omitido por redundância com o hematócrito e o hemograma completo.

O maior bloco da secção e o de maior rendimento: dez indicadores directos. Os acrescentos à lista internacional têm justificação clínica local — o ferro, a ferritina e a transferrina na investigação da anemia; o cálcio, o fósforo e o ácido úrico no seguimento da doença renal; o clearance de creatinina e o teste oral de tolerância à glicose no manejo crónico. O instrumento internacional agrupa transaminases e fosfatase alcalina num único item; aqui são duas linhas, o que mantém o indicador e acrescenta precisão.

A **carga viral do VIH** e a **contagem de CD4** merecem destaque: num país com tratamento antirretroviral descentralizado, saber quais as unidades que conseguem medir carga viral é decisão de investimento directa. O instrumento internacional agrupa as hepatites B e C num item cada, sem distinguir antigénio de anticorpo; aqui separam-se o HBsAg e o anti-HBs, que têm leituras clínicas diferentes.

Sem porta de grupo, porque o instrumento internacional também não lhe dá nenhuma.

O **exame parasitológico de fezes** é o item que o Guião exige no seu mínimo para marcar «Laboratório» (folha 15). A separação da tuberculose em **baciloscopia** e **teste molecular**, e da malária em **gota espessa** (aqui) e **teste rápido** (em 12.C.0), é deliberada: o indicador cumpre-se por qualquer das vias, e passamos a saber qual — que é o que decide onde colocar um GeneXpert.

### 12.C.V · Destino da amostra ou do doente

**Contributo próprio e ligação directa à árvore de referência da secção 3.** Nenhum instrumento internacional recolhe o destino da amostra ou do doente quando o exame não se faz na unidade.

É uma só pergunta, e não uma coluna por exame, porque a escala de três níveis já diz, exame por exame, se a amostra sai — o que falta é o destino, e o destino é quase sempre o mesmo. Se a primeira ronda mostrar muita dispersão na opção 96, abre-se uma coluna de destino em cada linha na ronda seguinte, ao custo de mais 49 campos.

**Nota de leitura.** A opção 3 das linhas 12.C — «não realizado por nenhuma destas vias» — é a mais importante de todas, porque distingue a unidade que não faz o exame mas garante o acesso da unidade onde o exame simplesmente não acontece. É essa diferença que mede acesso efectivo em vez de capacidade instalada.

**Pendência para o GEPE, com consequência directa neste bloco.** O Guião remete, na folha 13, para a definição do INSP dos **Laboratórios tipo I e tipo II**. Com o texto dessa norma, três coisas mudam: o agrupamento passa a ser por nível em vez de por disciplina clínica; a leitura passa de descritiva — «esta unidade realiza 14 dos 82 exames» — a cumprimento — «este centro de saúde realiza 11 dos 20 exames exigidos a um Laboratório tipo I»; e a pergunta «quem decidiu que um centro de saúde deve fazer TSH?» passa a ter resposta. Escrevemos já com o agrupamento clínico porque, se a norma chegar, a lista de exames não muda — muda apenas o agrupamento.

### 12.A · Imagiologia — exames de imagem

**Porque mudou.** A caixa da imagiologia desdobra-se em oito linhas, uma por exame; os indicadores contam apenas a opção 1, o que mantém a comparabilidade com outros países. A opção 2 é o acrescento nosso e é a que serve o país, porque distingue a unidade que garante o acesso por encaminhamento daquela onde o exame não acontece.

**Articula-se com a secção 9**, onde se **contam** os aparelhos de ecografia e de raio X: aqui mede-se a oferta do exame, lá o inventário do equipamento.

**Verificação a programar.** Assinalar quando a unidade declara realizar ecografia ou raio X e conta zero aparelhos correspondentes na secção 9.

### 12.B · Procedimentos e tecnologias

Três destas onze linhas substituem três caixas da Ficha e dizem o mesmo com o mesmo esforço de resposta — a **diálise**, a **radioterapia** e a **hemoterapia**, que passa a chamar-se transfusão de sangue por ser o termo mais claro. As outras oito são ganho líquido, a uma caixa por indicador.

**Uma linha merece destaque:** a administração de oxigénio é a tecnologia de maior rendimento clínico num centro de saúde.

A escala é de sim ou não porque nenhum destes procedimentos se faz por encaminhamento com retorno de resultado: ou se faz aqui, ou o doente é transferido — e a transferência está tratada na árvore de referência da secção 3.

### 12.D · Outros serviços de apoio

Sete das oito caixas são as da Ficha e mantêm-se com o mesmo sentido; muda apenas o enunciado, que passa a dizer «em funcionamento» por palavras.

**Duas precisões e um acrescento.** A reabilitação ganha a definição internacional, mais larga do que a fisioterapia — escrita no enunciado, a caixa abrange também quem faz reabilitação sem gabinete de fisioterapia. O número de blocos operatórios ganha «em condições de utilização». E o acrescento são os **cuidados paliativos**, uma caixa e um indicador, uma oferta própria dos cuidados primários: o controlo da dor no doente oncológico avançado faz-se no centro de saúde e no domicílio, não no hospital.

### 14.1 · Serviços de urgência — porta

**É a aplicação mais consequente da regra de que a porta é a actividade e não o órgão.** Com esta porta, o centro de saúde que atende urgências na própria consulta — o que é a regra na rede de cuidados primários — passa a contar como unidade com atendimento de urgência, ao lado das que têm Banco de Urgência, e entra no numerador do indicador de atendimento de urgência.

### 14.2.2 · Horas de funcionamento do banco de urgência

**É aqui que as duas caixas da Ficha — «Só Diurno» e «24 Horas» — se resolvem numa pergunta e um número.** Ganha-se em três frentes. A resposta é sempre uma só. O número contém as duas categorias da Ficha e todas as que ficam entre elas — as 12 horas, as 16 horas, o fim de semana só de manhã —, que é a realidade da maior parte da rede. E o indicador calcula-se de «igual a 24», pelo que perguntar as horas dá o indicador **e** o gradiente.

**Correspondência com a série histórica:** «Só Diurno» passa a ser um valor entre 01 e 23, e «24 Horas» passa a ser 24.

### 14.3 · Triagem formal

Uma caixa, um indicador, e é o quesito de maior rendimento de todo o bloco em relação ao esforço. Mede aquilo que mais determina o desfecho de um doente grave que chega a uma unidade com fila: se é visto por ordem de gravidade ou por ordem de chegada. A precisão «com critérios escritos» está no enunciado de propósito, para que a resposta não seja marcada por quem faz triagem informal pelo bom senso do enfermeiro de turno — que é prática corrente e meritória, mas não é um sistema.

### 14.4 · Pessoal próprio do banco de urgência

O indicador conta apenas a opção 1. A pergunta foi escrita com três opções em vez de duas porque **a situação mista é a mais frequente na rede** — um núcleo permanente reforçado por rotação nos turnos da noite — e porque uma escala de sim ou não obrigaria quem responde a escolher arbitrariamente. É a diferença entre um serviço de urgência com competência acumulada e um serviço assegurado por quem passa por lá.

### 14.5 · Presença clínica 24 horas

O indicador exige as duas condições ao mesmo tempo — um médico ou clínico de nível intermédio **e** um enfermeiro. A distinção entre «presente na unidade» e «de chamada» está no enunciado e nas opções porque é a diferença que decide o atendimento de uma emergência às três da manhã, e porque sem ela a resposta tende a ser afirmativa em qualquer unidade onde haja um profissional contactável. As opções 2 e 3 não entram no indicador, mas distinguem a unidade que está perto de cumprir da que está longe.

### 14.6 · Transporte para transferência

Um indicador por uma caixa. **Fecha pelo lado da urgência a discussão sobre a frota:** o que importa não é a unidade ter viatura própria, mas conseguir transporte quando precisa — e a opção 2, a ambulância chamada de outro local, é precisamente a resposta da maior parte dos centros de saúde. Articula-se com a secção 7 (frota da unidade), com 3.9 (viatura e motorista 24 horas) e com 20.1 (transporte de emergência nos serviços gerais): três leituras do mesmo problema, cada uma na sua secção, sem duplicação de campo.

### 14.7 · Acompanhamento na transferência

Mede a qualidade do próprio acto de referir, que é a operação mais frequente e mais crítica da rede: um doente transferido sem acompanhamento clínico perde, no caminho, a vigilância que justificava a transferência. A opção 2 não entra no indicador e fica porque é a resposta honesta da maior parte das unidades — acompanha-se quando há pessoal disponível —, e porque a distância entre «alguns casos» e «habitualmente» é um problema de dotação de pessoal, não de equipamento.

### 14.8 · Serviços de apoio à urgência — horas por dia

Pergunta-se o **número de horas** e não sim ou não, porque os três indicadores calculam-se de «igual a 24» — exactamente como em 14.2 — e portanto o número dá o indicador e o gradiente pelo mesmo esforço de resposta.

**O valor está menos em cada um deles e mais no conjunto:** um banco de urgência aberto 24 horas com laboratório aberto 8 horas é uma unidade que não consegue investigar o doente grave de madrugada, e essa combinação não é visível em nenhum dos três indicadores lido isoladamente. A opção 97 evita que uma unidade sem laboratório seja contada como unidade com laboratório fechado.

### 12.10 · Farmácia

**Mantém-se como caixa única.** O horário de funcionamento para a urgência é recolhido em 14.8.1, e a disponibilidade de medicamentos fica para o bloco próprio.

**Razão do parqueamento.** O que interessa medir na farmácia não é a existência do serviço, é a presença **observada** dos produtos na prateleira, dentro da validade: 181 linhas de produto em dez grupos, mais blocos condicionais de malária, tuberculose e antirretrovirais. Os indicadores contam apenas o produto visto e válido, pelo que a escala colapsa sem observação. É a tabela de maior rendimento para os cuidados primários — 37 indicadores — e merece decisão própria.

**Pendência aberta.** Está pedida ao MINSA a Lista Nacional de Medicamentos Essenciais com a indicação do exigido a cada nível da rede. Sem ela, as 181 linhas são demasiadas para um posto de saúde e não há critério defensável para as encurtar.

### 12.14 · Esterilização

Parqueado para o bloco de prevenção e controlo de infecções, e não por omissão: é o quesito em que a distância entre a existência do serviço e a sua eficácia é maior. O instrumento internacional não pergunta se existe esterilização — pergunta qual o método, se o autoclave está a funcionar no dia da visita, se há indicador de processo e se o pessoal foi formado. Nenhuma destas perguntas se responde sem observação.

**Remissão a registar:** o quesito 9.1.1 da secção 9 é o **esterilizador** enquanto equipamento, contado no inventário; este 12.14 é a esterilização enquanto **serviço**. Não se sobrepõem e nenhum substitui o outro.

## Secção 15 — Saúde da criança e vacinação

### 15.1 · Vacinação — porta do PAV

**Porque mudou.** A definição do Guião (folha 12) reúne três critérios: «a menores de 5 anos, com todos os antigénios (= Posto Fixo de Vacinação); será considerado afirmativo se são realizadas vacinações de rotina na US com periodicidade fixa, mesmo que não seja diária» — grupo de idade, completude dos antigénios e periodicidade. A proposta aproveita-a e dá a cada critério o seu quesito: a periodicidade em 15.1.1, a completude em 15.1.2, e o grupo de idade resolve-se na própria grelha.

**A opção 2 é nova** e serve a leitura que o Guião já implica: uma unidade que só vacina em campanhas não é um posto fixo de vacinação, mas também não é uma unidade onde nada acontece.

### 15.1.1 · Periodicidade da vacinação de rotina

Uma caixa, três indicadores. Aproveita a instrução do Guião, que já manda avaliar a periodicidade — «mesmo que não seja diária» —, e passa a registá-la, para que fique disponível na análise.

**É provavelmente o dado mais útil de todo o bloco do PAV** para a rede de cuidados primários: a distância entre vacinar todos os dias e vacinar uma vez por mês é a distância entre uma mãe que leva a criança quando pode e uma mãe que tem de acertar com o dia certo — e explica oportunidades perdidas de vacinação sem que nada falte na unidade.

### 15.1.2 · Antigénios oferecidos

**Vinte e cinco indicadores por dezanove caixas — o maior rendimento por campo de toda a proposta.** Deixa de se saber apenas quantas unidades vacinam e passa a saber-se **qual o antigénio que falta e onde**, que é a pergunta a que um plano de reforço da imunização tem de responder.

A **febre amarela** é acrescento próprio, por ser doença com transmissão em Angola e não constar da lista internacional.

**Pendência a abrir com o PAV:** confirmar estas dezanove linhas contra o calendário nacional de vacinação em vigor, retirando os antigénios que Angola não utiliza e acrescentando os que faltem. Retirar uma linha custa apenas o indicador correspondente e não afecta nenhum dos outros.

### 15.1.3 · Rupturas de stock por antigénio

**É a única decisão de peso deste bloco.**

*A favor:* 11 indicadores por 11 campos, todos autorreferidos, e a ruptura de stock é provavelmente a causa mais frequente de oportunidade perdida de vacinação — mede-se a cadeia de abastecimento sem precisar de observar a geleira. A ruptura é a única parte da família dos medicamentos que não exige verificação física, porque é memória de quem responde e não contagem de prateleira.

*Contra:* faz passar a grelha do PAV de 18 para 29 campos.

*Recomendação:* incluir, mas só para os antigénios do calendário infantil de rotina que Angola utiliza — o que, feita a confirmação com o PAV, deve reduzir as 11 linhas a 7 ou 8.

### 15.1.4 · Cadeia de frio

Parqueada para a fase da observação. **Não é omissão, é fronteira de módulo:** a tabela de prontidão da imunização tem 31 indicadores e exige ver o frigorífico a funcionar, ler o termómetro no dia da visita e verificar as vacinas na prateleira.

**Remissões.** A contagem de geleiras e arcas está no quesito 9.1.2 da secção 9 — e é contributo próprio do Mapa Sanitário, que conta as geleiras em vez de verificar apenas uma. A energia que as alimenta está no quesito 5.2.3. A manutenção de frigoríficos está no bloco 20.8, também parqueado.

### 15.1.5 · Procura activa de faltosos — vacinação

**Porque entra.** A continuidade dos cuidados depende de a unidade saber quem faltou e ir procurá-lo. A mesma pergunta repete-se em cada linha de cuidado com consultas marcadas e, no fim, em 18.4.2, como função dos ADECOS.

**Verificação a programar.** Na resposta 1, pedir para ver a lista ou o livro de faltosos do último mês.

### 15.2 · Puericultura — porta dos cuidados à criança

**A puericultura deixa de ser uma caixa entre outras e passa a ser a porta de toda a família dos cuidados à criança**, porque é isso que ela é na prática: o Guião define-a como «quando inclui peso e registo do mesmo no cartão infantil» (folha 12), isto é, a consulta de vigilância da criança. A monitorização do crescimento, que é o conteúdo dessa definição, passa a ser a primeira linha da grelha seguinte, onde gera indicador próprio.

### 15.2.1 · Cuidados à criança menor de 5 anos

**Cinco caixas da Ficha entram aqui e nenhuma se perde, com uma correspondência exacta** que vale registar: a Reidratação Oral (4.1 RO) é a linha 9; o Centro Nutricional Terapêutico, que o Guião define como serviço de tratamento da criança malnutrida grave «que inclui regime de internamento», é a linha 5; o Centro Nutricional Suplementar, «sem internamento, e que inclui o fornecimento de suplementos alimentares», é a linha 4; a vitamina A é a linha 6; e a puericultura é a linha 1. **As três caixas de nutrição da Ficha mapeiam-se exactamente nos três níveis de manejo do instrumento internacional**, o que mostra a solidez do desenho original.

O **albendazol** ganha linha própria: a desparasitação de rotina é contributo próprio do Mapa Sanitário, e conserva-se porque é a âncora de medicamentos mais simples do instrumento.

### 15.2.2 · Procura activa de faltosos — puericultura

**Porque entra.** A continuidade dos cuidados depende de a unidade saber quem faltou e ir procurá-lo. A mesma pergunta repete-se em cada linha de cuidado com consultas marcadas e, no fim, em 18.4.2, como função dos ADECOS.

**Verificação a programar.** Na resposta 1, pedir para ver a lista ou o livro de faltosos do último mês.

## Secção 16 — Saúde materna, do recém-nascido e planeamento familiar

### 16.1 · Consulta pré-natal

**A escala de três níveis é do próprio Guião**, que na folha 12 manda registar se a consulta é «completa, incompleta ou não é realizada», e a proposta dá a cada nível a sua opção de resposta — como faz com as camas em armazém, a data da visita anterior e a quantidade de ADECOS.

O Guião define ainda os critérios de «completa» — cartão de grávida, anamnese, peso, edemas, fundo uterino, mucosas, tensão arterial e manobras de Leopold, com um mínimo de TIP ou vacinação, ferro e ácido fólico, aconselhamento e desparasitação — e é essa lista que a grelha seguinte torna verificável item a item.

### 16.1.1 · Componentes da consulta pré-natal

Catorze linhas, um indicador por linha; com a porta 16.1 e a articulação com os ADECOS em 18.4.1, a consulta pré-natal fica medida por inteiro. **Quatro destas linhas são o mínimo que o próprio Guião exige para classificar a consulta como completa**, pelo que a grelha permite calcular a resposta de 16.1 em vez de a pedir como juízo.

**Articula-se com o laboratório:** a pesquisa de proteínas na urina é a fita reagente de 12.C.0.9, a testagem da sífilis é o teste rápido de 12.C.0.3 e a testagem do VIH é a de 12.C.0.1 — três pontos onde a coerência interna do formulário passa a ser verificável.

**A linha 14, sobre mutilação genital feminina, pode ser retirada** se não for pertinente para Angola: perde-se apenas um indicador e nada mais na tabela.

### 16.1.2 · Procura activa de faltosas — consulta pré-natal

**Porque entra.** A continuidade dos cuidados depende de a unidade saber quem faltou e ir procurá-lo. A mesma pergunta repete-se em cada linha de cuidado com consultas marcadas e, no fim, em 18.4.2, como função dos ADECOS.

**Verificação a programar.** Na resposta 1, pedir para ver a lista ou o livro de faltosos do último mês.

### 16.2 · Partos — porta

**A porta dos partos é nova** e junta-se às duas caixas de CONU-B e CONU-C, que se mantêm. Com ela, a unidade que atende partos normais sem capacidade obstétrica de urgência — que é a situação de muitos centros de saúde — fica registada como unidade com partos.

Conserva-se integralmente a instrução do Guião (folha 12), que manda registar «se houver sala de partos» e expressamente não registar quando «os trabalhadores da US atendem partos no domicílio das parturientes» — por isso a condição está escrita dentro da pergunta.

### 16.2.1 · CONU-B

**Duas caixas que já existem, cinco indicadores, e nem uma palavra a mudar: é o melhor custo-benefício de toda a secção.** A Ficha e o instrumento internacional usam aqui exactamente a mesma categoria, e as definições do Guião coincidem com as internacionais — CONU-B como antibióticos, ocitocina e anticonvulsivante parenterais, remoção manual da placenta e de restos ovulares; CONU-C como tudo o B mais cirurgia, isto é, cesariana e transfusão.

Às cinco funções-sinal do CONU-B enumeradas no Guião, a grelha seguinte junta o parto assistido instrumental e a reanimação do recém-nascido, que completam as sete da definição internacional.

**Nota de articulação com a avaliação EmONC** conduzida em paralelo: estes dois quesitos e a grelha seguinte são o ponto de contacto entre os dois instrumentos, e convirá que as definições sejam as mesmas nos dois.

### 16.2.3 · Funções-sinal obstétricas e neonatais

**Transforma a marcação de CONU-B e CONU-C de juízo em cálculo:** as caixas de 16.2.1 e 16.2.2 continuam a ser respondidas, e passam a poder ser confrontadas com as nove linhas que as definem. Uma unidade que marca CONU-B e declara não ter administrado anticonvulsivante parenteral nos últimos 3 meses é uma inconsistência a assinalar — e é informação útil, não um erro a corrigir, porque pode significar ausência de casos e não ausência de capacidade.

**O período de referência é de 3 meses e pergunta pelo que foi FEITO**, não pelo que a unidade poderia fazer: é a mesma opção de desenho dos três procedimentos de referência de 10.F, e por isso mede capacidade efectiva.

### 16.2.4 · Partos 24 horas por pessoal qualificado

O indicador conta as opções 1 e 2 — isto é, aceita o pessoal de chamada, ao contrário do que se fez na urgência em 14.5, onde o cálculo exige presença física. Mantemos a distinção nas opções porque ela importa à leitura nacional, mesmo não alterando o indicador.

Uma caixa, e uma informação nova no instrumento: **o parto é o acto que menos espera**, e saber quantas unidades com sala de partos têm de facto cobertura permanente é decisão de dotação de pessoal directa.

### 16.3 · Consulta pós-parto

A única alteração é separar a mãe do recém-nascido nas opções, porque são duas consultas distintas que muitas vezes não coexistem — e porque o indicador se cumpre com qualquer das duas, pelo que separá-las não o põe em risco. O Guião pede o mínimo de «uma anamnese» e esse critério mantém-se.

**Ampliação registada para uma ronda seguinte:** uma grelha de aconselhamento pós-parto (imunização, nutrição infantil, sinais de perigo no recém-nascido, cuidados do cordão, planeamento familiar, BCG e VOP ao recém-nascido, rede mosquiteira, amamentação exclusiva) daria mais 9 indicadores por 9 campos. Não foi incluída para conter o volume da secção.

[Indicadores que essa grelha daria: 3.1.6.1.2 a 3.1.6.1.10 (Q1835 e Q2248).]{.hhfa}

### 16.3.1.0 · Rastreios do recém-nascido — porta

**Bloco inteiramente novo.** Os rastreios do recém-nascido são medida própria do Mapa Sanitário e respondem a uma prioridade nacional.

### 16.3.1.1 a 16.3.1.8 · Rastreios do recém-nascido, rastreio a rastreio

A escala de três níveis é a mesma dos blocos de laboratório, pela mesma razão: num rastreio em papel de filtro o que importa é saber se a amostra sai e o resultado volta.

**Duas remissões, para não duplicar:** o diagnóstico precoce do VIH no recém-nascido exposto está em 17.5; a electroforese de hemoglobina e a pesquisa de hemoglobina S estão em 12.C.I, pelo que a linha 2 pergunta pelo **rastreio sistemático**, que é coisa distinta de ter o exame disponível.

**Nota para a revisão:** se for preciso cortar, as linhas 3 a 6 são as de menor exequibilidade na rede de cuidados primários e as candidatas naturais; as linhas 1, 2, 7 e 8 fazem-se com uma punção e um papel de filtro.

### 16.3.2.0 · Recém-nascido pequeno ou doente — porta

**Fica registado para decisão.** Trata dos cuidados ao recém-nascido pequeno ou doente, que a proposta ainda não cobre.

É **declarada** — não exige observação —, são 11 campos para 13 indicadores, e **nada há a inventar: as perguntas existem, estão validadas e têm indicador**. Ao contrário dos rastreios de 16.3.1, aqui o retorno é imediato.

A porta de três níveis distingue a unidade com unidade de cuidados especiais da que interna recém-nascidos doentes nas enfermarias comuns — distinção que a secção 8 não capta, porque a lista de camas decompõe por especialidade e por sexo da enfermaria e tem UCI neonatal, mas não cuidados especiais neonatais.

### 16.4 · Planeamento familiar — porta

**Dezasseis indicadores por treze campos, e o ganho não é só de volume — é de conteúdo.** O Guião manda marcar a caixa «se é oferecido pelo menos um método de planeamento familiar moderno (depo injetável, pílula, DiU, diafragma) excluindo o preservativo». A grelha método a método distingue a unidade que só tem pílula da unidade que coloca implantes e DIU — e a diferença entre as duas é justamente a que decide se uma mulher consegue um método de longa duração sem sair do seu município.

### 16.4.1 a 16.4.12 · Métodos de planeamento familiar

Com o preservativo perguntado em linha própria, a grelha permite os dois cálculos: o «método moderno» do Guião, que exclui o preservativo, e o «qualquer método moderno», que o inclui. O preservativo tem, além disso, indicador próprio e é o método mais distribuído da rede.

### 16.4.13 · Procura activa de faltosas — planeamento familiar

**Porque entra.** A continuidade dos cuidados depende de a unidade saber quem faltou e ir procurá-lo. A mesma pergunta repete-se em cada linha de cuidado com consultas marcadas e, no fim, em 18.4.2, como função dos ADECOS.

**Verificação a programar.** Na resposta 1, pedir para ver a lista ou o livro de faltosos do último mês.

## Secção 17 — VIH, tuberculose e malária

### 17.1 · VIH — aconselhamento e testagem

A caixa da Ficha fica como está e rende três indicadores. Articula-se com o laboratório por dois caminhos — o teste rápido de VIH e o autoteste, em 12.C.0 — e o indicador de capacidade de diagnóstico do VIH cumpre-se por qualquer deles ou por esta caixa, o que dá ao posto de saúde três vias para o mesmo indicador.

### 17.1.1 · Testagem do VIH por grupo de idade

Três caixas, cinco indicadores, e fecha a tabela da testagem. A separação por idade não é formalidade: **a testagem da criança exposta exige técnica distinta da do adulto** — o diagnóstico precoce no lactente faz-se por carga viral, que é o exame de 12.C.III — e é por isso que a testagem pediátrica é muito mais escassa do que a de adultos, o que as três caixas passam a mostrar.

### 17.2.1 · Profilaxia pré-exposição ao VIH (PrEP)

**Bloco inteiramente novo.** Pergunta-se à unidade se oferece a profilaxia pré-exposição ao VIH (PrEP); saber quantas pessoas a receberam exigiria ler processos clínicos, o que está fora do alcance de um cadastro.

**Porque entra:** a profilaxia pré-exposição ao VIH (PrEP) consta das recomendações da OMS e, num país com tratamento antirretroviral descentralizado, saber onde ela existe é informação directa para as decisões do programa.

A escala distingue iniciar de seguir pela mesma razão que no tratamento antirretroviral: a unidade que só redispensa é a maior parte da rede e perder-se-ia numa escala de sim ou não.

### 17.2.2 a 17.2.6 · Grupos a quem é oferecida a profilaxia pré-exposição ao VIH (PrEP)

**Nota para a revisão:** se for preciso cortar, a grelha de grupos (5 campos) é a candidata natural e a primeira pergunta sobrevive sozinha — é ela que responde a «onde há profilaxia pré-exposição ao VIH (PrEP)». A lista de populações-chave deve ser confirmada contra a norma do PNLS antes de ir a terreno.

### 17.3.1 · Profilaxia pós-exposição ao VIH (PEP) após exposição ocupacional

**Completa a profilaxia pós-exposição ao VIH (PEP) nas duas situações fora do contexto da violência sexual, que está em 10.E.3.3.**

**A profilaxia pós-exposição ao VIH (PEP) ocupacional é a que protege o próprio pessoal de saúde** e pertence ao mesmo universo da segurança no trabalho que a comissão de 19.2.16.

A escala pergunta pelo horário porque a janela é de 72 horas e, na prática, um acidente ocorre em turno: uma unidade que só fornece a profilaxia pós-exposição ao VIH (PEP) de manhã fornece-a a uma fracção dos casos. **Depende do bloco de medicamentos, que está parqueado** — sem antirretrovirais em stock a declaração não se verifica.

### 17.3.2 · Profilaxia pós-exposição ao VIH (PEP) após exposição sexual fora do contexto da violência

**Remissão importante, para não duplicar:** a profilaxia pós-exposição ao VIH (PEP) após violação ou violência sexual é a linha 10.E.3.3 e **não se repete aqui** — é lá que é medido. As duas leituras devem ser coerentes: uma unidade que declara a PEP aqui e não a declara em 10.E.3.3 é uma inconsistência a assinalar.

### 17.4 · Tratamento antirretroviral — porta

**A porta é mais larga do que a caixa actual, de propósito:** inclui o seguimento de doentes já em tratamento, e não apenas o início. Num país com tratamento descentralizado, a unidade que reconsulta e redispensa sem iniciar é a maior parte da rede, e a porta passa a incluí-la expressamente. A definição do Guião — «se for fornecido ARV como rotina de acordo com os protocolos do PNLS» — mantém-se válida para as duas situações.

### 17.4.1 · Tratamento antirretroviral por grupo de idade

O indicador conta as opções 1 e 2 — isto é, o seguimento conta como prestação, o que confirma a decisão de alargar a porta. Três caixas, sete indicadores.

**O tratamento pediátrico é a lacuna clássica da descentralização:** as formulações infantis têm cadeia de abastecimento própria e o seguimento exige competência distinta, pelo que a cobertura é muito mais estreita do que a de adultos. A grelha por grupo, a partir da caixa 17.5 da Ficha, permite ver essa diferença.

### 17.4.2 · Componentes do tratamento antirretroviral

**Quatro caixas, três indicadores.**

O que conta aqui é menos quem **inicia** o tratamento e mais quem o **mantém**, porque é a continuidade que determina o resultado — e a continuidade é trabalho de cuidados primários, não de hospital. O indicador de adesão exige as duas linhas ao mesmo tempo, o aconselhamento e o seguimento, e é por isso que são duas caixas e não uma.

### 17.4.3 · Procura activa de faltosos — tratamento antirretroviral

**Porque entra.** A continuidade dos cuidados depende de a unidade saber quem faltou e ir procurá-lo. A mesma pergunta repete-se em cada linha de cuidado com consultas marcadas e, no fim, em 18.4.2, como função dos ADECOS.

**Verificação a programar.** Na resposta 1, pedir para ver a lista ou o livro de faltosos do último mês.

### 17.5 · Prevenção da transmissão vertical

Mantém-se o código e a posição na Ficha; muda apenas o enunciado, que passa a dizer por palavras aquilo que o Guião já define, e separa a mãe do recém-nascido nas opções, porque são duas prestações com cadeias distintas.

**Uma precisão de vocabulário:** a profilaxia ao recém-nascido exposto não é tratamento de uma criança seropositiva, e o enunciado passa a distinguir as duas situações.

**Ampliação não incluída:** a grelha completa da transmissão vertical (13 linhas) daria mais 13 indicadores, e quatro dessas linhas já entram pela grelha pré-natal de 16.1.1.

### 17.6 · Cuidados e apoio ao doente com VIH

Uma caixa, dois indicadores. **Acrescenta à testagem e ao tratamento a terceira perna do VIH, os cuidados e o apoio** — o cotrimoxazol profiláctico, o tratamento das infecções oportunistas, o rastreio da tuberculose no doente com VIH, o apoio nutricional —, que é exactamente o trabalho de um centro de saúde com doentes em tratamento estável.

### 17.7 · Tuberculose — porta

**Porque mudou.** A caixa da Ficha corresponde especificamente ao DOTS — o Guião define-a como «tratamento anti-TB, directamente observável, de acordo com as normas do PNLTB» —. A proposta passa a abranger também a unidade que diagnostica e refere, ou que faz rastreio de contactos sem administrar o tratamento observado.

A porta alarga-se para qualquer serviço de tuberculose, e **o DOTS propriamente dito passa a ser uma linha da grelha de 17.7.2, onde conserva integralmente a definição do Guião**. Nada se perde e a leitura fica mais fina: passa a ser possível separar as unidades que diagnosticam das que tratam, que é a distinção que organiza a rede de tuberculose.

### 17.7.1 · Diagnóstico da tuberculose

O indicador conta as opções 1, 2 e 3 — isto é, cumpre-se também pelo envio da amostra, o que é adequado à rede de cuidados primários, onde a baciloscopia se faz muitas vezes no hospital municipal.

A terceira opção está separada porque **na tuberculose o encaminhamento do doente e o envio da amostra têm consequências programáticas diferentes: um doente encaminhado é um doente que pode não chegar.**

### 17.7.2 · Seguimento do doente com tuberculose

**A terceira linha é o DOTS da Ficha, com a definição do Guião conservada palavra por palavra**, incluindo a referência às normas do PNLTB. Nada muda para quem responde a essa linha; muda apenas que ela passa a ter duas companheiras que a tornam interpretável.

A separação das três prestações é a mesma opção de desenho do tratamento antirretroviral e pela mesma razão: **o que determina a cura da tuberculose não é iniciar o tratamento, é completar os seis meses** — e os três indicadores medem as três condições de o completar: ter consulta, ter medicamento e ter acompanhamento.

### 17.7.3 · Testagem do VIH nos doentes com tuberculose

**17.7.3 é a única ligação entre os dois programas verticais em todo o instrumento.** A co-infecção TB-VIH é a situação em que cada programa depende do outro para funcionar. Verificação a programar: uma unidade que trata tuberculose, tem teste rápido de VIH e não testa os doentes com tuberculose é uma lacuna de organização e não de recursos — e portanto barata de corrigir.

### 17.7.4 · Tuberculose resistente aos medicamentos

**17.7.4** não é prestação de cuidados primários, mas o mapa de onde se trata tuberculose resistente define para onde referir, e é o denominador natural de qualquer investimento em diagnóstico molecular.

### 17.7.5 · Quarto de isolamento

**17.7.5** pergunta-se directamente, em vez de se deduzir do inventário de enfermarias. Duas razões: a nossa lista de camas não tem linha de isolamento; e o isolamento interessa também às unidades sem internamento, onde um espaço de espera separado para o doente com tosse é medida de controlo de infecções com valor próprio. É o único elemento da família do controlo de infecções que se obtém por declaração.

### 17.7.6 · Procura activa de faltosos — tuberculose

**Porque entra.** A continuidade dos cuidados depende de a unidade saber quem faltou e ir procurá-lo. A mesma pergunta repete-se em cada linha de cuidado com consultas marcadas e, no fim, em 18.4.2, como função dos ADECOS.

**Verificação a programar.** Na resposta 1, pedir para ver a lista ou o livro de faltosos do último mês.

### 17.8.1 · Malária — porta

**É um dos acrescentos com mais peso de toda a secção:** a malária é a principal causa de consulta e de óbito na rede de cuidados primários angolana, e o quesito da Ficha sobre malária incide na distribuição de redes mosquiteiras. Três caixas novas acrescentam o **diagnóstico e o tratamento** e trazem oito indicadores.

### 17.8.2 · Via de diagnóstico da malária

**A terceira linha de 17.8.2 é a mais importante e a que raramente se pergunta:** o diagnóstico apenas clínico, sem teste, tem indicador próprio porque é o indicador de uma prática a corrigir — trata quem não tem malária e deixa sem diagnóstico quem tem outra coisa. Medi-la sem a julgar é o que permite dimensioná-la.

### 17.8.3 · Tratamento da malária

Em **17.8.3**, as opções separam a malária simples da malária grave, porque é a distinção clínica que decide o percurso do doente. As definições seguem o protocolo nacional de tratamento da malária. Verificação a programar: uma unidade que declara tratar casos graves e não tem artesunato injectável é uma inconsistência a assinalar quando o bloco de medicamentos entrar.

## Secção 18 — Acção comunitária

### 18.1 · Distribuição de redes mosquiteiras

Mantém-se o código e o sentido. A única alteração é trazer para dentro da pergunta o critério que o Guião já fixa — «distribuição regular (mais de 6 meses no ano)» —, para que todos os inquiridores o apliquem da mesma maneira.

**É contributo próprio:** o instrumento internacional só pergunta pela rede entregue em consulta — pré-natal, pós-parto e cuidados à criança — e não pela distribuição à população em geral, que é a modalidade do programa angolano. As duas leituras passam a coexistir.

### 18.2 · Brigadas móveis de vacinação

Mantêm-se integralmente, com as definições do Guião — incluindo as três exclusões, que são o que dá sentido à resposta — trazidas para dentro da pergunta. As duas caixas continuam separadas porque **medem esforços logísticos de ordem diferente**: uma unidade que faz equipas avançadas perto e não faz brigadas longe tem um problema de transporte, não de organização.

**Contributo próprio do Mapa Sanitário.** A actividade extramural e as brigadas móveis organizadas pela unidade são uma parte importante dos cuidados primários num país com a densidade populacional de Angola.

**Articula-se com a secção 7:** as motorizadas e as bicicletas da Ficha são, em muitas unidades, o meio exacto com que isto se faz.

### 18.4 · ADECOS

A caixa existe e mantém-se; **o que se acrescenta é o campo da quantidade, como o Guião já prevê**: «ADECOS: Agentes de Desenvolvimento Comunitário e de Saúde, trabalhando na Unidade Sanitária. Nesse caso, especificar a quantidade» (folhas 12 e 13).

### 18.4.0 · Número de ADECOS

Uma caixa de número resolve, e passa a haver pela primeira vez **um inventário da força de trabalho comunitária da rede**, que é informação central para um plano de investimentos em cuidados primários.

### 18.4.1 · Articulação com os ADECOS

**Seis caixas, uma por programa — e é o achado mais importante desta secção.** A ligação com os agentes comunitários mede-se em cada um dos seis programas, porque **a articulação entre a unidade e a comunidade é constitutiva dos cuidados primários e não um extra**.

Angola tem a infra-estrutura — os ADECOS existem e a Ficha já os registra — e o que se acrescenta é perguntar **para quê**, que é o que estas seis linhas fazem.

Reunir as seis numa única grelha, em vez de as dispersar pelos blocos, foi opção de desenho: quem responde pensa nos ADECOS uma vez e responde seis vezes, em lugar de ser interrompido seis vezes ao longo da secção.

**Verificação a programar.** Declarar articulação em seis áreas com zero ADECOS é uma inconsistência a assinalar.

### 18.4.2 · Procura de faltosos pelos ADECOS

**Porque entra.** A procura de quem faltou é uma das funções dos ADECOS. Esta grelha fecha a pergunta feita em cada linha de cuidado: ali pergunta-se se a unidade procura os faltosos; aqui, se os ADECOS fazem essa procura.

## Secção 19 — Gestão

### 19.1.1 Propriedade

**Porque mudou.** A opção «privada não lucrativa» desdobra-se em missão religiosa e organização não governamental, que em Angola têm padrões de financiamento, de pessoal e de permanência muito diferentes. Separá-las custa zero caixas e acrescenta uma leitura nova. Acrescenta-se ainda a propriedade pública não pertencente ao Serviço Nacional de Saúde que não seja militar.

### 19.1.2 Gestão

**Porque mudou.** Das opções da Ficha — «pública, privada, mista, outra» —, a gestão pública desdobra-se por nível, para responder à pergunta que importa à descentralização: **qual** nível público gere a unidade. A distinção entre gestão provincial e gestão municipal é central ao desenho da reforma dos cuidados primários e passa assim a ser recolhida. O enunciado passa também a dizer por palavras que a gestão pode não coincidir com a propriedade, para facilitar o preenchimento.

### 19.1.3 Orçamento próprio

**Porque está aqui.** Na Ficha, este quesito está no cabeçalho, junto da data da recolha. É um quesito de gestão financeira e passa para esta secção, onde deve ser combinado com outras informações sobre o financiamento da unidade. Conserva o código 19.1.3 até essa decisão; as opções estão nas pendências, no fim desta subsecção.

### 19.2.1 a 19.2.17 · Lista dos serviços e órgãos de gestão

**Porque mudou.** A escala de três níveis capta, sem acrescentar caixa nenhuma, a situação mais comum na rede: **a comissão existe no papel e não se reúne.** Com uma caixa de 0-1, essa unidade responde o mesmo que a unidade onde a comissão trabalha todas as semanas.

**Todas as comissões nomeadas se mantêm**, por decisão expressa, incluindo as que não têm equivalente no instrumento internacional.

### 19.2.14.1 · Revisão formal de casos

**É a aplicação mais clara da regra de que a porta é a actividade e não o órgão.** A porta deste bloco não é a existência da Comissão de Óbitos Hospitalares (quesito 19.2.14 da lista acima), mas a realização efectiva de revisões — porque **uma unidade pode revisar óbitos maternos sem ter comissão constituída, e é precisamente dela que queremos saber**. A caixa da comissão mantém-se, em paralelo, na lista de três níveis.

**A porta é o internamento e não o tipo de unidade**: o denominador de todo o bloco são as unidades com internamento, seja qual for o seu tipo. Um centro de saúde com camas onde ocorreu um óbito materno tem de ser perguntado — e é precisamente o caso que mais interessa à mortalidade materna.

### 19.2.14.3 · Revisão de caso nos últimos 3 meses

**As perguntas 19.2.14.3 e 19.2.14.6 são a verificação da declaração:** separam «realizamos rotineiramente» de «realizámos de facto nos últimos 3 meses», que é a diferença entre um sistema a funcionar e um sistema no regulamento.

### 19.2.13.1 · Comissão e reuniões de prevenção e controlo de infecções

Mesmo desenho: a actividade, não o órgão. A segunda linha de 19.2.13.1 — reuniões multidisciplinares onde os resultados são analisados — é a que capta as unidades sem comissão constituída que, apesar disso, discutem infecções. **É a parte da prevenção e controlo de infecções que cabe na gestão;** o resto — normas de prevenção e de isolamento, pessoal formado, avaliação sistemática, normas de limpeza — fica para um bloco próprio, ainda por construir.

### 19.2.18.1 · Actividades de garantia de qualidade

**Quesito inteiramente novo**, e o único acrescento desta subsecção que não tem correspondência em nenhuma caixa da Ficha. O bloco tem nove caixas, quase todas de resposta declarada pelo respondente.

### 19.2.18.6 · Documentação da análise da qualidade

O quesito **19.2.18.6** é o que separa um sistema real de um sistema declarado: pede documentação, e distingue «observado» de «referido, não visto».

### 19.2.1 + 19.2.10 e 19.2.2 + 19.2.6 · Arquivo, reporte e comité de gestão

As caixas mantêm-se na lista de três níveis. Ficam para o domínio de gestão dois blocos completos:

**Cadeia de arquivo, registo e reporte de dados** (a partir de 19.2.1 e 19.2.10) — cerca de 12 campos.

**Equipa ou comissão de gestão** (a partir de 19.2.2 e 19.2.6) — periodicidade e data das reuniões, plano operacional escrito e referência ao plano nas decisões, e sistema de rotina de participação da comunidade na gestão — cerca de 6 campos.

### Pendências desta subsecção

**19.2.15 — Comissão de Medicamentos.** A verificar se corresponde a uma comissão de aquisições de medicamentos, produtos e equipamento; se corresponder, a caixa que já existe passa a medir também essa função, sem qualquer alteração.

**19.2.8 e 19.2.9 — estatuto de unidade de ensino.** Propõe-se um quesito que registe se esta unidade sanitária acolhe formação de estudantes, internos, médicos em especialização ou técnicos de saúde em formação. Complementa as caixas dos órgãos que a Ficha já tem (escola de formação, núcleo de formação permanente) com a pergunta sobre o estatuto.

**19.1.3 — Orçamento próprio: com que informações combinar.** O quesito passou do cabeçalho para esta subsecção. Falta decidir que informações sobre o financiamento da unidade o acompanham. O instrumento internacional recolhe-as nestes temas:

| Tema | O que se pergunta |
|---|---|
| Autonomia de gestão | Se a unidade gere conta bancária própria e decide os seus gastos |
| Linhas orçamentais | Se o orçamento tem verbas para manutenção, medicamentos, pessoal e outras despesas |
| Fontes de financiamento | De onde vem o financiamento da unidade — Estado, parceiros, taxas cobradas aos utentes |
| Taxas cobradas aos utentes | Se a unidade cobra taxas, por que serviços, e se há isenções |
| Auditoria financeira | Se a unidade tem auditoria financeira externa anual |

A proposta é começar pela autonomia de gestão e pelas fontes de financiamento, as mais próximas da pergunta actual e as mais fáceis de responder numa visita.

## Secção 20 — Serviços gerais

### 20.1 · Acesso a transporte de emergência

O enunciado inclui expressamente o veículo **chamado de outro local**, porque é essa a situação da maior parte dos centros de saúde — e uma pergunta sobre veículo próprio deixaria essas unidades contadas como unidades sem transporte de emergência.

### 20.1.1 · Transporte de emergência disponível hoje

**20.1.1 é a verificação da declaração:** ter acesso a uma ambulância e ter uma ambulância com combustível e motorista hoje são coisas diferentes. Articula-se com 14.6 (urgência), com 3.9 (sistema de referência) e com a secção 7 (frota), sem duplicação de campo.

### 20.2 a 20.18 · Lista dos serviços gerais

Mesma razão de 19.2: a escala de três níveis distingue o serviço que existe e funciona do que existe no organigrama. A lista mantém-se por inteiro, incluindo os serviços sem equivalente internacional — capela, ajardinamento, salão de actos —, que são informação de gestão patrimonial com valor próprio.

### 20.18.1 · Recolha da opinião dos utentes

O Gabinete do Utente existe na Ficha como caixa e passa a ter o seu conteúdo medido: não se pergunta apenas se existe, mas se a opinião dos utentes é de facto recolhida e analisada, e com que periodicidade. É a única porta de entrada do instrumento para a perspectiva de quem usa os serviços.

### 20.7 e 20.16 · Duas remissões

**20.7** é desenvolvido na secção 6, Conectividade e meios informáticos. **20.16** é desenvolvido nos quesitos 5.5 e 5.6, na secção 5. Em 17 ficam apenas as linhas de remissão, sem caixa a preencher, para que a informação não seja recolhida duas vezes.

### 20.8 · Bloco de manutenção

A caixa de 20.8 mantém-se na lista de três níveis. O bloco completo — cerca de 25 campos — fica para o domínio de gestão e é a porta de entrada para duas subáreas inteiras:

**Manutenção de sistemas de infraestrutura** — se é feita manutenção preventiva ou correctiva, se existe plano de manutenção, e uma lista de 9 sistemas: electricidade, água, saneamento e esgotos, incinerador, ventilação ou ar condicionado, oxigénio central, altifalantes e comunicações, extintores e computadores, cada um com a escala «rotineiramente / às vezes, não rotineiramente / nunca / não aplicável».

**Manutenção de equipamento médico, de esterilização e de laboratório** — se é feita inspecção, teste ou manutenção preventiva, se existe plano conforme as recomendações do fabricante, e uma lista de 11 equipamentos: tanques ou concentradores de oxigénio, ventiladores, frigoríficos de vacinas, medicamentos ou sangue, incubadoras, autoclaves eléctricas, esterilizadores eléctricos de calor seco, analisador de hematologia, analisador de bioquímica, aparelho de raios X, TAC e ecógrafo — e ainda se existe um sistema de rotina de inspecção, manutenção e substituição.

**É candidato legítimo a entrar nesta ronda**, e está na lista de decisões da nota de apresentação: a manutenção é o lugar onde a diferença entre a contagem de equipamento (secção 9) e a sua verificação se explica.

