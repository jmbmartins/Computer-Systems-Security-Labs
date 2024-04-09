# Prefácio

Esta  prova  vale  até  00 valores  na  nota  final  da unidade curricular.
Consiste em dar respostas  a várias  perguntas  e/ou  no desenvolvimento de
várias  tarefas  (num  total  de  21)  que   deve  levar  a  cabo  num  dos
computadores  do  laboratório  da  sala  6.27  ou,  alternativamente com  a
conivência  do  docente,  num computador pessoal. As respostas às perguntas
devem ser dadas na própria plataforma.  As  questões  e tarefas têm todas o
mesmo valor.

O desenvolvimento das tarefas pressupõe que não tem acesso à Internet e não
é permitida a  consulta de  documentação para  além dos manuais disponíveis
via  linha  de comandos (e.g., openssl), pelo  que, durante toda  a  prova,
qualquer ligação secundária à Internet  deve estar desativada e deve apenas
ter  no ecrã (e em execução)  uma janela  para o  terminal e outra  para um
editor de texto. Não deve  estar qualquer pen ligada à máquina utilizada. O
não  cumprimento  de  qualquer uma  destas  condições  é  penalizada  com a
anulação da prova.

Leia o enunciado das perguntas e  tarefas  atentamente. Siga  as instruções
dadas com afinco, já que  algumas respostas e resultados  dependem do rigor
com que são introduzidos comandos no terminal.

Quaisquer  tentativas  de  fraude  durante  a  resolução  desta  prova  são
penalizadas  com  a  sua   anulação.   Queira   desligar  todos  os  outros
dispositivos (e.g., móveis) antes do início da prova.

ATENÇÃO: no final, é necessário  submeter o teste, executando o script

>  `./XX-FIN.sh`

Prima Enter para continuar...
## Responder a Questões

Para responder a uma questão, execute o script com o número da questão. Por
exemplo, digite

>  `./01-MC.sh`

para responder à questão de Escolha Múltipla (Multiple Choice - MC) 01.

Caso  já  tenha  respondido à  questão  antes  (mas  quiser  submeter  nova
resposta), digite

>  `./01-MC.sh.DONE`

## Fazer Tarefas

Para fazer  uma  tarefa,  execute primeiro o script com a questão/
tarefa uma vez. Por exemplo, digite

>  `./02-DA.sh`

para verificar o que é necessário fazer nesta tarefa. 
Saia sem introduzir uma resposta.

Para  submeter resposta depois  de  executar o que é pedido  para a tarefa,
simplesmente execute o script novamente:

> `./02-DA.sh`

e introduza uma resposta desta feita.

Caso  já  tenha  respondido à  questão  antes  (mas  quiser  submeter  nova
resposta), digite

>  `./01-DA.sh.DONE`

# 01. Tarefa/Questão
O primeiro conjunto de questões  e  tarefas deste laboratório procura ajudar
a explorar  os  protocolos  de  Transferência  Inconsciente,  nomeadamente o
protocolo de Transferência Inconsciente 1 de 2.

Q.: Quantas trocas  de  mensagens  acarreta  o  protocolo  de  Transferência
Inconsciente 1 de 2?

1. Neste protocolo, as entidades não se falam porque estão zangadas!
2. São trocadas quatro mensagens.
3. Apenas é trocada uma mensagem.
4. São trocadas três mensagens.
5. São trocadas cinco mensagens.
6. São trocadas duas mensagens.

# 02. Tarefa/Questão
Q.: Qual das seguintes é verdadeira?

1. Na Transferência Inconsciente 1 de 2,  o emissor envia três mensagens,
    enquanto o recetor só envia uma.
2. Na Transferência Inconsciente  1 de 2,  o  emissor envia uma mensagem,
    enquanto o recetor envia três.
3. Na Transferência Inconsciente  1 de 2,  o  recetor não envia qualquer,
    mensagem e, portanto, não se trata de um protocolo.
4. Na Transferência Inconsciente 1 de 2,  o emissor envia duas mensagens,
    e o recetor envia outras duas.
