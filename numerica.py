for k in range(1, N-1):
    for i in range(k+1, N):
        m[i][k] = a[i][k] / a[k][k]
        for j in range(k+1, N):
            a[i][j] = a[i][j]- m[i][j] * a[j][k]
        b[i] = b[i] - m[i][k] * b[i]