# pre-commit-hooks-matlab
Precommit hooks for MATLAB

# Requirements

- [MATLAB R2022b+](https://www.mathworks.com/products/matlab.html)
- [Python](https://www.python.org/downloads/)
- [`pre-commit`](https://pre-commit.com/) installed [`pip instal pre-commit`]

Tested on Windows 10, MATLAB R2023b.

# Usage:

- Install [`pre-commit`](https://pre-commit.com/) to your Python environment. 
- Add to your `.pre-commit-config.yaml`:
    ```
    repos:
    -   repo: https://github.com/dapperfu/pre-commit-hooks-matlab
        rev: 2023.09.018
        hooks:
        -   id: simulink_close_subsystems
        -   id: simulink_zoom_subsystems
        -   id: matlab_smart_indent
        -   id: matlab_justify
    ```
- Run `pre-commit run --all-files --verbose `

# Hooks.

- `simulink_close_subsystems` - Closes all open subsystem windows and tabs. Leaves the model to open directly to the top level Simulink model.
- `simulink_zoom_subsystems` - Scales all SubSystems to fit the window.
- `matlab_smart_indent` - Run [`TidyCode`](https://github.com/okomarov/TidyCode) `smartIndent` on all M-files. Ensuring consistent formatting.
- `matlab_justify` - Run [`TidyCode`](https://github.com/okomarov/TidyCode) `justify` on all m-files aligning `=`.

# TODO:

Hooks to be implemented.

- `matlab_align_io` -  Run [`alignIO.m`](https://github.com/dapperfu/simulink_PersonalToolchainTools/blob/master/alignIO.m) on a model so all Inports and Outports.
- `simulink_unit_delay_prettify` - [Run `unitDelayPrettify.m`](https://github.com/dapperfu/simulink_PersonalToolchainTools/blob/master/unitDelayPrettify.m) on a model so all unit delay blocks are aligned with the block they came out of.
- `matlab_mccabe` - Fail for [`checkcode`](https://www.mathworks.com/help/matlab/ref/checkcode.html)
    - *Display the McCabe cyclomatic complexity of each function in the file. In general, lower complexity values indicate programs that are easier to understand and modify. Evidence suggests that programs with higher complexity values are more likely to contain errors. Frequently, you can lower the complexity of a function by dividing it into smaller, simpler functions. Some people advocate splitting up programs that have a complexity value over 10.*
- `matlab_code_issues` - Fail for ['codeIssues`](https://www.mathworks.com/help/matlab/ref/codeissues.html).
- `simulink_slbuild` -  [`slbuild` - Build standalone executable file or model reference target for model](https://www.mathworks.com/help/simulink/slref/slbuild.html)
- `polyspace_bug_finder` - [Polyspace Bug Finder]](https://www.mathworks.com/products/polyspace-bug-finder.html) Integration?
    - *Polyspace Bug Finder identifies run-time errors, concurrency issues, security vulnerabilities, and other defects in C and C++ embedded software. Using static analysis, including semantic analysis, Polyspace Bug Finder analyzes software control flow, data flow, and interprocedural behavior. By highlighting defects as soon as they are detected, it lets you triage and fix bugs early in the development process.*
    - *Polyspace Bug Finder checks compliance with coding rule standards such as MISRA C®, MISRA C++, AUTOSAR C++14, CERT® C, CERT C++, and custom naming conventions. It generates reports consisting of bugs found, code-rule violations, and code quality metrics, including cyclomatic complexity.* 

# Debugging / Development

- [Optional]: [Fork to your own repository](https://github.com/login?return_to=%2Fdapperfu%2Fpre-commit-hooks-matlab)

## Checkout [`pre-commit-hooks-matlab`]

Checkout to somewhere in your workspace.

```
```git clone https://github.com/dapperfu/pre-commit-hooks-matlab.git```

cd <your project>

pre-commit try-repo ../pre-commit-hooks-matlab --all-files --verbose```
```

`pre-commit`` will run and check your Project repository for m-files and Simulink Models.