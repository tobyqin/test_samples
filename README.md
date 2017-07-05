# test_samples
To generate sample test results.

```shell
# install requirements
pip install -r requirements.txt

# generate tests.py
python prepare.py

# run the tests
py.test --junitxml results.xml tests.py

```