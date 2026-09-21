# Ghost in Registry

## 문제 상황

실행 파일과 이벤트 로그는 삭제됐지만 `NTUSER.DAT`과 `SYSTEM` 하이브가 남아 있었습니다. 목표는 사용자가 실행한 악성 프로그램의 원래 경로를 식별하는 것입니다.

## 분석 전략

레지스트리 하이브를 단순 텍스트로 보지 않고 다음 두 접근을 병행했습니다.

1. ASCII 및 UTF-16LE에서 `C:\...\.exe` 경로 패턴 문자열 카빙
2. 실행 흔적이 남는 UserAssist, MUICache, RecentDocs, AppCompatCache 영역 확인

## 결과와 검증

`NTUSER.DAT`에서 동일한 실행 경로가 두 차례 검출됐고, `SYSTEM`에서는 발견되지 않았습니다.

```text
C:\Users\Hacker\AppData\phantom.exe
```

사용자별 실행 흔적이 주로 `NTUSER.DAT`에 남는다는 점과 반복 검출 결과가 일치합니다. 실제 실행 파일이 삭제됐더라도 레지스트리의 참조 데이터는 별도로 남을 수 있습니다.

## Flag

```text
flag{C:\Users\Hacker\AppData\phantom.exe}
```

