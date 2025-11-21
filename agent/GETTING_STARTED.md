# CrewAI 시작하기 가이드

## ✅ API 키 테스트 완료!

OpenAI API 키가 정상적으로 작동하는 것을 확인했습니다. 이제 CrewAI 실습을 시작할 수 있습니다!

## 📚 CrewAI란?

**CrewAI**는 여러 AI 에이전트가 팀으로 협업하여 복잡한 작업을 수행하는 Python 프레임워크입니다.

### 핵심 개념

```
Crew (팀)
├── Agent 1 (연구원) → Task 1 (정보 조사)
├── Agent 2 (작가)   → Task 2 (글 작성)
└── Agent 3 (편집자) → Task 3 (검토 및 개선)
```

**3가지 핵심 요소**:
1. **Agent** - 특정 역할을 가진 AI 에이전트 (예: 연구원, 작가, 편집자)
2. **Task** - 에이전트가 수행할 구체적인 작업
3. **Crew** - 에이전트들을 하나의 팀으로 구성

### 실제 예시로 이해하기

블로그 포스트 작성 과정을 상상해보세요:

1. **연구원 에이전트** 📚
   - 역할: 주제에 대한 정보 수집
   - 작업: "AI 에이전트 프레임워크에 대해 조사하세요"
   - 결과: 구조화된 연구 자료

2. **작가 에이전트** ✍️
   - 역할: 정보를 바탕으로 글 작성
   - 작업: "연구 결과를 블로그 포스트로 작성하세요"
   - 결과: 완성된 블로그 글

3. **편집자 에이전트** 🔍
   - 역할: 글 검토 및 개선
   - 작업: "작성된 글을 검토하고 개선하세요"
   - 결과: 최종 완성본

## 🚀 실습 시작하기

### 방법 1: Jupyter 노트북 (추천! 초보자에게 최적)

대화형으로 단계별로 학습하며 실행할 수 있습니다.

```bash
cd agent/code_samples/crewai-practice
jupyter notebook crewai_tutorial.ipynb
```

**장점**:
- 각 단계를 실행하면서 결과 확인 가능
- 설명과 코드가 함께 있어서 이해하기 쉬움
- 중간에 멈추고 수정하면서 실험 가능

### 방법 2: Python 스크립트

전체 프로세스를 한 번에 실행합니다.

```bash
cd agent/code_samples/crewai-practice
python3 simple_agent.py
```

**주의**: 실행 시 다음 경고는 무시해도 됩니다:
```
NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+
```

## 📖 CrewAI 실습 내용

### 기본 예제: 2-에이전트 협업

**시나리오**: 연구원이 조사하고 작가가 글을 쓰는 간단한 워크플로우

```python
# 1. 연구원 에이전트 생성
researcher = Agent(
    role='연구원',
    goal='주어진 주제에 대해 깊이 있는 정보를 수집하고 분석합니다',
    backstory='당신은 경험이 풍부한 연구원입니다.',
    llm=llm
)

# 2. 작가 에이전트 생성
writer = Agent(
    role='기술 작가',
    goal='연구 내용을 명확하고 이해하기 쉬운 글로 작성합니다',
    backstory='당신은 기술 문서 작성 전문가입니다.',
    llm=llm
)

# 3. 작업 정의
research_task = Task(
    description="'AI 에이전트'에 대해 조사하세요",
    agent=researcher
)

writing_task = Task(
    description="연구 결과를 블로그 포스트로 작성하세요",
    agent=writer
)

# 4. Crew 구성 및 실행
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task]
)

result = crew.kickoff()  # 실행!
```

### 고급 예제: 3-에이전트 협업

**시나리오**: 연구 → 작성 → 편집의 3단계 워크플로우

편집자 에이전트를 추가하여 더 완성도 높은 결과물을 만듭니다.

## 💡 CrewAI의 강력한 점

### 1. 역할 분담으로 효율성 증대

각 에이전트가 자신의 전문 분야에 집중하므로 전체 작업의 품질이 향상됩니다.

**예시**:
- ❌ 나쁜 방법: 하나의 AI에게 "조사부터 편집까지 다 해줘"
- ✅ 좋은 방법: 연구원 → 작가 → 편집자 순서로 역할 분담

### 2. 자동화된 워크플로우

