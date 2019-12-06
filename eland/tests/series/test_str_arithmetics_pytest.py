#  Copyright 2019 Elasticsearch BV
#
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.

# File called _pytest for PyCharm compatability
import pytest
import numpy as np

from eland.tests.common import TestData, assert_pandas_eland_series_equal


class TestSeriesArithmetics(TestData):

    def test_invalid_add_num(self):
        with pytest.raises(TypeError):
            assert 2 + self.ed_ecommerce()['currency']

        with pytest.raises(TypeError):
            assert self.ed_ecommerce()['currency'] + 2

        with pytest.raises(TypeError):
            assert self.ed_ecommerce()['currency'] + self.ed_ecommerce()['total_quantity']

        with pytest.raises(TypeError):
            assert self.ed_ecommerce()['total_quantity'] + self.ed_ecommerce()['currency']

    def test_ser_add_ser(self):
        edadd = self.ed_ecommerce()['customer_first_name'] + self.ed_ecommerce()['customer_last_name']
        pdadd = self.pd_ecommerce()['customer_first_name'] + self.pd_ecommerce()['customer_last_name']

        assert_pandas_eland_series_equal(pdadd, edadd)

    def test_ser_add_str(self):
        edadd = self.ed_ecommerce()['customer_first_name'] + " is the first name."
        pdadd = self.pd_ecommerce()['customer_first_name'] + " is the first name."

        assert_pandas_eland_series_equal(pdadd, edadd)

    def test_str_add_ser(self):
        edadd = "The last name is: " + self.ed_ecommerce()['customer_last_name']
        pdadd = "The last name is: " + self.pd_ecommerce()['customer_last_name']

        assert_pandas_eland_series_equal(pdadd, edadd)

    def test_bad_str_add_ser(self):
        # TODO encode special characters better
        #      Elasticsearch accepts this, but it will cause problems
        edadd = " *" + self.ed_ecommerce()['customer_last_name']
        pdadd = " *" + self.pd_ecommerce()['customer_last_name']

        assert_pandas_eland_series_equal(pdadd, edadd)


    def test_ser_add_str_add_ser(self):
        pdadd = self.pd_ecommerce()['customer_first_name'] + self.pd_ecommerce()['customer_last_name']
        print(pdadd.name)
        edadd = self.ed_ecommerce()['customer_first_name'] + self.ed_ecommerce()['customer_last_name']
        print(edadd.name)

        print(edadd.info_es())

        assert_pandas_eland_series_equal(pdadd, edadd)

    def test_non_aggregatable_add_str(self):
        with pytest.raises(ValueError):
            assert self.ed_ecommerce()['customer_gender'] + "is the gender"

    def teststr_add_non_aggregatable(self):
        with pytest.raises(ValueError):
            assert "The gender is: " + self.ed_ecommerce()['customer_gender']

    def test_non_aggregatable_add_aggregatable(self):
        with pytest.raises(ValueError):
            assert self.ed_ecommerce()['customer_gender'] + self.ed_ecommerce()['customer_first_name']

    def test_aggregatable_add_non_aggregatable(self):
            with pytest.raises(ValueError):
                assert self.ed_ecommerce()['customer_first_name'] + self.ed_ecommerce()['customer_gender']
