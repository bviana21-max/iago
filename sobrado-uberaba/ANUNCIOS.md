# Sobrado Uberaba (ref. 4631): kit de anúncios

Página: `sobrado-uberaba/index.html` · Criativos: `sobrado-uberaba/criativos/` · Imagem de compartilhamento: `sobrado-uberaba/og.jpg`

Fonte de todos os dados: anúncio público da ref. 4631 (R$ 550.000, antes R$ 570.000; condomínio R$ 250; IPTU R$ 90,23; 75,4 m² privativos; 2 quartos; 1 banheiro + lavabo; 1 vaga; face norte; semi-mobiliado; aceita pet; aceita financiamento). Nada foi inventado: não há depoimentos, prazos ou descontos além da redução de preço que consta no anúncio.

---

## 1. Antes de ligar qualquer campanha

1. **Preencha o bloco `LP_CONFIG`** no fim do `index.html`. Já preenchidos: `whatsapp` ((41) 98735-7898), `corretor` (Nete Benicio) e `creci` (CRECI-PR 55283). Faltam só os IDs dos pixels.
   - `whatsapp`: DDI + DDD + número, só dígitos (ex.: `5541999998888`). Sem isso, os botões só rolam até o formulário e o lead não chega a ninguém.
   - `corretor` e `creci`: aparecem no rodapé. O CRECI é obrigatório em anúncio de imóvel (regra do COFECI), na página e no texto do anúncio.
   - `metaPixelId`, `ga4Id`, `googleAdsId`, `googleAdsLeadLabel`, `googleAdsContatoLabel`: os pixels só carregam se o ID estiver preenchido.
   - `webhook` (opcional): URL do Make, Zapier ou Google Apps Script para guardar cada lead numa planilha, além do WhatsApp.
2. **Publique a pasta `sobrado-uberaba/`** no mesmo lugar onde o site deste repositório é servido. A página fica em `https://SEU-DOMINIO/sobrado-uberaba/`.
3. **Troque `og.jpg` por URL absoluta** na tag `og:image` (ex.: `https://SEU-DOMINIO/sobrado-uberaba/og.jpg`). Sem isso, o link não mostra a foto quando compartilhado no WhatsApp.
4. **Teste no celular**: envie o formulário e confira se o WhatsApp abre com a mensagem pronta. Use o Meta Pixel Helper e o Google Tag Assistant para ver os eventos.
5. **Fotos**: elas têm a marca d'água da imobiliária que fez o anúncio original. Use-as só se você tiver autorização (ou se for a própria imobiliária).

### Eventos que a página dispara

| Ação do visitante | Meta Pixel | GA4 / Google Ads |
|---|---|---|
| Abre a página | `PageView`, `ViewContent` (valor 550.000) | `page_view` |
| Toca em qualquer botão de WhatsApp | `Contact` | `contact` + conversão `googleAdsContatoLabel` |
| Envia o formulário de visita | `Lead` | `generate_lead` + conversão `googleAdsLeadLabel` |
| Mexe no simulador (1ª vez) | `Simulador_usado` (custom) | `Simulador_usado` |
| Envia a simulação à corretora | `Simulacao_enviada` (custom) | `Simulacao_enviada` |
| Abre a galeria | `Galeria_aberta` (custom) | `Galeria_aberta` |

A mensagem do WhatsApp termina com `[ref. 4631 · meta/campanha]` quando o clique veio de anúncio com UTM. Assim a corretora sabe de onde veio cada lead, mesmo que o pixel falhe.

### Parâmetros de URL

- **Meta** (campo "Parâmetros de URL" do anúncio):
  `utm_source=meta&utm_medium=paid&utm_campaign=sobrado-uberaba-4631&utm_content={{ad.name}}`
- **Google Ads**: deixe a codificação automática (gclid) ligada e use como sufixo do URL final:
  `utm_source=google&utm_medium=cpc&utm_campaign=sobrado-uberaba-4631`

---

## 2. Meta Ads (Facebook e Instagram)

**Estrutura sugerida**: 1 campanha › 1 conjunto › 3 anúncios (A, B e C abaixo), cada um com os criativos de feed (`meta-feed-1080x1350.jpg`) e de Stories/Reels (`meta-stories-1080x1920.jpg`).

