count=0;time=0;remain=0;flag=0;
wait=0;t_time=0;
at=[];bt=[];rt=[]; 
n=int(raw_input("Enter number of Process : "))
remain=n
q=int(raw_input("Enter quantum slice : "))
i=0
while i<n:
	print  "For process :",i+1
	at.append(int(raw_input("Enter arrival time of process :")))
	bt.append(int(raw_input("Enter burst time of process :")))
	rt.append(bt[i])
	i+=1

print "\n\nProcess\t|Turnaround Time| Waiting Time\n"	
while remain!=0:
       if(rt[count]<q and rt[count]>0):
           time+=rt[count] 
           rt[count]=0 
           flag=1
       elif (rt[count]>0):
           rt[count]-=q 
           time+=q
       if(rt[count]==0 and flag==1):
            remain-=remain
            print("P[%d]\t|\t%d\t|\t%d\n",count+1,time-at[count],time-at[count]-bt[count]) 
            wait+=time-at[count]-bt[count]
            t_time+=time-at[count]
            flag=0  
       if(count==n-1): 
            count=0
       elif(at[count+1]<=time): 
            count+=count
       else:
            count=0           
print "\nAverage waiting time = ",wait*1.0/n
print "Average Turnaround time = ",t_time*1.0/n
 
