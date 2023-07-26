# 740. Eliminar y Ganar

## Medio

Se le da una matriz de enteros `nums`. Desea maximizar la cantidad de puntos que obtiene realizando la siguiente operación cualquier cantidad de veces:

- Elige cualquier `nums[i]` y bórralo para ganar puntos `nums[i]`. Luego, debe eliminar **todos** elementos iguales a `nums[i] - 1` y **todos** elementos iguales a `nums[i] + 1`.

Devuelve *la* ***cantidad máxima de puntos*** *que puedes ganar aplicando la operación anterior varias veces*.

**Ejemplo 1:**
<pre><strong>Entrada:</strong> números = [3,4,2]
<strong>Salida:</strong> 6
    <strong>Explicación:</strong> Puede realizar las siguientes operaciones:
- Eliminar 4 para ganar 4 puntos. En consecuencia, también se suprime 3. números = [2].
- Eliminar 2 para ganar 2 puntos. números = [].
Ganas un total de 6 puntos.
</pre>

**Ejemplo 2:**
<pre><strong>Entrada:</strong> números = [2,2,3,3,3,4]
<strong>Salida:</strong> 9
    <strong>Explicación:</strong> Puede realizar las siguientes operaciones:
- Eliminar un 3 para ganar 3 puntos. Todos los 2 y 4 también se eliminan. números = [3,3].
- Elimina un 3 nuevamente para ganar 3 puntos. números = [3].
- Elimina un 3 una vez más para ganar 3 puntos. números = [].
Ganas un total de 9 puntos.
</pre>

**Restricciones:**
- <code>1 <= números.longitud <= 2 * 10<sup>4</sup></code>
- <code>1 <= números[i] <= 10<sup>4</sup></code>
