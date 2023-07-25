# 509. Número de Fibonacci

## Fácil

Los **números de Fibonacci**, comúnmente denotados `F(n)` forman una secuencia, llamada **secuencia de Fibonacci**, tal que cada número es la suma de
los dos anteriores, partiendo de `0` y `1`. Eso es,

<pre>F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), para n > 1.
</pre>

Dado `n`, calcula `F(n)`.

**Ejemplo 1:**
<pre><strong>Entrada:</strong> n = 2
<strong>Salida:</strong> 1
<strong>Explicación:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

**Ejemplo 2:**
<pre><strong>Entrada:</strong> n = 3
<strong>Salida:</strong> 2
<strong>Explicación:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

**Ejemplo 3:**
<pre><strong>Entrada:</strong> n = 4
<strong>Salida:</strong> 3
<strong>Explicación:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

**Restricciones:**
- `0 <= n <= 30`
