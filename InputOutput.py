#!/usr/bin/env python
# coding: utf-8

# In[1]:


bil1 = input ('Isikan bilangan 1: ')
bil2 = input ('isikan bilangan 2: ')
hasil = int(bil1) + int(bil2)
print("hasil perjumlahan:",bil1,"+",bil2,"=",hasil)


# In[2]:


print("A","B","C","D", sep='@_@') #sep =  Separator / pembatas


# <p>3. Cara melakukan <b>print</b> dengan menabahkan and di ahir garis baris</p>

# In[7]:


print("A","B","C","D", sep='\n', end= "-_-")


# In[12]:


num_1 = 8
num_2 = 10

#hasil dari 8  modulus 10 = 8
#str.format()

print('hasil dari {} modulus {} = {}'.format (num_1,num_2,num_1%num_2))


# <hr><h1>Memformat Indeks<hr><h1>
#     <p>memformat dengan key (kunci)

# In[15]:


fname = "akbar"
mname = "samsudin"
lname = "supratman"

print('name anda {2} {0} {1}'. format (fname,mname,lname))


# In[17]:


print('nama anda {nama}, nilai anda {nilai}'.format(nama='samsudin',nilai=70))


# <h3>pengenalan String<h3>
#     

# In[25]:


univ = "Universitas Nusa putra"

print("karater pertama :",univ[0])
print("karakter terakhir :",univ[-1])
#Universitas
print(univ[0:11])
print(univ[-6:-1])
print(univ[17:])


# <h3> stiring<h3>
#     

# In[27]:


f_name = 'samsudin'
l_name = 'pesulap merah'

print(f'nama saya {f_name} {l_name}')

first = 100
second = 200

print(f'Hasil perjumlahan {first} + {second} = {first+second}')


# <h3>fungsi string<h3>
#    

# In[42]:


nama = "Saipul, Samsul, Sukimin"
nama2 = "Saipul, Samsul, Sukimin"
#split -> memisahkan string berdasarkan karakter tertentu
print(nama2.split())
print(nama.split(','))

#join ->menggambungkan string kedalam kumpulan karater
print('@'.join(nama.split (',')))

#input tgl lahir -> 18/agustus/1945
#input nama ->bill gates
#output:
#tgl :18 bulan:agustus, tahun :1945
#nama inisial : BG

tgl = input("masukan tanggal lahir : ")
nama = input("masukan nama : ")
pemisah = tgl.split("/")
print(f"tgl : {pemisah[0]},bulan:{pemisah[1]},{pemisah[2]}")
pemisah2 = nama.split()
nama_pertama = pemisah2[0]
nama_terakhir = pemisah2[1]
print(f"nama inisial : {nama_pertama[0]+nama_terakhir[0]}")      


# In[ ]:




