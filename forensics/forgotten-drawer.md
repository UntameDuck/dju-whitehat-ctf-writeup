# forgotten_drawer

## 문제 상황

`NTUSER.DAT` 레지스트리 하이브에 여러 인코딩과 미끼 문자열이 섞여 있었습니다. ASCII만 검색하면 주요 조각을 놓칠 수 있으므로 UTF-16LE, Base64, Hex를 함께 조사했습니다.

## 분석 흐름

### 1. 문자열 추출

ASCII와 UTF-16LE에서 길이 6 이상의 가독 문자열을 추출하고, `FLAG`, `{`, `}`, Base64 및 Hex 형태를 별도 후보군으로 분류했습니다.

### 2. 미끼 배제

오프셋 `0x0000123C` 부근에는 다음 값이 모여 있었습니다.

```text
FLAG{UPPERCASE_FAKE}
RmxhZ19mYWtl              → Flag_fake
666c61697b66616b657d      → flai{fake}
```

서로 다른 인코딩에서 `fake`를 반복한다는 점은 이 블록이 의도적인 decoy임을 강하게 뒷받침합니다.

### 3. 실제 조각 복원

오프셋 `0x0000137C` 인근에서는 다음 조각을 얻었습니다.

```text
UTF-16LE fragment: ag{re…challenge}
Z2lzdHJ5Xw==      → registry_
70757a7a6c655f    → puzzle_
```

조각은 물리적으로 인접했고, 오프셋 순서와 의미가 모두 자연스럽게 연결되었습니다.

## Flag

```text
FLAG{registry_puzzle_challenge}
```

## 판단 근거

완성된 문자열의 모양만 본 것이 아니라 인코딩 결과, 오프셋 근접성, 단어 경계, 미끼 블록과의 분리 여부를 함께 사용했습니다.

