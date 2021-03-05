
f = @(a,b,c, da, db, dc, x) ((a+da) .* exp(x) + (b+db) .* x.^(3/4)).^2 + (c+dc) .* cos(x).^2;
F = dlmread('data.txt');
figure;
[~,ind] = sort(F(:,1));
F = F(ind, :);
plot(F(:,1), F(:,2)); hold on;

N = length(F);
objfun = @(p,d,x,y) sum( (f(p(1), p(2), p(3), d(:,1), d(:,2), d(:,3), x) - y).^2 )/N;
x = F(:,1); y = F(:,2);
d = (rand(N,3) - 0.5) / 500;

options = optimset('TolFun', 1e-8, 'TolX', 1e-8, 'MaxIter', 10^5);
pars = fminsearch(@(p) objfun(p,d,x,y), [2,10,100], options);

plot(F(:,1), f(pars(1), pars(2), pars(3), d(:,1), d(:,2), d(:,3), F(:,1)));
disp(pars);