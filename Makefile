
.cpp.o:
	g++ -O3 -c -o $@ $<

all : example.x

example.x : aaa.o bbb.o example.o
	g++ aaa.o bbb.o example.o -o exmpale.x

clean:
	rm aaa.o bbb.o example.o exmpale.x

.PHONY : all clean
