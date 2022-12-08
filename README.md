# hungarian algorithm

### Description
* a python numpy implementation of hungarian algorithm (also known as Kuhn–Munkres algorithm).
* Rectangular matrix is supported. 
* 0.153 second when |X|=100 and |Y|=100,000 on my Mac.
    
### Example

```
matcher = KMMatcher([
    [2., 3., 0., 3.],
    [0., 4., 4., 0.],
    [5., 6., 0., 0.],
    [0., 0., 7., 0.]
])
matcher.solve(verbose=True)
```

result:
```
match 0 to 3, weight 3.0000
match 1 to 1, weight 4.0000
match 2 to 0, weight 5.0000
match 3 to 2, weight 7.0000
ans: 19.0000
```

or using default setting

```
weights = np.random.randn(n, m)
matcher = KMMatcher(weights)
best, all_matches, _ = matcher.solve()
```

### Performance
(only tested on my Mac)

```
N = |X|
M = |Y|
```

| N | M | time(seconds) |
| :----: | :----: | :----: |
|10|100,000|0.017|
|10|1,000,000|0.250|
| 100 | 10,000 | 0.026 |
| 100 | 100,000 | 0.153 |
| 100 | 1,000,000 | 2.004 |
|1,000| 1,000| 1.634|





### Reference
[topcoder c++ implementation](https://www.topcoder.com/community/competitive-programming/tutorials/assignment-problem-and-hungarian-algorithm/)


 


