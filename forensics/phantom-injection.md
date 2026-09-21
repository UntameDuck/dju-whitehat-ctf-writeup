# phantom_injection

## 분석 목표

메모리 덤프, C2 PCAP, Windows 이벤트 로그를 함께 분석해 악성 DLL 인젝션의 흔적과 플래그를 교차 검증했습니다.

## 1. 메모리

덤프 전체에 `flag\{[^}]{0,200}\}` 패턴을 적용해 다음 값을 발견했습니다.

```text
flag{phant0m_1nj3ct10n_ap7}
```

문자열은 덤프 말단부 근처에 있었으며, 주입된 DLL의 상수 영역 또는 실행 후 잔존 데이터로 해석했습니다.

## 2. 네트워크

`c2_traffic.pcap`의 payload에서는 다음 연속 문자열이 확인됐습니다.

```text
C2_TRAFFICphantom.dllflag{phant0m_1nj3ct10n_ap7}g
```

동일한 플래그와 `phantom.dll` 식별자가 함께 나타나 메모리 결과와의 연관성을 강화했습니다.

## 3. 이벤트 로그

`security.evtx`의 Event ID 4624에서 다음 침입 정황을 확인했습니다.

```text
LogonType = 10
Account   = Hacker
```

Logon Type 10은 원격 대화형 로그인(RDP)에 해당합니다. 직접 플래그를 포함하지는 않지만 침입 → DLL 인젝션 → C2 통신으로 이어지는 타임라인을 지지합니다.

## Flag

```text
flag{phant0m_1nj3ct10n_ap7}
```

단일 문자열 검색 결과에 의존하지 않고 메모리, 네트워크, 이벤트 로그가 같은 결론을 지지하도록 만든 것이 이 풀이의 핵심입니다.

