## git_exercise_2022(04/12~)

* Git 및 Github의 사용법을 다시 익히고, 이후 본인의 github 프로필을 원활하게 관리하기 위한 능력들을 연습한다.
* 원활한 git 운영을 위해 linux 명령어를 복습하면서 수행한다.

1. calculator.py & License 파일 생성 및 github에 저장 (commit message : "Create calculate")

   +) calculator.py의 경우 추가적인 수정을 통해 버전 변경

 ※ commit message('-m') 없이 commit 하기 : git commit -> 아래와 같은 메세지 출력
      ![image](https://user-images.githubusercontent.com/79882248/163896398-719fac5f-16e4-4f83-874d-1e059768d78b.png)
      
      -> #을 붙이지 않은 채 본인이 입력하고 싶은 commit message 입력
      -> 복잡하고 긴 commit message를 쉽게 남길 수 있음
      
(*) 노트북에서 한 작업 데스크탑에서 이어서 하기(4/14)
   - desktop의 local repository와 연결할 github의 원격 repository간 연동
   - git remote add (복사할 원격 repository address)
   - git clone 명령어를 통해 원격 repository의 내용 받아오기
   - git clone (복사할 원격 repository address)

2. manual README.md 파일을 만들어 원격 repository에 보내기
   - pull, push 명령어의 이해
   - git push : local repository → remote repository
   - git pull : remote repository → local repository
   - remote repository 사용 이유
     1. 안전성 : local repository에서의 돌발 상황(갑작스러운 삭제 등)에 대한 대처 가능
     2. 협업(Team Project) 가능

3. 다른 project 가져오기
   - git clone (복사할 github의 repository address) : github project의 repository를 그대로 복제

** Open Source Project
   - Source Code가 공개되어 있는 Project
   - numpy, Linux, MySQL Server 등
   - Source Code가 공개되어야 함
   - 누구나 code를 자유롭게 가져다가 사용할 수 있음
   - 원래의 코드를 자신이 원하는대로 수정할 수 있음
   - Open Source License
      - 기존의 open source 내용 중 조금이라도 사용한 부분이 있는 경우, 해당 부분을 표시하고 사용
      - open source가 활용되는 부분이 있는 Code는 Open Source로 공개해야 함
   - 장점
      - 무료로 사용 가능
      - 폐쇠적으로 Code를 관리하는 것 보다 Code의 신뢰도가 높을 수 있음(여러 개발자가 참여)
      - 프로젝트에 참여중인 다른 개발자들에게 질문을 할 수 있음
   - 단점
      - 참여자의 수가 적거나, 실력이 좋지 않은 경우 신뢰성이 낮아질 수 있음
      - Open Source의 문제 발생 시, 보상을 해주거나 책임을 질 주체가 없음

(+) Markdown 작성 시 참고 링크 : https://gist.github.com/ihoneymon/652be052a0727ad59601

4. commit history 살펴보기
   - git log : 해당 repository에서 진행하였던 commit 정보 출력
   ![image](https://user-images.githubusercontent.com/79882248/163896018-9c718af1-cbf4-41ff-9d52-372b65d2b5ac.png)

      - git log --pretty=oneline : commit 정보들을 한줄에 모두 출력
      ![image](https://user-images.githubusercontent.com/79882248/163895976-ba844d6f-2df2-4bb8-aa12-2c3a3b00f2a0.png)

   - git show (commit id 앞 4자리) : 해당 commit과 이전에 진행하였던 commit의 차이점을 보여줌
      - "---" : 해당 commit 이전의 모습
      - "+++" : 해당 commit에서의 모습

      ![image](https://user-images.githubusercontent.com/79882248/163895875-ead91e7d-b3a5-4e41-bdf8-e1b1bf28f536.png)

        