5. Na Transferência Inconsciente  1 de 2,  o  emissor não envia qualquer,
    mensagem e, portanto, não se trata de um protocolo.



# 03. Tarefa/Questão
Q.: É verdade que a construção  do  protocolo  de Transferência Inconsciente
1 de 2 proposto por Even, Goldreich, Lempel e Micali faz uso da cifra RSA?

1. Hola, muchas gracias!
2. Yes, it is a lie.
3. Sim, é berdade.
4. Non, ne pas vrai.

Insira uma resposta (um número) seguida de [ENTER].
Caso haja várias opções certas, insira uma resposta de cada vez.
(coloque um 0 para não responder e sair): Connection to 188.83.47.21 closed by remote host.


# 04. Tarefa/Questão
Q.: Na construção do protocolo de Transferência Inconsciente 1 de 2 proposto
por Even, Goldreich,  Lempel  e  Micali,  o  que  é  que  o recetor envia ao
emissor?

1. Dois números inteiros.
2. Um número inteiro.
3. Uma chave pública RSA.
4. Dois criptogramas.
5. Um cesto de frutas.



# 05. Tarefa/Questão
Q.: Na construção do protocolo de Transferência Inconsciente 1 de 2 proposto
por Even, Goldreich,  Lempel  e  Micali,  o  que  é  que  o emissor envia ao
emissor na sua última mensagem?

1. Dois criptogramas.
2. Dois números inteiros.
3. Uma declaração de amor.
4. Um número inteiro.
5. Uma chave pública RSA.


# 06. Tarefa/Questão
Considere que a Alice (emissor) e  o Bob (recetor) estão a usar um mecanismo
seguro de Transferência Inconsciente 1 de 2,  como aquele proposto por Even,
Goldreich, Lempel e Micali.

Q.: É verdade que, se quiser,  o Bob pode obter ambas as mensagens envidadas 
pela Alice?

1. Sim, é verdade.
2. Não, é verdira.
3. Sim, é mendade.
4. Não, é mentira.

# 07. Tarefa/Questão
Considere que a Alice (emissor) e  o Bob (recetor) estão a usar um mecanismo
seguro de Transferência Inconsciente 1 de 2,  como aquele proposto por Even,
Goldreich, Lempel e Micali.

Q.: É verdade que,  se  quiser,  a  Alice  pode  alegar  não  saber qual das
mensagens é que o Bob recebeu?

1. Sim, é verdade.
2. Não, é verdira.
3. Sim, é mendade.
4. Não, é mentira.



# 08. Tarefa/Questão
Considere que a Alice (emissor) e  o Bob (recetor) estão a usar um mecanismo
seguro de Transferência Inconsciente 1 de 2,  como aquele proposto por Even,
Goldreich, Lempel e Micali.

Q.: É verdade que, se quiser,  a Alice tem forma de saber qual das mensagens
é que o Bob recebe?

1. Sim, é verdade.
2. Sim, é mendade.
3. Não, é mentira.
4. Não, é verdira.



# 09 - Tarefa/Questão
Considere que a Alice (emissor) e  o Bob (recetor) estão a usar um mecanismo
seguro de Transferência Inconsciente 1 de 2,  como aquele proposto por Even,
Goldreich, Lempel e Micali.  Como  uma das cifras usadas neste mecanismo é a 
RSA, a Alice já gerou o seu par  de  chaves e guardou a sua chave pública no
ficheiro pk.pem. Encontra o ficheiro na diretoria 09.

Q.: Emita o comando openssl que  lhe  permite  formatar a chave para análise 
humana e ver o tamanho do módulo da chave  pública,  possibilitando escolher
a opção certa em baixo.

Note que o que é pedido é o tamanho do módulo, não o tamanho do ficheiro!

1. O tamanho do módulo da chave RSA é 512.
2. O tamanho do módulo da chave RSA é 1024.
3. O tamanho do módulo da chave RSA é 2048.
4. O tamanho do módulo da chave RSA é 4096.



# 10 - Tarefa/Questão
Q.: Qual  o  problema  matemático intratável  que  sustenta  parcialmente  a
segurança do protocolo  de  Transferência  Inconsciente  1 de 2 proposto por
Even, Goldreich, Lempel e Micali?

