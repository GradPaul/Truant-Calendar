# Truant-Calendar
# @copyright GradPaul

all: install

install:
	@echo 'Installing python dependencies'
	@pip install -r cmd/requirements.txt
	@echo 'Complete'
