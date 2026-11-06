"""Gera habilidades/index.html: curso de habilidades de venda aplicado ao MineMyLead."""
import os, html, json
E = html.escape
OUT = os.path.join(os.path.dirname(__file__), "..", "habilidades")
os.makedirs(OUT, exist_ok=True)

# (id, título, minutos, objetivo, ideia[], diga[], evite[], exercício, checklist[])
L = [
 ("mentalidade", "Vender é ajudar a decidir", 5,
  "Entender o seu papel: ajudar o cliente a decidir bem, não empurrar um produto.",
  ["O cliente compra quando entende o problema dele, vê que a solução serve e confia em quem está falando. As três coisas acontecem numa conversa, não num discurso.",
   "Seu papel é ajudar o cliente a decidir bem, inclusive quando a resposta honesta é “isso não é para você”. Quem diz isso uma vez ganha a confiança para todas as outras vezes.",
   "No MineMyLead, vendemos um ponto de partida de verdade: empresas certas, com dono, contato e prova. A conversa com essas empresas é do cliente. Não prometemos resposta, venda nem resultado, e isso torna a sua fala mais forte, porque tudo o que você diz pode ser cumprido."],
  ["Prefiro te dizer agora se não serve para o seu caso.", "A gente entrega o ponto de partida. A conversa com as empresas é sua."],
  ["Funciona para qualquer empresa.", "Você vai fechar muito com isso."],
  "Escreva em duas frases quem é o cliente que NÃO deve comprar o pacote. Depois diga em voz alta como você falaria isso para ele, com gentileza.",
  ["Sei dizer, em uma frase, o que vendo e o que não prometo", "Sei para quem o produto não serve"]),
 ("preparacao", "Prepare-se em 10 minutos", 5,
  "Chegar à call sabendo o suficiente para falar pouco e perguntar bem.",
  ["Preparar não é decorar. É reunir o mínimo que mostra respeito pelo tempo do cliente e deixa você livre para ouvir.",
   "Dez minutos bastam: leia o pedido (nome, site ou rede social, o que vende), abra o site ou o Instagram dele, anote uma hipótese de quem é o cliente ideal dele, escolha duas perguntas de descoberta, abra o pacote de exemplo e teste som, tela e internet.",
   "Tenha a hipótese, mas não a defenda. Ela serve para fazer a primeira pergunta, e a call serve para o cliente corrigir você."],
  ["Vi no seu site que você atende [tipo de empresa]. É esse o cliente que você mais quer?"],
  ["Entrar na call sem ter aberto o site dele.", "Fingir que já sabe tudo sobre o negócio dele."],
  "Escolha o site de uma empresa real. Em dez minutos, escreva: o que ela vende, para quem, uma hipótese de cliente ideal e duas perguntas.",
  ["Li o pedido do cliente", "Abri o site ou a rede social dele", "Tenho 2 perguntas prontas", "Testei som, tela e internet"]),
 ("abertura", "Abertura e rapport", 5,
  "Começar a call com calma, pauta combinada e espaço para o cliente falar.",
  ["Os primeiros três minutos definem o ritmo. Se você começa acelerado e falando do produto, o cliente fica na defensiva. Se começa calmo e combinando a pauta, ele relaxa e fala.",
   "Uma boa abertura tem quatro movimentos: agradecer, combinar a duração, dizer o que vai acontecer (entender, mostrar, decidir o próximo passo) e pedir permissão. Fale devagar, use o nome dele e sorria na voz.",
   "Rapport não é bajular nem fingir amizade. É interesse genuíno pelo negócio da pessoa. Uma pergunta sincera sobre o que ela faz vale mais que um elogio."],
  ["Oi, [nome], obrigado por separar esse tempo. Combinei trinta minutos com você. Primeiro quero entender como você vende hoje, depois te mostro o produto e vemos se faz sentido. Pode ser?"],
  ["Começar pelo produto.", "Falar rápido e sem pausa para ele responder."],
  "Grave um áudio de 30 segundos com a sua abertura. Ouça: o ritmo está calmo? Você pediu permissão? Regrave até soar natural.",
  ["Agradeci e combinei a duração", "Disse o que vai acontecer na call", "Pedi permissão", "Falei devagar"]),
 ("descoberta", "Descoberta: perguntas que abrem", 8,
  "Fazer perguntas que levam o cliente a explicar a dor com as próprias palavras.",
  ["Descoberta é a parte que mais vende. Quem descobre bem não precisa convencer: o cliente se convence ao explicar o problema.",
   "Prefira perguntas abertas (o que, como, quanto, quando) às fechadas (sim ou não). Uma estrutura conhecida, o método SPIN, organiza quatro tipos de pergunta: Situação, Problema, Implicação e Necessidade.",
   "Situação: “Como você encontra essas empresas hoje?”. Problema: “É fácil chegar no dono?”. Implicação: “Quanto tempo isso toma por semana? O que você deixa de fazer por causa disso?”. Necessidade: “Se amanhã você tivesse 100 empresas certas com o contato do dono, o que mudaria?”.",
   "Use poucas perguntas de situação (só o necessário) e invista nas de problema e implicação, que fazem o cliente sentir o peso do que descreveu. Não faça perguntas que induzem a resposta."],
  ["O que você vende e para quem?", "Hoje, como você encontra essas empresas? Quanto tempo isso toma por semana?", "O que é mais difícil nisso?", "Se tivesse 100 empresas certas com o contato do dono, o que mudaria na sua semana?"],
  ["Você não acha que perde muito tempo? (induz a resposta)", "Disparar cinco perguntas seguidas sem ouvir."],
  "Reescreva cinco perguntas fechadas como abertas. Ex.: “Você usa lista comprada?” vira “Como foi sua experiência com listas ou anúncios para achar clientes?”.",
  ["Fiz perguntas abertas", "Cobri situação, problema, implicação e necessidade", "Anotei as palavras do cliente"]),
 ("escuta", "Escute mais do que fala", 6,
  "Falar 30% e ouvir 70% na descoberta, e mostrar ao cliente que foi ouvido.",
  ["Quem escuta melhor vende melhor. Na descoberta, a meta é o cliente falar cerca de 70% do tempo.",
   "Quatro hábitos ajudam. Silêncio: espere três segundos antes de responder, pois muita gente completa a resposta nesse tempo. Paráfrase: “Se entendi bem, você perde tempo caçando o contato do dono.” Anotação: escreva as palavras exatas dele e as repita depois. Sem interrupção: não complete a frase do cliente.",
   "Repare nos sinais: hesitação, “mais ou menos”, “é que...”. Eles apontam o que ele ainda não disse. Peça: “Pode me contar mais sobre isso?”."],
  ["Se entendi bem, o que mais pesa hoje é achar o contato certo. É isso?", "Pode me contar mais sobre isso?"],
  ["Interromper para explicar o produto.", "Responder uma pergunta que ele não fez."],
  "Em uma conversa do dia a dia, parafraseie três vezes o que a pessoa disse antes de responder. Perceba como ela reage.",
  ["Esperei 3 segundos antes de responder", "Parafraseei o que ouvi", "Falei menos que ele"]),
 ("demonstracao", "Demonstre o que importa para ele", 6,
  "Mostrar só a parte do produto que responde ao que o cliente disse.",
  ["Quem mostra tudo cansa o cliente. Quem mostra o que ele pediu convence.",
   "A estrutura é simples: lembre a dor com as palavras dele, mostre a parte do aplicativo que resolve, aponte a prova e pergunte se faz sentido para ele.",
   "A demo do MineMyLead cabe em 7 minutos: a lista (1), uma empresa aberta com dono, contato e prova (3), o mapa e as estatísticas (1), o acompanhamento (1) e o fechamento da demo (1). Mostre uma empresa do perfil dele, se já tiver, ou o pacote de exemplo.",
   "Lembre: o aplicativo não envia mensagens. Quem fala com as empresas é o cliente, pelo WhatsApp, telefone ou e-mail dele."],
  ["Você disse que perde tempo caçando o contato. Olha aqui: o contato já vem com tipo e origem.", "Isso faz sentido para o seu dia a dia?"],
  ["Percorrer todas as telas “só para mostrar”.", "Dizer que o sistema envia as mensagens."],
  "Liste três dores hipotéticas de clientes e, para cada uma, a tela do aplicativo que responde. Treine dizer a frase de ligação em voz alta.",
  ["Usei as palavras do cliente na demo", "Mostrei a prova", "Perguntei se faz sentido"]),
 ("preco", "Preço e valor", 6,
  "Dizer o preço com clareza e ancorar o valor no custo atual do cliente.",
  ["Preço dito com insegurança vira objeção. Diga o valor de forma direta e faça silêncio. Quem fala primeiro depois do preço costuma ser quem cede.",
   "Valor não se compara com “barato”, e sim com o que o cliente gasta hoje: o tempo dele, o de quem pesquisa para ele, o dinheiro de anúncios e listas. Faça a conta com os números dele. Exemplo para pensar junto (não é dado nosso nem promessa): 10 minutos por empresa são cerca de 17 horas para 100.",
   "O pacote custa R$ 990, pagamento único, o que dá menos de dez reais por empresa. Antes de pagar, ele pode testar 3 leads de graça. Se pedir desconto, volte ao teste e ao valor por empresa. Exceção só com o Dan."],
  ["O pacote custa R$ 990, pagamento único. Dá menos de dez reais por empresa, com dono, contato e prova. [silêncio]", "Quanto vale uma hora sua, ou de quem pesquisa para você?"],
  ["“É só R$ 990, mas...” (o “só” e o “mas” enfraquecem)", "Dar desconto sem autorização."],
  "Diga o preço em voz alta dez vezes, sem “mas”, sem “só” e sem pedir desculpas. Grave e ouça. Depois, conte até cinco em silêncio.",
  ["Disse o preço sem rodeio", "Fiz silêncio depois", "Fiz a conta com os números dele"]),
 ("objecoes", "Objeções: ouvir, confirmar, responder, checar", 9,
  "Responder às dúvidas sem discutir, com honestidade e curto.",
  ["Objeção não é ataque. É o cliente pedindo mais informação ou mostrando um medo. Se você trata como discussão, perde. Se trata como pergunta, avança.",
   "Um método simples, em quatro passos: Ouvir sem interromper. Confirmar o que entendeu (“Entendi: o que preocupa é o preço, certo?”). Responder curto e honesto. Checar (“Isso responde? Tem mais alguma coisa?”).",
   "Descubra se a objeção é real ou uma cortina de fumaça. Pergunte: “Além disso, há algo mais que te preocupa?”. Se o preço é a única, trate o preço. Se há outra, trate a outra primeiro.",
   "Quando a resposta honesta é “não”, diga “não”. “Garante resultado?” Não. “É exclusivo?” Não. “O sistema envia as mensagens?” Não. Essas respostas, ditas com calma, aumentam a confiança.",
   "As respostas completas para as 10 objeções mais comuns estão no kit, na seção 9."],
  ["Entendi: o que preocupa é o preço, certo? São 100 empresas com dono, contato e prova por menos de dez reais cada, e você testa 3 de graça antes.", "Isso responde? Tem mais alguma coisa que te preocupa?"],
  ["“Mas você não entendeu...”", "Prometer o que não prometemos para vencer a objeção."],
  "Faça um role-play (veja a seção Personas) com as cinco objeções: caro, já tenho lista, garante resultado, é exclusivo, preciso pensar. Responda em voz alta usando os quatro passos.",
  ["Ouvi até o fim", "Confirmei o que entendi", "Respondi curto e honesto", "Chequei se respondeu"]),
 ("fechamento", "Fechamento", 6,
  "Pedir a decisão e sair da call com um próximo passo e uma data.",
  ["Quem não pede a decisão não ouve “sim” nem “não”. Fechar não é pressionar: é perguntar com clareza qual é o próximo passo.",
   "O teste grátis ajuda: é um compromisso pequeno que deixa o cliente ver o produto com o caso dele. Combine a entrega (até 24 horas) e uma conversa curta depois, com data e hora.",
   "Se ele disser “vou pensar”, descubra o que ficou em aberto: preço, confiança no dado ou prioridade? Ofereça os 3 leads de teste para ele decidir olhando o produto. Se disser “não”, agradeça, deixe a porta aberta e registre o motivo."],
  ["Isso é o tipo de empresa que você quer ver na sua lista?", "Começamos pelo pacote de 100 hoje? Qual forma de pagamento é melhor para você?", "Combinado: eu te mando os 3 leads até [dia/hora]. Falamos [dia] para você me dizer o que achou?"],
  ["Terminar com “qualquer coisa me chama”.", "Pressionar com urgência inventada."],
  "Escreva três jeitos diferentes de pedir a decisão, com o seu estilo. Treine cada um em voz alta, até o fim da frase sem hesitar.",
  ["Pedi a decisão", "Saí com data marcada", "Registrei o motivo, se foi “não”"]),
 ("followup", "Follow-up e ritmo", 5,
  "Cumprir o que prometeu e manter a conversa viva sem ser inconveniente.",
  ["A venda se decide muitas vezes depois da call. O follow-up mostra se você faz o que diz.",
   "No mesmo dia, mande uma mensagem curta com o resumo e o que você prometeu. Se prometeu o teste em 24 horas, cumpra. Cada contato seguinte precisa trazer algo novo: uma resposta, um dado, uma data. Evite o “só passando para saber”.",
   "Sugestão de ritmo: até três tentativas respeitosas; se não houver resposta, avise que a porta está aberta e pare. Registre sempre a etapa, a data e o próximo passo. Se alguém pedir para parar, pare e avise o time."],
  ["Oi, [nome]! Obrigado pela conversa. Pelo que você me contou, o seu cliente ideal é [cliente ideal]. Vou montar os 3 leads para isso e te aviso quando estiverem prontos."],
  ["Mandar a mesma mensagem três vezes.", "Insistir depois de um pedido para parar."],
  "Escreva um follow-up para cada situação: depois da call, na entrega do teste, e quando o cliente sumiu. Cada um deve trazer algo novo.",
  ["Mandei a mensagem no mesmo dia", "Cumpri o prazo prometido", "Registrei etapa, data e próximo passo"]),
 ("etica", "Ética e limites", 6,
  "Saber o que nunca dizer e como tratar os dados com respeito.",
  ["Honestidade é a estratégia de venda que mais funciona a longo prazo. Também protege você e a empresa.",
   "Nunca prometa resultado, exclusividade, garantia ou reposição: não existem. Nunca diga que o sistema envia mensagens. Nunca invente depoimento, número ou cliente. Nunca diga que um contato tipo B ou C “é do dono”: use o tipo. Nunca dê desconto sem falar com o Dan.",
   "Os dados vêm do cadastro público de CNPJ. Quem pedir para sair deve ser respeitado: pare o contato e avise contact@minemylead.com. Ao abordar, apresente-se, diga de onde veio o contato e ofereça a opção de parar.",
   "Você não dá aconselhamento jurídico. Para dúvidas sobre LGPD ou abordagem comercial, indique um advogado."],
  ["Se vender para pessoa física, não é o nosso produto, e prefiro dizer agora.", "Posso te mandar o contato do nosso e-mail para pedir remoção, se quiser."],
  ["“Garantido”, “resultado certo”, “exclusivo”, “automático”, “o melhor do mercado”."],
  "Pegue um anúncio de qualquer concorrente e marque o que a gente não poderia prometer. Reescreva uma frase dele de um jeito que possamos cumprir.",
  ["Não prometi nada que não cumprimos", "Apresentei-me e disse de onde veio o contato", "Ofereci a opção de parar"]),
 ("canais", "WhatsApp, telefone e e-mail", 5,
  "Escrever e falar curto, no canal certo, de um jeito fácil de responder.",
  ["Cada canal tem sua regra, mas todos pedem a mesma coisa: ser curto e facilitar a resposta.",
   "WhatsApp: uma ideia, uma pergunta, horário comercial, sem blocos de texto. Telefone: primeiro diga quem é, por que está ligando e peça 30 segundos. E-mail: assunto específico, cinco linhas e uma única chamada para ação.",
   "Em todos os canais: identifique-se, diga de onde veio o contato e ofereça parar. Isso aumenta as respostas e protege a todos."],
  ["Oi, [nome]! Aqui é [seu nome], da MineMyLead. Vi seu pedido de piloto. Posso te ligar [dia, hora] por 30 minutos?", "Assunto: Seus 3 leads de teste, [empresa]"],
  ["Mensagens longas com várias perguntas.", "Ligar sem se apresentar nem dizer o motivo."],
  "Escreva a mesma mensagem de convite para os três canais, respeitando a regra de cada um. Peça a um colega para ler e dizer o que respondeu.",
  ["Mensagem curta e com uma pergunta", "Identifiquei-me e disse de onde veio o contato"]),
]

