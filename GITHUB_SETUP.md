# GitHub 연결 가이드

## 1단계: GitHub 저장소 생성

1. https://github.com 에 로그인
2. 우측 상단 "+" 버튼 클릭 → "New repository" 선택
3. Repository 이름 입력 (예: `portfolio` 또는 `streamlit-portfolio`)
4. **Public** 또는 **Private** 선택
5. ⚠️ **중요**: "Add a README file", "Add .gitignore", "Choose a license"는 모두 **체크하지 마세요** (이미 로컬에 파일이 있음)
6. "Create repository" 클릭

## 2단계: 저장소 URL 복사

생성된 저장소 페이지에서 초록색 "Code" 버튼을 클릭하고 HTTPS URL을 복사하세요.
예: `https://github.com/사용자명/저장소명.git`

## 3단계: 로컬 저장소와 연결

터미널에서 다음 명령어를 실행하세요 (URL은 본인의 것으로 변경):

```bash
git remote add origin https://github.com/사용자명/저장소명.git
git branch -M main
git push -u origin main
```

## 완료!

이제 GitHub에서 코드를 확인할 수 있습니다!

