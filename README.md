# pythonINVADERS
jogo tipo space invaders criado com python 
Py Invasores do Espaço

Py Invasores do Espaço é um remake do clássico Space Invaders, desenvolvido em Python usando Pygame. O projeto inclui nave controlável pelo jogador, obstáculos, aliens com diferentes níveis de vida, sons, HUD e ondas progressivas de dificuldade.

🎮 Funcionalidades

Controle da nave: movimente para esquerda/direita e atire lasers com a barra de espaço.

Aliens em grupo: movimento lateral clássico e descida gradual.

Dificuldade diferenciada por alien:

Alien 1 → 1 tiro para ser destruído

Alien 2 → 2 tiros para ser destruído

Alien 3 → 3 tiros para ser destruído

Waves progressivas: até 5 ondas, aumentando velocidade dos aliens e da nave.

Vida da nave: 5 tiros permitidos; se zerar → game over.

Obstáculos: protegem a nave e podem ser destruídos por lasers.

HUD: vida da nave no canto inferior esquerdo, waves restantes no canto superior direito.

Sons: música de fundo, laser da nave e explosões.

Restart: pressione R após game over ou vitória.

🛠 Requisitos

Python 3.10+

Pygame

Instalação do Pygame:

pip install pygame-ce

🗂 Estrutura do projeto
SPACE_INVADERS/
│
├── main.py              # Arquivo principal do jogo
├── spaceship.py         # Classe da nave do jogador
├── alien.py             # Classe dos aliens inimigos
├── obstacle.py          # Classe dos obstáculos
├── laser.py             # Classe dos lasers (tiros)
├── Graphics/            # Pasta com imagens (nave, aliens, fundo)
│   ├── spaceship.png
│   ├── alien_1.png
│   ├── alien_2.png
│   ├── alien_3.png
│   └── background.png
└── Sounds/              # Pasta com efeitos sonoros
    ├── music.ogg
    ├── laser.ogg
    └── explosion.ogg

▶️ Como jogar

Execute o jogo:

python main.py


Controles:

Seta esquerda/direita: mover nave

Barra de espaço: disparar laser

R: reiniciar o jogo após game over ou vitória

Sobreviva a 5 ondas de aliens sem perder toda a vida.

💡 Dicas

Cada tipo de alien tem resistência diferente — priorize os mais fortes na última fila.

Use obstáculos como proteção, mas eles podem ser destruídos pelos tiros inimigos.

Os aliens atiram automaticamente a cada 1 segundo (ajustável).

A velocidade da nave e dos aliens aumenta a cada nova wave.

🔧 Customizações

Frequência de tiros dos aliens: altere no main.py no evento ALIEN_SHOOT:

pygame.time.set_timer(ALIEN_SHOOT, 1000)  # 1000ms = 1 tiro/segundo


Alinhamento inicial dos aliens: ajuste na função create_wave() os valores de x e y.

📜 Licença

Este projeto é para fins educativos e recreativos. Sinta-se à vontade para modificar e expandir o código.
