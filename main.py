import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
GRID_SIZE = 50  # Tamanho da floresta
TREE = 1  # Árvore           (VERDE)
BURNING = 2  # Pegando fogo  (LARANJA)
EMPTY = 0  # Espaço vazio    (PRETO)
BURNED = 3 # Arvore queimada (CINZA)

p_spread = 0.8  # Probabilidade de propagação do fogo

forest = np.random.choice([TREE, EMPTY], size=(GRID_SIZE, GRID_SIZE), p=[0.8, 0.2])

while True:
    fire_x, fire_y = np.random.randint(0, GRID_SIZE, size=2)
    if forest[fire_x, fire_y] == TREE:
        forest[fire_x, fire_y] = BURNING
        break

def plot_forest(forest, step):
    colors = {EMPTY: 'black', TREE: 'green', BURNING: 'orange', BURNED: 'gray'}
    cmap = plt.matplotlib.colors.ListedColormap([colors[EMPTY], colors[TREE], colors[BURNING], colors[BURNED]])
    plt.imshow(forest, cmap=cmap, interpolation="nearest")
    plt.title(f"Iteração: {step}")
    plt.axis("off")
    plt.pause(0.2)

# Simulação da propagação do fogo
plt.ion()
step = 0
while np.any(forest == BURNING):
    plot_forest(forest, step)
    step += 1

    new_forest = forest.copy()

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if forest[i, j] == TREE:
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for ni, nj in neighbors:
                    if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE and forest[ni, nj] == BURNING:
                        if np.random.rand() < p_spread:
                            new_forest[i, j] = BURNING
                        break
            elif forest[i, j] == BURNING:
                new_forest[i, j] = BURNED

    forest = new_forest

plt.ioff()
plt.show()
