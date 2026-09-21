# sealed_planet

## 문제 요약

`10_encrypted_disk.img`는 일반 파일시스템이 아니라 암호화 컨테이너였습니다. 목표는 형식을 식별하고, 제공된 단서에서 패스프레이즈를 찾아 컨테이너를 연 뒤 내부 플래그를 확인하는 것입니다.

## 1. 암호화 방식 식별

헤더와 `cryptsetup luksDump` 결과에서 `Version: 1`을 확인해 LUKS1 컨테이너로 판단했습니다.

```bash
cryptsetup luksDump 10_encrypted_disk.img
```

## 2. 패스프레이즈 적용

문제 설명의 후보를 검증한 결과 다음 값으로 컨테이너가 열렸습니다.

```text
orion_star_2025!
```

```bash
sudo losetup -fP 10_encrypted_disk.img
sudo cryptsetup open --type luks /dev/loop0p2 secret
```

## 3. 마운트와 내부 확인

```bash
sudo mkdir -p /mnt/secret
sudo mount /dev/mapper/secret /mnt/secret
ls -la /mnt/secret
cat /mnt/secret/flag.txt
```

내부 파일에서는 다음 값을 확인했습니다.

```text
flag{enc_disk_f0rens1c}
```

문제가 요구한 형식 `flag{A1_A2_A3}`에 따라 암호 형식, 패스프레이즈, 내부 문자열을 결합했습니다.

## Final Flag

```text
flag{LUKS_orion_star_2025!_enc_disk_f0rens1c}
```

