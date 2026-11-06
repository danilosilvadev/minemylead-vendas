"""Gera os infográficos (HTML 1080x1350). Renderize com tools/render.mjs -> assets/infograficos/*.png"""
import os, html
E = html.escape
OUT = os.path.join(os.path.dirname(__file__), "_info")
os.makedirs(OUT, exist_ok=True)

CSS = """
:root{--navy:#0F1B2D;--navy2:#17283f;--y:#FFE14D;--paper:#F4F1EA;--ink:#1C1915;--mute:#5E584F;--line:#DAD6CC}
*{box-sizing:border-box;margin:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{background:var(--paper);color:var(--ink);font:28px/1.4 "Instrument Sans",sans-serif;display:flex;flex-direction:column;padding:64px 64px 0}
h1,h2,h3,.f{font-family:"Bricolage Grotesque",sans-serif;letter-spacing:-.02em}
.top{display:flex;align-items:center;justify-content:space-between;margin-bottom:34px}
.brand{display:flex;align-items:center;gap:12px;font:800 30px "Bricolage Grotesque";color:var(--navy)}.brand i{font-style:normal;background:var(--y);padding:0 6px;border-radius:6px}
.brand svg{width:44px;height:44px}
.kick{font:600 22px "Instrument Sans";letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
h1{font-size:76px;line-height:1.02;font-weight:800;color:var(--navy);margin-bottom:14px}
h1 mark{background:none;color:#b58f00}
.sub{font-size:30px;color:var(--mute);margin-bottom:34px;max-width:900px}
.body{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.foot{margin:0 -64px;background:var(--navy);color:#c9d1dd;padding:22px 64px;display:flex;justify-content:space-between;font-size:22px;margin-top:20px}
.foot b{color:var(--y)}
.card{background:#fff;border:2px solid var(--line);border-radius:22px;padding:22px 26px}
.y{background:var(--y);border-color:var(--y);color:var(--navy)}
.n{background:var(--navy);border-color:var(--navy);color:#fff}
.badge{display:inline-grid;place-items:center;min-width:64px;height:64px;border-radius:50%;background:var(--navy);color:var(--y);font:800 32px "Bricolage Grotesque";flex:none}
.small{font-size:22px;color:var(--mute)}
.body.fill>.card{flex:1;align-items:center}.body.fill>.card.y,.body.fill>.card.n{flex:none}
"""

MARK = '<svg viewBox="0 0 64 64"><circle cx="32" cy="38" r="20" fill="#0F1B2D"/><path d="M12 36a20 20 0 0 1 40 0z" fill="#FFE14D"/><rect x="8" y="34" width="48" height="6" rx="3" fill="#FFE14D"/><circle cx="25" cy="44" r="3" fill="#fff"/><circle cx="39" cy="44" r="3" fill="#fff"/></svg>'

def page(slug, kick, title, sub, body, foot="minemylead.com", fill=False):
    h = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{slug}</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700;800&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="top"><div class="brand">{MARK}<span>Mine<i>My</i>Lead</span></div><div class="kick">{E(kick)}</div></div>
