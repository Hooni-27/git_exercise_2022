## git_exercise_2022(04/12~)

* Git 및 Github의 사용법을 다시 익히고, 이후 본인의 github 프로필을 원활하게 관리하기 위한 능력들을 연습한다.
* 원활한 git 운영을 위해 linux 명령어를 복습하면서 수행한다.

1. calculator.py & License 파일 생성 및 github에 저장 (commit message : "Create calculate")

   +) calculator.py의 경우 추가적인 수정을 통해 버전 변경

 ※ commit message('-m') 없이 commit 하기 : git commit -> 아래와 같은 메세지 출력
      ![image](https://user-images.githubusercontent.com/79882248/163896398-719fac5f-16e4-4f83-874d-1e059768d78b.png)
      
      -> #을 붙이지 않은 채 본인이 입력하고 싶은 commit message 입력
      -> 복잡하고 긴 commit message를 쉽게 남길 수 있음
      
 ※ git commit --amend : 최신 commit을 수정해서 다시 새로운 commit으로 만들기
 
 
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


* 긴 Command에 alias 설정 (git config)
   - git log --pretty=oneline -> git history로 설정
   - git config alias.history "log --pretty=oneline"
  
5. 두 Commit 간의 차이 보기(git diff)
   - git diff (이전 commit id 앞 4자리) (앞 commit id 앞 4자리)

6. git에서 HEAD의 의미
   - HEAD : 어떤 Commit 하나를 가리킴
      -> 보통 가장 최근에 한 Commit을 가리킴
   - HEAD의 중요성
      - Working Directory / Working Tree의 내부 => HEAD가 가리키는 commit에 따라 구성
   - git reset : 이전에 하였던 commit을 가리키도록 하는 명령어
      - git reset --hard (가고싶은 commit id 앞 4자리) : 가고싶은 commit으로 HEAD 이동
      - git reset을 통해 HEAD가 과거의 commit을 가리키게 할 수 있음
      - Working Directory의 내용도 과거 commit의 모습으로 돌아가게 할 수 있음
   - --hard, --soft, --mixed
      - HEAD가 working directory, staging area, repository 중 어디 영역까지 reset하는지에 따라 구분
      - ![image](https://user-images.githubusercontent.com/79882248/163928821-b9acacb2-541d-462a-8cc5-1f18e8e501d5.png)
   - reset 전 상태로의 복구 : git pull 사용(단, 이전 내용에 대해 git push가 이루어져야 함)
   - HEAD 기준 reset
      - HEAD^ : HEAD 바로 이전 commit을 나타냄
      - HEAD~n : HEAD 보다 n번째 전에 있는 commit을 나타냄
   - commit message 이외에 tag 달기
      - git tag [tag name] [commit id]
      - project directory에 있는 모든 tag 조회 : git tag
      - 각 tag와  연결된 commit 확인 : git show [tag name]

5. Branch
   - 하나의 code 관리 흐름
   - branch 생성 : git branch [branch name]
      - 생성 된 branch로 바로 이동 : git checkout -b [bramch name]
   - 만든 branch로의 이동 : git checkout [가고싶은 branch name]
   - branch 조회 : git branch
   - branch 삭제 : git branch -d [삭제할 branch name]
   - branch의 Merge(병합) : git merge [합치고 싶은 branch] -> 다른 branch에서의 내용을 가져와야할 때 사용하기 유용
      - merge 시 comflict이 나는 경우 : 합치고자 하는 branch와 target branch 간의 충돌 발생(두가지 중 무엇을 반영해야하는지 모름)
      - ![image](https://user-images.githubusercontent.com/79882248/165004082-11100c68-fb20-47ff-a942-d247801d69f9.png)
      - 해결 방법1
         1. conflict가 발생한 file을 연다
         2. merge의 결과가 되었으면 하는 모습대로 code를 수정한다
         3. 수정 후 commit
      - 해결 방법2 : merge의 작업 취소
         - git merge --abort
         - confilct가 발생한 file들이 너무 많아, conflict를 최소화할 수 있는 방식으로 file들을 다시 수정하고 commit한 뒤 merge를 진행하고 싶은 경우
         - 좀 더 이후에 merge하고 싶은 경우 유용
      - 단일 file이 아닌 여러개의 file에서 conflict가 발생한 경우
         - 파일 하나씩 confilct를 해결 후 git add [file name]을 통해 "하나씩" staging area에 올린다
         - 모든 file들의 conflict들을 다 해결하고, git add . 를 통해 한번에 staging area에 올린다
   - HEAD와 Branch의 관계
      - HEAD : 어떤 commit 하나를 가리킴
      - branch : 하나의 코드 관리 흐름
      - ![image](https://user-images.githubusercontent.com/79882248/165007548-0ffc076e-7590-45a1-8b97-282fcb30b6dd.png)
      - HEAD는 master branch를 통해 간접적으로 commit을 가리킴
      - ![image](https://user-images.githubusercontent.com/79882248/165007665-06f241e5-ec68-4d6c-b047-3d5505bfcd63.png)
      - Merge Commit
      - ![image](https://user-images.githubusercontent.com/79882248/165007934-9f273961-8f8c-4431-b1a6-6bcc40b1b523.png)
      - git reset command의 원리
         1. HEAD는 여전히 같은 branch(master)를 가리킴
         2. HEAD가 가리키는 branch가 다른 특정 commit을 가리킴
         => HEAD가 간접적으로 가리키던 commit도 바뀌게 됨
         => 과거의 commit으로 git reset 하여도, 이후 commit들이 삭제되지 않고 유지됨
         => git reset은 현재 HEAD가 가리키는 commit 이후의 commmit으로도 이동할 수 있음
   - git checkout과 git reset의 차이
      - git checkout : HEAD가 commit을 직접적으로 가리키게 할 수 있음 + branch를 직접 가리키게 만들 수 있음
      - git reset : HEAD는 branch를 통해서 간접적으로 commit을 가리킴
      - ![image](https://user-images.githubusercontent.com/79882248/165010152-5b952b20-17f2-4d36-9f87-71a794ee49b8.png)
   - merge
      - Fast-forward Merge
         - 새로운 commit이 생기는게 아닌 branch가 이동하게 되는 merge
         - commit history에서 같은 line 상에 있는 branch를 merge할 경우 발생
         - ![image](https://user-images.githubusercontent.com/79882248/165012278-0f5df243-9d17-4c63-b261-95a31a53bec2.png)

      - 3-way Merge
         - 3가지의 commmit을 고려해서 merge 실행
         - ![image](https://user-images.githubusercontent.com/79882248/165012349-294d3177-c3ba-45ef-bc3b-f61211fe529b.png)
            1. 두 갈래로 갈라지기 전 공통 조상이 되는 commit
            2. 한 branch가 가리키는 commit
            3. 다른 branch가 가리키는 commit
            => 해당 commit들을 기준으로 merge commit을 자동으로 만들어 냄

6. 실무에서 Git과 GitHub
   - git pull : remote repositor의 branch를 검토할 필요없이 바로 merge하고 싶은 경우 사용
   - git fetch : merge를 하지 않고, 가져오는것만 진행
      - remote repository에 있는 branch의 내용을 일단 가져와서 살펴본 후, merge하고 싶을 때 사용
      - git diff (local) (remote) : 차이점 확인
   - git blame (확인하고자 하는 file) : 어떤 파일의 특정 코드를 누가 작성했는지 찾아내기 위한 command
   - git show (확인하고자 하는 commit id) : 해당 commit에 해당하는 code의 변경점 확인
   - 이미 remote repository에 올라간 commit을 취소해야하는 경우
      - git revert [되돌리고 싶은 commit의 id]
      - local repository에서만 작업을 하는 경우 : reset으로도 해결 가능
      - ![image](https://user-images.githubusercontent.com/79882248/165198274-3a8cec0b-55ec-45bf-b4df-3ea0dd0c2230.png)
         -> 해당 상태에서는 git push를 실행할 수 없음 : remote repository보다 한단계 아래의 commit에 있기 때문
      - ![image](https://user-images.githubusercontent.com/79882248/165198425-3c4b17dc-f676-47cb-ab4d-09d9638218c8.png)
   - 여러 commit 취소하기(git revert의 범위 지정)
      - git revert (되돌리고 싶은 commit id의 이전 id)..(취소할 commit id의 끝 범위)
      - ![image](https://user-images.githubusercontent.com/79882248/165198700-473176aa-1121-4213-aba3-5369a9c41bc1.png)
         -> 이떄, "facd...." commit은 포함되지 않는다 

7. Git 활용
   - git reset 후 다시 돌아오기
      - git reset (--hard/--mixed/--soft) [최신 commit id or 돌아가고 싶은 commit id]
      - reset을 해도 그 이후 commit들이 삭제되는 것은 아님
      - 최신 commit id를 모르는 경우 : git reflog
   - commit history를 보는 다양한 방법(git log --pretty=oneline)
      - 현재 위치한 branch의 commit history뿐만 아니라 다른 branch의 commit history 확인 : --all 옵션 추가
      - --graph option : commit history가 각 branch와의 관계가 잘 드러나도록 그래프 형식으로 출력
      - ![image](https://user-images.githubusercontent.com/79882248/165201123-262b0252-ee92-4397-99ae-922a17549bbb.png)
   - git을 GUI 환경에서 사용하게 할 수 있는 프로그램 : Sourcetree, GitKraken 등
   - git rebase : base를 다시 지정, commit을 재배치한다
      - git rebase --continue : conflict가 발생하여 제대로 진행되지 못한 rebase를 계속 진행(git commit으로 진행하지 않는다)
      - ![image](https://user-images.githubusercontent.com/79882248/165203105-8c4ff918-4048-4df7-9d6c-1883bb0a0b67.png)
      - ![image](https://user-images.githubusercontent.com/79882248/165203166-9e395ced-f53e-4c8a-ad08-b05fb60a1858.png)
      - merge와 rebase와 차이점
         - rebase는 새로운 commit을 만들지 않는다.
         - rebase로 만들어진 commit history는 merge로 만들어진 commit history보다 좀 더 깔끔하다.
   - 작업 내용 임시 저장(git stash)
      - git stash : working directory에서 작업하던 내용을 git이 따로 보관(stack 형태로 저장)
      - git stash list : stack에 저장된 내용 확인
      - 최근 commit 이후로 작헙했던 내용은 모두 스택에 옮겨지고, working directory 내부는 다시 최근 commit의 상태로 초기화
      - git stash apply : stack에 있는 내용을 다시 working directory로 가져와서 적용
   - 잘못된 branch에서 작업하는 경우
      - git stash 활용
         1. git stash로 stack에 작업 내용 저장
         2. 올바른 branch로 가서 다시 git stash apply를 실행
   - git stash drop [삭제하고 싶은 작업 내용의 id] : 이미 적용한 작업내용을 stack에서 지우기
   - git stash pop [작업 내용의 id] : 작업 내용을 적용하면서, 동시에 stack에서 제거해주는 commmand
      - stack에 저장된 작업 내용을 working directory에 적용할 때, 나중에 또 사용할 필요가 없는 경우 사용
   - 필요한 commit만 가져오는 Command(git cherry-pick)
      - git cherry-pick (가져오고 싶은 commit id)
   - 여러 commit을 하나의 commmit으로 만들기
      - git reset의 option 활용
         - --mixed, --soft option 사용 
         - HEAD는 이전 commit을 가리키지만 working directory는 그대로 유지