- **Objetivo**: Leads, com local de conversão "Site" e evento `Lead`. Se o pixel ainda não estiver configurado, comece com Tráfego otimizando para "Visualizações da página de destino" e troque assim que o pixel registrar os primeiros leads.
- **Categoria especial**: se o Gerenciador pedir a categoria "Moradia", marque-a. Ela limita filtros de idade e localização; use Curitiba + região e deixe a Meta otimizar.
- **Público**: Curitiba e região metropolitana, público amplo (Advantage+). Com o pixel aprendendo, público amplo costuma render mais que interesses.
- **Orçamento de teste**: R$ 60 por dia durante 14 dias (R$ 840 no total). Não pause nenhum anúncio antes de ele ter umas 1.000 impressões; depois disso, desligue o de maior custo por lead.
- **Botão**: "Saiba mais" (leva para a página) ou "Enviar mensagem" se preferir uma campanha separada direto para o WhatsApp.

### Anúncio A: aposta na oferta (preço + condomínio)

**Texto principal**
> Sobrado inteiro, em condomínio fechado, por R$ 550 mil. O preço baixou R$ 20 mil.
>
> 🏡 2 quartos + lavabo, 75,4 m² privativos
> ☀️ Face norte, o lado que recebe sol em Curitiba
> 🍳 Cozinha planejada com ilha, cooktop e coifa
> 🐶 Aceita pet · condomínio de R$ 250/mês
>
> Semi-mobiliado e pronto para a sua mudança no Uberaba. Veja as 32 fotos reais e simule a parcela.
>
> Corretora responsável: Nete Benicio · CRECI-PR 55283

**Título**: Sobrado no Uberaba por R$ 550 mil
**Descrição**: Condomínio fechado · R$ 250/mês

### Anúncio B: aposta no ângulo (sair do apartamento)

**Texto principal**
> Cansou de vizinho de cima e de condomínio que só sobe?
>
> Este sobrado no Uberaba tem dois andares só seus, em condomínio fechado, com taxa de R$ 250 por mês. Cozinha com ilha, armários planejados em todos os ambientes, vaga na frente da porta e aceita pet.
>
> R$ 550 mil, aceita financiamento. Agende sua visita pelo WhatsApp.
>
> Corretora responsável: Nete Benicio · CRECI-PR 55283

**Título**: Troque o elevador pela sua escada
**Descrição**: Sobrado 2 quartos · R$ 550 mil

### Anúncio C: aposta no formato (pergunta curta, gancho local)

**Texto principal**
> Em Curitiba, quando o sol aparece, ele entra pela sua janela?
>
> Neste sobrado, sim: face norte, em condomínio fechado no Uberaba. 2 quartos, cozinha com ilha, semi-mobiliado e condomínio de R$ 250.
>
> R$ 550 mil. Veja as fotos e agende sua visita.
>
> Corretora responsável: Nete Benicio · CRECI-PR 55283

**Título**: Sobrado face norte no Uberaba
**Descrição**: Semi-mobiliado · aceita pet

Depois de 14 dias, o vencedor diz qual mensagem puxar nas próximas rodadas: se o B ganhar, o público responde mais à troca de estilo de vida do que ao preço.

---

## 3. Google Ads (Pesquisa)

**Campanha**: Pesquisa, local Curitiba + região metropolitana (raio de 25 km do imóvel), idioma português. Orçamento de teste: R$ 40 por dia (R$ 560 em 14 dias). Lance: Maximizar cliques nas duas primeiras semanas; mude para Maximizar conversões quando houver 15 ou mais conversões registradas.

### Palavras-chave (correspondência de frase)

```
"sobrado à venda uberaba"
"sobrado uberaba curitiba"
"casa à venda uberaba curitiba"
"casa em condomínio uberaba"
"sobrado em condomínio curitiba"
"casa em condomínio fechado curitiba"
"sobrado 2 quartos curitiba"
"sobrado à venda curitiba"
"casa 2 quartos à venda curitiba"
"sobrado semi mobiliado curitiba"
```

