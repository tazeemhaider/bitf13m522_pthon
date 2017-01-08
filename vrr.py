wait=0
t_time=0
count=0
at=[];bt=[];rt=[];aq=[];io=[];rqt=[];wt=[]; inp=[]
n = int(input("Enter Total Process:\t ")) 
remain=n
i=0
q= int(input("Enter quantum time:\t"))
io.append(int(raw_input("Enter input/output time : "))) #assuming i/o for even processes
for i in xrange(n):
        print  "For process :",i+1
	at.append(int(raw_input("Enter arrival time of process :")))
	bt.append(int(raw_input("Enter burst time of process :")))
	rt.append(bt[i])
	i+=1
inp.append(0)
rqt.append(q)
wt.append(0)
time=0;
while remain!=0:
      
      for i in xrange(n):
          if i%2!=0:
             time+=q
             rt[i]=bt[i]-q
             wait+=time-at[count]-bt[count]
             t_time+=time-at[count] 
          elif i%2==0:
             time+=inp
             inp[i]=time+inp
             rqt[i]=rt[i]-inp
             wait+=time-at[count]-bt[count]
             t_time+=time-at[count] 

print ("Average Waiting Time= ",wait*1.0/n)
print ("Avg Turnaround Time = ",t_time*1.0/n) 
  


