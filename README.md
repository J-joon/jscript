# jscript

`uvx`로 설치해서 실행하는 스크립트 패키지입니다.

현재 제공되는 커맨드:

- `fix-tasks`: 데이터 파일(`.csv`, `.parquet`)의 인덱스 보조 컬럼(`__index_level_0__`)을 정리합니다.

## 설치 및 실행

로컬 패키지 기준으로 실행:

```bash
uvx --from . fix-tasks ./data/example.csv
```

옵션:

```bash
uvx --from . fix-tasks ./data/example.csv --mode index --suffix .bak
```

백업 파일은 기본적으로 `*.backup` suffix로 생성됩니다.

### 지원 포맷

- `csv`
- `parquet`, `pq`
