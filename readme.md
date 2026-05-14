# Introduzione

NumPy è una libreria Python che permette di lavorare in modo efficiente con array multidimensionali e operazioni matematiche ad alte prestazioni. Per questo task è richiesto di implementare alcune funzioni utilizzando la libreria NumPy.

# Istruzioni

- Esegui il fork di questo progetto e assicurati che il tuo repository sia pubblico. Quindi, importa il progetto nel tuo IDE (es. PyCharm).
- Non puoi cambiare la firma delle funzioni fornite (nel file `task.py`) né rinominarle.
- Non puoi interagire con i tuoi colleghi: lavora individualmente e fai del tuo meglio.
- Le funzionalità da implementare sono descritte tramite un insieme di sub-task.
- Implementa le funzioni una alla volta, seguendo rigorosamente l’ordine fornito dai sub-task. Non leggere in anticipo le sub-task successive.
- Un sub-task può considerarsi completato quando sei sicuro che la funzionalità richiesta sia stata implementata correttamente.
- Ogni volta che completi un sub-task, esegui il commit e il push del codice.
- Al termine del compito, assicurati di aver eseguito il push di tutto il progetto sul repository.

# Sub-task

Ricordati di leggere e implementare i sub-task uno alla volta, seguendo l’ordine fornito. Non passare al sub-task successivo finché quello corrente non è stato completato. Implementa le funzionalità richieste lavorando nel file `task.py`.

---

## Sub-task 1 – Prodotto Scalare

Il prodotto scalare è un’operazione tra due vettori che restituisce un numero reale ottenuto sommando i prodotti delle componenti corrispondenti dei vettori.

### Requisito

Implementa la funzione:

```python
prodotto_scalare(v1: list, v2: list) -> float
````

Questa funzione riceve due liste di numeri e restituisce il prodotto scalare come float.

### Esempi

```python id="ps1"
Input: v1 = [1, 2, 3], v2 = [4, 5, 6]
Output: 32.0
```

```python id="ps2"
Input: v1 = [1, 0], v2 = [0, 1]
Output: 0.0
```

```python id="ps3"
Input: v1 = [-1, -2], v2 = [2, 3]
Output: -8.0
```

---

## Sub-task 2 – Operazioni Elemento per Elemento

Le operazioni elemento per elemento (element-wise) sono operazioni in cui una funzione viene applicata separatamente a ciascun elemento di una struttura dati (come un array o una matrice), producendo un risultato della stessa forma.

### Requisito

Implementa la funzione:

```python
operazioni_elemento_per_elemento(v1: list, v2: list) -> tuple
```

Questa funzione riceve in input due liste di numeri della stessa lunghezza e restituisce una tupla contenente quattro array NumPy: somma, differenza, prodotto e divisione.

Ogni array contiene il risultato dell’operazione corrispondente applicata elemento per elemento alle due liste, rispettando l’ordine degli elementi.

### Esempi

```python id="oe1"
Input: v1 = [1, 2, 3], v2 = [4, 5, 6]
Output: (
    array([5, 7, 9]),
    array([-3, -3, -3]),
    array([4, 10, 18]),
    array([0.25, 0.4, 0.5])
)
```

```python id="oe2"
Input: v1 = [10, 20], v2 = [2, 5]
Output: (
    array([12, 25]),
    array([8, 15]),
    array([20, 100]),
    array([5.0, 4.0])
)
```

```python id="oe3"
Input: v1 = [0, 0], v2 = [1, 1]
Output: (
    array([1, 1]),
    array([-1, -1]),
    array([0, 0]),
    array([0., 0.])
)
```

---

## Sub-task 3 – Prodotto Matriciale

Il prodotto matriciale di due matrici calcola una nuova matrice dove ogni elemento in posizione `(i, j)` è il prodotto scalare della i-esima riga della prima matrice per la j-esima colonna della seconda matrice.

### Requisito

Implementa la funzione:

```python
prodotto_matriciale(m1: list, m2: list) -> np.ndarray
```

Questa funzione riceve due liste di liste (rappresentanti matrici bidimensionali) e restituisce il prodotto matriciale come array NumPy.

### Esempi

```python id="pm1"
Input: m1 = [[1, 2], [3, 4]], m2 = [[5, 6], [7, 8]]
Output: array([[19, 22], [43, 50]])
```

```python id="pm2"
Input: m1 = [[1, 0], [0, 1]], m2 = [[2, 3], [4, 5]]
Output: array([[2, 3], [4, 5]])
```

```python id="pm3"
Input: m1 = [[2, 0], [1, 2]], m2 = [[1, -1], [0, 1]]
Output: array([[2, -2], [1, 1]])
```

---

## Sub-task 4 – Risolvere un Sistema Lineare

Un sistema di equazioni lineari del tipo `Ax = b` consiste in una matrice dei coefficienti `A`, un vettore dei termini noti `b` e un vettore incognito `x` di cui vogliamo calcolare i valori.

### Requisito

Implementa la funzione:

```python
risolvi_sistema_lineare(A: list, b: list) -> np.ndarray
```

Questa funzione riceve la matrice quadrata dei coefficienti `A` (come lista di liste) e il vettore dei termini noti `b` (come lista), e restituisce il vettore soluzione `x` come array NumPy.

### Esempi

```python id="rsl1"
Input: A = [[2, 1], [1, 3]], b = [5, 7]
Output: array([1.6, 1.8])
```

```python id="rsl2"
Input: A = [[1, 0], [0, 1]], b = [3, 4]
Output: array([3., 4.])
```

```python id="rsl3"
Input: A = [[3, 1], [1, 2]], b = [9, 8]
Output: array([2., 3.])
```

---

## Sub-task 5 – Correlazione tra Matrici 2x2

La correlazione statistica (nello specifico, il coefficiente di Pearson) misura il grado di dipendenza lineare tra due insiemi di dati.

Quando abbiamo due matrici di dimensione identica (come due matrici 2x2), possiamo valutarne la correlazione appiattendo i loro valori (flattening) e trattandoli come due array lineari.

### Requisito

Implementa la funzione:

```python
correlazione_matrici(m1: list, m2: list) -> float
```

Questa funzione riceve due matrici 2x2 (sotto forma di liste di liste) e restituisce il coefficiente di correlazione di Pearson (un numero float compreso tra `-1.0` e `1.0`) calcolato tra i valori “appiattiti” (sequenziali) delle due matrici.

### Esempi

```python id="cm1"
Input: m1 = [[1, 2], [3, 4]], m2 = [[2, 4], [6, 8]]
Output: 1.0  # Perfetta correlazione positiva
```

```python id="cm2"
Input: m1 = [[1, 2], [3, 4]], m2 = [[4, 3], [2, 1]]
Output: -1.0  # Perfetta correlazione negativa
```
