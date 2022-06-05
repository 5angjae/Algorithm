# `input()` vs `sys.stdin.readline()`

> 백준 풀이를 보다보면 시간초과가 나는 경우 input()을 사용하는 것이 아니라, sys 모듈의 sys.stdin.readline()을 사용해 시간초과를 해결하는 경우가 많다. 단순히 시간을 줄이기 위해 sys.stdin.readline() 을 사용해도 되지만 이유를 알고 사용하는 것과 이유를 모르고 사용하는 것에는 차이가 있기 때문에 그 이유를 알아보려고 한다.

## python 2.x

python 2.x 버전에서는 입력을 받기 위한 함수로 `input()`과 `raw_input()`을 사용했다.

`raw_input()`은 입력값을 무조건 문자열로 받는 반면에, `input()`은 입력으로 들어온 값을 evaluate 해서 그 값에 맞는 자료형으로 초기화하는 과정을 거친다. 즉, 이 과정을 거치는 `input()`은 `raw_input()`에 비해 상대적으로 느리다.



## python 3.x

`raw_input()`함수가 사라지면서 `input()`이 그 역할을 하게 되었다.

따라서 input()도 결과적으로 입력값을 문자열로 받게 되었다.



## 차이점

input() 내장 함수는 parameter로 prompt 메세지를 받을 수 있다.

하지만 sys.stdin.readline()은 prompt 메세지를 인수로 받지 않는다.



input() 함수는 입력 받은 값의 개행 문자를 삭제시켜서 리턴한다.

반면에 sys.stdin.readline()은 개행 문자를 포함한 값을 리턴한다. 대신 귀찮은 점이 있다.



이 두가지 차이에 의해 input()이 sys.stdin.readline()에 비교해서 느리다.



