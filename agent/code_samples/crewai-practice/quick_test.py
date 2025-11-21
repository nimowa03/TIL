"""
CrewAI 빠른 테스트 - verbose 오류 수정 확인
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("CrewAI 설정 테스트")
print("=" * 60)

# 1. API 키 확인
api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    print(f"✅ API 키 설정됨: {api_key[:20]}...")
else:
    print("❌ API 키가 설정되지 않음")
    exit(1)

# 2. 라이브러리 import
try:
    from crewai import Agent, Task, Crew
    from langchain_openai import ChatOpenAI
    print("✅ 라이브러리 import 성공")
except Exception as e:
    print(f"❌ Import 실패: {e}")
    exit(1)

# 3. 간단한 Crew 생성 테스트
try:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=api_key
    )

    agent = Agent(
        role='테스터',
        goal='간단한 테스트',
        backstory='테스트용 에이전트',
        verbose=True,  # Boolean 값으로 수정
        llm=llm
    )

    task = Task(
        description='간단한 인사를 해주세요',
        agent=agent,
        expected_output='인사말'
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True  # Boolean 값으로 수정 (이전에는 2였음)
    )

    print("✅ Crew 생성 성공 (verbose=True)")
    print(f"   - 에이전트 수: {len(crew.agents)}")
    print(f"   - 작업 수: {len(crew.tasks)}")

    print("\n" + "=" * 60)
    print("🎉 모든 설정이 정상입니다!")
    print("=" * 60)
    print("\n이제 실제 예제를 실행할 수 있습니다:")
    print("1. jupyter notebook crewai_tutorial.ipynb")
    print("2. python3 simple_agent.py")

except Exception as e:
    print(f"❌ Crew 생성 실패: {e}")
    print(f"\n오류 타입: {type(e).__name__}")
    exit(1)