# personas para role-play (fictícias)
P = [
 ("Marina", "Agência de marketing digital · Porto Alegre", "Desconfiada. Já comprou lista e se frustrou.", "“Já tenho lista.”", "Descobrir o que falhou na lista anterior e mostrar a diferença: dono, origem do contato e prova.", "Falar mal da lista dela. Ela se defende."),
 ("Carlos", "Software de gestão para pequenas empresas · Belo Horizonte", "Sensível a preço. Conta cada real.", "“É caro.”", "Fazer a conta com os números dele e levar ao teste grátis.", "Dar desconto. O preço é R$ 990."),
 ("Dra. Paula", "Escritório de contabilidade · Campinas", "Cautelosa. Gosta de pensar muito.", "“Preciso pensar.”", "Descobrir o que está em aberto e marcar uma data para falar depois do teste.", "Pressionar com urgência inventada."),
 ("Rafael", "Distribuidora de embalagens · Joinville", "Direto e impaciente. Quer números.", "“Você garante resultado?”", "Responder “não” com calma e transformar em “você mede no aplicativo”.", "Prometer resposta ou venda para agradar."),
 ("Juliana", "Cursos de culinária para pessoas · Salvador", "Simpática e curiosa. Vende para pessoa física.", "“Funciona para o meu ramo?”", "Dizer, com franqueza e gentileza, que o produto ainda não serve para ela.", "Vender mesmo assim."),
 ("Sérgio", "Consultoria de RH · Recife", "Cuidadoso com dados e regras.", "“De onde vêm os dados? Posso usar?”", "Explicar a origem (cadastro público de CNPJ), a opção de sair e indicar um advogado nas dúvidas jurídicas.", "Dar parecer jurídico ou dizer “pode tudo”."),
]

