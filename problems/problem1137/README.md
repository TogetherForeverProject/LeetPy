# 1137. N-th Tribonacci Number

## Easy

The Tribonacci sequence T<sub>n</sub> is defined as follows:

T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n &gt;= 0.

Given `n`, return the value of T<sub>n</sub>.

**Example 1:**
<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

**Example 2:**
<pre><strong>Input:</strong> n = 25
<strong>Output:</strong> 1389537
</pre>

**Constraints:**
- `0 <= n <= 37`
- The answer is guaranteed to fit within a 32-bit integer, ie. `answer <= 2^31 - 1`.