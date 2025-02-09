ciphertxt = "KR1BI{CAhbs_4fW_MkrLC_Xg_kTu}"
        #    FL1TZ{ROund_DnD_RouND_We_gOo}

# bech teshel l3amalya letters lkoll raddithom majuscule
ciphertxt = ciphertxt.upper()

# alpha_ord_upper te5ou carctere trajja3 l'ordre alphabetique dielou

def alpha_ord_upper(ch) :
  return ord(ch)-64

# upper_char te5ou l'ordre alpha w trajja3 l carctere (ken lel majuscule)
def upper_char(n):
  return chr(n+64)

# cipher_ord hya liste ta3 l'ordre alphabetique lkol lettre f ciphertext (ay 7ajja a part les lettres to93od kima hya)
cipher_ord = [str(alpha_ord_upper(w))  if w.isalpha() else w for w in ciphertxt]

# falg_ord hya lista ta3 l'ordre alphabetique lkol lettre fel flag 
flag_ord = []

for i in range(len(cipher_ord)):
  
  if ciphertxt[i].isalpha() and cipher_ord[i].isnumeric():
    flag_ord.append(str((int(cipher_ord[i])-i+20)%26+1))
    
  else :
    flag_ord.append(cipher_ord[i])


print (cipher_ord)
print(flag_ord)

# Finally kol order alphabetique walla lettre correspondante lih w t7at f string flag
flag = ''
for w in flag_ord :
  if str(w).isnumeric() :
    flag += upper_char(int(w))
  else :
    flag += w

print(flag)
# flag = FLATZ{ROUND_DND_ROUND_WE_GOO}
# 1 wallet A w 4 fama wallet D wa9teli lezmha to93od 4 ( DND = 4ND ) sinon kol lettre minuscule f cipher texte twalli minuscule zeda fel flag
# output shoudl be FL1TZ{ROUND_4ND_ROUND_WE_GOO}
