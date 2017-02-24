# This is a Makefile, which will be explained later in the course.
# Please don't look at it yet :-)

publish: slides_bash commit
	echo "convert the slides to pdf, commit, and push to github"
	git push


test_exercises: start help ignorecase multiplefiles
generate_exercises: generate_grep generate_awk

testrule:
	echo this is a Makefile rule
	echo You can associate it to as many commands you want

notebook:
	jupyter nbconvert --to notebook --execute PEB\ Bash\ Workshop.ipynb

generate_grep:
	python src/generate_grep_exercise.py

generate_awk:
	Rscript src/generate_awk_exercise.R

start:
	grep start exercises/2_searching_patterns.txt

help:
	grep help exercises/2_searching_patterns.txt

ignorecase:
	grep -i -c ignorecase exercises/2_searching_patterns.txt
	grep 21 exercises/2_searching_patterns.txt

multiplefiles:
	grep 'regex' exercises/multiplefiles/*

piping:
	grep ORGANISM exercises/genes/mgat_genes.gb | grep 'Homo sapiens'
	grep ORGANISM exercises/genes/mgat_genes.gb | grep taurus

regex:
	grep 'AAA..TTT' exercises/genes/sequences.fasta


awk1:
	awk '$$1=="chr8" && $$4>100000 && $$5<200000 ' exercises/genes/chr8.gff

commit:
	-git commit -a

slides_bash:
	jupyter nbconvert --to slides  slides/*.ipynb

goodbye:
	@cowsay -W 12 'I hope you have enjoyed the workshop :-)'
	@cowthink -W 12 "Now let's go for dinner"
	@cowsay -W 22 "Note: real genomes do not contain hidden cows"
