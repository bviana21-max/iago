---
version: 1.8
name: elo-digital-design
description: >
  Sistema editorial de serviço, calmo e legível, para uma consultoria de tecnologia
  pessoal e presença digital. Canvas de papel morno (#EFEDE7) com cartões brancos
  elevados e hairlines quentes; tinta quase preta (#16191C) carrega toda a
  hierarquia. A única voltagem cromática é o verde-sinal #0B5D3B, reservado a
  ESTADO e MEDIDA (afinidade calculada, status, recomendação) — nunca à CTA
  primária, que é sempre tinta. Display em Bricolage Grotesque 500/600 com tracking
  negativo proporcional; texto em Instrument Sans a partir de 18px, porque parte do
  público tem 60+; JetBrains Mono para números, scores e rótulos de sistema. O gesto
  assinatura é a barra de afinidade: o site mede o encaixe entre pessoa e serviço e
  mostra a medida.
cinema_layer: >
  Camada estrutural derivada da ficha `apple`: tiles full-bleed que alternam
  papel e quase-preto, com a troca de superfície funcionando como divisor;
  vídeo como protagonista e chrome que recua; press-state scale(.96) em todo
  elemento clicável; a ÚNICA sombra do sistema (rgba(0,0,0,.22) 3px 5px 30px)
  reservada à mídia apoiada na superfície — nunca em cartão, botão ou texto.
  Divergência deliberada: a Apple corta seco entre tiles; aqui há uma "ponte"
  de 56–110px em gradiente entre papel e escuro, porque o canvas morno pede
  transição em vez de choque.
governing_system: >
  Derivado da ficha `intercom` da biblioteca DESIGN.md (estrutura, superfície
  cream + cartão branco, hairlines, raios modestos, display sans peso 500,
  ausência de sombras). Voltagem, tipografia e escala de corpo foram substituídas:
  o Fin Orange dá lugar ao verde-sinal e o corpo sobe de 16px para 18px por
  acessibilidade. Inspiração estrutural, não clonagem.

colors:
  canvas: "#EFEDE7"
  surface: "#FFFFFF"
  surface-2: "#E4E1D8"
  ink: "#16191C"
  ink-muted: "#565B58"
  ink-subtle: "#5C615D"
  hairline: "#D6D2C8"
  hairline-soft: "#E4E1D8"
  voltage: "#0B5D3B"
  voltage-soft: "#DDEAE0"
  voltage-line: "#B9D3C4"
  voltage-on-dark: "#7FD3A8"
  zap: "#25D366"          # verde WhatsApp — o único ponto de saturação alta do site
  zap-hover: "#1BC257"
  zap-ink: "#062616"      # tinta sobre o verde: 8,17:1 (o branco da marca daria 1,98:1)
  zap-halo: "rgba(37,211,102,.45)"
  alerta: "#8A5220"
  alerta-soft: "#F6E9DC"
  inverse: "#12161A"
  inverse-ink: "#F2F1EC"
  inverse-muted: "#A6ADA8"

typography:
  display-xl: { family: Bricolage Grotesque, size: "clamp(2.25rem, 1.4rem + 3.6vw, 4.15rem)", weight: 500, lineHeight: 1.03, letterSpacing: "-0.035em" }
  display-lg: { family: Bricolage Grotesque, size: "clamp(1.75rem, 1.2rem + 2.1vw, 2.85rem)", weight: 500, lineHeight: 1.10, letterSpacing: "-0.027em" }
  headline:   { family: Bricolage Grotesque, size: "clamp(1.2rem, 1.05rem + .5vw, 1.45rem)", weight: 500, lineHeight: 1.22, letterSpacing: "-0.015em" }
  lead:       { family: Instrument Sans, size: "20px", weight: 400, lineHeight: 1.50 }
  body:       { family: Instrument Sans, size: "18px", weight: 400, lineHeight: 1.55 }
  body-sm:    { family: Instrument Sans, size: "15.5px", weight: 400, lineHeight: 1.50 }
  button:     { family: Instrument Sans, size: "16px", weight: 600, letterSpacing: "-0.01em" }
  eyebrow:    { family: JetBrains Mono, size: "13px", weight: 400, letterSpacing: "0.06em", transform: uppercase }
  data:       { family: JetBrains Mono, size: "12–15px", weight: 400, features: "tabular-nums" }

spacing: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px, 12: 48px, 16: 64px, section: "clamp(56px, 8vw, 104px)" }
radii:   { xs: 4px, sm: 6px, md: 8px, lg: 12px, xl: 16px, pill: 999px }
shadows: none   # profundidade vem da troca de superfície (branco sobre papel), nunca de sombra
motion:
  ease-out: "cubic-bezier(.16,1,.3,1)   # entradas — arranque rápido, pouso macio"
  estado: "0.33s cubic-bezier(.5,0,0,.75) — TODA troca de estado (hover, cor, borda, foco). Vem da ficha `tesla` da biblioteca: consistência em movimento importa tanto quanto consistência em cor. Exceção: pressão fica em 120ms, resposta ao toque não espera."
  ease-inout: "cubic-bezier(.65,0,.35,1) # trocas de estado"
  durations: "120 / 180 / 240 / 380 / 520 / 760ms — nada acima de 760"
  regra: "só transform e opacity (compositor); nunca width, height, margin ou padding"
  ease-legado: "cubic-bezier(.22,.61,.36,1)"
  reveal: "720ms — opacity + translateY(20px) + blur(5px)→0"
  stagger: "70ms por filho, teto de 8 filhos"
  barra: "800ms (largura do score)"
  flip: "620ms + 28ms de escalonamento (reordenação do catálogo)"
  press: "scale(.96) em btn, op, chip e caminho"
  header: "380ms — recolhe ao descer, retorna ao subir"
  hero-scrub: "escala 1.06→1.16 e saída do texto, atrelado à rolagem via rAF"
  micro: "140–160ms"
  palavra: "760ms, translateY(115%)→0, 45ms por palavra, teto de 14"
  passo-quiz: "190ms de saída à esquerda + 520ms de entrada pela direita"
  score: "barra 900ms scaleX + contagem numérica 900ms ease-out-cubic"
  halo-zap: "2,1s × 3 repetições, e para — atenção, não distração"
  paralaxe: "animation-timeline: view(), ±3,5% no vídeo do tile, zero JavaScript"
  progresso: "scaleX da barra de leitura, rAF, passive listener"
  revelacao: "posição na tela + rAF (não IntersectionObserver), cascata inicial de 110ms com teto de 3s; rearme quando o bloco sai bem para fora da tela, para que a entrada não seja um evento único"
  altura-visivel: "min(innerHeight, visualViewport.height); se ainda for >1,3x a tela física, usa a tela — moldura ajustada ao conteúdo mente sobre o que está em cena"
  interruptor: "data-motion=ligado|desligado no <html>, escrito uma vez no carregamento; ?movimento=1|0 é parâmetro de teste, não controle de interface"
---

## Camada de motion (arquivo próprio)

O movimento vive em `elo-motion.css` + `elo-motion.js`, colados no fim do
`<style>` e antes de `</body>`. Contrato:

- **Um único `requestAnimationFrame` para o site inteiro**, com fase de leitura
  (`getBoundingClientRect`) separada da fase de escrita (estilo/classe) — loops
  concorrentes e layout thrash são a causa nº 1 de INP ruim em site animado.
- **`.js-motion` no `<html>`**: o estado inicial oculto só é aplicado depois que
  o JS confirma que vai animar. Sem JS, o conteúdo nasce visível.
- **`data-motion=ligado|desligado`** escrito uma vez no carregamento.
- **`data-desempenho="baixo"`** (≤4 GB de RAM ou ≤4 núcleos): sai o `blur` de
  superfície grande e a paralaxe de vídeo; a entrada continua.
- **Movimento reduzido ≠ sem animação**: fica o fade, sai o deslocamento, a
  escala, o blur e a paralaxe. Matar todo feedback tira da pessoa a informação
  de que algo respondeu ao toque dela.
- **Guardas obrigatórias**: `matchMedia`, `Element.animate` e `scrollIntoView`
  são checados antes do uso. Um ambiente sem WAAPI perde a animação do passo,
  nunca a navegação do diagnóstico.
- Ganchos: `[data-palavras]`, `.rev`/`[data-rev]`, `.barra__f[data-score]`,
  `[data-contador]`, `.cabecalho`, `.progresso__f`, `.heroi-cine__midia`,
  `.heroi-cine__texto`, `.tile__midia`, `.btn--zap`, `[data-superficie="escura"]`.
- API: `ELOMotion.medir(escopo)`, `ELOMotion.passo(sai, entra)`,
  `ELOMotion.reordenar(mutacao)`.

## Alto contraste (modo, não variação)

`data-contraste="alto"` não é "um branco diferente" — é outro modo de renderizar:

| Camada | Padrão | Alto contraste |
|---|---|---|
| Papel / tinta | `#EFEDE7` / `#16191C` (15,1:1) | `#FFFFFF` / `#000000` (**21:1**) |
| Cinzas de apoio | `ink-muted`, `ink-subtle` | **eliminados** — todo texto vira tinta |
| Hairlines | 1px `#D6D2C8` | **2px `#000000`** em cartão, botão, chip, opção e motor |
| Superfície escura | `#12161A` | **`#000000`** com texto branco puro |
| Voltagem | `#0B5D3B` | `#00532F` (9,2:1) · no escuro `#8CF3BE` (15,7:1) |
| WhatsApp | `#25D366` + tinta escura | `#0A7C36` + branco (5,3:1) — a saturação cede à legibilidade |
| Véu sobre vídeo | gradiente em 4 paradas | **opaco a 86%** |
| Estado selecionado | fundo verde-suave | **preto sólido com texto branco** |
| Links | sem sublinhado | **sublinhados** |
| Foco | 3px | **4px** |
| Opacidade como informação | cartão fora do filtro a 42% | **proibida** — volta a 100% |

Regra que originou o modo: **nada pode ser comunicado só por opacidade, só por matiz ou só por hairline de 1px.**

## Escala de leitura (token vivo)

`--escala` multiplica toda a tipografia de corpo: `1` · `1.14` (A+) · `1.3` (A++).
Não é um recurso de acessibilidade escondido no rodapé: fica no cabeçalho, ao lado
da CTA, porque o próprio público do negócio precisa dele. O modo `data-contraste="alto"`
troca o canvas por branco puro, escurece hairlines e leva a tinta a `#000000`.

Regra: nenhum componente pode quebrar em `--escala: 1.3`. Alturas fixas são proibidas
em qualquer elemento que contenha texto — use `min-height` e padding.

## Layout & Grid

- Container 1200px, padding lateral `clamp(18px, 4vw, 40px)`.
- Catálogo 2 colunas → 1 coluna em 820px. Planos `auto-fit / minmax(258px, 1fr)`.
- Jornada em 6 colunas → 3 → 2.
- Texto corrido nunca passa de ~70ch (`.lead` fecha em 62ch).
- Respiro vertical de seção: `clamp(56px, 8vw, 104px)`. O papel morno faz o trabalho
  que o branco faria em outro sistema.

## Componentes (estados)

| Componente | Default | Hover | Selecionado / Ativo | Foco |
|---|---|---|---|---|
| `btn--primaria` | fundo `ink`, texto branco, raio 8px, min-height 52px | `#000` | `translateY(1px)` | outline 3px `voltage` |
| `btn--secundaria` | `surface` + 1px `hairline` | borda `ink` | — | idem |
| `btn--zap` | fundo `voltage` | `#0a4c31` | — | idem |
| `op` (opção do diagnóstico) | `canvas` + 1px `hairline`, min-height 60px | borda `ink` | fundo `voltage-soft`, inset ring `voltage`, marca preenchida | idem |
| `chip` (filtro) | `surface` + hairline, pill | — | fundo `ink`, texto branco | idem |
| `serv` (cartão de serviço) | `surface` + hairline, raio 12px | — | `data-apagado="1"` → opacidade .42 | — |
| `plano--destaque` | fundo `inverse`, texto claro | — | — | — |
| `barra__f` | scaleX(0)→score em 900ms, origem à esquerda | — | — | — |
| `btn--zap` | verde #25D366 com tinta #062616, ícone gira no hover, halo 3× ao entrar em cena | varredura + halo | `scale(.97)` | outline 3px |
| `pal` / `pal__i` | palavra do título, sobe de dentro da própria linha; pontuação cola na palavra anterior (caixas inline-block criam ponto de quebra entre si) | — | — | — |
| `pal--v` | palavra em destaque no título: `voltage` no papel, `voltage-on-dark` no escuro — a pontuação fica fora do span colorido | — | — | — |
| `progresso` | barra de leitura de 3px no topo, `scaleX` | — | — | — |
| `p3` (como funciona) | `surface` + hairline, numeração mono em voltagem | — | — | — |
| `sinal` (alerta de golpe) | disco âmbar `#F6E9DC` / `#8A5220` (5,3:1), hairline inferior | — | — | — |
| `barrafixa` (mobile) | fixa no rodapé < 640px, blur, duas ações | — | — | — |
| `hamb` / `navmob` | menu do cabeçalho < 1080px, painel empilhado | — | `aria-expanded="true"` | outline 3px |
| `heroi-cine` | vídeo full-bleed 100svh + scrim vertical em 4 paradas, texto ancorado embaixo | — | scrub por rolagem | — |
| `tile` / `tile--papel` | seção full-bleed escura ou papel, grade .92fr/1.08fr, mídia 16:10 com a sombra do sistema | — | vídeo toca só em cena | — |
| `ponte` | faixa de 56–110px em gradiente entre duas superfícies | — | — | — |

## Uso da voltagem (regra dura)

O verde `#0B5D3B` só aparece em: score de afinidade, barra de afinidade, chips de
"por quê", eyebrow, pontos de status, selo de plano, CTA de WhatsApp e ícone de
caminho. **Nunca** como fundo de seção, gradiente ou CTA genérica. Se um bloco
precisa de destaque, ele sobe para `surface` branco ou desce para `inverse`.

## Do

- Elevar do papel para o branco quando a informação exige foco.
- Manter uma única CTA primária por dobra; as demais viram secundária ou fantasma.
- Números sempre em mono, tabular, com o sufixo explicando a unidade ("% de afinidade").
- Numerar apenas o que é sequência real (jornada 01→06, portfólio 01→08).
- Escrever o benefício antes da especificação, sempre.

## Don't

- Sem sombra em cartão, sem gradiente decorativo, sem pill em CTA.
- Sem cinza abaixo de `#5C615D` em texto sobre papel (quebra AA no público 60+).
- Sem emoji como ícone, sem ícone sem rótulo.
- Sem terceira família tipográfica.
- Sem porcentagem sem explicação: toda medida exibida precisa dizer o que mede.
- Sem esconder navegação no celular: se o link some, ele vira menu — nunca desaparece.
- Sem rótulo de navegação que quebre em duas linhas: `white-space:nowrap` e, se não couber, o item sai do desktop e vive no menu. Máximo de 5 itens na barra.
- Sem movimento que o sistema não queira: `prefers-reduced-motion`, `saveData` e rede 2G desligam vídeo, scrub, FLIP e revelações — o site permanece completo e legível.
- Sem vídeo autoplay com som, sem vídeo como texto, sem vídeo carregado fora de cena.
- Sem animação em `width`, `height`, `margin` ou `padding` — força recálculo de layout e derruba INP/CLS.
- Sem loop infinito competindo com a leitura: o halo do WhatsApp roda 3 vezes e para.
- Sem branco sobre o verde do WhatsApp (1,98:1). A tinta escura é obrigatória.
- Sem verde escuro sobre superfície escura: no papel é `#0B5D3B`, no escuro é `#7FD3A8`. A regra vale para eyebrow, selo, score **e destaque dentro do título**.
- Sem vírgula, ponto ou reticência como palavra independente em título fatiado.
- Sem controle de animação exposto ao visitante: animado é o padrão, e quem quer menos movimento já disse isso ao sistema operacional. Preferência já declarada não se pergunta de novo.
- Sem revelação presa a `IntersectionObserver`: em moldura alta ele dispara para a página toda de uma vez e o movimento vira invisível.
- Sem bloco que dependa de animação para existir: varredura de segurança aos 4 s e aos 8 s revela o que sobrou.
- Sem animação de entrada de uso único: se a entrada só acontece uma vez, num painel alto ela ocorre inteira antes de alguém olhar e o site parece parado para sempre. Blocos que saem de cena rearmam.

## Arquivos

- `index.html` — site completo, autocontido (CSS e JS inline), pronto para deploy.
- `og-image.png` — 1200×630, mesma linguagem, gerado a partir destes tokens.
- 3 vídeos (Higgsfield / Kling 3.0 Turbo, 16:9, 5s, loop mudo): herói, tile "vida digital", tile "presença digital".
- Fontes: Bricolage Grotesque, Instrument Sans, JetBrains Mono (Google Fonts, licença OFL).
