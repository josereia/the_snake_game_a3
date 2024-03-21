default: run

deps:
	@echo "Installing deps"
	@pip install pipenv
	@pipenv install

shell:
	@echo "Launching subshell"
	@pipenv shell

run:
	@echo "Running game"
	@python ./src/main.py

clean:
	@echo "Cleaning project"
	@rm -rf build/
