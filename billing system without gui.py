f=open("C:/Users/ELCOT/Desktop/ki.txt","r+")
g=f.readlines()
pl=open("C:/Users/ELCOT/Desktop/bi.txt","r+")
kl=pl.readlines()
print(f)
k=[]
p=0
z=[]
s=[]
fu=[]
on=0
for i in g:
    print(i)
def e():
    while True:
        n=str(input('enter the item:')).strip().lower()
        p=0
        on=0
        for w in k:
            p=float(p)+float(w)
        if 'sum' in n:
            pl=' '
            print(z)
            print('----------------------------------------------')
            print('---------------------KFC----------------------')
            print('Item                                     price')
            for count in range(len(z)):
                n = (-len(z[count]))+46
                n = (n - len(str(k[count]))) - 3
                print(z[count],pl*n,"{:.2f}".format(k[count]))
            m = -5 + 46
            m = (m - len(str(p))) - 3
            print('----------------------------------------------')
            print('Total',pl*m,"{:.2f}".format(p))
            print('----------------------------------------------')
            break
        if n==kl[0].strip().lower():
            print('username is correct')
            j=str(input('enter the password:')).strip().lower()
            if j==kl[1]:
                print('hi k')
                print('1)add item\n2)remove item\n3)change price')
                t=int(input('Enter the number you want to do:'))
                if t==1:
                    po=str(input('Enter the item:')).strip().lower()
                    pa=str(input('Enter the item price:')).strip().lower()
                    for oneS in g: 
                        for j in range(len(oneS)):
                            if oneS[j] == 'R':
                                if oneS[j+1]== 's':
                                    ok = oneS[:j].lower().strip().split('(',1)
                                    if po.lower().strip() == ok[0].strip():
                                        print('item already in menu')
                                        break
                        else:
                                        f.write('\n'+po.lower()+"   Rs "+pa.lower())
                                        print('Item added successfully ')
                                        f.close()
                                        break
                    break
                
                if t==2:
                    fd=open("C:/Users/ELCOT/Desktop/ki.txt","w")
                    uo=str(input('Enter the item:')).strip().lower()
                    for oneS in g: 
                        for j in range(len(oneS)):
                            if oneS[j] == 'R':
                                if oneS[j+1]== 's':
                                    ok = oneS[:j].lower().strip().split('(',1)
                                    if uo.lower().strip() == ok[0].strip():
                                        g.remove(oneS)
                                        print(uo,'\tsucessfully removed')
                                        for top in g:
                                            fd.write(top)
                                        fd.close()
                                        on=1
                                        break
                    if on==0:
                        print(uo,'\tNot in menu')
                        break
                    break
                if t==3:
                    fl=open("C:/Users/ELCOT/Desktop/ki.txt","w")
                    ppo=str(input('Enter the item:')).strip().lower()
                    ppa=str(input('Enter the price:')).strip().lower()
                    for oneS in g: 
                        for j in range(len(oneS)):
                            if oneS[j] == 'R':
                                if oneS[j+1]== 's':
                                    ok = oneS[:j].lower().strip().split('(',1)
                                    if ppo.lower().strip() == ok[0].strip():
                                        g.remove(oneS)
                                        g.insert(len(g),'\n'+ppo.lower()+"  Rs "+ppa.lower())
                                        for top in g:
                                            fl.write(top)
                                        fl.close()
                                        print(ppo,'price changed successfully')
                                        break
                    break
        for oneS in g:# item and prize pireekuthu!
          #print(oneS)
          for j in range(len(oneS)):
               if oneS[j] == 'R':
                   if oneS[j+1]== 's':
                       ok = oneS[:j].lower().strip().split('(',1)
                       if n.lower().strip() == ok[0].strip():
                           z.append(n)
                           k.append(float(oneS[j+2:]))
                           print(z)
                           print(k)
                           on = 1
        if on == 0:
            print(n,'This object is not in menu list or empty')                     
e()

