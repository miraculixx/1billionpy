.PHONY: build run
CFLAGS=-O2
RUNS=10
#NICE=nice -n-20

build:
	gcc $(CFLAGS) baseline.c -o baseline-c; chmod +x baseline-c
	go buildy -o baseline-go baseline.go; chmod +x baseline-go
	touch baselinecython.pyx; CFLAGS=$(CFLAGS) python setup.py build_ext --inplace
	python -m py_compile baseline.py
	python -m py_compile baselinecython-run.py
	CLAGS=$(CFLAGS) cythonize -a -i ap7.py

run: 
	sleep 5
	hyperfine --warmup 1 --min-runs $(RUNS) --max-runs $(RUNS) --cleanup 'sleep 5' --export-markdown 'report-$(CFLAGS)-$(RUNS).md' --export-csv 'report-$(CFLAGS)-$(RUNS).csv' \
		'$(NICE) ./baseline-c 10 > /dev/null' \
		'$(NICE) ./baseline-go 10 > /dev/null' \
        '$(NICE) pypy -su baseline.py 10 > /dev/null' \
        '$(NICE) python -c "import ap7; ap7.compute(10)" >/dev/null' \
        '$(NICE) python -su baselinecython-run.py 10 >/dev/null'

