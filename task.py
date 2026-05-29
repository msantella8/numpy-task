import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    """Sub-task 1: Prodotto Scalare."""
    v1=np.array(v1)
    v2=np.array(v2)
    p=np.inner(v1,v2)
    return p

    pass

def rango_matrice(m: list) -> int:
    """Sub-task 2: Calcola il rango di una matrice."""
    m=np.array(m)
    r=np.linalg.matrix_rank(m)
    return r
    pass

def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    """Sub-task 3: Risolvere un Sistema Lineare."""
    A=np.array(A)
    b=np.array(b)
    x=np.linalg.solve(A,b)
    return x
    pass

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""
    m1=np.array(m1)
    m2=np.array(m2)
    mf1=m1.flatten()
    mf2=m2.flatten()
    cm=np.corrcoef(mf1,mf2)
    return cm

    pass

def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    pass


def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[4, 3], [2, 1]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()
