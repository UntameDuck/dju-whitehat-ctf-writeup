# silent_storage

## 접근 전략

파일시스템 일부가 손상되어 정상 마운트만으로는 데이터의 완전성을 기대하기 어려웠습니다. 따라서 파일 구조에 의존하지 않는 원시 바이트 문자열 카빙을 우선했습니다.

## 분석 절차

1. `disk.img`를 바이트 단위로 읽었습니다.
2. `FLAG{`, `flag{`와 흔한 변형(`FlAg{`, `F1AG{`, `FL4G{`)을 검색했습니다.
3. 매치 지점에서 닫는 `}`까지를 길이 제한과 함께 추출했습니다.
4. 중복을 제거하고 문자열의 의미와 문제 맥락을 비교했습니다.

발견된 후보:

```text
FLAG{UPPERCASE_IS_FAKE}
flag{deleted_file_recovered}
flag{wrong_one}
flag{not_the_real_flag}
```

## 후보 판별

문제는 손상된 파일시스템과 삭제 데이터 복구를 강조했습니다. `deleted_file_recovered`는 이 상황과 직접 연결됩니다. 나머지 세 후보는 이름 자체가 fake/wrong/not real을 명시해 의도적인 미끼로 판단할 수 있습니다.

## Flag

```text
flag{deleted_file_recovered}
```

문자열 카빙은 삭제 파일에도 효과적이지만 원래 파일의 메타데이터와 문맥을 잃을 수 있습니다. 따라서 후보가 여러 개라면 문제 서사와 주변 바이트를 반드시 함께 검증해야 합니다.

