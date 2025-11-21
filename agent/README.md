# CrewAI 실습 가이드

AI 에이전트 프레임워크 중 하나인 **CrewAI**를 학습하고 실습하기 위한 저장소입니다.

## 목차

- [CrewAI란?](#crewai란)
- [설치](#설치)
- [핵심 개념](#핵심-개념)
- [실습 가이드](#실습-가이드)
- [디렉토리 구조](#디렉토리-구조)
- [참고 자료](#참고-자료)

## CrewAI란?

CrewAI는 여러 AI 에이전트가 협업하여 복잡한 작업을 수행할 수 있도록 설계된 Python 프레임워크입니다.

### 주요 특징

- **멀티 에이전트 협업**: 각기 다른 역할을 가진 여러 에이전트가 팀으로 협력
- **역할 기반 설계**: 각 에이전트에게 특정 역할과 목표 부여
- **순차적 작업 실행**: 작업을 순서대로 실행하며 이전 결과를 다음 작업에 전달
- **유연한 통합**: OpenAI, Anthropic 등 다양한 LLM 지원

### 왜 CrewAI를 사용하나요?

CrewAI는 복잡한 작업을 작은 단위로 나누고, 각 단위를 전문화된 에이전트에게 할당할 수 있게 해줍니다. 마치 실제 팀이 협업하듯이 AI 에이전트들이 함께 작업할 수 있습니다.

## 설치

### 1. CrewAI 설치

```bash
pip install crewai
```

### 2. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 OpenAI API 키를 추가하세요:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## 핵심 개념

CrewAI의 세 가지 핵심 개념을 이해하는 것이 중요합니다:

### 1. Agent (에이전트)

특정 역할과 목표를 가진 AI 에이전트입니다.

**주요 속성**:
- `role`: 에이전트의 역할 (예: "연구원", "작가", "편집자")
- `goal`: 에이전트가 달성하려는 목표
- `backstory`: 에이전트의 배경 스토리 (페르소나 정의)
- `verbose`: 작업 과정을 출력할지 여부
- `allow_delegation`: 다른 에이전트에게 작업 위임 허용 여부
- `llm`: 사용할 언어 모델

**예시**:
```python
researcher = Agent(
    role='연구원',
    goal='주어진 주제에 대해 깊이 있는 정보를 수집하고 분석합니다',
    backstory='당신은 경험이 풍부한 연구원입니다.',
    verbose=True,
    llm=llm
)
```

### 2. Task (작업)

에이전트가 수행할 구체적인 작업입니다.

**주요 속성**:
- `description`: 작업에 대한 상세한 설명
- `agent`: 이 작업을 수행할 에이전트
- `expected_output`: 예상되는 결과물

**예시**:
```python
research_task = Task(
    description="AI 에이전트 프레임워크에 대해 조사하세요.",
    agent=researcher,
    expected_output="AI 에이전트 프레임워크에 대한 구조화된 연구 결과"
)
```

### 3. Crew (팀)

여러 에이전트와 작업을 하나의 팀으로 구성합니다.

**주요 속성**:
- `agents`: 팀에 속한 에이전트 목록
- `tasks`: 수행할 작업 목록 (순서대로 실행됨)
- `verbose`: 작업 과정 출력 여부 (True/False)

**예시**:
```python
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True  # True: 상세 출력, False: 최소 출력
)

# 실행
result = crew.kickoff()
```

## 실습 가이드

### 방법 1: Jupyter 노트북으로 실습 (추천)

단계별 설명과 함께 대화형으로 학습할 수 있습니다.

```bash
cd code_samples/crewai-practice
jupyter notebook crewai_tutorial.ipynb
```

### 방법 2: Python 스크립트 실행

```bash
cd code_samples/crewai-practice
python3 simple_agent.py
```

### 실습 내용

#### 기본 예제
- 2개의 에이전트 (연구원 + 작가) 협업
- AI 에이전트 프레임워크 주제로 블로그 포스트 작성
- 결과를 마크다운 파일로 저장

#### 고급 예제
- 3개의 에이전트 (연구원 + 작가 + 편집자) 협업
- 3단계 워크플로우: 연구 → 작성 → 편집
- 주제 커스터마이징 실습

## 디렉토리 구조

```
agent/
├── README.md                          # 이 파일
└── code_samples/
    └── crewai-practice/
        ├── README.md                  # CrewAI 실습 상세 가이드
        ├── crewai_tutorial.ipynb      # Jupyter 노트북 (추천)
        └── simple_agent.py            # Python 스크립트 버전
```

## 실습 예제 상세

### 예제 1: 간단한 2-에이전트 시스템

**시나리오**: 연구원이 정보를 조사하고, 작가가 블로그 포스트를 작성

**워크플로우**:
1. 연구원 에이전트 → "AI 에이전트 프레임워크" 조사
2. 작가 에이전트 → 조사 결과를 바탕으로 블로그 포스트 작성

**학습 포인트**:
- Agent 생성 방법
- Task 정의 방법
- Crew로 팀 구성 및 실행

### 예제 2: 3-에이전트 협업 시스템

**시나리오**: 연구 → 작성 → 편집 워크플로우

**워크플로우**:
1. 연구원 → 정보 조사
2. 작가 → 글 작성
3. 편집자 → 검토 및 개선

**학습 포인트**:
- 복잡한 워크플로우 설계
- 에이전트 간 결과물 전달
- 역할 분담의 효율성

## 커스터마이징

### 주제 변경

`research_task`의 `description`을 수정하여 원하는 주제로 변경:

```python
research_task = Task(
    description="'LangChain의 주요 기능'에 대해 조사하세요.",
    agent=researcher
)
```

### LLM 모델 변경

다른 모델 사용 또는 온도 조정:

```python
llm = ChatOpenAI(
    model="gpt-4",      # 더 강력한 모델
    temperature=0.5     # 더 일관된 결과 (0.0 ~ 1.0)
)
```

### 에이전트 추가

새로운 역할의 에이전트 생성:

```python
reviewer = Agent(
    role='리뷰어',
    goal='작성된 글의 정확성을 검증합니다',
    backstory='당신은 기술 검토 전문가입니다.',
    llm=llm
)
```

## 문제 해결

### API 키 오류

```
ValueError: OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.
```

**해결**: `.env` 파일에 `OPENAI_API_KEY=your_key` 형식으로 추가

### .env 파일 로드 문제

**해결**: `python-dotenv` 설치 및 사용

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()
```

## 다음 단계

CrewAI를 더 깊이 학습하려면:

1. **도구(Tools) 추가**: 웹 검색, 파일 읽기 등의 도구를 에이전트에게 제공
2. **메모리 기능**: 에이전트가 이전 대화를 기억하도록 설정
3. **다양한 LLM**: Claude, Gemini 등 다른 모델 통합
4. **실전 프로젝트**: 실제 문제를 해결하는 에이전트 시스템 구축

## 참고 자료

### 공식 문서
- [CrewAI 공식 문서](https://docs.crewai.com/)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)
- [LangChain 문서](https://python.langchain.com/)

### 관련 프레임워크
- [AutoGen](https://microsoft.github.io/autogen/) - Microsoft의 멀티 에이전트 프레임워크
- [LangGraph](https://langchain-ai.github.io/langgraph/) - LangChain의 그래프 기반 워크플로우
- [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/) - Microsoft의 AI 오케스트레이션 SDK

## 라이선스

이 저장소는 학습 목적으로 작성되었습니다.
