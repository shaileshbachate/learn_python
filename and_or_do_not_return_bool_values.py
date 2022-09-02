
print(0 or '' or [])            # []
print(1 or 'shail' or [2, 3])   # 1
print(0 or {10} or [])          # {10}

print(0 and '' and [])          # 0
print(1 and 'shail' and [2, 3]) # [2, 3]
print(1 and {} and [])          # {}
print("------------------------------------------------------------------------")

def use_of_this_feature(arg=None):
    arg = arg or []
    arg.append(4)
    print(arg)

use_of_this_feature()
use_of_this_feature()
use_of_this_feature([67, 78])
