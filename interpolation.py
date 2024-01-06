def newton_interpolation(x, y):
    n = len(x)
    coefficients = [y[0]]

    for i in range(1, n):
        divided_diff = [0] * (n - i)
        for j in range(n - i):
            if x[j + i] == x[j]:
                divided_diff[j] = 0  # Handle case where x[j + i] equals x[j] to avoid division by zero
            else:
                divided_diff[j] = (y[j + 1] - y[j]) / (x[j + i] - x[j])
        coefficients.append(divided_diff[0])
        y = divided_diff

    return coefficients
