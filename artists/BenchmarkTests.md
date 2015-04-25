 Test Name      | Test 1 | Test 2 | Test 3 | Test 4 |
------ | ------ | ------ | ------ | ------ |
Requests | 1000 | 1000 | 2000 | 2000 |
Concurrency | 100 | 10 | 100 | 10 |
TT (s) | 122.648 | 123.365 | 247.267 | 243.099 | 
TPR (ms) | 122.684 | 123.365 | 123.633 | 121.549 |
Failed | 0 | 0 | 0 | 0 |
Completed | 1000 | 1000 | 2000 | 2000 |

*TT = Total Time, TPR = Time Per Request

###Test 1

**Parameters**
>Requests: 1000
Concurrency: 100

**Results**
>Server Software: Werkzeug/0.9.6
Server Hostname:localhost
Server Port:5000

>Document Path:          /artists/
Document Length:        42300 bytes

>Concurrency Level:      100
Time taken for tests:   122.684 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      42448000 bytes
HTML transferred:       42300000 bytes
Requests per second:    8.15 [#/sec] (mean)
Time per request:       12268.378 [ms] (mean)
Time per request:       122.684 [ms] (mean, across all concurrent requests)
Transfer rate:          337.89 [Kbytes/sec] received

>Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   3.2      0      11
Processing:   132 11667 2134.6  12240   12498
Waiting:      123 11666 2134.7  12239   12498
Total:        135 11668 2131.9  12240   12498

>Percentage of the requests served within a certain time (ms)
  50%  12240
  66%  12254
  75%  12268
  80%  12293
  90%  12431
  95%  12447
  98%  12470
  99%  12480
 100%  12498 (longest request)

###Test 2

**Parameters**
>Requests: 1000 
Concurrency: 10

**Results**
>Server Software:        Werkzeug/0.9.6
Server Hostname:        localhost
Server Port:            5000

>Document Path:          /artists/
Document Length:        42300 bytes

>Concurrency Level:      10
Time taken for tests:   123.365 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      42448000 bytes
HTML transferred:       42300000 bytes
Requests per second:    8.11 [#/sec] (mean)
Time per request:       1233.647 [ms] (mean)
Time per request:       123.365 [ms] (mean, across all concurrent requests)
Transfer rate:          336.02 [Kbytes/sec] received

>Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:   134 1228  72.6   1222    1446
Waiting:      133 1228  72.6   1222    1446
Total:        134 1228  72.6   1222    1446

>Percentage of the requests served within a certain time (ms)
  50%   1222
  66%   1227
  75%   1231
  80%   1236
  90%   1275
  95%   1314
  98%   1340
  99%   1370
 100%   1446 (longest request)

###Test 3

**Parameters**
>Requests: 2000 
Concurrency: 100

**Results**
>Server Software:        Werkzeug/0.9.6
Server Hostname:        localhost
Server Port:            5000

>Document Path:          /artists/
Document Length:        42300 bytes

>Concurrency Level:      100
Time taken for tests:   247.267 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      84896000 bytes
HTML transferred:       84600000 bytes
Requests per second:    8.09 [#/sec] (mean)
Time per request:       12363.343 [ms] (mean)
Time per request:       123.633 [ms] (mean, across all concurrent requests)
Transfer rate:          335.29 [Kbytes/sec] received

>Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    4  63.0      0     997
Processing:  4930 12060 805.7  12114   15974
Waiting:     4929 12060 805.7  12114   15974
Total:       4934 12064 824.5  12114   16928

>Percentage of the requests served within a certain time (ms)
  50%  12114
  66%  12121
  75%  12126
  80%  12132
  90%  12154
  95%  12242
  98%  12271
  99%  14618
 100%  16928 (longest request)

###Test 4

**Parameters**
>Requests: 2000 
Concurrency: 10

>Server Software:        Werkzeug/0.9.6
Server Hostname:        localhost
Server Port:            5000

>Document Path:          /artists/
Document Length:        42300 bytes

>Concurrency Level:      10
Time taken for tests:   243.099 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      84896000 bytes
HTML transferred:       84600000 bytes
Requests per second:    8.23 [#/sec] (mean)
Time per request:       1215.493 [ms] (mean)
Time per request:       121.549 [ms] (mean, across all concurrent requests)
Transfer rate:          341.04 [Kbytes/sec] received

>Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:   148 1213  44.7   1214    1253
Waiting:      148 1212  44.7   1214    1252
Total:        148 1213  44.7   1214    1253

>Percentage of the requests served within a certain time (ms)
  50%   1214
  66%   1217
  75%   1219
  80%   1220
  90%   1224
  95%   1229
  98%   1235
  99%   1238
 100%   1253 (longest request)
