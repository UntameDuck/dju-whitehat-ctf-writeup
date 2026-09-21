# 데이터 저장소

## 취약점 개요

Flask 기반 백업/복구 서비스의 `/backup` 엔드포인트가 JSON의 `data` 값을 Python `eval()`에 전달했습니다.

```python
data_object = eval(data)
```

## 발견 과정

1. `/backup`, `/restore` 엔드포인트를 확인했습니다.
2. 일반 문자열 `test`를 전달했을 때 `name 'test' is not defined` 오류가 발생했습니다.
3. 이 오류는 입력이 데이터가 아니라 Python 표현식으로 평가된다는 가설을 지지했습니다.
4. `__import__("os").system("ls")` 형태의 표현식으로 OS 명령 실행 가능성을 검증했습니다.
5. 파일시스템 탐색에서 `/app/flag.txt`를 찾았습니다.
6. `open("/app/flag.txt").read()`를 평가해 내용을 회수했습니다.

응답은 Base64로 인코딩된 pickle 직렬화 데이터였으므로, 응답 디코딩 단계까지 포함해 결과를 확인했습니다. 원문에는 플래그 값이 남아 있지 않습니다.

## 영향

`eval()`은 단순 정보 노출이 아니라 애플리케이션 권한으로 임의 Python 코드를 실행합니다. 파일 열람, 시스템 명령 실행, 네트워크 통신, 추가 페이로드 설치로 이어질 수 있는 Critical 취약점입니다.

## 대응

입력을 코드로 평가하지 말고 JSON parser와 명시적 schema validation을 사용해야 합니다. pickle 역시 신뢰되지 않은 데이터의 역직렬화에 사용하면 안 됩니다.

