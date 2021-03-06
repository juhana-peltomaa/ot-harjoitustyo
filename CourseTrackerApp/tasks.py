from invoke import task


# Initialize the database with command "poetry run invoke build"
@task
def build(ctx):
    ctx.run("python3 src/build.py")


# Run the application with command "poetry run invoke start"
@task
def start(ctx):
    ctx.run("python3 src/index.py")


@task
def test(ctx):
    ctx.run("pytest src")


# Run coverage and generate html report with command "poetry run invoke coverage-report"
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")


# Run pylint checks with command "poetry run invoke lint"
@task
def lint(ctx):
    ctx.run("pylint src")


# Run autopep8 formation with command "poetry run invoke format"
@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