# quiz
Q = [
 ("Na descoberta, quanto do tempo o cliente deve falar?", ["Cerca de 30%", "Cerca de 50%", "Cerca de 70%", "Quanto menos, melhor"], 2, "A meta é o cliente falar cerca de 70%. Você fala 30% e faz as perguntas."),
 ("O cliente diz “é caro”. O que você faz primeiro?", ["Dá desconto", "Ouve, confirma o que entendeu e responde curto", "Explica todas as funções do aplicativo", "Diz que ele não entendeu o valor"], 1, "Ouvir, confirmar, responder e checar. Desconto só com o Dan."),
 ("Qual destas frases você pode dizer?", ["“Você vai fechar muito com isso.”", "“Os contatos são exclusivos seus.”", "“Entregamos um ponto de partida de verdade, e você mede o que acontece.”", "“O sistema dispara as mensagens por você.”"], 2, "Não prometemos resultado nem exclusividade, e o sistema não envia mensagens."),
 ("O contato de uma empresa é do tipo B. Como você descreve?", ["“É o celular do dono.”", "“Chega à empresa: e-mail de função ou telefone fixo.”", "“É um contato garantido.”", "“É compartilhado por várias empresas.”"], 1, "B chega à empresa. Só o tipo S é o dono direto, e o C é compartilhado."),
 ("Depois de dizer o preço, o melhor é:", ["Justificar rapidamente", "Pedir desculpas", "Fazer silêncio e deixar o cliente responder", "Dar um desconto antes que ele peça"], 2, "O silêncio dá espaço ao cliente. Quem fala primeiro costuma ceder."),
 ("O cliente vende cursos para pessoas físicas. O que fazer?", ["Vender o pacote assim mesmo", "Dizer com franqueza que o produto ainda não serve para ele", "Oferecer desconto", "Prometer que vai funcionar"], 1, "O pacote é de empresas que vendem para empresas. Dizer a verdade protege a confiança."),
 ("Qual pergunta é de implicação (SPIN)?", ["“O que você vende?”", "“É fácil chegar no dono?”", "“Quanto tempo isso toma por semana? O que você deixa de fazer?”", "“Se tivesse 100 empresas certas, o que mudaria?”"], 2, "Implicação faz o cliente sentir o custo do problema: tempo, dinheiro, oportunidade."),
 ("Ao final da call, o ideal é:", ["Dizer “qualquer coisa me chama”", "Sair com próximo passo e data marcada", "Mandar o preço por mensagem depois", "Esperar o cliente ligar"], 1, "Quem pede a decisão e marca a data mantém a venda andando."),
 ("O cliente pede para parar de receber contato. Você:", ["Insiste mais uma vez", "Para e avisa o time (contact@minemylead.com)", "Troca de canal", "Ignora, pois o dado é público"], 1, "Quem pede para sair deve ser respeitado e bloqueado nos próximos pacotes."),
 ("O que o teste grátis entrega?", ["O pacote de 100 com desconto", "3 leads escolhidos para o que ele vende, por e-mail, em até 24 horas", "Um acesso de 7 dias ao sistema", "Uma garantia de resultado"], 1, "São 3 leads, preparados à mão pelo time, enviados em até 24 horas."),
]

