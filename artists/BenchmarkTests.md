Benchmark Tests
---------------

###Data Table

Test Name | Test 1 | Test 2 | Test 3 | Test 4 |
--------- | ------ | ------ | ------ | ------ |
Requests | 1000 | 1000 | 2000 | 2000 |
Concurrent | 100 | 10 | 100 | 10 |
TT (s) | 4.089 | 4.109 | 8.646 | 8.724 |
TPR (ms) | 4.089 | 4.109 | 4.323 | 4.362 |
Failed Requests | 0 | 0 | 0 | 0 |
Completed Requests | 1000 | 1000 | 2000 | 2000 |

*TT = Total Time, TPR = Time Per Request, s = seconds, ms = miliseconds

###Test 1

>**Parameters:**
 - Requests: 1000
 - Concurrency: 100

>**Results:**
 - Server Software:        Werkzeug/0.9.6
 - Server Hostname:        localhost
 - Server Port:            5000

 > - Document Path:          /artists/
 - Document Length:        19 bytes

 > - Concurrency Level:      100
 - Time taken for tests:   4.089 seconds
 - Complete requests:      1000
 - Failed requests:        0
 - Total transferred:      164000 bytes
 - HTML transferred:       19000 bytes
 - Requests per second:    244.57 [#/sec] (mean)
 - Time per request:       408.877 [ms] (mean)
 - Time per request:       4.089 [ms] (mean, across all concurrent requests)
 - Transfer rate:          39.17 [Kbytes/sec] received

> - Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   3.1      0      11
Processing:     8  388  71.9    407     423
Waiting:        2  387  71.9    407     422
Total:         13  389  69.2    407     423

> - Percentage of the requests served within a certain time (ms)
 - 50%    407
 - 66%    408
 - 75%    409
 - 80%    409
 - 90%    419
 - 95%    421
 - 98%    422
 - 99%    422
 - 100%    423 (longest request)

###Test 2

>**Parameters:**
 - Requests: 1000
 - Concurrency: 10

>**Results:**
 - Server Software:        Werkzeug/0.9.6
 - Server Hostname:        localhost
 - Server Port:            5000

 > - Document Path:          /artists/
 - Document Length:        19 bytes

 > - Concurrency Level:      10
 - Time taken for tests:   4.109 seconds
 - Complete requests:      1000
 - Failed requests:        0
 - Total transferred:      164000 bytes
 - HTML transferred:       19000 bytes
 - Requests per second:    243.37 [#/sec] (mean)
 - Time per request:       41.090 [ms] (mean)
 - Time per request:       4.109 [ms] (mean, across all concurrent requests)
 - Transfer rate:          38.98 [Kbytes/sec] received

> - Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4   41   2.8     40      59
Waiting:        4   41   2.8     40      59
Total:          4   41   2.8     40      59

> - Percentage of the requests served within a certain time (ms)
 - 50%     40
 - 66%     41
 - 75%     41
 - 80%     42
 - 90%     42
 - 95%     44
 - 98%     46
 - 99%     57
 - 100%     59 (longest request)

###Test 3

>**Parameters:**
 - Requests: 2000
 - Concurrency: 100

>**Results:**
 - Server Software:        Werkzeug/0.9.6
 - Server Hostname:        localhost
 - Server Port:            5000

> - Document Path:          /artists/
 - Document Length:        19 bytes

> - Concurrency Level:      100
 - Time taken for tests:   8.646 seconds
 - Complete requests:      2000
 - Failed requests:        0
 - Total transferred:      328000 bytes
 - HTML transferred:       38000 bytes
 - Requests per second:    231.31 [#/sec] (mean)
 - Time per request:       432.314 [ms] (mean)
 - Time per request:       4.323 [ms] (mean, across all concurrent requests)
 - Transfer rate:          37.05 [Kbytes/sec] received

> - Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       2
Processing:    12  422  60.7    422     538
Waiting:       12  422  60.7    422     538
Total:         14  422  60.4    422     538

> - Percentage of the requests served within a certain time (ms)
 - 50%    422
 - 66%    426
 - 75%    440
 - 80%    447
 - 90%    466
 - 95%    494
 - 98%    530
 - 99%    534
 - 100%    538 (longest request)

###Test 4

>**Paramaters:**
 - Requests: 2000
 - Concurrency: 10

>**Results:**
 - Server Software:        Werkzeug/0.9.6
 - Server Hostname:        localhost
 - Server Port:            5000

> - Document Path:          /artists/
 - Document Length:        19 bytes

> - Concurrency Level:      10
 - Time taken for tests:   8.724 seconds
 - Complete requests:      2000
 - Failed requests:        0
 - Total transferred:      328000 bytes
 - HTML transferred:       38000 bytes
 - Requests per second:    229.25 [#/sec] (mean)
 - Time per request:       43.621 [ms] (mean)
 - Time per request:       4.362 [ms] (mean, across all concurrent requests)
 - Transfer rate:          36.72 [Kbytes/sec] received

> - Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    15   43   6.9     41     110
Waiting:       15   43   6.9     41     109
Total:         15   43   6.9     41     110

> - Percentage of the requests served within a certain time (ms)
 - 50%     41
 - 66%     42
 - 75%     43
 - 80%     44
 - 90%     49
 - 95%     57
 - 98%     65
 - 99%     78
 - 100%    110 (longest request)