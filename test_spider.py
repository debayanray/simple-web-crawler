# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from spider import main

base_url = 'http://wiprodigital.com'
web_spider = None
NO_ITERATIONS = 3
MAX_DEPTH = 1


def setUp():
    """initialize the spider."""
    global web_spider
    web_spider = main.Spider(base_url)


def test_spider():
    """execute weaving."""
    web_spider.weave(max_depth=MAX_DEPTH)

if __name__ == '__main__':
    import timeit
    time_taken = timeit.timeit(
        "from __main__ import test_spider; test_spider()",
        setup="from __main__ import setUp; setUp()",
        number=NO_ITERATIONS)

    web_spider.display_weave_result(indent=2)

    print('-' * 120)
    print(('Ran %(number)s passes on "%(url)s" (depth - %(max_depth)s) '
           'in %(time)s sec ( %(time_msec)s msec/pass ).') %
          {'number': NO_ITERATIONS, 'url': base_url, 'max_depth': MAX_DEPTH,
           'time': time_taken,
           'time_msec': 1000 * (time_taken / NO_ITERATIONS)})
