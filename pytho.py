outer=int(input())
atta=list(map(int,input().split()))
pit=[]
qit=[]
for i in range(len(atta)):
	if i%2==0:
		pit.append(atta[i])
	else:
		qit.append(atta[i])
sat=sum(pit)
rat=sum(qit)
if(sat>rat):
	print(sat)
else:
	print(rat)
