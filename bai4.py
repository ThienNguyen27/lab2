Date=input("Date in MM/DD/YYYY: ")
slicea=slice(0,3)
sliceb=slice(3,6)
slicec=slice(6,10)
print(f"Date in DD/MM/YYYY: {Date[sliceb]+Date[slicea]+Date[slicec]}")

