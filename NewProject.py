import os
import sys
para = sys.argv[1]

with open("README.md", "r") as f:
    for i in f:
        if para in i:
            i = i.split("|")[1].split("](https://leetcode.cn/problems/")
            i1, i2 = i[0].replace("[", ""), i[1].replace("/)", "")
            
            os.system(f"vim {i1}.{i2}.py")
            os.system(f"sh SUMBIT.sh {i1}.{i2}.py")
#