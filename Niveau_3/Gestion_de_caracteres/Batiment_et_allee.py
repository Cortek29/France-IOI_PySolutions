import sys
sys.stdout.write(''.join([str(ord(sys.stdin.readline().replace('\n', '')[0]) - 64), chr(int(sys.stdin.readline().replace('\n', ''))+64)]))