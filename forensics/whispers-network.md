# whispers_network

## 아티팩트

- `access12.log` — 321 bytes
- `net12.pcap` — 340 bytes

## 1. 로그에서 키 가설 도출

웹 로그에서 다음 요청을 확인했습니다.

```http
GET /shadow?key=Z HTTP/1.1
```

`key=Z`는 네트워크 페이로드에 적용된 단일 바이트 XOR 키라는 가설을 세우게 했습니다.

## 2. PCAP 재조립

캡처는 Ethernet 헤더 없이 RAW IPv4/TCP 데이터로 구성됐고, 총 5개의 TCP payload 조각이 있었습니다. 패킷 순서를 유지해 payload를 결합했습니다.

## 3. XOR 및 Base64

결합한 바이트마다 문자 `Z`를 XOR하자 다음 문자열이 나왔습니다.

```text
ZmxhZ3tuM3R3MHJrXzN4ZjFsX3B1enpsM30=
```

Base64 형식과 길이 조건을 만족하므로 디코딩해 최종 평문을 얻었습니다.

## Flag

```text
flag{n3tw0rk_3xf1l_puzzl3}
```

로그의 키, PCAP의 데이터, 디코딩 결과라는 서로 다른 증거가 한 흐름으로 연결되므로 단순 우연한 문자열보다 신뢰도가 높습니다.

