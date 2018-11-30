f = [1 2];

while true 
    fn = sum(f(end-1:end));
    if fn <  4000000
        f = [f fn];
    else
        break;
    end
end

sum(f.*(not(mod(f,2))))