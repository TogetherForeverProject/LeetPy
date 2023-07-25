# 746. Costo mínimo para subir escaleras

## Fácil

Se le proporciona una matriz de enteros 'costo', donde 'costo[i]' es el costo del <código>i<sup>ésimo</sup></código> paso en una escalera. Una vez que pague el costo, puede subir uno o dos escalones.

Puede comenzar desde el paso con el índice `0` o el paso con el índice `1`.

Retorno *el costo mínimo para llegar a la parte superior del piso*.

**Ejemplo 1:**
<pre><strong>Entrada:</strong> costo = [10, 15, 20]
<fuerte>Salida:</fuerte> 15
<strong>Explicación:</strong> Comenzará en el índice 1.
- Paga 15 y sube dos escalones para llegar a la cima.
El costo total es de 15.
</pre>

**Ejemplo 2:**
<pre><strong>Entrada:</strong> costo = [1,100,1,1,1,100,1,1,100,1]
<strong>Salida:</strong> 6
<strong>Explicación:</strong> Comenzará en el índice 0.
- Paga 1 y sube dos escalones para llegar al índice 2.
- Paga 1 y sube dos escalones para llegar al índice 4.
- Paga 1 y sube dos escalones para llegar al índice 6.
- Paga 1 y sube un escalón para alcanzar el índice 7.
- Paga 1 y sube dos escalones para llegar al índice 9.
- Paga 1 y sube un escalón para llegar a la cima.
El costo total es de 6.
</pre>

**Restricciones:**
- `2 <= costo.longitud <= 1000`
- `0 <= costo[i] <= 999`