### Palavras-chave negativas

```
aluguel, alugar, aluga, locação, temporada, leilão, terreno, lote, comercial,
sala comercial, apartamento, kitnet, minha casa minha vida, mcmv, grátis, emprego, vaga de emprego
```

### Anúncio responsivo: títulos (até 30 caracteres)

| # | Título | Caracteres |
|---|---|---|
| 1 | Sobrado à Venda no Uberaba | 26 |
| 2 | Condomínio Fechado | 18 |
| 3 | Sobrado por R$ 550 Mil | 22 |
| 4 | Condomínio de R$ 250 por Mês | 28 |
| 5 | Face Norte, Sol no Inverno | 26 |
| 6 | Cozinha Planejada com Ilha | 26 |
| 7 | Semi-Mobiliado e Aceita Pet | 27 |
| 8 | 2 Quartos em Curitiba | 21 |
| 9 | Preço Baixou R$ 20 Mil | 22 |
| 10 | Agende Sua Visita | 17 |
| 11 | Aceita Financiamento | 20 |
| 12 | Veja as 32 Fotos Reais | 22 |
| 13 | Simule a Parcela no Site | 24 |
| 14 | Vaga na Frente da Casa | 22 |
| 15 | Saia do Apartamento | 19 |

Fixe o título 1 na posição 1 para que todo anúncio comece dizendo o que é e onde fica.

### Anúncio responsivo: descrições (até 90 caracteres)

| # | Descrição | Caracteres |
|---|---|---|
| 1 | Sobrado de 2 quartos em condomínio fechado no Uberaba. Face norte e cozinha com ilha. | 85 |
| 2 | Semi-mobiliado: armários planejados, cooktop, forno e coifa. Aceita pet. | 72 |
| 3 | R$ 550 mil e condomínio de R$ 250. Aceita financiamento. Simule a parcela no site. | 82 |
| 4 | Veja as 32 fotos reais, simule o financiamento e fale com a corretora pelo WhatsApp. | 84 |

### Recursos (extensões)

- **Sitelinks** (até 25 caracteres):
  - Ver as 32 Fotos → `/sobrado-uberaba/#tour`
  - Simular Parcelas → `/sobrado-uberaba/#parcelas`
  - Agendar Visita → `/sobrado-uberaba/#visita`
  - Localização → `/sobrado-uberaba/#local`
- **Frases de destaque**: Condomínio R$ 250/mês · Face Norte · Aceita Pet · Semi-Mobiliado · Aceita Financiamento · Condomínio Fechado · Corretora CRECI-PR 55283
- **Snippet estruturado** (cabeçalho "Comodidades"): Cozinha com ilha · Armários planejados · Aquecimento a gás · Portão eletrônico
- **Imagens**: `quadrado-1200x1200.jpg` e `paisagem-1200x630.jpg`

---

## 4. Criativos

| Arquivo | Uso |
|---|---|
| `criativos/meta-feed-1080x1350.jpg` | Feed do Instagram e do Facebook (4:5) |
| `criativos/meta-stories-1080x1920.jpg` | Stories e Reels (9:16); o texto fica fora das faixas de interface |
| `criativos/quadrado-1200x1200.jpg` | Google (imagens de Pesquisa e Display) e feed quadrado |
| `criativos/paisagem-1200x630.jpg` | Google Display e coluna da direita do Facebook |
| `og.jpg` | Prévia do link no WhatsApp e nas redes |

Todos os criativos trazem o selo "Nete Benicio · CRECI-PR 55283" no canto da foto.

## 5. Rotina das duas primeiras semanas

- **Dia 1**: conferir se os eventos `Lead` e `Contact` aparecem no Gerenciador de Eventos e nas conversões do Google Ads.
- **Diariamente**: responder cada lead no WhatsApp em poucas horas; lead imobiliário esfria rápido.
- **Dia 7**: comparar custo por lead entre A, B e C (Meta) e ver os termos de pesquisa do Google para adicionar negativas.
- **Dia 14**: manter o anúncio vencedor, escrever duas variações dele e realocar a verba do canal com menor custo por visita agendada.
