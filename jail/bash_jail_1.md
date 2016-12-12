First enter a bash shell by simply typing `bash` at the input prompt. Then execute this command:
```
cat flag.txt | tee /dev/tty
```

This will make a copy of the output and send the copy to stdout.
