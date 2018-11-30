% 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
% 
% What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

% init
N = 20;
Nl = [1:N]';
pl = primes(N);

% find emax = argmax_i (2^i < N)
i = 1;
while(2^i<N)
    i = i+1;
end
emax = i-1;

% maximum exp for each primes
ml=zeros(N, numel(pl), emax);
for i=1:emax
    ml(:,:,i) = mod(Nl, pl.^i)<1;
end

% 
pel = max(sum(ml,3),[],1);
prod(pl.^pel)
