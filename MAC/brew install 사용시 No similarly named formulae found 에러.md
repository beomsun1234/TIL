# brew install 사용시 No similarly named formulae found 에러

    % brew install git
    Warning: No available formula with the name "git".
    ==> Searching for similarly named formulae...
    Error: No similarly named formulae found.
    ==> Searching for a previously deleted formula (in the last month)...
    Error: No previously deleted formula found.
    ==> Searching taps on GitHub...
    Error: No formulae found in taps.

해당 에러 발생

아래 명령어로 brew 의 코어 디렉터리를 삭제 후 

    rm -fr $(brew --repo homebrew/core)
    
    
다시 설치하면 문제 해결!!!

    brew install git
