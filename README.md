# Python CI/CD Test Project

This is a small Python project you can use to test a CI/CD pipeline. It includes:

- A simple Python package in `src/calculator_service`
- Unit tests in `tests`
- Local helper scripts in `scripts`
- A GitHub Actions workflow that runs tests on pull requests and after merges to `main`

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run Tests Locally

```bash
python -m pytest
```

Or use the helper script:

```bash
./scripts/run_tests.sh
```

## Trigger The Pipeline

1. Push this project to a GitHub repository.
2. Create a branch:

   ```bash
   git checkout -b test-ci-change
   ```

3. Make a small code or test change.
4. Commit and push the branch:

   ```bash
   git add .
   git commit -m "Test CI pipeline"
   git push -u origin test-ci-change
   ```

5. Open a pull request into `main`.
6. GitHub Actions will run the `test` job automatically on the pull request.
7. Merge the pull request into `main`.
8. GitHub Actions will run again on the `push` to `main`; this represents the post-merge CI/CD trigger.

You can also trigger the workflow manually from GitHub:

1. Go to your repository on GitHub.
2. Open the **Actions** tab.
3. Select **Python CI/CD Pipeline**.
4. Click **Run workflow**.

## Workflow Behavior

The workflow is defined at `.github/workflows/python-ci.yml`.

- Pull request to `main`: installs the project and runs tests.
- Push to `main`: installs the project, runs tests, builds a package, uploads the build artifact, and runs a deployment simulation.
- Manual run: same checks can be started from the GitHub Actions UI.

## Where To Customize CD

Edit the `deploy` job in `.github/workflows/python-ci.yml` and replace the `echo` commands with your real deployment command, such as deploying to a server, container registry, cloud service, or internal environment.
