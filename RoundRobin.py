def roundRobin(pid, time, at):
    Q=[]
    T = []
    quant=2
    i=0
    
    while(len(pid)>0):
        if ((len(T)>0 and at[i]>T[-1]) or (at[i]>sum(T))):
            i+=1
            i=i%len(pid)
            continue
        else:
            if time[i]>=quant:
                Q.append(pid[i])
                if(len(T)>0):
                    T.append(quant+T[-1])
                else:
                    T.append(quant)
                time[i]-=quant
                if time[i]==0:
                    pid.pop(i)
                    time.pop(i)
                else:
                    i+=1
            elif time[i]<quant:
                Q.append(pid[i])
                if(len(T)>0):
                    T.append(time[i]+T[-1])
                else:
                    T.append(time[i])
                pid.pop(i)
                time.pop(i)
            else:
                i+=1
            if i>=len(pid) and len(pid)>0:
                i=i%len(pid)
    print(Q, T)
    
    
print(roundRobin([1,2,4,5],[4,3,1,2], [1,0,4,7]))
