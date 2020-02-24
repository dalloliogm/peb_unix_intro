# This is a Makefile, which will be explained later in the course.
# Please don't look at it yet :-)

explain: explain_text
	@echo Try running "make explain" to read an explanation
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

make_exercise:
	@echo "Run this rule to complete the first Make exercise"
	@echo "Make allows to save pipelines of Unix commands, and quickly re-execute them"
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

slides_bash_pdf:
	jupyter nbconvert --to pdf  slides/*.ipynb

explain_text:
	@echo
	@echo 'this Makefile contains all the rules and scripts used to '
	@echo 'generate the exercises in this module.'
	@echo
	@echo 'For example, there is a "generate_grep" rule which'
	@echo 'creates all the files for the grep exercises (biopython needs to be installed first)'
	@echo
	@echo 'There are also rules to test if the exercises work correctly,'
	@echo 'e.g. help, ignorecase, and so on.'
	@echo 
	@echo 'Makefiles are a simple way to describe a pipeline, combining commands'
	@echo 'and rules together '


goodbye:
	@cowsay -W 12 'I hope you have enjoyed the workshop :-)'
	@cowthink -W 12 "Now let's go for dinner"
	@cowsay -W 22 "Note: real genomes do not contain hidden cows"
