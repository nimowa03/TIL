# CrewAI 간단한 에이전트 실습

## 개요
이 예제는 CrewAI를 사용하여 두 개의 에이전트(연구원, 작가)가 협업하는 간단한 시스템을 구현합니다.

## 설치

```bash
pip3 install crewai
```

## 환경 설정

1. 프로젝트 루트의 `.env` 파일에 OpenAI API 키를 추가하세요:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

2. `.env` 파일이 `.gitignore`에 포함되어 있는지 확인하세요 (이미 설정되어 있음).

## CrewAI 핵심 개념

### 1. Agent (에이전트)
- **역할**: 특정 역할과 목표를 가진 AI 에이전트
- **주요 속성**:
  - `role`: 에이전트의 역할
  - `goal`: 에이전트의 목표
  - `backstory`: 에이전트의 배경 스토리 (페르소나 정의)
  - `verbose`: 작업 과정 출력 여부
  - `allow_delegation`: 다른 에이전트에게 작업 위임 허용 여부
  - `llm`: 사용할 언어 모델

### 2. Task (작업)
- **역할**: 에이전트가 수행할 구체적인 작업
- **주요 속성**:
  - `description`: 작업 설명 (구체적일수록 좋음)
  - `agent`: 작업을 수행할 에이전트
  - `expected_output`: 예상되는 결과물

### 3. Crew (팀)
- **역할**: 여러 에이전트와 작업을 하나의 팀으로 구성
- **주요 속성**:
  - `agents`: 팀에 속한 에이전트 목록
  - `tasks`: 수행할 작업 목록 (순서대로 실행됨)
  - `verbose`: 출력 상세도 (0: 최소, 1: 보통, 2: 상세)

## 실행 방법

```bash
cd /Users/charlee/Desktop/TIL/02-explore-agentic-frameworks/code_samples/crewai-practice
python3 simple_agent.py
```

## 예제 구조

```
simple_agent.py
├── 1. LLM 설정 (OpenAI GPT-3.5-turbo)
├── 2. 에이전트 생성
│   ├── 연구원 (Researcher)
│   └── 작가 (Writer)
├── 3. 작업 정의
│   ├── 연구 작업 (Research Task)
│   └── 작성 작업 (Writing Task)
├── 4. Crew 구성
└── 5. 실행 및 결과 저장
```

## 작동 방식

1. **연구 단계**:
   - 연구원 에이전트가 'AI 에이전트 프레임워크'에 대해 조사
   - 주요 프레임워크와 특징을 분석

2. **작성 단계**:
   - 작가 에이전트가 연구 결과를 받아서 블로그 포스트 작성
   - 마크다운 형식으로 구조화된 글 생성

3. **결과 저장**:
   - 최종 결과가 `agent_output.md` 파일로 저장됨

## 커스터마이징 방법

### 주제 변경
`research_task`의 `description`을 수정하세요:

```python
research_task = Task(
    description="""'당신이 원하는 주제'에 대해 조사하세요.
    다음 내용을 포함해야 합니다:
    - ...
    """,
    agent=researcher
)
```

### 에이전트 추가
새로운 에이전트를 만들고 Crew에 추가할 수 있습니다:

```python
editor = Agent(
    role='편집자',
    goal='작성된 글을 검토하고 개선합니다',
    backstory='...',
    llm=llm
)

editing_task = Task(
    description='작성된 글을 검토하고 개선점을 제안하세요',
    agent=editor
)

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task]
)
```

### LLM 모델 변경
다른 OpenAI 모델을 사용하거나 온도를 조정할 수 있습니다:

```python
llm = ChatOpenAI(
    model="gpt-4",  # 더 강력한 모델
    temperature=0.5  # 더 일관된 결과 (0.0 ~ 1.0)
)
```

## 참고사항

- OpenAI API를 사용하므로 API 요금이 부과됩니다
- 첫 실행 시 에이전트가 생각하는 과정이 모두 출력되므로 다소 시간이 걸릴 수 있습니다
- `verbose=True`를 통해 에이전트의 사고 과정을 실시간으로 확인할 수 있습니다

## 다음 단계

1. **도구(Tools) 추가**: 웹 검색, 파일 읽기 등의 도구를 에이전트에게 제공
2. **메모리 추가**: 에이전트가 이전 대화를 기억하도록 설정
3. **다양한 LLM 사용**: Anthropic Claude, Google Gemini 등 다른 LLM 통합
4. **복잡한 워크플로우**: 더 많은 에이전트와 작업을 조합

## 문제 해결

### OPENAI_API_KEY 오류
```
ValueError: OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.
```
→ `.env` 파일에 `OPENAI_API_KEY=your_key` 형식으로 추가하고, 파일이 프로젝트 루트에 있는지 확인하세요.

### 환경 변수 로드 문제
Python에서 `.env` 파일을 자동으로 로드하려면 `python-dotenv` 패키지를 설치하고 사용하세요:

```bash
pip3 install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()  # .env 파일 로드
```
