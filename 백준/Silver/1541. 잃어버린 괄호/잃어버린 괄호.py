import sys

# A-(B+C+D) 형태가 최소값이 나옴

expressions = sys.stdin.readline().strip()

parts = expressions.split('-')

result = sum(map(int, parts[0].split('+')))
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

print(result)