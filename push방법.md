```python
student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   01_python/01_python_intro.ipynb

no changes added to commit (use "git add" and/or "git commit -a")

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git add .
warning: LF will be replaced by CRLF in 01_python/01_python_intro.ipynb.
The file will have its original line endings in your working directory

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   01_python/01_python_intro.ipynb


student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git commit -m 190715"
> ^C

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git commit -m "11"
[master e29b501] 11
 1 file changed, 1 insertion(+), 1 deletion(-)

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git log
commit e29b501b29bbb8cb420afc6a1a3ab1469723ef55 (HEAD -> master)
Author: nayulbak1 <nayulbak1@gmail.com>
Date:   Mon Jul 15 17:33:03 2019 +0900

    11

commit 7505ae27fb98684b064757c2d88069b709f905f5 (origin/master, origin/HEAD)
Merge: d68eb1b 4113d9e
Author: nayulbak1 <nayulbak1@gmail.com>
Date:   Mon Jul 15 17:30:34 2019 +0900

    :Wq
    erge branch 'master' of https://github.com/nayulbak1/-TIL

commit d68eb1b2bb1eed1b597bf5d96ca8089b1caf0d3a
Author: nayulbak1 <nayulbak1@gmail.com>
Date:   Mon Jul 15 17:30:25 2019 +0900

    test commit

commit c32ee814a34c0b090815247e7584cd8d4b02fe2f
Author: nayulbak1 <nayulbak1@gmail.com>
Date:   Mon Jul 15 16:31:01 2019 +0900

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git log
commit e29b501b29bbb8cb420afc6a1a3ab1469723ef55 (HEAD -> master)
Author: nayulbak1 <nayulbak1@gmail.com>
Date:   Mon Jul 15 17:33:03 2019 +0900

    11

commit 7505ae27fb98684b064757c2d88069b709f905f5 (origin/master, origin/HEAD)
Merge: d68eb1b 4113d9e
Author: nayulbak1 <nayulbak1@gmail.com>
Date:   Mon Jul 15 17:30:34 2019 +0900

    :Wq
    erge branch 'master' of https://github.com/nayulbak1/-TIL

commit d68eb1b2bb1eed1b597bf5d96ca8089b1caf0d3a
Author: nayulbak1 <nayulbak1@gmail.com>
Date:   Mon Jul 15 17:30:25 2019 +0900

    test commit

commit c32ee814a34c0b090815247e7584cd8d4b02fe2f
Author: nayulbak1 <nayulbak1@gmail.com>
Date:   Mon Jul 15 16:31:01 2019 +0900

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 374 bytes | 374.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/nayulbak1/-TIL.git
   7505ae2..e29b501  master -> master

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$ ^C

student@DESKTOP MINGW64 ~/Desktop/test/TIL (master)
$
```

