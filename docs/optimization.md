# Otimização e verificação

- A arte compacta tem 60 colunas × 35 linhas; a cópia original aparada permanece no repositório.
- Os GIFs têm 420 × 380 pixels, 18 quadros, loop contínuo e transparência. O ritmo é de 110 ms por quadro (1,98 s por loop).
- Na versão gerada para instalação, os GIFs têm aproximadamente 32 KB cada, com uma paleta pequena e sem dependências externas.
- O README usa `<picture>` para selecionar a cor adequada ao tema claro ou escuro. A alternativa empilhada está documentada em `README-SETUP.md` para telas estreitas.
- O README é Markdown com estrutura HTML simples; a animação não depende de JavaScript, CSS ou canvas.
- A validação local confere os caminhos de imagem, a transparência e os quadros dos GIFs, os SVGs, as dimensões da arte e a igualdade entre o fallback ASCII e o arquivo compacto. Faça uma última conferência visual na prévia do GitHub após publicar.