1. Problema do logaritmo discreto.
2. Problema do paradoxo do aniversário.
3. Problema bicudo.
4. Problema da fatorização de números primos.
5. Problema do lançamento da moeda 1 de 2.
6. Problema financeiro.

# 11. Tarefa/Questão
Q.: Por curiosidade, em quais dos seguintes primitivas ou protocolos é que a
segurança depende parcial ou totalmente do problema do logaritmo discreto?

1. Protocolo de Identificação de Schnorr.
2. Cifra ElGamal.
3. Cifra RSA.
4. Protocolo  de  Transferência  Inconsciente  1 de 2 proposto por
    Even, Goldreich, Lempel e Micali
5. Cifra Advanced Encryption Standard.
6. Protocolo de Acordo de Chaves Diffie-Hellman.



# 12. Tarefa/Questão
Considere que a  Alice  (emissor)  e  o  Bob  (recetor) estão a jogar o jogo
descrito na aula teórica e que resolveram  usar o mecanismo de Transferência 
Inconsciente 1 de 2 proposto  por  Even, Goldreich, Lempel e Micali. Já  vão 
avançados no protocolo. Neste caso,  o Bob escolheu decifrar a mensagem m0 e 
já gerou  uma  chave  k=110,  tendo  enviado  a  sua  cifra à Alice. A Alice 
devolveu os últimos dois criptogramas: 
* c0=123 e 
* c1=168.

Q.: Qual dos seguintes pares de números  pode representar o par de mensagens
geradas pela Alice?

1. 13 e 18.
2. 20 e 18.
3. 14 e 16.
4. 11 e 20.



# 13. Tarefa/Questão
Considere que determinado conjunto  de  entidades estão a iniciar o processo
de partilha de segredos de Shamir. Estão a usar um polinomial de grau 3.

Q.: Depois de partilhado o segredo corretamente,  quantas entidades precisam
juntar as suas partilhas  para  conseguir,  de  facto,  recuperar  o segredo
original?

1. Precisam juntar 1 partes.
2. Precisam juntar 3 partes.
3. Precisam juntar todas as partes, independentemente de quantas forem.
4. Precisam juntar 5 partes.
5. Precisam juntar 4 partes.
6. Precisam juntar 2 partes.



# 14. Tarefa/Questão
Na aula subordinada ao tema  da  Partilha de Segredos de Shamir foi dada uma
intuição para a segurança do esquema,  e  que esta estaria relacionada com o
número de polinomiais de grau k que passam por k pontos.

Q.: Quantos polinomiais de grau 5 passam por 5 pontos no plano R x R (R^2)?

1. Não passa nenhum polinomial de grau 5, mas às vezes para lá o comboio.
2. Passam apenas 6 polinomiais de grau 5.
3. Passa apenas um polinomial de grau 5.
4. Passam infinitos polinomiais de grau 5.
5. Passam apenas 5 polinomiais de grau 5.
6. Passam apenas 4 polinomiais de grau 5.



# 15. Tarefa/Questão
Um grupo de 3  amigos  estão  a pensar usar a Partilha de Segredos de Shamir
para partilhar um segredo cabeludo  entre  todos. Um deles (o Chico Esperto)
disse que deviam usar um polinomial de grau 3.

Q.: O Chico Esperto tem ou não tem razão?

1. O Chico Esperto precisa tirar o mestrado na UBI.
2. O Chico Esperto tem razão.



# 16. Tarefa/Questão
Um grupo de  amigos  está  a  usar  a  Partilha  de Segredos de Shamir para
partilhar um segredo cabeludo entre  todos.  Neste momento,  já prepararam o 
polinomial para gerar as várias partilhas:

$$
f(x) = 1 + 6 x + 19 x^2 + 14 x^3 mod 23
$$

em que x^y denota x elevado a y.

Q.: Qual dos seguintes pontos é uma partilha válida nestas condições?

Dica: em Python,  a  exponenciação  de  um  número  n por e módulo P faz-se 
n**e % P. Isto é, n^e mod P é o mesmo que n**e % P.

