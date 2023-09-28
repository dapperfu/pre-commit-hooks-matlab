# pre-commit-hooks-matlab
Precommit hooks for MATLAB


```
repos:
-   repo: https://github.com/dapperfu/pre-commit-hooks-matlab
    rev: master
    hooks:
    -   id: smart-indent
        args: ['--files', 'all']  # Use '--files' to specify the files to process

    -   id: justify
        args: ['--files', 'all']  # Use '--files' to specify the files to process

    -   id: close-simulink-subsystems
        args: ['--files', 'all']  # Use '--files' to specify the files to process

    -   id: de-highlight
        args: ['--files', 'all']  # Use '--files' to specify the files to process

```
