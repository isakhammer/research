import matplotlib.pyplot as plt
import numpy as np

# Probability of coin 1
p_1=0.5
# Probability head coin 1
ph_1=0.5
# Probability head coin 2
ph_2=1

#
# Analytical calculation
print('Analytical results')
# P(1|h)= P(1,h)/p(h)=p(1,h) / \sum_i p(i)*p(h|i)
p1_given_h= (1-p_1)*ph_2/(p_1*ph_1+(1-p_1)*ph_2)
print(p1_given_h)
# P(1|h,h)= P(1,h,h)/p(h,h)=p(1,h,h) / \sum_i p(i)*p(h,h|i)
p1_given_hh=(1-p_1)*ph_2*ph_2/(p_1*ph_1*ph_1+(1-p_1)*ph_2*ph_2)
print(p1_given_hh)

# Simulate
N=100
# Initialize coin selected {0,1}
coin=np.zeros((N,1))
# Initialize result of tosses {0,1}
res=np.zeros((N,2))

for b in range(1,N):
   # Draw coin at random
   uu=np.random.uniform(0,1)
   if uu<p_1:
       # unbiased
 
      # Draw result toss 1
       u1=np.random.uniform(0,1)
       if u1<ph_1:
           res[b-1,0]=1
 
       # Draw result toss 2
       u2=np.random.uniform(0,1)
       if u2<ph_1:
           res[b-1,1]=1

   if uu>p_1:
       # biased
       coin[b-1]=1;
       # Draw result toss 1
       u1=np.random.uniform(0,1)
       if u1<ph_2:
           res[b-1,0]=1
        
       # Draw result toss 2
       u2=np.random.uniform(0,1)
       if u2<ph_2:
           res[b-1,1]=1



plt.clf;
plt.plot(np.linspace(0,N-1,N),res.sum(axis=1))
plt.hold
# plot only unbiased coin
fcoin1=np.where(coin==0)
res1=res[fcoin1,:]
plt.plot(fcoin1,res1.sum(axis=2),'ro')
plt.ylabel('Number of heads in two tosses')
plt.xlabel('Realization')
plt.show()
print('Simulation results')

rr0=res[:,0]
indH=np.where(rr0==1);
ind1_given_H=np.where(coin[indH]==1);
p1_h_sim=np.size(ind1_given_H,axis=1)/np.size(indH,axis=1)
print(p1_h_sim)

rrsum=res.sum(axis=1)
indHH=np.where(rrsum==2);
ind1_given_HH=np.where(coin[indHH]==1);
p1_hh_sim=np.size(ind1_given_HH,axis=1)/np.size(indHH,axis=1)
print(p1_hh_sim)