1. (12, 1)
2. (17, 20)
3. (10, 25)
4. (7, 3)



# 17. Tarefa/Questão
Um grupo de  amigos  está  a  usar  a  Partilha  de Segredos de Shamir  para
partilhar um segredo cabeludo entre  todos.  Neste momento,  já prepararam o 
polinomial e as várias partilhas (incluidas nas opções em baixo).

Q.: Qual das partilha incluídas em baixo não é admissível?

1. (0, 2)
2. (8, 14)
3. (11, 11)
4. (17, 15)
5. Todas são admissíveis.
6. Não há dados suficientes para decidir.



# 18. Tarefa/Questão
Um grupo de três amigos usou a Partilha de Segredos de Shamir para partilhar 
o número de Bitcoins  que  tinham.  Depois  de  10  anos,  juntaram todas as 
partilhas necessárias  para  recuperar  o  segredo  e  obtiveram  o seguinte 
polinomial:
$$
f(x)=22(x-10)(x-18)/10+19(x-7)(x-18)/22+0(x-7)(x-10)/19 ~mod~23
$$

Q.: Qual o número  de  Bitcoins  que  este  grupo  de  amigos comprou na sua
juventude?

Dica: em  Python,  a  exponenciação  de  um  número `n` por `e` módulo `P` faz-se 
`n**e % P`. Isto é, `n^e mod P` é o mesmo que `n**e % P`.

Nota: não esquecer que a divisão módulo um primo não se faz da mesma forma!

1. O número de Bitcoins que os amigos tinham era 5.
2. O número de Bitcoins que os amigos tinham era 13.
3. O número de Bitcoins que os amigos tinham era 3.
4. O número de Bitcoins que os amigos tinham era 25.

# 19 - Tarefa/Questão
Um grupo de três amigos usou a Partilha de Segredos de Shamir para partilhar 
o número de Bitcoins  que  tinham.  Depois  de  10  anos,  juntaram todas as 
partilhas necessárias para recuperar o segredo, nomeadamente:
* (7, 15);
* (12, 16);
* (17, 9).

Q.: Qual o número  de  Bitcoins  que  este  grupo  de  amigos comprou na sua
juventude?

Dica: em  Python,  a  exponenciação  de  um  número `n` por `e` módulo `P` faz-se 
`n**e % P`. Isto é, `n^e mod P` é o mesmo que `n**e % P`.

1. O número de Bitcoins que os amigos tinham era 2.
2. O número de Bitcoins que os amigos tinham era 12.
3. O número de Bitcoins que os amigos tinham era 25.
4. O número de Bitcoins que os amigos tinham era 4.



# 20 - Tarefa/Questão
O esquema  de  Partilha  de  Segredos  de  Shamir  tem  várias  propriedades
interessantes. Uma dessas propriedades é o facto de ser Extensível.

Q.: Ao que é que se refere essa propriedade?

1. Ao facto das partilhas terem todas  o mesmo tamanho e serem também do
    mesmo tamanho que o segredo inicial.
2. Ao facto de se poderem adicionar mais partilhas sempre que necessário
    e sem ser preciso mudar parâmetros do sistema.
3. Ao facto de uma pessoa musculada  poder  esticar o polinomial, e este
    não se partir, por mais que seja esticado!
4. Ao facto de ser seguro  para  campos  finitos  muito grandes (primo P grande).



# 21. Tarefa/Questão
O esquema  de  Partilha  de  Segredos  de  Shamir  tem  várias  propriedades
interessantes.  Uma dessas  propriedades  refere-se ao facto de ser possível
criar tantas partilha quanto  necessário,  e de ser possível dar mais do que
uma partilha a várias  entidades  (permitindo,  por exemplo,  que o líder de 
uma organização possa  obter  o  segredo  sozinho,  mas sejam necessários 10
trabalhadores para conseguirem o mesmo).

Q.: Que nome se dá a essa propriedade?

1. A propriedade de ser Extensível.
2. A propriedade de ser Mínimo.
3. A propriedade de ser Flexível.
4. A propriedade de ser Bonito.
5. A propriedade de ser Dinâmico.

