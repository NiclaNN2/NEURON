temps=[0:500]';
positions=[2:200];
t=length(temps);
l=length(positions);
data=zeros(t,l);
data(:,1)=[0:500];

for x = 2:l
    for u = 1:t
        if(mod(x,100)==0 && mod(u,50)==0)
           disp(x)
           disp(u)
        end
        data(u,x)=50*exp(-((x-l/2)/(l/4))^2)*exp(-((u-t/2)/(t/4))^2);
    end
end

