# Purple Digital Stage

## Direção visual

A referência fotográfica tem formato vertical 4:5 e concentra vermelho no chapéu/gola, âmbar na guitarra e luz de palco quente sobre um fundo muito escuro. O banner é uma composição horizontal original: roxo noturno domina; lavanda ilumina chuva, cordas e texto; âmbar/vermelho aparecem apenas como referência indireta na luz. A figura e a guitarra são silhuetas vetoriais simplificadas, sem retrato ou detalhe facial. O nome Prince aparece apenas como referência artística, sem alegar vínculo oficial.

## Estrutura

`README.md` mantém o conteúdo essencial em texto Markdown, usa imagens do próprio repositório, arte ASCII de largura compacta, stack honesta em aprendizado, e não inventa projetos ou links. `assets/purple-stage-banner.svg` é o banner original estático. `assets/purple-rain.gif` é a animação autônoma. `assets/guitar-ascii.txt` conserva uma cópia editável da arte. `docs/create_purple_rain.py` recria o GIF com Pillow.

## Compatibilidade e acesso

O README usa Markdown e HTML simples para centralizar as imagens. Não inclui JavaScript, CSS, iframe ou reprodução de áudio. O SVG não contém scripts/animação. GIF fornece movimento com fallback de texto alternativo; o essencial também está escrito no README. Elementos fluem verticalmente e imagens usam largura percentual; ASCII fica em bloco de texto rolável pelo visualizador. O GIF é silencioso e não comunica níveis reais de habilidade nem estados de sistema.

## Como alterar

Edite `README.md` no repositório `tiagx422/tiagx422`. Para atualizar a chuva, execute `python docs/create_purple_rain.py` com Pillow instalado. Mantenha caminhos relativos e confirme que GIF e SVG estão no diretório `assets/`. A lista de projetos pode ser preenchida quando houver repositórios públicos que queira destacar.
