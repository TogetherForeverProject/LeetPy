# 1137. N-ésimo número de Tribonacci

## Fácil

La secuencia de Tribonacci T<sub>n</sub> se define de la siguiente manera:

T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1 y T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> para n >= 0.

Dado `n`, devuelve el valor de T<sub>n</sub>.

**Ejemplo 1:**
<pre><strong>Entrada:</strong> n = 4
<strong>Salida:</strong> 4
<strong>Explicación:</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

**Ejemplo 2:**
<pre><strong>Entrada:</strong> n = 25
<strong>Salida:</strong> 1389537
</pre>

**Restricciones:**
- `0 <= n <= 37`
- Se garantiza que la respuesta se ajuste a un número entero de 32 bits, es decir. `respuesta <= 2^31 - 1`.
