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

import re
import urlparse

import requests

# import parsers


class Spider(object):

    _link_regex = re.compile(r'href="(.*?)"')
    """Regex that matches href="" attribute.

    It is the HTML <a> regexp
    """

    parsers = None
    """Contains all parsers"""

    scrape_data = None
    """Contains the complete scrape data"""

#     def __init__(self, base_url, parsers=None):
    def __init__(self, base_url):
        """A class which scrapes the web page data recursively.

        It uses it parsers to do the parsing jobs and displays the
        gathered data when queried.
        :param base_url: The base URL to scrape. It should include scheme
            portion of the URL. For now only ``http`` is supported.
            example: http://vendor.com
        :param parsers: collection of parsers. Defaults to None
        """
        self._base_url = base_url
#         self.parsers = parsers or []
        self.parsers = []
        self.scrape_data = {}
#         self.parsers.append(parsers.EmailParser())

    def _crawl(self, url, max_level):
        # Limit the recursion level
        if(max_level == 0):
            return

        # Get the webpage content
        resp = requests.get(url)

        # Check if successful
        if(resp.status_code != 200):
            # LOG it
            return

        samedomain_urls = set()
        external_urls = set()
        # Find and follow all the links
        links = self._link_regex.findall(resp.text)
        for link in links:
            link = link.strip()
            if (link.startswith(self._base_url)
                    or (not link.startswith('http'))):
                # It is a same domain link
                # Get an absolute URL for the link
                link = urlparse.urljoin(url, link)
                samedomain_urls.add(link)
            else:
                # It is an external url
                external_urls.add(link)

        self.scrape_data[url] = {
            'Same Domain URLs': samedomain_urls,
            'External URLs': external_urls,
        }

        for samedomain_url in samedomain_urls:
            self._crawl(samedomain_url, max_level - 1)

        for parser in self.parsers:
            result = parser.parse(resp.text)
            self.scrape_data[url].update({
                result.display_name: result.parsed_data
            })

    def weave(self, max_depth=None):
        """Method to initiate the scraping.

        :param max_depth: The depth upto which scraping should be done.
            The value None means there's no limit to the level at which
            the scraping has to be performed. Defaults to None.
        """
        self._crawl(self._base_url, max_depth)

    def display_weave_result(self, indent=1):
        """Display the scraped data.

        It outputs the data on sys::out. The scraped data remains in this
        form:

            {
                "http://vendor.com": {
                    "Same Domain URLs": set(["http://vendor.com/about-us",
                                             "http://vendor.com/contact-us",
                                             ...
                                            ])
                    "External URLs": set(["http://google.com/blah-blah",
                                          "http://twitter.com/blah-blah",
                                          ...
                                        ])
                    <parser1 display-name>: set([parsed_data_1,
                                                 parsed_data_2,
                                                 ...
                                                ])
                    <parser2 display-name>: ...

                    ...
                }
                "http://vendor.com/products": {
                    "Same Domain URLs": ...
                    "External URLs": ...
                    <parser1 display-name>: ...
                    <parser2 display-name>: ...
                    ...
                }
                ...
            }

        :param indent: The indentation to be maintained while displaying
            the result. Defaults to 1.
        """
        def formatted_print(item, underline_pattern=None, indent=None):
            if indent is not None:
                print(' ' * indent),
            print('%s' % item)

            if underline_pattern is not None:
                if indent is not None:
                    print(' ' * indent),
                print(underline_pattern * len(item))

        for url, url_data in self.scrape_data.items():

            formatted_print(url, underline_pattern='^')

            for item_attr, item_val in url_data.items():

                formatted_print(
                    item_attr, underline_pattern='-', indent=indent)

                for val in item_val:
                    formatted_print(val, indent=(indent * 2))
