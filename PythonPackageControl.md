# Python 的套件管理
## 使用pip / pip3
```bash
# 環境變數有 <PYTHON_INSTALLED_DIR>
c:\> python --version
c:\> python --m pip --version # 執行在C:\python3\Lib\site-packages 下的python module
# 環境變數有 <PYTHON_INSTALLED_DIR>\Scripts, 以下假設<PYTHON_INSTALLED_DIR>\Scripts 有在環境變數
c:\> pip --version
c:\> pip3 --version
```
>Python Command Arguments:
>>-m mod : run library module as a script (terminates option list)

```bash
c:\> pip install -U pip setuptools # Install pip, setuptools
c:\> pip install wheel # Install wheel
c:\> pip install beautifulsoup4 # Install beautifulsoup4
```

pip3 search PACKAGE_NAME

pip3 install PACKAGE_NAME
pip3 uninsatll PACKAGE_NAME
pip3 list
pip3 list -o / pip3 list --outdate
pip install -U PACKAGE_NAME

pip3 freeze

pip3 list -o --format=freeze / pip list --outdate --format=freeze

pip3 list -o --format=freeze > requirement.txt
http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip



## 手動安裝

## 參考
[Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.io/)
[pip Quick start](https://pip.pypa.io/en/stable/quickstart/)
[Installing Python Modules](https://docs.python.org/3.5/installing/index.html#installing-index)

    # install through pip, ref [1], [2], [3], [4], [5]
    
    
    

    # install from distributing, ref [6], [7]
    c:\> cd %SOURCE_FOLDER%
    c:\> python
    >>> help
    >>> modules # list all installed module
    >>> python setup.py install  ||  >>> setup.py install
    >>> help
    >>> modules # list all installed module
Reference: 


    [3] https://pip.pypa.io/en/stable/reference/pip_install/ # Introduct pip install and its arguments
    [4] https://pip.pypa.io/en/stable/reference/pip_uninstall/ # Introduct pip uninstall and its arguments
    [5] https://pip.pypa.io/en/stable/reference/pip_list/ # Introduct pip list and its arguments
    [6] https://docs.python.org/2/install/
    [7] https://docs.python.org/3.5/install/
    [8] https://pypi.python.org/pypi
