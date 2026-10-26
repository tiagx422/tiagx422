# Purple terminal profile

O README usa o ASCII enviado pelo Tiago como foco principal. A cópia fonte aparada está em `assets/ascii-art-original.txt`; a versão compacta em `assets/ascii-art-compact.txt` reduz o desenho de 93 × 54 para 60 × 35 células para caber ao lado das informações no bloco monoespaçado.

A coluna da direita mostra somente dados já informados: Tiago/tiagx422, tecnologias em aprendizado, foco em praticar e a referência musical. Os comandos são texto decorativo, não comandos executados. A chuva roxa é uma animação local separada. Prince e *While My Guitar Gently Weeps* aparecem como referências artísticas, sem sugerir vínculo oficial.

## Estrutura

- `README.md`: bloco ASCII e terminal lado a lado, breve apresentação, stack, projetos e rodapé.
- `assets/ascii-art-original.txt`: desenho enviado, sem linhas vazias externas.
- `assets/ascii-art-compact.txt`: versão usada no README.
- `assets/purple-rain.gif`: chuva digital em loop.
- `docs/create_purple_rain.py`: gerador da animação.
- `docs/optimization.md`: compatibilidade, dimensões e checagens.

## Atualização

Edite `README.md` para mudar as informações. Edite `assets/ascii-art-compact.txt` para ajustar o desenho da versão exibida. A arte fonte fica preservada em `assets/ascii-art-original.txt`. Para recriar a animação, execute `python docs/create_purple_rain.py` com Pillow instalado.
