a={"Ram":63,"Ashok":75,"Payal":546}
print(a.items())
print(a.keys())
print(a.values())
print(a.update({"Ram":700}))
print(a.get("Payal","anhy")) # ye none return karta h agar key present na ho dict mai 
print(a["Payal"],a["anhy"]) # ye error return karta h agar key present na ho dict mai lekin kaam dono ka same h 