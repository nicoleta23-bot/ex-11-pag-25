n=int(input('Introduceti numarul de elemente : '))
while n>10:
    n=int(input('dati un nr mai mic decat 10: '))
a=[]
print('introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    q=int(input('Dati elementul:'))
    a.extend([q])
print(a)

print('a) afiseaza pe ecran componentele tabloului la un interval de 5 pozitii')
print(a[::5])
print('b) afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator')
print(a[::-1])
print('c) sorteaza componentele tabloului in ordine descrescatoare ')
c=sorted(a)
c.sort(reverse=True)
print(c)
print('d) afiseaza pe ecran doar componentele pare ')
d=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        r=a[i]
        d.extend([r])
print(d)
print('e) afiseaza pe ecran media aritmetica a componentelor pare ')
e=round(sum(d)/len(d),2)
print(e)
print('f) afiseaza pe ecran doar componente impare ')
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        s=a[i]
        f.extend([s])
print(f)
print('g) afiseaza pe ecran doar componentele care sunt mai mari ca x si nu sunt divizibile cu y ')
x=int(input('introduceti x: '))
y=int(input('introduceti y: '))
g=[]
for i in a:
    if((i>x)and(i%x!=0)):
        v=i
        g.extend([v])
print(g)        
print('h) afiseaza pe ecran doar componentele care sunt mai mari ca x si mai mici decat y  ')
h=[]
for i in a:
    if((i>x)and(i<y)):
        z=i
        h.extend([z])
print(h)
print('i) afiseaza pe ecran pozitiile componentelor impare negative ')
it=[]
for i in a:
    if i<0:
        it.extend([a.index(i)])
print(it)        
print('j) afiseaza pe ecran pozitiile componentelor ce contin doar doua cifre semnificative ')
print('k) inlocuieste prima componenta a tabloului cu componenta de valoarea minima din tabloul respectiv ')
k=a.copy()
k[0]=min(k)
print(k)
print('l) inlocuieste componenta de valoare minima din tabloul respectiv cu prima componenta a acestuia ')
l=a.copy()
l[l.index(min(l))]=l[0]
print(l)
print('m) creeaza un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatura ')
print('n) creeaza un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatura ')
print('o) creeaza un tablou nou, format doar din acele componente ale tabloului introdus de la tastatura care au cel mult 4 divizori')