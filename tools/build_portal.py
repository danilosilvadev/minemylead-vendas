import json, html
S = json.load(open('/home/danj-12vram/dev/MineMyLead-app/docs/sales-kit/video-scripts.json', encoding='utf-8'))
cap = open('/home/danj-12vram/dev/minemylead-vendas/assets/imagens/carrossel/legenda-instagram.txt', encoding='utf-8').read().strip()
E = html.escape

aulas = [
    ("1-o-que-vendemos", "O que vendemos", "O produto, o preço e o que não prometemos.", "0:54"),
    ("2-como-conduzir-a-call", "Como conduzir a call", "As cinco partes da reunião e as perguntas de descoberta.", "0:56"),
    ("3-comparar-e-justificar-o-preco", "Comparar e justificar o preço", "Fazer na mão, anúncio, lista, contratar alguém: e a conta por empresa.", "0:46"),
    ("4-objecoes-e-fechamento", "Objeções e fechamento", "As cinco objeções de quase toda call e como pedir a decisão.", "0:56"),
]
aulas_html = ""
for i, (f, t, d, dur) in enumerate(aulas, 1):
    lines = "".join(f"<li>{E(x)}</li>" for x in S[str(i)])
    aulas_html += f'''<article class="vc" id="aula-{i}">
<video controls preload="none" playsinline poster="assets/posters/aula-{i}.jpg" src="assets/videos/aulas/{f}.mp4"></video>
<div class="vb"><span class="num">Aula {i}</span><h3>{t}</h3><p>{d}</p>
<div class="row"><a class="btn sm" href="assets/videos/aulas/{f}.mp4" download>Baixar vídeo · {dur}</a></div>
<details><summary>Ler o texto da aula</summary><ol class="tx">{lines}</ol></details></div></article>
'''

mk = [
    ("video-venda", "Vídeo de venda", "O gancho, o problema e a entrega: a voz explica por que vender para empresas começa por achar a empresa certa. Sem sistema e sem personagens.", "0:54", "vertical"),
    ("video-sistema", "O sistema na tela", "O produto mostrado por dentro, com o app refeito em animação: lista, mapa, prova e o sinal \"precisa do que você vende\".", "0:40", "vertical"),
    ("video-personagens", "O filme dos personagens", "A história da rua dos números: um mineiro, o Lead e o Número explicam o que a MineMyLead faz.", "1:00", "vertical"),
]
mk_html = ""
for f, t, d, dur, _ in mk:
    mk_html += f'''<article class="vc v9">
<video controls preload="none" playsinline poster="assets/posters/{f}.jpg" src="assets/videos/marketing/{f}.mp4"></video>
<div class="vb"><span class="num">9:16 · {dur}</span><h3>{t}</h3><p>{d}</p>
<div class="row"><a class="btn sm" href="assets/videos/marketing/{f}.mp4" download>Baixar vídeo</a></div></div></article>
'''
app_html = '''<article class="vc wide">
<video controls preload="none" playsinline poster="assets/posters/app-desktop.jpg" src="assets/videos/marketing/app-desktop.mp4"></video>
<div class="vb"><span class="num">Computador · 0:28</span><h3>O app no computador</h3><p>Boas-vindas, lista, empresa aberta com a prova, mapa e resultados. Bom para mostrar numa call.</p>
<div class="row"><a class="btn sm" href="assets/videos/marketing/app-desktop.mp4" download>Baixar vídeo</a></div></div></article>
<article class="vc v9 small">
<video controls preload="none" playsinline poster="assets/posters/app-celular.jpg" src="assets/videos/marketing/app-celular.mp4"></video>
<div class="vb"><span class="num">Celular · 0:28</span><h3>O app no celular</h3><p>A mesma animação, na versão do celular.</p>
<div class="row"><a class="btn sm" href="assets/videos/marketing/app-celular.mp4" download>Baixar vídeo</a></div></div></article>
'''

