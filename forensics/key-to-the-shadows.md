# Key to the Shadows

## 전체 공격 흐름

```text
access11.log의 접미사
    + suspect_mem11.raw의 접두사
    → LUKS2 패스프레이즈
    → disk11.img 복호화
    → flag.txt
```

## 1. 키 조각 수집

`access11.log`에서 다음 토큰을 확인했습니다.

```text
token=realm2025!
```

메모리 덤프에서는 Base64 문자열을 발견했습니다.

```text
U2hhZG93Xw== → Shadow_
```

두 문자열의 경계가 자연스럽게 연결되므로 다음 패스프레이즈를 구성했습니다.

```text
Shadow_realm2025!
```

## 2. 디스크 복호화

헤더 검사에서 LUKS2 서명을 확인했습니다.

```bash
sudo losetup -fP disk11.img
losetup -a
sudo cryptsetup open --type luks2 /dev/loop0 secret
sudo mkdir -p /mnt/secret
sudo mount /dev/mapper/secret /mnt/secret
cat /mnt/secret/flag.txt
```

## Flag

```text
flag{Shadow_realm2025!}
```

서로 독립된 로그와 메모리에서 얻은 조각이 실제 LUKS2 컨테이너를 여는 데 성공했으므로, 키 조합 가설을 기능적으로 검증할 수 있었습니다.

