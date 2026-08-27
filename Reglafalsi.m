function Reglafalsi(f,a,b,es,maxit)
% bm(@(x) 3*x-cos(x)-1,0,1,100,.000001)
%graph
figure;
hold on;
grid on;
fplot(0,'--k')
fplot(f,'LineWidth',2)
xlim([a,b])
xlabel('X axis')
ylabel('Y axis')
title('Root finding using regula Falsi')

%function
if f(a) * f(b) > 0
    disp('Not possible')
    return;
end

fprintf('\n#    a   b   f(a)    f(b)    c   f(c)    er\n');

%veriable
count = 0;
c = (a* f(b) - b * f(a) )/( f(b) - f(a)) ;
cold  = c;
er = inf;
erplot = zerss(1,maxit);

while abs(er) > es && count < maxit

    count = count + 1;
    cold = c;
    c = (a* f(b) - b * f(a) )/( f(b) - f(a)) ;
    fc =f(c);
    plot(c,f(c),'LineWidth',2);

    if count >0
        er= abs((c-cold)/c);
    end
    erplot(count) =er;

    fprintf('\n%d    %f   %f   %f    %f    %f   %f    %f\n',count,a,b,f(a),f(b),c,f(c),er);

    product  =f(a) * f(c);

    if product == 0
        er= 0
    elseif product>0
        a=c;
    else
        b=c;
    end
end

figure;
hold on;
grid on;
fplot(0,'--k')
xlabel('X axis')
ylabel('Y axis')
title('Relative error')
plot(erplot(1:count),'LineWidth',2)

fprintf('\nThe approxiamte root is =%f\n',c)



end