slides = ["Capa: a promessa", "O trabalho que ninguém vê", "O que vem em cada empresa", "A prova, não o palpite", "Nossa missão", "Teste grátis e preço"]
sl_html = "".join(
    f'<figure><a href="assets/imagens/carrossel/slide-{i}.png" target="_blank" rel="noopener"><img src="assets/imagens/carrossel/slide-{i}.png" alt="Slide {i} do carrossel"></a>'
    f'<figcaption><b>Slide {i}</b><a class="btn sm" href="assets/imagens/carrossel/slide-{i}.png" download>Baixar</a></figcaption></figure>'
    for i in range(1, 7))

logos = [
    ("logo-foto-de-perfil-instagram.png", "Foto de perfil", "Instagram, WhatsApp, LinkedIn", "lt"),
    ("logo-horizontal-claro.png", "Horizontal, fundo claro", "Assinatura de e-mail, propostas", "lt"),
    ("logo-horizontal-escuro.png", "Horizontal, fundo escuro", "Slides e vídeos escuros", "dk"),
    ("logo-mascote-fundo-transparente.png", "Mascote, fundo transparente", "PNG para usar sobre qualquer cor clara", "ck"),
    ("logo-mascote-para-fundo-escuro.png", "Mascote para fundo escuro", "PNG para fundos escuros", "dk"),
    ("logo-mascote.svg", "Mascote em SVG", "Vetor: aumenta sem perder qualidade", "lt"),
    ("logo-mascote-escuro.svg", "Mascote em SVG, versão escura", "Vetor para fundos escuros", "dk"),
    ("icone-app.svg", "Ícone do app", "Quadrado, como aparece no computador", "lt"),
]
lg_html = "".join(
    f'<figure class="lg"><div class="lgi {c}"><img src="assets/imagens/logos/{f}" alt="{E(t)}"></div>'
    f'<figcaption><b>{t}</b><span>{d}</span><a class="btn sm" href="assets/imagens/logos/{f}" download>Baixar</a></figcaption></figure>'
    for f, t, d, c in logos)

frases = [
    "Quem já precisa de você. O pacote é seu.",
    "100 empresas. Dono, contato e prova.",
    "Menos garimpo, mais conversa.",
    "Listas dizem quem. Nós mostramos por que vale abordar.",
    "Veja antes de comprar: 3 leads grátis.",
    "Um ponto de partida de verdade.",
]
fr_html = "".join(f'<div class="cp"><p>{E(x)}</p><button class="btn sm" data-copy>Copiar</button></div>' for x in frases)

msgs = [
    ("Convite para a call", "Oi, [nome]! Aqui é [seu nome], da MineMyLead. Vi o seu pedido do teste grátis. Podemos conversar uns 30 minutos [dia] às [hora]? Eu quero entender como você vende hoje, te mostrar o produto e combinar o próximo passo. Se preferir outro horário, me diga."),
    ("Depois da call, no mesmo dia", "Oi, [nome]! Obrigado pela conversa de hoje. Pelo que você me contou, o seu cliente ideal é [cliente ideal]. Vou montar os 3 leads de teste para isso e te aviso quando estiverem prontos. Combinamos de falar de novo [dia]. Qualquer dúvida, é só chamar."),
    ("Entrega do teste", "Oi, [nome]! Os 3 leads de teste estão prontos. Cada empresa vem com o dono, o melhor contato direto e a prova tirada do site dela. Dá uma olhada e me diz o que achou. Se fizer sentido, o pacote de 100 empresas custa R$ 990, pagamento único."),
    ("Se ele ainda está pensando", "Oi, [nome]! Passando para saber se você viu os 3 leads de teste. Se algo não fez sentido para o seu cliente ideal, me conta: posso ajustar o perfil. Sem pressa, e sem compromisso."),
]
ms_html = "".join(
    f'<div class="cp"><div><b>{t}</b><p>{E(x)}</p></div><button class="btn sm" data-copy>Copiar</button></div>' for t, x in msgs)


