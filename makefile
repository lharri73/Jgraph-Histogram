GRAPHS = jgraphs/normal3.jgr \
		 jgraphs/normal30.jgr \
		 jgraphs/random3_10-100.jgr \
		 jgraphs/random3_30-100.jgr \
		 jgraphs/random2_20-10.jgr

FINAL = $(GRAPHS:.jgr=.jpg)

all: folders $(FINAL)

folders: data graphs
	mkdir -p data
	mkdir -p graphs
	mkdir -p jgraphs

clean:
	rm -rdv data graphs jgraph

jgraphs/normal3.jgr:
	python scripts/normal_data_maker.py data/normal3.txt 3 100
	python main.py data/normal3.txt $@
jgraphs/normal30.jgr:
	python scripts/normal_data_maker.py data/normal30.txt 30 100
	python main.py data/normal30.txt $@
jgraphs/random3_10-100.jgr:
	python scripts/random_data_maker.py data/random3_10-100.txt 3 100
	python main.py data/random3_10-100.txt $@ --nbins 10
jgraphs/random3_30-100.jgr:
	python scripts/random_data_maker.py data/random3_30-100.txt 3 100
	python main.py data/random3_30-100.txt $@ --nbins 30
jgraphs/random2_20-10.jgr:
	python scripts/random_data_maker.py data/random2_20-10.txt 2 10
	python main.py data/random2_20-10.txt $@ --nbins 20

%.jpg: %.jgr
	/home/jplank/bin/LINUX/jgraph -P $*.jgr | ps2pdf - | convert -density 300 - -quality 100 $<.jpg
	mv $<.jpg graphs

.PHONY: all clean
