size, outer = input('Enter size and outermost layer : ').split()
digits_length = int(len(outer))
size, outer = int(size), int(outer)

def layerCake(size, outer, length):
    matrix = [[0] * size for _ in range(size)]
    for layer in range((size + 1) // 2):
        value = outer - layer

        for i in range(layer, size - layer):
            matrix[layer][i] = value

        for i in range(layer + 1, size - layer):
            matrix[i][size - layer - 1] = value

        for i in range(size - layer - 2, layer - 1, -1):
            matrix[size - layer - 1][i] = value

        for i in range(size - layer - 2, layer, -1):
            matrix[i][layer] = value

    for row in matrix:
        for val in row:
            print(f' {val:>{length}}', end='')
        print()

if __name__ == "__main__":
    layerCake(size, outer, digits_length)