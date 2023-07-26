# 198. Ladrón de casas

## Medio

Eres un ladrón profesional que planea robar casas a lo largo de una calle. Cada casa tiene una cierta cantidad de dinero escondido, la única restricción que te impide robar en cada una de ellas es que las casas adyacentes tienen sistemas de seguridad conectados y **se comunicará automáticamente con la policía si dos casas adyacentes fueron asaltadas en la misma noche**.

Dada una matriz de enteros `nums` que representa la cantidad de dinero de cada casa, devuelva *la cantidad máxima de dinero que puede robar esta noche* ***sin alertar a la policía***.

**Ejemplo 1:**
<pre><strong>Entrada:</strong> números = [1,2,3,1]
<strong>Salida:</strong> 4
<strong>Explicación:</strong> Roba la casa 1 (dinero = 1) y luego roba la casa 3 (dinero = 3).
Monto total que puedes robar = 1 + 3 = 4.
</pre>

**Ejemplo 2:**
<pre><strong>Entrada:</strong> números = [2,7,9,3,1]
<strong>Salida:</strong> 12
<strong>Explicación:</strong> Robar casa 1 (dinero = 2), robar casa 3 (dinero = 9) y robar casa 5 (dinero = 1).
Monto total que puedes robar = 2 + 9 + 1 = 12.
</pre>

**Restricciones:**
- `1 <= números.longitud <= 100`
- `0 <= números[i] <= 400`