<h1>{title}</h1><p class="sub">{sub}</p>
<div class="body{" fill" if fill else ""}">{body}</div>
<div class="foot"><span>Portal do vendedor</span><b>{E(foot)}</b></div></body></html>"""
    open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8").write(h)

# 1 ---- a call de 30 minutos
parts = [("0–3", "Abertura", "Calma, combine a pauta e dê espaço para ele falar", 3),
         ("3–12", "Descoberta", "Você fala 30%, ele 70%. Perguntas abertas", 9),
         ("12–19", "Demonstração", "Mostre uma empresa: dono, contato e prova", 7),
         ("19–23", "Oferta do teste", "3 leads grátis, para o que ele vende", 4),
         ("23–28", "Preço e objeções", "R$ 990. Depois do preço, silêncio", 5),
         ("28–30", "Fechamento", "Decisão e próximo passo com data", 2)]
bar = "".join(f'<div style="flex:{m};background:{c};height:30px"></div>' for (_, _, _, m), c in zip(parts, ["#FFE14D", "#0F1B2D", "#FFE14D", "#0F1B2D", "#FFE14D", "#0F1B2D"]))
rows = "".join(f'<div class="card" style="display:flex;gap:22px;align-items:center;padding:18px 24px"><div class="f" style="font-size:34px;font-weight:800;min-width:150px;color:#b58f00">{a} min</div><div><div class="f" style="font-size:36px;font-weight:700;color:#0F1B2D">{b}</div><div class="small" style="font-size:25px">{c}</div></div></div>' for a, b, c, _ in parts)
page("1-a-call-de-30-minutos", "Estrutura da venda", "A call de <mark>30 minutos</mark>", "Seis partes. Quem descobre a dor vende melhor.",
     f'<div style="display:flex;border-radius:15px;overflow:hidden;margin-bottom:10px">{bar}</div>{rows}'
     '<div class="card y" style="font-size:27px;font-weight:600;text-align:center">Saia da call com uma data marcada para falar depois do teste.</div>', fill=True)

# 2 ---- comparativo
hdr = ["", "Dono", "Contato", "Prova", "Custo"]
data = [("Pesquisa manual", "Se você achar", "Você caça", "Você confere", "Seu tempo"),
        ("Anúncios pagos", "Não: alcança quem vê", "Não se aplica", "Não", "Todo mês"),
        ("Lista comprada", "Nem sempre", "Muitos sem origem", "Não", "Varia"),
        ("Contratar quem pesquise", "Depende", "Depende", "Depende", "Salário, todo mês"),
        ("MineMyLead", "Sócio do cadastro, com cargo", "Melhor contato, com tipo e origem", "Trecho do site da empresa", "R$ 990, uma vez")]
def cell(t, us, head=False):
    st = "background:#FFE14D;color:#0F1B2D;font-weight:700" if us else "background:#fff"
    if head: st = "background:#0F1B2D;color:#FFE14D;font:700 24px 'Instrument Sans'"
    return f'<div style="{st};padding:10px 14px;border-radius:12px;font-size:25px;line-height:1.25;display:flex;align-items:center">{E(t)}</div>'
g = "".join(cell(h, False, True) for h in hdr)
for r in data:
    us = r[0] == "MineMyLead"
    g += f'<div style="padding:16px 4px;font:700 24px \'Bricolage Grotesque\';display:flex;align-items:center;color:#0F1B2D">{E(r[0])}</div>' + "".join(cell(x, us) for x in r[1:])
page("2-contra-o-jeito-de-hoje", "Comparativo", "Contra o jeito <mark>de hoje</mark>", "O cliente sempre compara. Fale das alternativas com respeito.",
     f'<div style="display:grid;grid-template-columns:200px 1.1fr 1.1fr 1fr 1fr;grid-template-rows:64px repeat(5,minmax(0,1fr));gap:10px;flex:1;min-height:0">{g}</div>'
     '<p class="small" style="margin-top:16px">Descrições gerais por categoria; fornecedores variam. Antes de citar o preço de um concorrente, confira o site dele no dia.</p>')

# 3 ---- a conta
page("3-a-conta-por-empresa", "Preço e valor", "A conta é <mark>simples</mark>", "Cem empresas, um pagamento, menos de dez reais cada.",
     '<div style="display:flex;align-items:center;justify-content:center;gap:22px;margin:6px 0 10px"><div class="card n" style="text-align:center;padding:24px 28px"><div class="f" style="font-size:66px;white-space:nowrap;font-weight:800;color:#FFE14D;line-height:1">R$ 990</div><div class="small" style="color:#c9d1dd">pagamento único</div></div><div class="f" style="font-size:60px;font-weight:800">÷</div><div class="card" style="text-align:center;padding:24px 28px"><div class="f" style="font-size:78px;font-weight:800;line-height:1">100</div><div class="small">empresas</div></div><div class="f" style="font-size:60px;font-weight:800">=</div><div class="card y" style="text-align:center;padding:24px 28px"><div class="f" style="font-size:66px;white-space:nowrap;font-weight:800;line-height:1">R$ 9,90</div><div style="font-size:22px">por empresa</div></div></div>'
     '<div class="f" style="font-size:36px;font-weight:800;margin:14px 0 4px">Como justificar o valor</div>'
     '<div class="card" style="display:flex;gap:20px;align-items:center"><span class="badge">1</span><div><b>Tempo.</b> “Quanto tempo você leva para achar uma empresa, o dono e o contato?” Multiplique por 100 com ele.</div></div>'
     '<div class="card" style="display:flex;gap:20px;align-items:center"><span class="badge">2</span><div><b>Custo da hora.</b> “Quanto vale uma hora sua, ou de quem pesquisa para você?”</div></div>'
     '<div class="card" style="display:flex;gap:20px;align-items:center"><span class="badge">3</span><div><b>Risco baixo.</b> “Você testa 3 de graça antes. E paga uma vez só.”</div></div>'
     '<div class="card" style="background:#fffbe0;border-color:#FFE14D;font-size:23px">Exemplo para pensar junto: 10 minutos por empresa são cerca de 17 horas para 100. É um <b>exemplo</b>, não um dado nosso nem uma promessa de economia. Use os números do cliente.</div>')

# 4 ---- anatomia do lead
lead = [("Vende para empresas", "“Distribuidora de ferragens e fixadores para construtoras e lojas de materiais.” (trecho do site)"),
        ("Precisa do que você vende", "Atende construtoras: o público do seu perfil de compra."),
        ("Dono no cadastro", "Ricardo S. · Administrador · confiança 80%"),
        ("Contato S · WhatsApp", "(11) 9••••-••01 · celular de empresa com um sócio só · o mesmo contato aparece no site"),
        ("Contato B · e-mail", "e-mail de função: a caixa da empresa"),
        ("Cadastro", "CNPJ, ativa, aberta em 2005, porte micro")]
rr = "".join(f'<div style="flex:1;align-items:center;display:flex;gap:18px;padding:16px 22px;border-top:2px solid #DAD6CC"><div style="font-weight:700;min-width:260px;color:#0F1B2D">{a}</div><div style="color:#3a352d;font-size:27px">{E(b)}</div></div>' for a, b in lead)
page("4-o-que-vem-em-cada-empresa", "O produto por dentro", "O que vem em <mark>cada empresa</mark>", "Dono, contato, tipo, origem e prova. Tudo no mesmo lugar.",
     f'<div class="card" style="padding:0;overflow:hidden;flex:1;display:flex;flex-direction:column"><div style="background:#0F1B2D;color:#fff;padding:20px 24px;display:flex;justify-content:space-between;align-items:center"><span class="f" style="font-size:36px;font-weight:800">Ferragens Aurora</span><span style="color:#FFE14D;font-size:24px">Curitiba/PR · Atacado</span></div>{rr}</div>'
     '<p class="small" style="margin-top:10px">Exemplo fictício. O pacote de exemplo está em minemylead.com/pt/amostra/</p>')

# 5 ---- tipos de contato
tipos = [("S", "Dono direto", "Ex.: o celular do sócio único da empresa."),
         ("A", "Dono provável", "Há indício forte de que chega ao dono."),
         ("B", "Chega à empresa", "E-mail de função ou telefone fixo: a caixa da empresa."),
         ("C", "Compartilhado", "O mesmo contato aparece em várias empresas.")]
tt = "".join(f'<div class="card" style="display:flex;gap:26px;align-items:center;padding:24px 28px"><span class="badge" style="min-width:96px;height:96px;font-size:54px">{a}</span><div><div class="f" style="font-size:42px;font-weight:800;color:#0F1B2D">{b}</div><div style="font-size:26px;color:#3a352d">{c}</div></div></div>' for a, b, c in tipos)
page("5-tipos-de-contato", "Glossário", "Cada contato tem <mark>tipo e origem</mark>", "Assim o cliente sabe onde apostar primeiro.",
     tt + '<div class="card y" style="font-size:27px;font-weight:700">Nunca diga que o contato “é do dono” se for tipo B ou C. Use o tipo.</div>', fill=True)

# 6 ---- caminho do cliente
passos = [("Interesse", "Ele pede o piloto ou o teste no site. Chega um e-mail para o time."),
          ("Call de 30 min", "Você descobre, mostra o produto e oferece o teste."),
          ("Teste grátis", "3 leads para o que ele vende, por e-mail, em até 24 horas."),
          ("Decisão", "Gostou? Pacote de 100 por R$ 990, pagamento único."),
          ("Entrega", "Perfil de compra, pacote (HTML, CSV, JSON) e o aplicativo."),
          ("Acompanhamento", "Conversa curta depois: o que funcionou, quais contatos chegaram.")]
pp = "".join(f'<div class="card" style="display:flex;gap:22px;align-items:center;padding:20px 26px"><span class="badge" style="min-width:72px;height:72px;font-size:38px">{i}</span><div><div class="f" style="font-size:38px;font-weight:800;color:#0F1B2D">{a}</div><div style="font-size:25px;color:#3a352d">{b}</div></div></div>' for i, (a, b) in enumerate(passos, 1))
page("6-o-caminho-do-cliente", "Estrutura da venda", "O caminho <mark>do cliente</mark>", "Do pedido ao acompanhamento, em seis passos.", pp, fill=True)

# 7 ---- objeções
obj = [("“É caro.”", "São 100 empresas com dono, contato e prova por menos de dez reais cada. E você testa 3 de graça antes."),
       ("“Já tenho lista.”", "A sua traz o dono, a origem do contato e por que a empresa combina com você? A nossa traz."),
       ("“Garante resultado?”", "Não. Entregamos o ponto de partida e você mede o que acontece no aplicativo."),
       ("“É exclusivo?”", "Não. A mesma empresa pode estar em outros pacotes. O valor está na qualidade e na prova."),
       ("“Vocês disparam as mensagens?”", "Não. Você fala com as empresas do seu jeito: WhatsApp, telefone ou e-mail.")]
oo = "".join(f'<div class="card" style="padding:18px 26px;display:flex;flex-direction:column;align-items:flex-start;justify-content:center"><div class="f" style="font-size:36px;font-weight:800;color:#b58f00">{a}</div><div style="font-size:27px;color:#1C1915">{E(b)}</div></div>' for a, b in obj)
page("7-cinco-objecoes", "Objeções", "5 objeções, <mark>5 respostas</mark>", "Ouça, confirme, responda curto e honesto, cheque.", oo, fill=True)

# 8 ---- diga / não diga
diga = ["“Um ponto de partida de verdade.”", "“Cada contato vem com tipo e origem.”", "“Você testa 3 de graça antes.”", "“Pagamento único, sem mensalidade.”", "“Funciona sem internet e não envia nada a ninguém.”", "“Se vender para pessoa física, não é o nosso produto.”"]
nao = ["Resultado, resposta ou venda garantidos", "Exclusividade ou garantia de reposição", "“O sistema envia as mensagens”", "Depoimento, número ou cliente inventado", "“O contato é do dono” (se for tipo B ou C)", "Desconto sem falar com o Dan"]
col = lambda t, items, bg, fg, mk: f'<div style="flex:1;display:flex;flex-direction:column;gap:12px"><div class="f" style="background:{bg};color:{fg};padding:18px 24px;border-radius:18px;font-size:42px;font-weight:800">{t}</div>' + "".join(f'<div class="card" style="font-size:25px;padding:16px 20px;flex:1;display:flex;gap:12px;align-items:center"><b style="color:{bg};font-size:34px">{mk}</b><span>{E(x)}</span></div>' for x in items) + '</div>'
page("8-diga-e-nao-diga", "Regras de ouro", "O que <mark>dizer</mark> e o que nunca dizer", "Honestidade vende. A promessa certa é a que a gente cumpre.",
     f'<div style="display:flex;gap:18px;flex:1;min-height:0">{col("Diga", diga, "#1d8a5a", "#fff", "✓")}{col("Nunca diga", nao, "#b3261e", "#fff", "✕")}</div>')

# 9 ---- descoberta
sp = [("S", "Situação", "O que você vende e para quem? Como encontra essas empresas hoje?"),
      ("P", "Problema", "Quando você acha a empresa, é fácil chegar no dono? O que é mais difícil nisso?"),
      ("I", "Implicação", "Quanto tempo isso toma por semana? O que você deixa de fazer por causa disso?"),
      ("N", "Necessidade", "Se amanhã tivesse 100 empresas certas com o contato do dono, o que mudaria?")]
ss = "".join(f'<div class="card" style="display:flex;gap:22px;align-items:center;padding:22px 26px"><span class="badge" style="min-width:76px;height:76px;font-size:42px">{a}</span><div><div class="f" style="font-size:36px;font-weight:800;color:#0F1B2D">{b}</div><div style="font-size:26px;color:#3a352d">{E(c)}</div></div></div>' for a, b, c in sp)
page("9-perguntas-de-descoberta", "Habilidade: descobrir", "Perguntas que <mark>abrem</mark> a venda", "Quatro tipos de pergunta, nessa ordem. Anote as palavras dele.",
     ss + '<div class="card y" style="font-size:27px;font-weight:700;text-align:center">Você fala 30%. Ele fala 70%. Depois repita as palavras dele: “você disse que perde tempo caçando o contato”.</div>')
print("ok")
