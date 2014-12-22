# AoikProjectStart-Python
Start code for Python project.

Best practices cover:
- [Package bootstrap](#package-bootstrap)
- [Argument parsing](#argument-parsing)
- [Error handling](#error-handling)

Tested working with:
- Python 2.7, 3.2+

## Table of Contents
- [Setup](#setup)
  - [Setup via git](#setup-via-git)
  - [Find entry program](#find-entry-program)
- [Best Practices](#best-practices)
  - [Package bootstrap](#package-bootstrap)
  - [Argument parsing](#argument-parsing)
  - [Error handling](#error-handling)

## Setup

### Setup via git
Clone this repo to local
```
git clone https://github.com/AoiKuiyuyou/AoikProjectStart-Python
```

You can run the **setup.py** file in the local repo dir
```
python setup.py install
```
The effect is equivalent to installation via pip.

### Find entry program
If the installation is via pip, or you have run the **setup.py** in the local
 repo dir, then a command named **aoikprojectstart** should be available from command
 line. Run
```
aoikprojectstart
```

And because the package has been installed to system package dir, it's
also ok to run it via module name
```
python -m aoikprojectstart
```

If command **aoikprojectstart** is not available, you can still run the entry program
 directly. Go to the local repo dir. The entry program is
 **src/aoikprojectstart/aoikprojectstart.py**. Run
```
python src/aoikprojectstart/aoikprojectstart.py
```
- No requirement on the working dir, ```aoikprojectstart.py``` can be run anywhere
  as long as the path is correct.
- No need to add dir **src**'s path to environment variable **PYTHONPATH**
   because ```aoikprojectstart.py``` knows how to [bootstrap itself](#package-bootstrap).

## Best Practices

### Package bootstrap
**package bootstrap** means your program does not require a user to add the src
 dir containing your program's package to environment variable **PYTHONPATH**.
 Instead, your program adds the src dir to **sys.path** itself.

A program supporting package bootstrap results in better user experiences
 because it works out-of-the-box. A user can run it via file path, instead of
 only module name.

To support package bootstrap, first of all, decide which module is the
 program entry. In our case, it is
 [aoikprojectstart.py](/src/aoikprojectstart/aoikprojectstart.py)
 and [\__main__.py](/src/aoikprojectstart/__main__.py)
 (**\__main__.py** is for making the package runnable when using
 ```python -m aoikprojectstart```). The two entry modules' content is exactly
 the same.

In the entry module **aoikprojectstart.py**, it calls function
 [pythonpath_init](/src/aoikprojectstart/aoikprojectstart.py#L7) to do the
 bootstrap.

Inside the function **pythonpath_init** at
 [here](/src/aoikprojectstart/aoikprojectstart.py#L12), we have removed empty
 string and the entry module's dir from **sys.path**, in order to avoid relative
 shading by chance. Also remember to add
 ```from __future__ import absolute_import``` to each module file, to ensure
 relative shading would not happen.

Inside the function **pythonpath_init** at
 [here](/src/aoikprojectstart/aoikprojectstart.py#L17), we have added dir
 **dep** to **sys.path**. Dir **dep** is another PYTHONPATH dir,
 independent of the src dir. It contains dep libs that we prefer to include as
 built-in instead of external dependency.

It's worth mentioning that even though there is a **\__init__.py** inside dir
 **dep**, it is solely for the convenience of packaging. We should always import
 packages in dir **dep** as top level packages, e.g.
 ```
import aoikargutil
 ```
 instead of 
 ```
import aoikprojectstart.dep.aoikargutil
 ```

After calling the function **pythonpath_init**, the entry module calls the
 actual **main** implementation from module
 [main_imp.py](/src/aoikprojectstart/main_imp.py).
 The merit of putting main implementation code in another module is that in all
 but the entry module, the import statements can be put at the top of the file,
 as we usually do. These modules do not need to be concerned about package
 bootstrap, because at the time they are imported, the bootstrap is done.

Gochas to notice:
- Don't be attempted to refactor **pythonpath_init** into a separate module
   for reusability. It must be defined inside a program entry module. It can
   not be imported from another module because importing is not working yet
   until you call **pythonpath_init**.
- Don't be attempted to use relative import in a program entry module, hoping it
   works so the whole ```pythonpath_init``` code can be removed. Relative
   import does not work if the program is run via file path because the entry
   module is given name **\__main__** by Python and has no package information.
   Relative import does work if the program is run via module name like
   ```python -m aoikprojectstart```. However, running program via module
   name requires **PYTHONPATH** is well configured by a user, which is the
   opposite of what we have been assuming.
- Naming the entry module **aoikprojectstart.py**, the same name as the top
   level package, might cause relative shading in sibling modules. Always add
   ```from __future__ import absolute_import``` to each module to avoid any
   relative shading by chance.

### Argument parsing
We use standard library [argparse](https://docs.python.org/2/library/argparse.html)
 for argument parsing, along with utility lib
 [AoikArgUtil](https://github.com/AoiKuiyuyou/AoikArgUtil-Python) that brings
 some convenience for everyday use cases. See the
 [best practices](https://github.com/AoiKuiyuyou/AoikArgUtil-Python#argparse-best-practices)
 provided by **AoikArgUtil** on how to use **argparse**.

### Error handling
After the entry module calls module
 [main_imp.py](/src/aoikprojectstart/main_imp.py)'s
 function [main](/src/aoikprojectstart/main_imp.py#L167), the function in turn
 calls function [main_imp](/src/aoikprojectstart/main_imp.py#L31) and only
 catches **KeyboardInterrupt** and **Exception**. **KeyboardInterrupt** is for
 the case when a user presses **Ctrl+C** to terminate the program. Any other
 exception caught there reveals an exception leak that should have been handled
 in the function **main_imp**.

In the function [main_imp](/src/aoikprojectstart/main_imp.py#L31), anything that
 may cause an error should be put in a try-catch block. And in case an error
 happens, print a user friendly message and quit the program with a [unique exit
 code](/src/aoikprojectstart/main_const.py#L9). See an example
 [here](/src/aoikprojectstart/main_imp.py#L138).

 A command argument **-V** has been provided to show debug message (e.g.
  traceback) of an error. It can be set on by default, if the program's intended
  users enjoy so.