한 번 설정하면 자동으로 순차적으로 실행됩니다.

```
연구원 작업 완료 → 결과를 작가에게 전달 → 작가 작업 완료 → 결과를 편집자에게 전달
```

### 3. 유연한 커스터마이징

```python
# 주제 변경
research_task = Task(
    description="'LangChain'에 대해 조사하세요",  # 원하는 주제로 변경
    agent=researcher
)

# 모델 변경
llm = ChatOpenAI(
    model="gpt-4",      # 더 강력한 모델 사용
    temperature=0.3     # 창의성 조절 (0.0~1.0)
)

# 에이전트 추가
reviewer = Agent(
    role='리뷰어',
    goal='기술적 정확성을 검증합니다'
)
```

## 🎯 실습 목표별 추천 경로

### 목표 1: CrewAI 개념 이해하기
1. **README.md** 읽기 - 핵심 개념 파악
2. **이 문서** 읽기 - 전체 흐름 이해
3. **crewai_tutorial.ipynb** 1-6번 셀 실행 - 기본 설정 확인

### 목표 2: 간단한 예제 실행해보기
1. **crewai_tutorial.ipynb** 전체 실행
2. 결과 확인 - `crewai_output.md` 파일 확인
3. 주제 바꿔서 다시 실행 (8번 실습 섹션)

### 목표 3: 나만의 에이전트 만들기
1. 기본 예제를 이해했다면
2. 새로운 에이전트 추가 (9번 고급 실습)
3. 완전히 다른 주제로 실습
   - 예: 영화 리뷰 작성 (연구원 → 리뷰어 → 편집자)
   - 예: 여행 계획 수립 (조사원 → 기획자 → 예산 관리자)

## 🔧 문제 해결

### 문제 1: `.env` 파일을 못 찾음

**해결**:
```bash
# 현재 위치 확인
pwd

# 프로젝트 루트로 이동
cd /Users/charlee/Desktop/TIL

# .env 파일 확인
cat .env
```

### 문제 2: CrewAI import 오류

```
TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'
```

**원인**: Python 3.9에서 타입 힌트 문제

**해결**:
```bash
# Python 3.10+ 사용 권장
python3 --version

# 또는 최신 버전의 CrewAI 설치
pip3 install 'crewai>=0.28.0'
```

### 문제 3: API 호출 실패

```
Error code: 401 - invalid_api_key
```

**해결**:
1. API 키 확인: https://platform.openai.com/api-keys
2. 사용량 확인: https://platform.openai.com/usage
3. `.env` 파일에 올바른 키 저장 확인

## 📚 다음 학습 단계

CrewAI를 마스터했다면:

1. **도구(Tools) 추가**
   - 웹 검색 도구로 실시간 정보 수집
   - 파일 읽기/쓰기 도구
   - API 호출 도구

2. **메모리 기능**
   - 이전 대화 기억하기
   - 장기 메모리 활용

3. **다른 LLM 통합**
   - Claude (Anthropic)
   - Gemini (Google)
   - 로컬 LLM (Ollama)

4. **실전 프로젝트**
   - 자동 블로그 작성 시스템
   - 코드 리뷰 자동화
   - 데이터 분석 및 리포트 생성

## 🎓 학습 리소스

### 공식 문서
- [CrewAI 공식 문서](https://docs.crewai.com/)
- [CrewAI 예제 모음](https://github.com/joaomdmoura/crewAI-examples)

### 관련 프레임워크 비교
- **AutoGen** - 이벤트 기반, 분산 에이전트 시스템
- **LangGraph** - 그래프 기반 워크플로우
- **Semantic Kernel** - 엔터프라이즈급 AI 오케스트레이션

**CrewAI의 장점**:
- 간단하고 직관적인 API
- 역할 기반 설계로 이해하기 쉬움
- 빠른 프로토타이핑에 적합

## ✨ 실습을 시작하세요!

```bash
# 1. Jupyter 노트북 실행 (추천)
cd agent/code_samples/crewai-practice
jupyter notebook crewai_tutorial.ipynb

# 2. 또는 Python 스크립트 실행
python3 simple_agent.py
```

**Tip**: 노트북을 실행하면서 각 셀의 출력을 확인하고, 코드를 수정해가며 실험해보세요.
이것이 가장 효과적인 학습 방법입니다! 🚀