# autoavaliação (0-2)
R = ["Preparei a call (site, hipótese, perguntas)", "Abri com calma e combinei a pauta", "Fiz perguntas abertas na descoberta", "Falei cerca de 30% e ouvi cerca de 70%", "Parafraseei o que ouvi", "Mostrei só o que importava para ele", "Disse o preço com clareza e fiz silêncio", "Tratei as objeções sem discutir", "Não prometi nada que não cumprimos", "Pedi a decisão e saí com data marcada"]

PLAN = [
 ("Dia 1", "Veja as 4 aulas em vídeo (4 minutos) e leia as seções 1 a 3 do kit."),
 ("Dia 2", "Leia o kit: preço, comparativo e a call. Faça as lições 1 e 2 desta página."),
 ("Dia 3", "Lições 3 e 4. Grave sua abertura (30 s) e reescreva 5 perguntas fechadas como abertas."),
 ("Dia 4", "Lições 5 e 6. Treine a parafrasear em conversas do dia a dia."),
 ("Dia 5", "Lição 7. Diga o preço 10 vezes em voz alta. Grave e ouça."),
 ("Dia 6", "Lição 8. Leia as 10 respostas do kit e reescreva 3 com suas palavras."),
 ("Dia 7", "Descanso. Releia as frases de marca e os “nunca dizer”."),
 ("Dia 8", "Lições 9 a 12. Escreva follow-ups e mensagens para os 3 canais."),
 ("Dia 9", "Faça o quiz. Revise as respostas erradas."),
 ("Dia 10", "Role-play 1 com a Marina (já tenho lista) e role-play 2 com o Carlos (é caro)."),
 ("Dia 11", "Role-play 3 com a Dra. Paula e 4 com o Rafael."),
 ("Dia 12", "Role-play 5 com a Juliana (dizer “não serve”) e 6 com o Sérgio (dados)."),
 ("Dia 13", "Call completa de 30 minutos com um colega observando. Ele preenche a ficha de autoavaliação."),
 ("Dia 14", "Reveja a ficha, escolha uma habilidade para melhorar e marque sua primeira call de verdade."),
]

