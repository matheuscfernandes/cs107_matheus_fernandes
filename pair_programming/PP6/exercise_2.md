
f(x, y) = [x^2 + y^2, exp(x+y)]

| var|  func   | Current |   Deriv           | \partial x | \partial y |
|----|---------|---------| ----------------- | ---------- |----------- |
| x  | 1       | 1       | \dot{x}           | (1)        | (0)        |
| y  | 1       | 1       | \dot{y}           | (0)        | (1)        |
| v1 | x^2     | 1       | 2\dot{x}x         |  2         |  0         |
| v2 | y^2     | 1       | 2\dot{y}y         |  0         |  2         |
| f1 | v1+v2   | 2       | \dot{v1}+dot{v2}  |  2         |  2         |
| v3 | x+y     | 2       | \dot{x}+\dot{y}   |  1         |  1         |
| f2 | exp(v3) | 7.389   | \dot{v3}exp(v3)   |  2.718282  | 2.718282   |

