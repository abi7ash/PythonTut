# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:04:51 2021

@author: abilash
"""

#One-bit ECC Hamming Code for 8-bit data

#giv_code = input("Enter the 12 bit code From LSB to MSB");
giv_code = [0,0,1,0,1,0,0,1,1,0,0,0];   #Code with 5th bit error
#giv_code = [0,0,1,0,1,0,1,1,1,0,0,0];  # Correct Code


#%% Generate check bits dependence
seq = [];
i=val=0;
ecc_len = len(giv_code);

#seq - Sequence of indicies for code correction bits
while val < ecc_len:
    val = 2**i;
    i=i+1;
    if val < ecc_len:
        seq.append(val);

#data_seq - sequence of indicies for data bits
data_seq = []
for i in range(1,ecc_len+1):
    if seq.count(i) == 0:
        data_seq.append(i);

#n - code word width 
# n = 4;
#import math as mymath
#n = '0'+str(round(mymath.log2(ecc_len)))+'b';

def bin_seq_gen(lst):
    y = [];
    for num in lst:
        y.append(f'{num:04b}');
        # y.append(f'{num:n}');
    return y;

gen_bin4seq = bin_seq_gen(seq);
gen_bin4data = bin_seq_gen(data_seq);

#%% Obtain Check bits from given code
#seq = [1,2,4,8];
giv_checkbits = [];

# for i in seq:
#     print(i);
#     # print(giv_checkbits);
#     giv_checkbits.append(giv_code[i-1]);

giv_checkbits = [giv_code[i-1] for i in seq];

#%%
dep = [];
dep = seq.copy();
p = 0;
for i in seq:
    temp = [];
    for j in data_seq:
        print(i);
        print(j);
        if i & j == i:
            temp.append(j);
    dep[p] = temp;
    p = p + 1;


#%% Generate Check Bits as per Code
#dep = [[3,5,7,9,11],[3,6,7,10,11],[5,6,7,12],[9,10,11,12]];

#function for generating xor operation of all elements in list - lst
def seq_xor_op(lst):
    xor_res = lst[0];
    for i in range(1,len(lst)-1):
        xor_res = xor_res ^ lst[i];
    return xor_res;

#Function for selecting elements from main_seq 
#with indicies provided by sel_lst

def lst_gen(main_seq,sel_lst):
    ret_lst = [];
    ret_lst = [main_seq[i-1] for i in sel_lst];
    return ret_lst;

#Generate check bits
gen_checkbits = [];
for i in range(1,len(dep)+1):
    # print(gen_checkbits,i);
    gen_checkbits.append(seq_xor_op(lst_gen(giv_code,dep[i-1])));

print(gen_checkbits);

#%%
def list2list_xor(lst1,lst2):
    if len(lst1)==len(lst2):
        xor_res = []
        for i in range(1,len(lst1)+1):
            # print(i);
            xor_res.append(lst1[i-1]^lst2[i-1]);
            # print(xor_res);
        return xor_res;
    else:
        return print("lists of unequal length");
    
#%%    
print("The Given Check bits are ",giv_checkbits);
print("The generate Check bits are ",gen_checkbits);
print("The Resulting syndrome (LSB First) is")
print(list2list_xor(gen_checkbits, giv_checkbits));