def li(x): return "".join(f"<li>{E(i)}</li>" for i in x)

lessons = ""
for n, (id_, t, mins, obj, idea, diga, evite, ex, chk) in enumerate(L, 1):
    lessons += f'''<article class="ls" id="{id_}" data-id="{id_}">
<header><span class="n">{n}</span><div><h3>{E(t)}</h3><span class="meta">{mins} min de leitura</span></div><label class="done"><input type="checkbox" data-done="{id_}"> <span>Concluída</span></label></header>
<p class="obj"><b>Objetivo:</b> {E(obj)}</p>
{"".join(f"<p>{E(p)}</p>" for p in idea)}
<div class="two"><div class="say"><b>Diga</b><ul>{li(diga)}</ul></div><div class="avoid"><b>Evite</b><ul>{li(evite)}</ul></div></div>
<div class="ex"><b>Exercício</b><p>{E(ex)}</p></div>
<ul class="chk">{"".join(f'<li><label><input type="checkbox"> {E(c)}</label></li>' for c in chk)}</ul>
</article>
'''

personas = ""
for nome, quem, perfil, obj, meta, arm in P:
    personas += f'''<article class="pp"><h3>{E(nome)}</h3><span class="who">{E(quem)}</span>
<p><b>Perfil:</b> {E(perfil)}</p><p><b>Objeção principal:</b> <span class="o">{E(obj)}</span></p><p><b>Seu objetivo:</b> {E(meta)}</p><p class="trap"><b>Armadilha:</b> {E(arm)}</p></article>
'''

