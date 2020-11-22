import pytest
import yaml


class Test_Data:

    @pytest.mark.parametrize("a,b",yaml.safe_load(open("./data.yaml")))
    def test_a(self,a,b):

        print(a+b)



if __name__ == '__main__':
    pytest.main(["test_data.py"])