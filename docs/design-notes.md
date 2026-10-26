# Purple terminal profile

O README usa o ASCII enviado pelo Tiago à esquerda e as informações de perfil à direita, seguindo o formato de duas colunas do exemplo ASCII Magic. Um elemento `<picture>` seleciona um SVG com composição horizontal para telas largas e uma composição empilhada para celulares. Os SVGs usam apenas formas e texto estáticos, sem scripts ou dependências externas. O ASCII fonte está em `assets/ascii-art-original.txt`; a versão compacta está em `assets/ascii-art-compact.txt`.

A coluna de informações mostra dados já informados: Tiago/tiagx422, tecnologias em aprendizado, foco em praticar e referência musical. As linhas com `$` são ilustração, não comandos executados. A chuva roxa continua como GIF local independente. Prince e *While My Guitar Gently Weeps* aparecem como referências artísticas, sem sugerir vínculo oficial.

## Estrutura

- `README.md`: imagem adaptativa, animação, apresentação, stack, projetos e rodapé.
- `assets/profile-desktop.svg`: composição lado a lado.
- `assets/profile-mobile.svg`: composição vertical para telas estreitas.
- `assets/ascii-art-original.txt`: desenho enviado, sem linhas vazias externas.
- `assets/ascii-art-compact.txt`: amostragem ASCII usada nas duas composições.
- `assets/purple-rain.gif`: chuva digital em loop.
- `docs/create_purple_rain.py`: gerador da animação.
- `docs/optimization.md`: compatibilidade, dimensões e checagens.
