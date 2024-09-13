original_str =input('enter the original string');
rotated_str =input('enter the roteted string');


temp_str= rotated_str + rotated_str;
#temp_str = rotated_str * 2

if temp_str.find(original_str)==-1:
    print(rotated_str,'is not rottated string')

else:
    print(rotated_str,' is a rotated string')