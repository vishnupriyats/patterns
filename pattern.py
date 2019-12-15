#1
n = 6
for i in range(1, n):
    for j in range( i,0,-1):
        print j,
    print ""

# #2
n=6
for i in range(n-1,-1,-1):
    for j in range( n-1,i,-1):
        print j,
    print ""
 
print"" 
# #3

n=6
for i in range(n-1,0,-1):
    for j in range(i,n):
        print j,
    print ""   
# #4

n=10
for i in range(n-1,-2,-2):
    for j in range( n-1,i+1,-2):
        print j,
    print "" 

print""

# #5
n=10
for i in range(1,10,+2):
    for j in range( 1,i+1,+2):
        print j,
    print "" 

#6
n = 6
for i in range(1, n):
    output2=[]
    for x in range(n-1,i,-1):
        print "",    
    for j in range( i,0,-1):
        output2.append(str(j))
    print "".join(output2),
    print ""


n = 6
for i in range(n-1,-1,-1):
    output2=[]
    for x in range(n-1,i,-1):
        print "",    
    for j in range( i,0,-1):
        output2.append(str(j))
    print "".join(output2),    
    print ""

# # n=5
# for i in range(n,0,-1):
#     for x in range(i,1,-1):
#         print "", 
#     for j in range(i,n+1):
#         print j,
#         if j==n :
#             for y in range(n-1,i-1,-1):
#                 print y,
#     print ""   

# output = []
# output = [" ", " ", " ", " ", "1", "\n", " ", " ", " ","2", "1", "\n"]
# print "".join(output)

#7

n=7
for i in range(n,0,-1):
    output1=[]
    for x in range(i,1,-1):
        print "", 
    for j in range(i,n+1):
       output1.append(str(j))
    for k in range(i,n+1):
        if k==n :
            for y in range(n-1,i-1,-1):
                output1.append(str(y))
    print "".join(output1),    
    print ""   

# #8
n=7
for i in range(n,0,-1):
    output1=[]
    for x in range(i,1,-1):
        print "", 
    for j in range(i,n+1):
       output1.append(str(j))
    for k in range(i,n+1):
        if k==n :
            for y in range(n-1,i-1,-1):
                output1.append(str(y))
    print "".join(output1),    
    print ""   
for i in range(2,n+1):
    output1=[]
    for x in range(i,1,-1):
        print "", 
    for j in range(i,n+1):
       output1.append(str(j))
    for k in range(i,n+1):
        if k==n :
            for y in range(n-1,i-1,-1):
                output1.append(str(y))
    print "".join(output1),    
    print ""       

#9    
a="vishnupriya"
n = len(a)
for i in range(0, n):
    output2=[]
    for x in range(n-1,i,-1):
        print "",    
    for j in range( i,-1,-1):
        output2.append(a[j])
    for k in range(i,-1,-1):
        if a[k]==a[0]:
            for y in range(k+1,i+1):
                output2.append(a[y])
    print "".join(output2),
    print ""
for i in range(n-2,-1,-1):
    output2=[]
    for x in range(n-1,i,-1):
        print "",    
    for j in range( i,-1,-1):
        output2.append(a[j])
    for k in range(i,-1,-1):
        if a[k]==a[0]:
            for y in range(k+1,i+1):
                output2.append(a[y])
    print "".join(output2),
    print ""

#10

a="vishnupriya"
n = len(a)
for i in range(0, n):
    output2=[]
    for x in range(n-1,i,-1):
        print "",    
    for j in range( i,-1,-1):
        output2.append(a[j])
    for k in range(i,-1,-1):
        if a[k]==a[0]:
            for y in range(k+1,i+1):
                output2.append(a[y])
    print "".join(output2),
    print ""