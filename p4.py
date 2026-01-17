import subprocess
import time
import sys
p = subprocess.Popen(['./problem4'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# 发送第一次输入（任意字符串）
p.stdin.write("test\n")
p.stdin.flush()
time.sleep(0.1)
# 发送第二次输入（任意字符串）
p.stdin.write("test\n")
p.stdin.flush()
time.sleep(0.1)
# 发送关键输入：-1
p.stdin.write("-1\n")
p.stdin.flush()
output, error = p.communicate()
print(output)
if error:
    print("错误信息：", error)