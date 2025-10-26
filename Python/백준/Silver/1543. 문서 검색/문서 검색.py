import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
text = input().rstrip()
goal = input().rstrip()

print(text.count(goal))
