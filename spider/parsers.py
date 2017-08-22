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

import abc
import collections
import re

import six


# Representation of Parser's parsed result
ParserResult = collections.namedtuple('ParserResult',
                                      ['display_name', 'parsed_data'])


@six.add_metaclass(abc.ABCMeta)
class ParserBase(object):

    name = None
    """The Parser name.

    Needs to specified in derived classes.
    """

    @property
    @abc.abstractmethod
    def matching_regex(self):
        """The Regex that matches the what the parser attempts to retrieve.

        Override this property to specify the regex that the
        parser uses to match against.
        """

    @property
    @abc.abstractmethod
    def display_name(self):
        """The human understandable name.

        Gets used to display the parsed result.
        """

    def parse(self, resp_data):
        """Master method which scrapes this response data.

        Not to be overriden (as of now).
        :param resp_data: Response data (string).
        :returns: A namedtuple containing the ``display_name`` of parser
            and the parsed result ``parsed_data``. the parsed result is
            a set of fetched values.
        """
        result = set(self.matching_regex.findall(resp_data))
        return ParserResult(display_name=self.display_name,
                            parsed_data=result)


class EmailParser(ParserBase):

    name = 'emails'

    @property
    def matching_regex(self):
        return re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')

    @property
    def display_name(self):
        return 'E-mail Addresses'


class ImageParser(ParserBase):

    name = 'images'

    @property
    def matching_regex(self):
        return re.compile(r'<img\s+[^>]*src="([^"]*)"[^>]*>')

    @property
    def display_name(self):
        return 'Images'
