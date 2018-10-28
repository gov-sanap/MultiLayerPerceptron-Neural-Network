import numpy as np
d=np.array([[ 1, -1, -1, -1, -1, -1, -1, -1, -1, -1],[-1,  1, -1, -1, -1, -1, -1, -1, -1, -1],[-1, -1,  1, -1, -1, -1, -1, -1, -1, -1],[-1, -1, -1,  1, -1, -1, -1, -1, -1, -1],[-1, -1, -1, -1,  1, -1, -1, -1, -1, -1],[-1, -1, -1, -1, -1,  1, -1, -1, -1, -1],[-1, -1, -1, -1, -1, -1,  1, -1, -1, -1],[-1, -1, -1, -1, -1, -1, -1,  1, -1, -1],[-1, -1, -1, -1, -1, -1, -1, -1,  1, -1],[-1, -1, -1, -1, -1, -1, -1, -1, -1,  1]])
#z=np.array([[0,0,-1],[0,1,-1],[1,0,-1],[1,1,-1]])
#d=np.array([[-1],[1],[1],[-1]])
z=np.array([[0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]])
n=len(z)#no.of input samples
zd=len(z[0])#each sample dimension after augmentaion
t=0#int(input("Activation Fuction as unipolar sigmoid for 1 or bipolar sigmoid for 0\n"))
l=1#denotes value of lambda
c=0.1 #denotes value of learning rate
#take number of neurons from user
hln=10#int(input("Enter the number of neurons in hidden layer\n"))
oln=10#int(input("Enter the number of neurons in output layer\n"))
def f(v,z,l,t):
    net=np.matmul(v,z)
    if t==1:
        return 1 / (1 +np.exp(-net*l))
    else:
        return (1 - np.exp(-net*l)) / (1 +np.exp(-net*l))
def fd(o,t):
    if t==1:
        return o*(1-o)
    else:
        return (1-o**2)
#weight matrix for hidden layer will be of dimension (hln,zd)
#v=np.array([[1,2,3],[4,5,6]])#
v=np.random.random_sample((hln,zd))
v1=v
#weight matrix for hidden layer will be of dimension (oln,zd)
#w=np.array([[1,2,3]])#
w=np.random.random_sample((oln,hln+1))
#w=np.array([[ 0.39933929,  5.23043882,  0.29221077,  0.33987578, -0.6926569 ,-0.62237485,  0.88028267, -0.81707466, -0.68353567,  0.77986604,0.76147989],[-1.47384553,  0.17859951,  0.74169433,  0.29193893,  5.14651031,-0.04968467,  0.95973368, -0.52794395, -0.43008701,  0.1355528 , 0.81295238], [-2.83535394, -1.03255464,  2.00129744,  2.23564332, -1.15097454,-1.24664518,  1.84712172, -0.71756542, -1.64382263,  2.29420174, 1.89156203], [-0.61197095, -2.26740224,  2.00834128,  2.99047445, -1.87921942,-2.47993575,  2.37524494, -1.11389203, -2.57172338,  2.74241635, 2.14333575],[-0.03897547, -0.68849816,  0.42808767,  0.43776319, -0.13298208,0.24655033,  0.186002  ,  5.36814933, -0.07881754,  0.2315233 ,0.0673626 ],[ 0.23986221,  0.54121596,  0.67484427,  0.4678964 ,  0.21679908,4.48412121,  0.70218668, -0.08557952,  4.5015835 ,  0.99747709,0.86478937],[-1.39105388, -0.1083682 ,  1.39914349,  1.52716924,  0.07657836,-4.56695801,  1.37957019, -0.17898731,  5.06905016,  0.89214922,1.53947565],[-1.06108445, -0.52059939,  2.10849458,  2.34037028, -0.45498401,5.03419659,  1.44693551, -1.82310783, -4.36600822,  1.45532654,1.90551882],[-2.04128937, -1.65682   ,  2.24217341,  2.10182545, -2.13472756,-2.84809328,  2.44153306, -0.32702698, -1.44281757,  2.29142773,1.98932771],[ 6.19990684, -1.24009089,  1.05875612,  0.26040642,  0.19191568, 0.23546456,  0.5370289 , -0.5070223 ,  1.0124442 ,  0.3005812 , 0.89898435]])

w1=w
Emax=0.01
tc=0
E=1
while E>Emax:
    tc=tc+1
    E=0
    for j in range(0,n):
        y=[]
        y=[f(v[i,:],z[j,:],l,t) for i in range(0,hln)]
        y.append(-1)
        o=[]
        o=[f(w[i,:],y,l,t) for i in range(0,oln)]
        E=E+0.5*np.sum([(d[j,i]-o[i])**2 for i in range(0,oln)])
        #del_o=dk-ok*f'(netk)
        del_o=[(d[j,i]-o[i])*fd(o[i],t) for i in range(0,oln)]
        del_y=[(fd(y[i],t)*np.matmul(w[:,i],del_o)) for i in range(0,hln)]
        w=w+c*np.multiply(np.vstack(del_o),[y])
        #print(del_y)
        v=v+c*np.multiply(np.vstack(del_y),[z[j,:]])
        #print(w)
        #print(v)
    if tc%1000==0:
        print("Training cycle "+str(tc))
        print("And the error is "+str(E))
print("Training cycle "+str(tc))
print("And the error is "+str(E))
print("Initial V is "+str(v1))
print("Final V is "+str(v))
print("Initial W is "+str(w1))
print("Final W is "+str(w))
np.savetxt("v.csv", v, delimiter=",")
np.savetxt("w.csv", w, delimiter=",")


