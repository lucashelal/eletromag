# Contributing Guidelines

Thank you for your interest in contributing to my project! This document outlines the coding style, documentation conventions, pull request model, and code review process that I follow.

You can find our _Overall Standards Manual_ in the [GitHub main page](https://github.com/lucashelal), that is valid for all projects I develop.

## Coding Style

I follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) for C++, [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) for Python, [Google Julia Style Guide](https://google.github.io/styleguide/juliaguide.html) for Julia and [Google LaTeX Style Guide](https://google.github.io/styleguide/texguide.html) for LaTeX and highly encourage you to maintain it.

Please make sure to adhere to these style guides when writing code.

## Commit and Branches Policies

### Commit Messages

Commit messages should be clear and descriptive. They should follow the conventional commit format:

1. **fix**: A commit of the type `fix` patches a bug in your codebase.
2. **feat**: The `feat` type is used when a new feature is added to the codebase.
3. **docs**: This type is used for commits that update documentation.
4. **style**: The `style` type is for formatting changes that do not affect the meaning of the code (white-space, formatting, etc).
5. **refactor**: Use `refactor` when improving the format/structure of the code without changing its behavior.
6. **test**: The `test` type is for adding missing tests or correcting existing ones.
7. **chore**: Use `chore` for regular code maintenance tasks.

### When to Commit

You should commit your changes frequently. A good rule of thumb is to make a commit whenever you've made a significant change that you'd want to revert or isolate, should an issue arise. However, make sure each commit contains related changes. Unrelated changes should be committed separately.

### Stashing Changes

If you're in the middle of some changes and need to switch branches, you can use `git stash` to save your changes and apply them later. This is useful when you need to pull the latest changes from the remote repository but don't want to commit your current changes yet.

### Branches

When contributing, create a new branch for each feature or bug fix. This keeps your changes isolated and makes it easier to integrate them into the main codebase. Once your changes are complete, you can open a pull request to merge your branch into the `develop` branch. This is our _Documentation Conventions Manual_. You can find a standardized manual on our [GitHub main page](https://github.com/lucashelal).

## Pull Request Model

To contribute to my project, please follow these steps:

1. Fork the repository to your own GitHub account.
2. Create a new branch for your changes.
3. Make your changes and commit them to your branch.
4. Push your branch to your forked repository.
5. Open a pull request from your branch to the main repository.
6. Provide a clear and concise description of your changes in the pull request.
7. Wait for the code review process to begin.

We recommend using the [GitHub Pull Request Template](https://docs.github.com/en/github/building-a-strong-community/about-issue-and-pull-request-templates) to provide a standardized format for your pull request description. This template helps ensure that all necessary information is included, such as a summary of the changes, any related issues, and any additional context or considerations.

## Code Review Process

All pull requests will go through a code review process. A designated code reviewer will review your changes and provide feedback. Please be open to constructive criticism and be prepared to make necessary changes based on the feedback received.

The code reviewer is responsible for reviewing and approving pull requests. They will ensure that the code follows the coding style, adheres to the documentation conventions, and meets the project's requirements. If you have any questions or concerns during the code review process, feel free to reach out to the code reviewer.

## Release Process

Our release process follows a standard Git flow model. Here's a brief overview:

1. **Development**: All development work happens on feature branches created from the `develop` branch. Once a feature or bug fix is complete, it is merged back into `develop`.

2. **Staging**: When we're ready to prepare a new release, we create a release branch from `develop`. This branch is used to finalize the release, including updating version numbers, adding release notes, and performing any other necessary tasks.

3. **Release**: Once the release branch is ready, it is merged into `main`, and a new version is tagged.

4. **Hotfixes**: If a critical issue is found in the `main` branch, a hotfix branch is created from `main`. Once the issue is resolved, the hotfix branch is merged back into both `main` and `develop`.

### Clearance Policy

All changes must be reviewed and approved by a project maintainer before they can be merged into the `develop` or `main` branches. This ensures that all changes meet our quality standards and that the codebase remains stable and secure.

### Versioning

We follow Semantic Versioning (SemVer) for our releases. Each release version number has the format `MAJOR.MINOR.PATCH`:

- `MAJOR` version increments indicate incompatible API changes.
- `MINOR` version increments indicate the addition of functionality in a backwards-compatible manner.
- `PATCH` version increments indicate backwards-compatible bug fixes.

For example, if the current version is 2.3.1 and we add a new feature without breaking any existing functionality, the new version would be 2.4.0.

## Documentation Conventions

We strive to maintain clear and comprehensive documentation for our project. When contributing, please ensure that your code is well-documented and follows the [insert documentation conventions here]. This includes providing inline comments, writing docstrings, and documenting any public APIs.

This is our _Documentation Conventions Manual_. You can find a standardized manual on our [GitHub main page](https://github.com/lucashelal).

