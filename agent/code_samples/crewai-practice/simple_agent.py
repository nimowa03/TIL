"""
CrewAI 간단한 에이전트 예제
이 예제는 연구 에이전트와 작성 에이전트가 협업하여 주제에 대한 리포트를 작성합니다.
"""
import os
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# OpenAI API 키 설정 (환경 변수에서 가져옴)
# .env 파일에 OPENAI_API_KEY=your_key_here 형식으로 저장해야 합니다
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")

# LLM 설정
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=api_key
)

# 1. 연구 에이전트 생성
researcher = Agent(
    role='연구원',
    goal='주어진 주제에 대해 깊이 있는 정보를 수집하고 분석합니다',
    backstory="""당신은 경험이 풍부한 연구원입니다.
    복잡한 주제를 이해하기 쉽게 정리하는 능력이 뛰어납니다.
    항상 정확하고 신뢰할 수 있는 정보를 제공합니다.""",
    verbose=True,  # 에이전트의 작업 과정을 출력
    allow_delegation=False,  # 다른 에이전트에게 작업 위임 허용 여부
    llm=llm
)

# 2. 작성 에이전트 생성
writer = Agent(
    role='기술 작가',
    goal='연구 내용을 바탕으로 명확하고 이해하기 쉬운 글을 작성합니다',
    backstory="""당신은 기술 문서 작성 전문가입니다.
    복잡한 기술 개념을 일반인도 이해할 수 있도록 쉽게 설명합니다.
    구조화되고 논리적인 글쓰기를 선호합니다.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. 작업(Task) 정의
research_task = Task(
    description="""'AI 에이전트 프레임워크'에 대해 조사하세요.
    다음 내용을 포함해야 합니다:
    - AI 에이전트 프레임워크란 무엇인가?
    - 주요 프레임워크 3가지
    - 각 프레임워크의 특징

    간결하고 핵심적인 정보만 포함하세요.""",
    agent=researcher,
    expected_output="AI 에이전트 프레임워크에 대한 구조화된 연구 결과"
)

writing_task = Task(
    description="""연구원의 조사 결과를 바탕으로 블로그 포스트를 작성하세요.
    다음 구조를 따르세요:
    1. 서론: AI 에이전트 프레임워크 소개
    2. 본론: 주요 프레임워크 설명
    3. 결론: 프레임워크 선택 가이드

    한국어로 작성하고, 마크다운 형식을 사용하세요.""",
    agent=writer,
    expected_output="AI 에이전트 프레임워크에 대한 완성된 블로그 포스트 (마크다운 형식)"
)

# 4. Crew 생성 (에이전트들을 하나의 팀으로 구성)
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True  # True: 상세 출력, False: 최소 출력
)

# 5. Crew 실행
if __name__ == "__main__":
    print("="*50)
    print("CrewAI 에이전트 실행 시작")
    print("="*50)

    try:
        result = crew.kickoff()

        print("\n" + "="*50)
        print("최종 결과:")
        print("="*50)
        print(result)

        # 결과를 파일로 저장
        with open('agent_output.md', 'w', encoding='utf-8') as f:
            f.write(result)
        print("\n결과가 'agent_output.md' 파일로 저장되었습니다.")

    except Exception as e:
        print(f"\n오류 발생: {e}")
        print("OPENAI_API_KEY가 .env 파일에 올바르게 설정되어 있는지 확인하세요.")
