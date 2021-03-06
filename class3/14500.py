# 테트로미노

import sys

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0

tetromino = [
    # 1자
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    # ㅁ자
    [(0, 0), (0, 1), (1, 0), (1, 1)],

    # ㄴ자
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],

    # ㄹ자
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],

    # ㅗ자
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)]
]

for r in range(N):
    for c in range(M):
        for tetro in tetromino:
            mid_sum = 0
            for i in range(len(tetro)):
                nr = r + tetro[i][0]
                nc = c + tetro[i][1]
            # for dx, dy in tetro:
            #     nr = r + dx
            #     nc = c + dy
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    break
                mid_sum += board[nr][nc]

            result = max(result, mid_sum)

print(result)
