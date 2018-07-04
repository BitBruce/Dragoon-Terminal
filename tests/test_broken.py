#!/usr/bin/env python3

# To run the tests, use: python3 -m pytest --capture=sys

# from dragoonterminal.database import Database
# from tests.test_utils import expected_len


# def broken_test_extra_length(region_name='extra'):
#     assert len(Database().get_extra()) == expected_len(region_name)
#
#
# def broken_test_logo_length(region_name='logo'):
#     assert len(Database().get_logo()) == expected_len(region_name)
#
#
# def broken_test_spirit_length(region_name='spirit'):
#     assert len(Database().get_spirit()) == expected_len(region_name)
#
#
# def broken_test_character_length(region_name='character'):
#     assert len(Database().get_character()) == expected_len(region_name)
#
#
# def broken_test_location_length(region_name='location'):
#     assert len(Database().get_location()) == expected_len(region_name)
#
#
# def broken_test_all_length(region_name='all'):
#     expected = expected_len(region_name) + expected_len('extra')
#     assert len(Database().get_all()) == expected
