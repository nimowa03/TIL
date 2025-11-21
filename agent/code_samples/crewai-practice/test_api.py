"""
OpenAI API 키 테스트 스크립트
CrewAI를 실행하기 전에 API 키가 제대로 작동하는지 확인합니다.
"""
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

print("=" * 60)
print("OpenAI API 키 테스트")
print("=" * 60)

# 1. API 키 확인
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("❌ OPENAI_API_KEY가 설정되지 않았습니다.")
    print("   .env 파일에 API 키를 추가하세요.")
    exit(1)

print(f"✅ API 키가 설정되었습니다: {api_key[:20]}...")

# 2. OpenAI 라이브러리 import 테스트
try:
    from langchain_openai import ChatOpenAI
    print("✅ langchain_openai 라이브러리가 설치되어 있습니다.")
except ImportError:
    print("❌ langchain_openai가 설치되지 않았습니다.")
    print("   다음 명령어로 설치하세요: pip install langchain-openai")
    exit(1)

# 3. 간단한 API 호출 테스트
print("\n" + "=" * 60)
print("OpenAI API 연결 테스트 중...")
print("=" * 60)

try:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=api_key
    )

    # 간단한 테스트 메시지
    from langchain_core.messages import HumanMessage

    messages = [HumanMessage(content="안녕하세요! 간단히 인사해주세요.")]
    response = llm.invoke(messages)

    print("✅ API 연결 성공!")
    print(f"\n응답: {response.content}\n")

    print("=" * 60)
    print("🎉 OpenAI API 테스트 통과!")
    print("=" * 60)

    print("\n다음 단계:")
    print("1. CrewAI 설치: pip3 install 'crewai>=0.28.0'")
    print("2. Jupyter 노트북 실행: jupyter notebook crewai_tutorial.ipynb")
    print("   또는")
    print("3. Python 스크립트 실행: python3 simple_agent.py")

except Exception as e:
    print(f"❌ API 호출 실패: {e}")
    print("\nAPI 키가 유효한지 확인하세요:")
    print("1. https://platform.openai.com/api-keys 에서 키 확인")
    print("2. 사용량 제한이 남아있는지 확인")
    print("3. API 키가 정확히 복사되었는지 확인")
    exit(1)
