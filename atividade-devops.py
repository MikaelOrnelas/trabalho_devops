arq_r = open('/Users/1700628/Documents/ips.txt','r')
texto = arq_r.readlines()
validos = []
invalidos = []
for a in texto:
    for b in a.split('.'):
        print(b)
    if b == '000':
        invalidos.append(a)
    else:
        validos.append(a)
arq_r.close()

arq_w = open('/Users/1700628/Documents/validos.txt','w')
arq_w.writelines(validos)
arq_w.close()

arq_w2 = open('/Users/1700628/Documents/invalidos.txt','w')
arq_w2.writelines(invalidos)
arq_w2.close()