infos = [("1-a-call-de-30-minutos","A call de 30 minutos"),("2-contra-o-jeito-de-hoje","Contra o jeito de hoje"),("3-a-conta-por-empresa","A conta por empresa"),("4-o-que-vem-em-cada-empresa","O que vem em cada empresa"),("5-tipos-de-contato","Tipos de contato"),("6-o-caminho-do-cliente","O caminho do cliente"),("7-cinco-objecoes","5 objeções, 5 respostas"),("8-diga-e-nao-diga","Diga e nunca diga"),("9-perguntas-de-descoberta","Perguntas de descoberta")]
inf_html = "".join(
    f'<figure><a href="assets/infograficos/{f}.png" target="_blank" rel="noopener"><img src="assets/infograficos/{f}.png" alt="{E(t)}"></a>'
    f'<figcaption><b>{E(t)}</b><a class="btn sm" href="assets/infograficos/{f}.png" download>Baixar</a></figcaption></figure>' for f, t in infos)
skills = ["Vender é ajudar a decidir","Prepare-se em 10 minutos","Abertura e rapport","Descoberta: perguntas que abrem","Escute mais do que fala","Demonstre o que importa para ele","Preço e valor","Objeções: ouvir, confirmar, responder, checar","Fechamento","Follow-up e ritmo","Ética e limites","WhatsApp, telefone e e-mail"]
sk_html = "".join(f'<li><a href="habilidades/#{i}"><span>{n}</span>{E(t)}</a></li>' for n,(i,t) in enumerate(zip(["mentalidade","preparacao","abertura","descoberta","escuta","demonstracao","preco","objecoes","fechamento","followup","etica","canais"], skills),1))

page = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="#0F1B2D">
<title>Portal do vendedor · MineMyLead</title>
<meta name="description" content="Aulas, kit do vendedor, vídeos de marketing, imagens e textos prontos para vender o MineMyLead.">
<link rel="icon" href="assets/imagens/logos/icone-app.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700;800&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--navy:#0F1B2D;--navy2:#17283f;--yellow:#FFE14D;--paper:#F4F1EA;--ink:#1C1915;--mute:#5E584F;--line:#DAD6CC;--card:#fff;--ok:#1d8a5a}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth;scroll-padding-top:64px}}
body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 "Instrument Sans",system-ui,sans-serif}}
h1,h2,h3{{font-family:"Bricolage Grotesque",sans-serif;letter-spacing:-.02em;line-height:1.12;margin:0}}
a{{color:inherit}}
.top{{position:sticky;top:0;z-index:20;background:var(--navy);color:#fff;display:flex;gap:6px;align-items:center;padding:8px 16px;overflow-x:auto;white-space:nowrap;scrollbar-width:none}}
.top::-webkit-scrollbar{{display:none}}
.top .lg0{{display:flex;align-items:center;gap:8px;font:800 18px "Bricolage Grotesque",sans-serif;text-decoration:none;margin-right:10px}}
.top .lg0 img{{width:26px;height:26px}}.top .lg0 i{{color:var(--yellow);font-style:normal}}
.top a.n{{color:#c9d1dd;text-decoration:none;font-size:14px;padding:6px 10px;border-radius:8px}}.top a.n:hover{{background:var(--navy2);color:#fff}}
.hero{{background:var(--navy);color:#fff;padding:60px 16px 56px;position:relative;overflow:hidden}}
.hero .in,main{{max-width:1040px;margin:0 auto}}
.hero .tag{{display:inline-block;font:600 13px "Instrument Sans";letter-spacing:.08em;text-transform:uppercase;background:var(--yellow);color:var(--navy);padding:4px 12px;border-radius:99px;margin-bottom:18px}}
.hero h1{{font-size:clamp(34px,6.4vw,62px);font-weight:800;max-width:15em}}.hero h1 mark{{background:none;color:var(--yellow)}}
.hero p{{color:#c9d1dd;font-size:19px;max-width:36em;margin:18px 0 26px}}
.hero .mascot{{position:absolute;right:max(16px,calc(50% - 520px));top:36px;width:150px;opacity:.95}}
@media(max-width:760px){{.hero .mascot{{display:none}}}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--yellow);color:var(--navy);font:700 16px "Instrument Sans",sans-serif;padding:12px 20px;border-radius:12px;text-decoration:none;border:0;cursor:pointer}}
.btn:hover{{filter:brightness(.95)}}.btn.ghost{{background:transparent;color:#fff;box-shadow:inset 0 0 0 2px #3a4c66}}
.btn.sm{{font-size:14px;padding:8px 14px;border-radius:9px;background:var(--navy);color:var(--yellow)}}
.btn.sm.done{{background:var(--ok);color:#fff}}
.cta{{display:flex;flex-wrap:wrap;gap:10px}}
main{{padding:0 16px 80px}}
section{{padding:60px 0 0}}
.k{{font:600 13px "Instrument Sans";letter-spacing:.08em;text-transform:uppercase;color:var(--mute);margin-bottom:10px;display:flex;gap:10px;align-items:center}}
.k:before{{content:"";width:22px;height:4px;border-radius:2px;background:var(--yellow)}}
h2{{font-size:clamp(26px,4vw,38px);font-weight:800;margin-bottom:10px}}
.lede{{color:var(--mute);max-width:40em;margin:0 0 22px}}
.steps{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:-26px;position:relative}}
.step{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 18px 18px 64px;position:relative;box-shadow:0 8px 24px rgba(15,27,45,.08)}}
.step b{{position:absolute;left:16px;top:16px;width:36px;height:36px;border-radius:50%;background:var(--navy);color:var(--yellow);font:800 18px "Bricolage Grotesque";display:grid;place-items:center}}
.step h3{{font-size:18px;margin-bottom:4px}}.step p{{margin:0;color:var(--mute);font-size:15px}}
.grid3{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 22px}}
.card h3{{font-size:19px;margin-bottom:6px}}.card p{{margin:0 0 14px;color:var(--mute)}}
.card .row{{display:flex;gap:8px;flex-wrap:wrap}}
.big{{font:800 44px "Bricolage Grotesque";letter-spacing:-.03em;display:block;line-height:1}}
.facts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:16px}}
.facts .card{{background:var(--navy);color:#fff;border:0}}.facts .card p{{color:#c9d1dd;margin:6px 0 0}}.facts .big{{color:var(--yellow)}}
.vgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;align-items:start}}
.vgrid.v9s{{grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}}
.vc{{background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;display:flex;flex-direction:column}}
.vc video{{width:100%;display:block;background:#000;aspect-ratio:16/9;object-fit:contain}}
.vc.v9 video{{aspect-ratio:9/16;max-height:70vh}}
.vc.small video{{aspect-ratio:9/16;max-height:520px}}
.vb{{padding:16px 18px 18px}}.vb h3{{font-size:20px;margin:2px 0 6px}}.vb p{{margin:0 0 12px;color:var(--mute);font-size:15px}}
.num{{font:600 12px "Instrument Sans";letter-spacing:.08em;text-transform:uppercase;color:#8a6d00;background:#fff4c2;border-radius:99px;padding:3px 10px;display:inline-block}}
.row{{display:flex;gap:8px;flex-wrap:wrap}}
details{{margin-top:12px;border-top:1px solid var(--line);padding-top:10px}}summary{{cursor:pointer;font-weight:600;font-size:15px}}
.tx{{margin:10px 0 0;padding-left:20px;font-size:15px;color:#3a352d}}.tx li{{margin:6px 0}}
.sub{{font:700 20px "Bricolage Grotesque";margin:34px 0 12px}}
.car{{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px}}
.car figure,.logos figure{{margin:0;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden}}
.car img{{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;background:#ddd}}
.car figcaption{{display:flex;justify-content:space-between;align-items:center;padding:8px 10px;font-size:14px;gap:6px}}
.logos{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}}
.lgi{{height:150px;overflow:hidden;padding:16px}}.lgi img{{display:block;width:100%;height:118px;object-fit:contain}}
.lgi.lt{{background:#fff}}.lgi.dk{{background:var(--navy)}}
.lgi.ck{{background:conic-gradient(#e7e4dc 25%,#fff 0 50%,#e7e4dc 0 75%,#fff 0) 0 0/20px 20px}}
.lg figcaption{{display:flex;flex-direction:column;gap:4px;padding:10px 12px 12px;font-size:14px;align-items:flex-start}}.lg figcaption span{{color:var(--mute);font-size:13px}}.lg figcaption .btn{{margin-top:6px}}
.cp{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;display:flex;gap:14px;justify-content:space-between;align-items:flex-start;margin-bottom:10px}}
.cp p{{margin:4px 0 0;white-space:pre-line}}.cp > p{{margin:0;font-size:18px;font-family:"Bricolage Grotesque",sans-serif;font-weight:700}}
.cp .btn{{flex:none}}
.fr{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:0 12px}}
.capbox{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px}}
.capbox pre{{margin:0 0 14px;white-space:pre-wrap;font:15px/1.6 "Instrument Sans",sans-serif}}
.note{{background:#fffbe0;border-left:5px solid var(--yellow);border-radius:0 12px 12px 0;padding:12px 18px;margin:16px 0;font-size:15px}}
.sk{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:8px}}.sk a{{display:flex;gap:12px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 14px;text-decoration:none;font-weight:600;font-size:16px}}.sk a span{{width:30px;height:30px;border-radius:50%;background:var(--navy);color:var(--yellow);display:grid;place-items:center;font:800 15px "Bricolage Grotesque";flex:none}}.sk a:hover{{border-color:var(--navy)}}
footer{{background:var(--navy);color:#c9d1dd;padding:28px 16px;margin-top:70px;font-size:14px}}footer .in{{max-width:1040px;margin:0 auto}}
</style>
</head>
<body>
<nav class="top" aria-label="Seções"><a class="lg0" href="./"><img src="assets/imagens/logos/icone-app.svg" alt=""><span>Mine<i>My</i>Lead</span></a>
<a class="n" href="#comecar">Começar</a><a class="n" href="#aulas">Aulas</a><a class="n" href="#habilidades">Habilidades</a><a class="n" href="#slides">Slides</a><a class="n" href="#infograficos">Infográficos</a><a class="n" href="#kit">Kit</a><a class="n" href="#marketing">Vídeos</a><a class="n" href="#imagens">Imagens</a><a class="n" href="#textos">Textos</a></nav>

<header class="hero"><div class="in">
<img class="mascot" src="assets/imagens/logos/logo-mascote-para-fundo-escuro.png" alt="">
<span class="tag">Portal do vendedor</span>
<h1>Tudo o que você precisa para <mark>vender</mark> o MineMyLead.</h1>
<p>Aulas em vídeo, curso de habilidades de venda, slides, infográficos, o kit completo, os vídeos de marketing, as imagens para postar e os textos prontos. Em um lugar só, e tudo pode ser baixado.</p>
<div class="cta"><a class="btn" href="#aulas">Começar pelas aulas</a><a class="btn ghost" href="kit/">Abrir o kit do vendedor</a><a class="btn ghost" href="#marketing">Vídeos e imagens</a></div>
</div></header>

<main>
<div class="steps" id="comecar">
<div class="step"><b>1</b><h3>Veja as 4 aulas</h3><p>Cerca de 4 minutos no total. Depois, faça o curso de habilidades de venda.</p></div>
<div class="step"><b>2</b><h3>Leia o kit e veja os slides</h3><p>Roteiro minuto a minuto, comparativos e o que nunca dizer, em página, PDF, slides e infográficos.</p></div>
<div class="step"><b>3</b><h3>Use os materiais</h3><p>Vídeos, imagens e textos prontos para mandar ou postar. Depois, faça a sua primeira call.</p></div>
</div>

<section id="resumo">
<div class="k">O produto em 30 segundos</div>
<h2>O que você vende</h2>
<p class="lede">Um pacote de 100 empresas brasileiras que vendem para outras empresas, cada uma com o dono, o melhor contato direto e o motivo de estar na lista, com a prova tirada do site dela.</p>
<div class="facts">
<div class="card"><span class="big">R$ 990</span><p>pagamento único, pelo pacote de 100. Sem mensalidade.</p></div>
<div class="card"><span class="big">3 leads</span><p>de teste, de graça, antes de pagar. A equipe monta à mão.</p></div>
<div class="card"><span class="big">&lt; R$ 10</span><p>por empresa, com dono, contato e prova.</p></div>
</div>
<div class="note"><b>Nunca prometa</b> resposta, venda ou resultado, nem exclusividade. A gente entrega um ponto de partida de verdade. O resto da conversa é do cliente. Veja a lista completa no <a href="kit/#nunca">kit</a>.</div>
</section>

<section id="aulas">
<div class="k">Curso</div>
<h2>4 aulas curtas</h2>
<p class="lede">Veja na ordem, antes da primeira call. Cada aula tem o texto falado, caso você prefira ler ou consultar depois.</p>
<div class="vgrid">
{aulas_html}</div>
</section>


<section id="habilidades">
<div class="k">Habilidades de venda</div>
<h2>Aprenda a vender de verdade</h2>
<p class="lede">Um curso de 12 lições curtas, aplicado ao nosso produto: o que dizer, o que evitar e um exercício por lição. Tem também 6 personas para ensaiar, um quiz de 10 perguntas, uma ficha de autoavaliação da call e um plano de 14 dias.</p>
<div class="row" style="margin-bottom:16px"><a class="btn" href="habilidades/">Abrir o curso</a><a class="btn sm" href="habilidades/#personas">Personas para role-play</a><a class="btn sm" href="habilidades/#quiz">Fazer o quiz</a><a class="btn sm" href="habilidades/#plano">Plano de 14 dias</a></div>
<ol class="sk">{sk_html}</ol>
</section>

<section id="slides">
<div class="k">Slides</div>
<h2>Duas apresentações prontas</h2>
<p class="lede">Abrem no navegador (setas, clique ou deslize; tecla F para tela cheia) e também em PDF. No celular, gire a tela.</p>
<div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr))">
<div class="card"><h3>Apresentação para o cliente</h3><p>12 slides para mostrar na call: o problema, o que ele recebe, uma empresa por dentro, a prova, os tipos de contato, o app, a comparação, o preço, o teste grátis e o que não prometemos.</p><div class="row"><a class="btn sm" href="slides/apresentacao-cliente/">Abrir os slides</a><a class="btn sm" href="assets/pdf/slides-apresentacao-cliente.pdf" download>Baixar PDF</a></div></div>
<div class="card"><h3>Treinamento do vendedor</h3><p>16 slides com as habilidades por trás de uma boa call: mentalidade, preparação, abertura, descoberta, escuta, demonstração, preço, objeções, fechamento, follow-up, ética e canais.</p><div class="row"><a class="btn sm" href="slides/treinamento-vendedor/">Abrir os slides</a><a class="btn sm" href="assets/pdf/slides-treinamento-vendedor.pdf" download>Baixar PDF</a></div></div>
</div>
</section>

<section id="infograficos">
<div class="k">Infográficos</div>
<h2>Para consultar e mandar</h2>
<p class="lede">Nove infográficos em imagem (1080 × 1350). Use como cola na hora da call, imprima ou mande no WhatsApp para o time.</p>
<div class="row" style="margin-bottom:16px"><a class="btn" href="assets/infograficos/todos-os-infograficos.zip" download>Baixar todos (.zip)</a></div>
<div class="car">{inf_html}</div>
</section>

<section id="kit">
<div class="k">Kit do vendedor</div>
<h2>O guia completo da venda</h2>
<p class="lede">Estrutura da venda, benefícios, comparativo com a concorrência, preço, roteiro da call minuto a minuto, objeções, frases e checklists.</p>
<div class="grid3">
<div class="card"><h3>Kit em página</h3><p>Abre bem no celular, com menu por seções. Bom para consultar durante a call.</p><div class="row"><a class="btn sm" href="kit/">Abrir o kit</a></div></div>
<div class="card"><h3>Kit em PDF</h3><p>21 páginas, para imprimir ou ler sem internet.</p><div class="row"><a class="btn sm" href="assets/pdf/kit-do-vendedor.pdf" download>Baixar o PDF</a><a class="btn sm" href="assets/pdf/kit-do-vendedor.pdf" target="_blank" rel="noopener">Abrir</a></div></div>
<div class="card"><h3>Atalhos do kit</h3><p>Direto ao que você precisa agora.</p><div class="row"><a class="btn sm" href="kit/#call">A call</a><a class="btn sm" href="kit/#objecoes">Objeções</a><a class="btn sm" href="kit/#comparativo">Comparativo</a><a class="btn sm" href="kit/#preco">Preço</a></div></div>
</div>
</section>

<section id="marketing">
<div class="k">Vídeos de marketing</div>
<h2>Vídeos para mandar e postar</h2>
<p class="lede">Os três vídeos de lançamento, em formato vertical (Instagram, Reels, WhatsApp), com a voz da marca. Toque para ver e baixe o arquivo.</p>
<div class="vgrid v9s">
{mk_html}</div>
<div class="sub">O app em animação</div>
<div class="vgrid" style="grid-template-columns:2fr 1fr">
{app_html}</div>
</section>

<section id="imagens">
<div class="k">Imagens</div>
<h2>Carrossel, logos e legenda</h2>
<p class="lede">O post de apresentação para o Instagram: 6 imagens (1080 × 1350, formato 4:5), na ordem, com a legenda pronta.</p>
<div class="row" style="margin-bottom:16px"><a class="btn" href="assets/imagens/todas-as-imagens.zip" download>Baixar tudo (carrossel + logos, .zip)</a></div>
<div class="car">{sl_html}</div>
<div class="sub">Legenda do post</div>
<div class="capbox"><pre id="cap">{E(cap)}</pre><div class="row"><button class="btn sm" data-copy-id="cap">Copiar a legenda</button><a class="btn sm" href="assets/imagens/carrossel/legenda-instagram.txt" download>Baixar .txt</a></div></div>
<div class="sub">Logos</div>
<div class="logos">{lg_html}</div>
</section>

<section id="textos">
<div class="k">Textos prontos</div>
<h2>Frases e mensagens</h2>
<p class="lede">Copie, troque o que está entre colchetes e envie. Escreva com as suas palavras sempre que puder.</p>
<div class="sub" style="margin-top:0">Frases da marca</div>
<div class="fr">{fr_html}</div>
<div class="sub">Mensagens para o dia a dia</div>
{ms_html}
<div class="note">Mande mensagem só para quem pediu o teste ou autorizou o contato. Se alguém pedir para parar, pare e avise o time: contact@minemylead.com.</div>
</section>
</main>

<footer><div class="in"><b>MineMyLead</b> · Portal do vendedor · atualizado em 06/11/2026 · Material interno do time de vendas. Não compartilhe com clientes.</div></footer>
<script>
function flash(b,t){{var o=b.textContent;b.textContent=t;b.classList.add('done');setTimeout(function(){{b.textContent=o;b.classList.remove('done')}},1600)}}
function copyText(t,b){{
  function ok(){{flash(b,'Copiado!')}}
  if(navigator.clipboard&&window.isSecureContext){{navigator.clipboard.writeText(t).then(ok,function(){{fb()}})}}else fb();
  function fb(){{var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity=0;document.body.appendChild(a);a.select();try{{document.execCommand('copy');ok()}}catch(e){{flash(b,'Copie manualmente')}};a.remove()}}
}}
document.querySelectorAll('[data-copy]').forEach(function(b){{b.addEventListener('click',function(){{var c=b.closest('.cp');var p=c.querySelector('p');copyText(p.textContent.trim(),b)}})}});
document.querySelectorAll('[data-copy-id]').forEach(function(b){{b.addEventListener('click',function(){{copyText(document.getElementById(b.dataset.copyId).textContent,b)}})}});
document.addEventListener('play',function(e){{document.querySelectorAll('video').forEach(function(v){{if(v!==e.target)v.pause()}})}},true);
</script>
</body>
</html>
'''
open('/home/danj-12vram/dev/minemylead-vendas/index.html', 'w', encoding='utf-8').write(page)
print(len(page))
