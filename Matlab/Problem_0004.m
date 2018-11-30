a=[100:999];
A = a'*a;
B = num2str(A(:));
max(str2num(B).*not(str2num(B)-str2num(fliplr(B))))
