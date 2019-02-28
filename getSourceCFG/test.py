import os
import subprocess

# cmd = "clang -cc1 -analyze -analyzer-checker=debug.DumpCFG test.c -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk"
cmd = "../tool ../tests/traverse.c"
res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
result = res.stderr.readlines()
for i in result:
  print(str(i[:-1], encoding='utf8'))


# p = os.popen(cmd)
# x = p.read()
# print("---------------!!!!!!!!!!!!!")
# print (x)


