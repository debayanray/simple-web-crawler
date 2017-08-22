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

from spider import parsers

import testtools


class EmailParserTestCase(testtools.TestCase):

    def setUp(self):
        super(EmailParserTestCase, self).setUp()
        with open('spider/tests/unit/'
                  'html_samples/sample_template.html', 'r') as f:
            self.resp_data = f.read()

        self.email_parser = parsers.EmailParser()

    def test_parse(self):
        # | WHEN |
        result = self.email_parser.parse(self.resp_data)
        # | THEN |
        expected = {'xyz@gmail.com', 'abc@gmail.com'}
        self.assertEqual('E-mail Addresses', result.display_name)
        self.assertEqual(expected, result.parsed_data)


class ImageParserTestCase(testtools.TestCase):

    def setUp(self):
        super(ImageParserTestCase, self).setUp()
        with open('spider/tests/unit/'
                  'html_samples/sample_template.html', 'r') as f:
            self.resp_data = f.read()

        self.image_parser = parsers.ImageParser()

    def test_parse(self):
        # | WHEN |
        result = self.image_parser.parse(self.resp_data)
        # | THEN |
        expected = {'pic_mountain.jpg', 'html5.gif'}
        self.assertEqual('Images', result.display_name)
        self.assertEqual(expected, result.parsed_data)
