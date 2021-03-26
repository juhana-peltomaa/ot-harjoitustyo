from invoke import task

# Run coverage and generate html report with command "poetry run invoke coverage-report"
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

# Run pylint checks with command "poetry run invoke lint"
@task
def lint(ctx):
    ctx.run("pylint src")
