# hidden_whisper

## 관찰

`capture.pcapng`에서 ASCII 문자열을 추출하자 다음 형태의 HTTP 요청이 반복됐습니다.

```http
GET /?q=MZWGCZ33 HTTP/1.1
Host: 127.0.0.1:8000

GET /?q=MRVHKQ2U HTTP/1.1
Host: 127.0.0.1:8000
```

짧고 일정한 문자 집합을 가진 `q` 값이 여러 요청에 걸쳐 나타났기 때문에, 분할 전송된 인코딩 데이터로 가설을 세웠습니다.

## 복원

1. 패킷 순서를 유지한 채 모든 `q` 파라미터를 수집했습니다.
2. 문자 집합과 길이를 근거로 Base32와 Base64를 우선 비교했습니다.
3. Base32 디코딩에서 다음 가독 조각이 순서대로 나왔습니다.

```text
flag{
djuCT
Ffor2
025_p
cap_t
est}
```

4. 패킷 순서대로 결합해 완전한 토큰을 만들었습니다.

## Flag

```text
FLAG{djuCTFfor2025_pcap_test}
```

패킷에서 문자열이 보였다는 사실만으로 끝내지 않고, 전송 순서와 인코딩의 성공 여부를 함께 검증한 것이 핵심입니다.

