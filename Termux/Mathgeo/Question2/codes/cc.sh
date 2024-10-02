gcc main.c func.so -Wl,-rpath=$(pwd) -lm
./a.out

