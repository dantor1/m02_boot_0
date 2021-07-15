def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0 # para que no pegue el cascotazo con el None

print(sumatorio(4))