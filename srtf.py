at=[];bt=[];rt=[];
sum_wait=0;t_turnaround=0
n=int(raw_input("Enter number of Process : "))
i=0
while i<n:
	print  "For process :",i+1
	at.append(int(raw_input("Enter arrival time of process :")))
	bt.append(int(raw_input("Enter arrival time of process :")))
	rt.append(bt[i])
	i+=1

print "\n\nProcess\t|Turnaround Time| Waiting Time\n"
rt.append(99999)
time=0;remain=0;j=i   	
while remain!=n:
        smallest=j
	i=0;        
	while i<n:
            if at[i]<=time and rt[i]<rt[smallest] and rt[i]>0:
                smallest=i
            i+=1       
        rt[smallest]-=1
        if rt[smallest]==0:
            remain+=1
            endTime=time+1
            print smallest+1,"\t","\t",endTime-at[smallest],"\t","\t",endTime-bt[smallest]-at[smallest]
            sum_wait+=endTime-bt[smallest]-at[smallest]
            t_turnaround+=endTime-at[smallest]
    	time+=1
print "\nAverage waiting time = ",sum_wait*1.0/n
print "Average Turnaround time = ",t_turnaround*1.0/5
 
