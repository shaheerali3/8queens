import numpy as np
import random

boardheight=8
#sizeofpop=5
def createpop(sizeofpop):
    gene = np.random.randint(8, size=(sizeofpop,8))
    return gene

#print(x)

def fitfunc(pop):
    fitvalues=[]

    for p in pop:
        penalty = 0
        for i in range(8):
            r=p[i]
            for j in range(8):
                if(i==j):
                    continue

                dist=(i - j)
                if(dist<0):
                    dist=-dist

                if p[j] in [r,r-dist,r+dist]:
                    penalty += 1
        fitvalues.append(penalty)
    return -1 * np.array(fitvalues)

#fitval=(fitfunc(x,8))
#print("fitval is this",fitval)


def selection(fitvalues,pop):

    probarray=fitvalues.copy()
    probarray += abs(probarray.min())+1
    probarray=probarray/probarray.sum()
    # for i in fitvalues:
    #     sum+=i
    # for i in fitvalues:
    #     newprob =(i/sum)
    #     probarray.append(newprob)
    N=len(pop)
    #print(N)
    #print(probarray)
    indices=np.arange(N)
    selind=np.random.choice(indices,size=N,p=probarray)
    #print("this is selind ",selind)
    selpop=pop[selind]
    return selpop

#print(selection(fitval,x))

def crossover(p1,p2,pc):
    x=np.random.random()
    if(x < pc):
        m=np.random.randint(1,8)
        array=np.array(p1)

        firstchild=np.concatenate([p1[:m],p2[m:]])
        secondchild=np.concatenate([p2[:m],p1[m:]])

    else:
         firstchild=p1.copy()
         secondchild=p2.copy()
    return firstchild,secondchild
def mutation(single,probmut):
    x=np.random.random()
    if(x < probmut):
        z=np.random.randint(8)
        single[z]=np.random.randint(8)
    return single

def crossoverandmutate(chosenpop,pc,pm):
    N=len(chosenpop)
    newarray=np.empty((N,8),dtype=int)
    i=0
    while(i<N):
        #print(i,N)

        parent=chosenpop[i]
        #print("this is",parent)
        parent2 = chosenpop[i + 1]

        c1,c2 = crossover(parent,parent2,pc)
        newarray[i]=c1
        newarray[i+1]=c2
        i=i+2
    for i in range(N):
        mutation(newarray[i],pm)
    return newarray

def runqueens(maxgen,pc,pm):
    bfo=None
    for gen in range(maxgen):
        x = createpop(1000)
        fitval = fitfunc(x)
        besti=fitval.argmax()
        bestfit=fitval[besti]
        #print("best fit",bestfit)
        if(bfo==None or bestfit>bfo):
            bfo=bestfit
            best_sol=x[besti]
        if(bestfit==0):
            print("optimal solution found")
            break
        selected_pop = selection(fitval,x)
        popx=crossoverandmutate(selected_pop,pc,pm)
    print()
    print("this is",best_sol)
    l = [[0 for j in range(8)] for i in range((8))]
    count=0
    for i in best_sol:
        l[count][i]='Q'
        count=count+1
    print("this is what the board looks like")
    print(np.matrix(l))



runqueens(1000,pc=0.7,pm=0.05)
















