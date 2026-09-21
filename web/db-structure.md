# DB Structure

## 취약점 개요

검색어가 다음과 유사한 SQL 문자열에 직접 결합됐습니다.

```sql
SELECT * FROM posts WHERE title LIKE '%<input>%'
```

입력으로 문자열 리터럴을 닫고 `UNION SELECT`를 추가할 수 있었으며, 결과가 정상 검색 화면에 출력되는 Union-based SQL Injection이었습니다.

## 분석 과정

1. 따옴표 입력에 따른 응답 변화로 SQL 문맥을 확인했습니다.
2. `UNION SELECT`를 사용해 원래 결과 집합과 공격자 쿼리 결과를 결합했습니다.
3. `information_schema.tables`에서 `boardapp` schema의 테이블을 조회했습니다.

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'boardapp';
```

4. `information_schema.columns`를 조회해 각 테이블의 컬럼 구조를 복원했습니다.
5. `posts`, `users` 테이블의 존재와 구조를 확인했습니다.

원문에는 실제 HTTP 파라미터, UNION 컬럼 수를 맞춘 최종 페이로드, 플래그 값이 기록되어 있지 않습니다.

## 영향

읽기 권한 범위에 따라 게시글과 사용자 데이터가 노출될 수 있습니다. DB 계정 권한이 과도하면 데이터 변경이나 추가 시스템 침해로도 확장될 수 있습니다.

## 안전한 구현

```php
$stmt = $pdo->prepare("SELECT * FROM posts WHERE title LIKE ?");
$stmt->execute(["%" . $input . "%"]);
```

Prepared Statement의 핵심은 “이스케이프를 잘한다”가 아니라 SQL 구조와 데이터를 분리한다는 점입니다. 여기에 DB 최소 권한, 상세 오류 비공개, 쿼리 로깅 및 탐지를 함께 적용해야 합니다.

