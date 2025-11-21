# CrewAI 문제 해결 가이드

## ✅ 수정 완료된 오류

### 오류 1: verbose 파라미터 오류

**오류 메시지**:
```
ValidationError: 1 validation error for Crew
verbose
  Input should be a valid boolean, unable to interpret input [type=bool_parsing, input_value=2, input_type=int]
```

**원인**: CrewAI 최신 버전(0.5.0+)에서 `verbose` 파라미터가 정수(0, 1, 2)에서 불리언(True/False)으로 변경됨

**해결**: ✅ **모든 파일 수정 완료**

수정 전:
```python
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=2  # ❌ 오류 발생
)
```

수정 후:
```python
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True  # ✅ 정상 작동
)
```

**수정된 파일들**:
- ✅ [crewai_tutorial.ipynb](code_samples/crewai-practice/crewai_tutorial.ipynb) - 셀 15, 21, 23
- ✅ [simple_agent.py](code_samples/crewai-practice/simple_agent.py) - 라인 75
- ✅ [README.md](README.md) - 라인 97-105

---

## ⚠️ Python 버전 호환성 문제

### 오류 2: Python 3.9 타입 힌트 오류

**오류 메시지**:
```
TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'
```

**원인**: CrewAI 0.5.0이 Python 3.10+의 타입 힌트 문법 사용 (`str | None`)

**현재 Python 버전 확인**:
```bash
python3 --version
```

### 해결 방법

#### 방법 1: Python 3.10+ 사용 (권장)

**macOS (Homebrew 사용)**:
```bash
# Python 3.11 설치
brew install python@3.11

# 버전 확인
python3.11 --version

# CrewAI 설치
pip3.11 install crewai python-dotenv langchain-openai
```

**실행 시**:
```bash
# Jupyter
python3.11 -m jupyter notebook crewai_tutorial.ipynb

# Python 스크립트
python3.11 simple_agent.py
```

#### 방법 2: 이전 버전 CrewAI 사용 (임시 방편)

Python 3.9를 계속 사용해야 한다면:

```bash
# 현재 버전 제거
pip3 uninstall crewai

# 이전 버전 설치 (Python 3.9 호환)
pip3 install 'crewai<0.5.0'
```

**주의**: 이전 버전에서는 `verbose=2` 형식을 사용해야 할 수 있습니다.

---

## 🔧 기타 문제 해결

### 문제 3: API 키 인식 안 됨

**증상**:
```
OPENAI_API_KEY가 설정되지 않았습니다
```

**해결**:

1. `.env` 파일 위치 확인:
```bash
cd /Users/charlee/Desktop/TIL
cat .env
```

2. 환경 변수 직접 설정:
```bash
export OPENAI_API_KEY="your_actual_api_key"
python3 agent/code_samples/crewai-practice/simple_agent.py
```

3. Python 스크립트에서 직접 설정 (테스트용):
```python
import os
os.environ['OPENAI_API_KEY'] = 'your_actual_api_key'
```

### 문제 4: Jupyter가 .env 파일을 못 읽음

**해결**:

1. Jupyter를 프로젝트 루트에서 실행:
```bash
cd /Users/charlee/Desktop/TIL
jupyter notebook agent/code_samples/crewai-practice/crewai_tutorial.ipynb
```

2. 또는 노트북 셀에서 절대 경로 사용:
```python
from dotenv import load_dotenv
import os

# 절대 경로로 .env 파일 로드
env_path = '/Users/charlee/Desktop/TIL/.env'
load_dotenv(env_path)

api_key = os.getenv('OPENAI_API_KEY')
```

### 문제 5: OpenSSL 경고

**경고 메시지**:
```
NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+
```

**상태**: ⚠️ 무시해도 됨 (기능에 영향 없음)

**원인**: macOS 시스템 Python이 LibreSSL 사용

**영향**: 경고만 표시되고 실제 기능은 정상 작동

**제거하려면** (선택사항):
```bash
# Homebrew Python 사용
brew install python@3.11
pip3.11 install --upgrade urllib3
```

---

## 📋 전체 환경 점검 체크리스트

실습 전에 다음 사항들을 확인하세요:

### 1. Python 버전
```bash
python3 --version
```
- ✅ Python 3.10 이상 (권장)
- ⚠️ Python 3.9 (CrewAI 이전 버전 필요)
- ❌ Python 3.8 이하 (지원 안 됨)

### 2. 패키지 설치
```bash
pip3 list | grep -E "crewai|langchain|dotenv"
```
필요한 패키지:
- ✅ crewai (0.5.0 이상, Python 3.10+)
- ✅ langchain-openai
- ✅ python-dotenv

### 3. API 키 설정
```bash
cd /Users/charlee/Desktop/TIL
cat .env | grep OPENAI_API_KEY
```
- ✅ API 키가 `sk-`로 시작
- ✅ `.env` 파일이 프로젝트 루트에 위치

### 4. API 키 테스트
```bash
cd agent/code_samples/crewai-practice
python3 test_api.py
```
예상 결과:
```
✅ API 연결 성공!
응답: 안녕하세요! 만나서 반가워요...
```

---

## 🚀 권장 실행 순서

### Step 1: 환경 확인
```bash
# Python 버전 확인
python3 --version

# Python 3.9라면 3.10+ 설치 권장
brew install python@3.11
```

### Step 2: 패키지 설치
```bash
# Python 3.10+ 사용 시
pip3 install crewai python-dotenv langchain-openai

# Python 3.9 사용 시 (임시)
pip3 install 'crewai<0.5.0' python-dotenv langchain-openai
```

### Step 3: API 키 테스트
```bash
cd /Users/charlee/Desktop/TIL/agent/code_samples/crewai-practice
python3 test_api.py
```

### Step 4: 실습 시작
```bash
# Jupyter 노트북 (추천)
jupyter notebook crewai_tutorial.ipynb

# 또는 Python 스크립트
python3 simple_agent.py
```

---

## 💡 도움이 필요하면

1. **Python 버전 문제**: Python 3.11 설치 권장
2. **API 키 문제**: [test_api.py](code_samples/crewai-practice/test_api.py) 실행
3. **CrewAI 오류**: [quick_test.py](code_samples/crewai-practice/quick_test.py)로 설정 확인

모든 문제가 해결되면:
- ✅ `test_api.py` 통과
- ✅ `quick_test.py` 통과
- ✅ 실습 시작 준비 완료!
