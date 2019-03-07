sudo ls -1 /var/lib/jenkins/workspace/GIT_CODING_TRIGGER/php/ && sudo git -c http.sslVerify=false --git-dir=/var/lib/jenkins/workspace/GIT_CODING_TRIGGER/php/.git  pull ||sudo git -c http.sslVerify=false clone https://lead:123456789@gitlab.example.com/root/php.git  /var/lib/jenkins/workspace/GIT_CODING_TRIGGER/php/
cd /var/lib/jenkins/workspace/GIT_CODING_TRIGGER/php/; sudo git -c http.sslVerify=false  pull; sudo git checkout re-1.0 || exit 1
CURRENT_COMMIT_ID=`sudo git log --oneline -1 | awk '{print $1}'`
cd /var/lib/jenkins/workspace/GIT_CODING_TRIGGER/;
LAST_COMMIT_ID=`cat LAST_ID` ||: 
echo "$CURRENT_COMMIT_ID"  >  LAST_ID
if [ x"$LAST_COMMIT_ID" == x"$CURRENT_COMMIT_ID" ];then
    exit 1
else
    exit 0
fi
