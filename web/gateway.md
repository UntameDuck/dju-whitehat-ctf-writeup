# Gateway

> [!NOTE]
> 원문에는 취약점 종류와 공격 단계만 남아 있으며, 실제 raw request와 플래그는 기록되어 있지 않습니다.

## 공격 체인

```text
프론트엔드/백엔드 HTTP 파싱 차이
 → Content-Length와 Transfer-Encoding 경계 불일치
 → HTTP Request Smuggling
 → 외부에서 차단된 /internal-api/debug 접근
 → debug 기능의 Python eval() 악용
 → RCE 및 플래그 획득
```

## 분석 관점

이 문제의 중요한 점은 취약점이 두 신뢰 경계에 걸쳐 있다는 것입니다.

1. 게이트웨이와 백엔드가 요청 끝을 다르게 해석합니다.
2. 게이트웨이는 외부 요청 하나로 보지만 백엔드는 남은 바이트를 두 번째 내부 요청으로 처리합니다.
3. 네트워크 위치만으로 보호하던 debug endpoint에 도달합니다.
4. debug endpoint의 `eval()`이 최종적으로 코드 실행을 허용합니다.

## 대응

- 모든 계층에서 HTTP parsing과 메시지 framing을 일관되게 적용합니다.
- 모호한 `Content-Length`/`Transfer-Encoding` 조합을 연결 입구에서 거부합니다.
- 내부 API도 강한 인증·인가를 수행합니다.
- debug endpoint를 운영 환경에서 제거합니다.
- 사용자 입력을 `eval()`하지 않습니다.

