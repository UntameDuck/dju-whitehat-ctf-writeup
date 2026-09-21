# 대전대학교 화이트해커 경진대회 Write-up

> **Result: 1st Place 🏆**

대전대학교 화이트해커 경진대회에서 해결한 문제를 분야별로 정리한 저장소입니다. 단순히 페이로드만 나열하기보다, **어떤 관찰에서 출발해 어떤 가설을 세웠고, 무엇으로 검증했는지**가 드러나도록 구성했습니다.

> [!IMPORTANT]
> 이 문서는 대회가 종료된 뒤 교육 및 기록 목적으로 정리한 것입니다. 모든 공격은 대회가 허용한 환경에서만 수행했습니다.

## 문서 작성 기준

- 원문에 있는 사실, 주소, 오프셋, 페이로드를 우선했습니다.
- 원문에 없는 팀명·점수·플래그는 추정하지 않았습니다.
- 플래그 값을 적지 않은 문제는 `획득(값 미기록)`으로 표시했습니다.
- 기록이 요약 수준인 문제는 `요약 기록`으로 구분했습니다.
- 각 풀이를 `관찰 → 가설 → 검증 → 공격/복원 → 결과` 순서로 통일했습니다.

## 문제 목록

| 분야 | 문제 | 핵심 기법 | 기록 상태 |
|---|---|---|---|
| Reversing | [Reverse Alchemy](./reversing/reverse-alchemy.md) | XOR 연쇄식 역연산 | 상세 |
| Reversing | [Reverse Alchemy 2](./reversing/reverse-alchemy-2.md) | 순환 XOR, 기지 평문 | 상세 |
| Pwn | [Loveletter](./pwn/loveletter.md) | Shell command injection, blacklist bypass | 상세 |
| Pwn | [Mystery Function Call](./pwn/mystery-function-call.md) | 함수 포인터 덮어쓰기, ret2win | 상세 |
| Pwn | [Breaking the Box](./pwn/breaking-the-box.md) | 음수 인덱스 OOB write | 상세 |
| Pwn | [FOLLOW THE RETS](./pwn/follow-the-rets.md) | 스택 정렬, ret2shell_code | 상세 |
| Forensics | [BSOD GPS](./forensics/bsod-gps.md) | EXIF GPS 분석 | 상세 |
| Forensics | [fragments_of_memory](./forensics/fragments-of-memory.md) | 메모리 문자열 카빙, 미끼 판별 | 상세 |
| Forensics | [forgotten_drawer](./forensics/forgotten-drawer.md) | Registry, UTF-16LE/Base64/Hex | 상세 |
| Forensics | [hidden_whisper](./forensics/hidden-whisper.md) | PCAP, HTTP, Base32 | 상세 |
| Forensics | [sealed_planet](./forensics/sealed-planet.md) | LUKS 디스크 복호화 | 상세 |
| Forensics | [silent_storage](./forensics/silent-storage.md) | 손상 디스크 문자열 카빙 | 상세 |
| Forensics | [whispers_network](./forensics/whispers-network.md) | PCAP XOR, Base64 | 상세 |
| Forensics | [Key to the Shadows](./forensics/key-to-the-shadows.md) | 로그·메모리 키 조합, LUKS2 | 상세 |
| Forensics | [phantom_injection](./forensics/phantom-injection.md) | 메모리·PCAP·EVTX 교차 검증 | 상세 |
| Forensics | [Ghost in Registry](./forensics/ghost-in-registry.md) | UserAssist/MUICache 문자열 카빙 | 상세 |
| Web | [시큐어 병원](./web/secure-hospital.md) | IDOR/BOLA | 상세 |
| Web | [크로노스](./web/chronos.md) | XXE | 상세 |
| Web | [Ping Masters](./web/ping-masters.md) | OS command injection, `${IFS}` | 상세 |
| Web | [빈티지 마켓](./web/vintage-market.md) | LFI → log poisoning → RCE | 요약 기록 |
| Web | [내부 감사 시스템 침투 작전](./web/internal-audit.md) | LFI → SSH → SUID privesc | 요약 기록 |
| Web | [사진 저장소](./web/photo-storage.md) | Upload bypass, Apache misconfiguration | 요약 기록 |
| Web | [데이터 저장소](./web/data-storage.md) | Python `eval()` code injection | 상세 요약 |
| Web | [당신은 로봇입니까?](./web/are-you-robot.md) | LFI → upload race → RCE | 요약 기록 |
| Web | [Gateway](./web/gateway.md) | HTTP request smuggling → internal RCE | 요약 기록 |
| Web | [DB Structure](./web/db-structure.md) | UNION-based SQL injection | 상세 요약 |
| Misc | [딩동게이트](./misc/dingdong-gate.md) | 시간 조건 분석 및 접속 자동화 | 상세 |

## 저장소 구조

```text
writeup/
├── README.md
├── reversing/
├── pwn/
├── forensics/
├── web/
├── misc/
└── scripts/
```

재현용 스크립트는 [`scripts`](./scripts/)에 분리했습니다. 원격 주소와 바이너리 경로는 대회 당시 환경을 기준으로 하므로, 현재는 실행되지 않을 수 있습니다.