quiz_json = json.dumps([{"q": q, "o": o, "a": a, "e": e} for q, o, a, e in Q], ensure_ascii=False)
rub = "".join(f'<tr><td>{E(c)}</td><td class="sc"><label><input type="radio" name="r{i}" value="0"> 0</label><label><input type="radio" name="r{i}" value="1"> 1</label><label><input type="radio" name="r{i}" value="2"> 2</label></td></tr>' for i, c in enumerate(R))
plan = "".join(f'<li><b>{d}</b><span>{E(t)}</span></li>' for d, t in PLAN)
toc = "".join(f'<a href="#{l[0]}"><span>{i}</span>{E(l[1])}</a>' for i, l in enumerate(L, 1))

page = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Habilidades de venda · MineMyLead</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700;800&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--navy:#0F1B2D;--navy2:#17283f;--y:#FFE14D;--paper:#F4F1EA;--ink:#1C1915;--mute:#5E584F;--line:#DAD6CC;--ok:#1d8a5a;--bad:#b3261e}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth;scroll-padding-top:64px}}
body{{margin:0;background:var(--paper);color:var(--ink);font:17px/1.65 "Instrument Sans",system-ui,sans-serif}}
h1,h2,h3{{font-family:"Bricolage Grotesque",sans-serif;letter-spacing:-.02em;line-height:1.12;margin:0}}
.top{{position:sticky;top:0;z-index:20;background:var(--navy);color:#fff;display:flex;gap:6px;align-items:center;padding:8px 16px;overflow-x:auto;white-space:nowrap;scrollbar-width:none}}
.top a{{color:#c9d1dd;text-decoration:none;font-size:14px;padding:6px 10px;border-radius:8px}}.top a:hover{{background:var(--navy2);color:#fff}}.top b{{font:800 18px "Bricolage Grotesque";margin-right:8px}}.top b i{{font-style:normal;color:var(--y)}}
.hero{{background:var(--navy);color:#fff;padding:56px 16px 48px}}.in,main{{max-width:900px;margin:0 auto}}
.tag{{display:inline-block;font:600 13px "Instrument Sans";letter-spacing:.08em;text-transform:uppercase;background:var(--y);color:var(--navy);padding:4px 12px;border-radius:99px;margin-bottom:16px}}
.hero h1{{font-size:clamp(34px,6vw,56px);font-weight:800}}.hero h1 mark{{background:none;color:var(--y)}}.hero p{{color:#c9d1dd;font-size:19px;max-width:36em;margin:16px 0 0}}
main{{padding:0 16px 80px}}section{{padding:52px 0 0}}
.k{{font:600 13px "Instrument Sans";letter-spacing:.08em;text-transform:uppercase;color:var(--mute);margin-bottom:8px;display:flex;gap:10px;align-items:center}}.k:before{{content:"";width:22px;height:4px;border-radius:2px;background:var(--y)}}
h2{{font-size:clamp(26px,4vw,36px);font-weight:800;margin-bottom:10px}}h3{{font-size:23px;font-weight:700}}
.lede{{color:var(--mute);margin:0 0 18px}}
.prog{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:-26px 0 0;position:relative;box-shadow:0 8px 24px rgba(15,27,45,.08)}}
.pb{{height:10px;border-radius:99px;background:#ece9df;overflow:hidden;margin-top:8px}}.pb i{{display:block;height:100%;width:0;background:var(--y);transition:width .3s}}
.toc{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:8px;margin-top:6px}}
.toc a{{color:var(--ink);display:flex;gap:12px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 14px;text-decoration:none;font-weight:600;font-size:16px}}
.toc a span{{width:30px;height:30px;border-radius:50%;background:var(--navy);color:var(--y);display:grid;place-items:center;font:800 15px "Bricolage Grotesque";flex:none}}.toc a:hover{{border-color:var(--navy)}}
.ls{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px 24px;margin:16px 0}}
.ls header{{display:flex;gap:14px;align-items:center;margin-bottom:12px}}.ls header>div{{flex:1}}
.n{{width:42px;height:42px;border-radius:50%;background:var(--navy);color:var(--y);display:grid;place-items:center;font:800 20px "Bricolage Grotesque";flex:none}}
.meta{{font-size:13px;color:var(--mute)}}
.done{{font-size:14px;font-weight:600;display:flex;gap:6px;align-items:center;cursor:pointer;background:#f4f2ee;border-radius:99px;padding:6px 12px}}.done input{{accent-color:var(--ok);width:18px;height:18px}}
.ls.is-done{{border-color:var(--ok)}}.ls.is-done .n{{background:var(--ok);color:#fff}}
.obj{{background:#fffbe0;border-left:5px solid var(--y);padding:10px 14px;border-radius:0 10px 10px 0}}
.ls p{{margin:10px 0}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}}@media(max-width:640px){{.two{{grid-template-columns:1fr}}}}
.say,.avoid{{border-radius:12px;padding:12px 16px;font-size:15.5px}}.say{{background:#e9f6ef;border-left:5px solid var(--ok)}}.avoid{{background:#fdeceb;border-left:5px solid var(--bad)}}
.say ul,.avoid ul{{margin:6px 0 0;padding-left:18px}}.say li,.avoid li{{margin:4px 0}}
.ex{{background:#eef3fa;border-left:5px solid #2a78d6;border-radius:0 12px 12px 0;padding:10px 16px}}.ex p{{margin:4px 0 0}}
.chk{{list-style:none;padding:0;margin:14px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:6px 14px;font-size:15px}}.chk input{{accent-color:var(--navy);width:17px;height:17px;vertical-align:-3px}}
.pg{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}}
.pp{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px}}.pp h3{{font-size:22px}}.who{{font-size:13px;color:var(--mute);display:block;margin-bottom:8px}}.pp p{{margin:6px 0;font-size:15.5px}}
.o{{background:var(--y);padding:1px 8px;border-radius:6px;font-weight:600}}.trap{{color:#8a2a24}}
.card{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px 22px}}
.btn{{background:var(--navy);color:var(--y);font:700 15px "Instrument Sans";padding:10px 18px;border-radius:10px;border:0;cursor:pointer;text-decoration:none;display:inline-block}}.btn.alt{{background:#ece9df;color:var(--navy)}}
.qq{{margin:18px 0}}.qq h4{{margin:0 0 8px;font:700 19px "Bricolage Grotesque"}}
.qo{{display:block;width:100%;text-align:left;background:#fff;border:2px solid var(--line);border-radius:12px;padding:10px 14px;margin:6px 0;font:inherit;cursor:pointer}}.qo:hover{{border-color:var(--navy)}}
.qo.ok{{background:#e9f6ef;border-color:var(--ok)}}.qo.no{{background:#fdeceb;border-color:var(--bad)}}.qo:disabled{{cursor:default}}
.qe{{font-size:15px;color:var(--mute);margin:4px 0 0;display:none}}.qe.show{{display:block}}
.score{{font:800 40px "Bricolage Grotesque";margin:12px 0}}
table{{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;font-size:15.5px}}td{{padding:10px 14px;border-bottom:1px solid var(--line)}}tr:last-child td{{border-bottom:0}}.sc{{white-space:nowrap;text-align:right}}.sc label{{margin-left:12px;cursor:pointer}}.sc input{{accent-color:var(--navy)}}
.plan{{list-style:none;padding:0;margin:0;display:grid;gap:8px}}.plan li{{display:flex;gap:14px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 14px}}.plan b{{min-width:60px;color:#8a6d00}}
footer{{background:var(--navy);color:#c9d1dd;padding:26px 16px;margin-top:60px;font-size:14px}}
@media print{{.top{{display:none}}.ls,.pp{{break-inside:avoid}}body{{background:#fff}}}}
</style></head><body>
<nav class="top"><b>Mine<i>My</i>Lead</b><a href="../">← Portal</a><a href="#licoes">Lições</a><a href="#personas">Personas</a><a href="#quiz">Quiz</a><a href="#ficha">Autoavaliação</a><a href="#plano">Plano de 14 dias</a></nav>
<header class="hero"><div class="in"><span class="tag">Curso de habilidades</span><h1>Aprenda a <mark>vender</mark> de verdade</h1><p>12 lições curtas, exercícios, personas para ensaiar, um quiz e uma ficha de autoavaliação. Tudo aplicado ao MineMyLead: o que dizer, o que evitar e como treinar.</p></div></header>
<main>
<div class="prog" id="prog"><b id="pt">Seu progresso: 0 de {len(L)} lições</b><div class="pb"><i id="pf"></i></div><span style="font-size:13px;color:var(--mute)">O progresso fica salvo neste navegador.</span></div>

<section id="como"><div class="k">Como usar</div><h2>Um jeito de estudar</h2>
<p class="lede">Cada lição leva de 5 a 9 minutos. Leia, faça o exercício em voz alta e marque como concluída. A ordem segue uma call real: preparar, abrir, descobrir, ouvir, mostrar, falar de preço, tratar objeções, fechar e acompanhar.</p>
<div class="toc">{toc}</div></section>

<section id="licoes"><div class="k">Lições</div><h2>12 habilidades</h2>
{lessons}</section>

<section id="personas"><div class="k">Treino</div><h2>Personas para ensaiar</h2>
<p class="lede">Clientes fictícios para role-play. Peça a um colega para interpretar a persona e dar a objeção principal, sem facilitar. Você tem 10 minutos por persona. O objetivo e a armadilha mostram o que observar.</p>
<div class="pg">{personas}</div></section>

<section id="quiz"><div class="k">Teste</div><h2>Quiz: 10 perguntas</h2>
<p class="lede">Escolha a melhor resposta. A explicação aparece logo depois.</p>
<div class="card" id="quizbox"></div></section>

<section id="ficha"><div class="k">Avaliação</div><h2>Ficha de autoavaliação da call</h2>
<p class="lede">Preencha depois de cada call, ou peça a um colega que observe. Dê 0 (não fiz), 1 (fiz em parte) ou 2 (fiz bem). Imprima com Ctrl+P.</p>
<table>{rub}</table>
<p><b>Total: <span id="rt">0</span> de {len(R)*2}</b> · <span id="rm">Preencha os critérios.</span></p></section>

<section id="plano"><div class="k">Plano</div><h2>14 dias para a primeira call</h2>
<p class="lede">Uma sugestão de rotina: de 30 a 45 minutos por dia.</p>
<ol class="plan">{plan}</ol></section>
</main>
<footer><div class="in" style="max-width:900px;margin:0 auto"><b>MineMyLead</b> · Habilidades de venda · material interno do time. Os conceitos gerais (SPIN, escuta ativa, tratamento de objeções) são práticas de vendas conhecidas, adaptadas ao nosso produto. Para dúvidas jurídicas, consulte um advogado.</div></footer>
<script>
var Q={quiz_json};
function ls(k,v){{try{{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}}catch(e){{return null}}}}
/* progresso das lições */
var boxes=[].slice.call(document.querySelectorAll('[data-done]'));
function upd(){{var n=0;boxes.forEach(function(b){{var a=b.closest('.ls');a.classList.toggle('is-done',b.checked);if(b.checked)n++}});document.getElementById('pt').textContent='Seu progresso: '+n+' de '+boxes.length+' lições';document.getElementById('pf').style.width=(n/boxes.length*100)+'%'}}
boxes.forEach(function(b){{b.checked=ls('mml-done-'+b.dataset.done)==='1';b.addEventListener('change',function(){{ls('mml-done-'+b.dataset.done,b.checked?'1':'0');upd()}})}});upd();
/* quiz */
var qb=document.getElementById('quizbox'),hit=0,ans=0;
Q.forEach(function(q,i){{var d=document.createElement('div');d.className='qq';var h=document.createElement('h4');h.textContent=(i+1)+'. '+q.q;d.appendChild(h);var ex=document.createElement('p');ex.className='qe';ex.textContent=q.e;
 var ord=q.o.map(function(_,k){{return k}}).sort(function(){{return Math.random()-.5}});ord.forEach(function(j){{var t=q.o[j];var b=document.createElement('button');b.className='qo';b.textContent=t;b.dataset.j=j;b.onclick=function(){{if(d.dataset.a)return;d.dataset.a=1;ans++;var bs=d.querySelectorAll('.qo');bs.forEach(function(x){{x.disabled=true;if(+x.dataset.j===q.a)x.classList.add('ok')}});if(j===q.a){{hit++}}else{{b.classList.add('no')}}ex.classList.add('show');if(ans===Q.length)fin()}};d.appendChild(b)}});d.appendChild(ex);qb.appendChild(d)}});
var rs=document.createElement('div');rs.id='qr';qb.appendChild(rs);
function fin(){{var p=hit/Q.length;rs.innerHTML='<div class="score">'+hit+' de '+Q.length+'</div><p>'+(p>=.9?'Excelente. Você está pronto para os role-plays.':p>=.7?'Bom. Revise as lições das respostas erradas e tente de novo.':'Releia as lições e o kit, e tente de novo.')+'</p>';var b=document.createElement('button');b.className='btn';b.textContent='Refazer o quiz';b.onclick=function(){{location.hash='#quiz';location.reload()}};rs.appendChild(b);ls('mml-quiz',hit+'/'+Q.length)}}
/* ficha */
var rads=[].slice.call(document.querySelectorAll('input[type=radio]'));
function rsum(){{var t=0,c=0;var names={{}};rads.forEach(function(r){{if(r.checked){{t+=+r.value;names[r.name]=1}}}});c=Object.keys(names).length;document.getElementById('rt').textContent=t;document.getElementById('rm').textContent=c<{len(R)}?'Preencha os '+({len(R)}-c)+' critérios que faltam.':(t>={len(R)*2*0.85:.0f}?'Call muito bem conduzida.':t>={len(R)*2*0.6:.0f}?'Boa base. Escolha uma habilidade para melhorar.':'Revise as lições com nota 0 e repita o role-play.')}}
rads.forEach(function(r){{r.addEventListener('change',rsum)}});
</script></body></html>'''
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)
print(len(page))
