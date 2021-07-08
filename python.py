"""
# 1152. 단어의 개수
    - split() : 공백을 기준으로 분할. 리스트로 저장됨
    ex) words = "hello world : 헬로우 월드"
        words.split() = ["hello", "world", ":", "헬로우", "월드"]

# 1929. 소수 구하기
    - 에라토스테네스의 체 : 자연수 n까지 소수 구하는 방법
                        최소 소수인 2부터 sqrt(n)까지 확인하면서
                        소수인 경우(True), 본인보다 큰 (본인을 제외) 본인의 배수를 모두 False로 바꿔줌

# 1920. 수 찾기
    - 이진탐색 이용 : 값을 비교할 때마다 찾는 값이 있을 범위를 절반씩 좁히면서 탐색
                    계산 복잡도는 O(logn)
                    반드시 자료를 정렬 후에
        * input() 보다 sys.stdin.readlint()이 빠르다

# 2109. 통계학 중 최빈값
    - counter 모듈 사용 : 리스트 원소들의 개수가 알고 싶을 때
    ex) Counter('hello world').most_common()
        -> [('l', 3), ('0', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

        * most_common 매서드는 데이터의 개수가 많은 순으로 정렬된 배열을 리턴

"""

