# 태식이 봇 🐶

## 기능
| 명령어 | 설명 |
|--------|------|
| `태식봇 번역 on` / `태식봇 번역 온` | 현재 채널 번역 켜기 |
| `태식봇 번역 off` / `태식봇 번역 오프` | 현재 채널 번역 끄기 |

- 번역 ON 채널에서 메시지를 보내면 각 단어가 **월월월...** 로 변환됨
- 역할 ID `1520785215113662615` 를 가진 사람만 명령어 사용 가능

---

## 설치 방법

### 1. Python 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 디스코드 봇 토큰 설정
`.env` 파일을 만들거나, 아래처럼 환경변수 설정:

**Windows (CMD)**
```cmd
set DISCORD_TOKEN=여기에_토큰_붙여넣기
python bot.py
```

**Mac / Linux**
```bash
export DISCORD_TOKEN=여기에_토큰_붙여넣기
python bot.py
```

### 3. 디스코드 개발자 포털 설정
- https://discord.com/developers/applications 접속
- 봇 → **Message Content Intent** 반드시 활성화!

---

## 24시간 운영 (Railway 무료 배포)

1. GitHub에 이 폴더 올리기
2. https://railway.app 접속 → GitHub 연동
3. 리포 선택 후 배포
4. **Variables** 탭 → `DISCORD_TOKEN` 환경변수 추가
5. 끝! 컴퓨터 꺼도 봇이 살아있음 ✅

---

## 봇 초대 링크 만들기
개발자 포털 → OAuth2 → URL Generator
- Scopes: `bot`
- Bot Permissions: `Send Messages`, `Read Messages/View Channels`, `Manage Messages`
