import logging
import subprocess

logger = logging.getLogger(__name__)


class Morfeusz:
    def analyse(self, text):
        logger.info("Text to analyse: {}".format(text))
        res = subprocess.run(
            'morfeusz_analyzer',
            input=text.encode('utf8'),
            stdout=subprocess.PIPE,
            stderr=None)
        logger.debug("Raw output: {}".format(res.stdout.decode('utf8')))
        return self._parse_output(res.stdout.decode('utf8'))

    def generate(self, word):
        logger.info("Word to generate: {}".format(word))
        res = subprocess.run(
            'morfeusz_generator',
            input=word.encode('utf8'),
            stdout=subprocess.PIPE,
            stderr=None)
        out = res.stdout.decode('utf8').strip()[1:-1]  # removing [ and ]
        logger.debug("Raw output: {}".format(out))
        items = [item.strip() for item in out.split('\n')]
        return [tuple(self._parse_generate_output(item)) for item in items]

    def _parse_generate_output(self, text):
        if '#' not in text:
            return list(map(lambda x: x.replace("#", r','), text.replace(r',,', '#,').split(',')))
        return text.split(',')

    def _parse_output(self, text):
        text = text.strip()
        if not text:
            return []
        entities = text.split(']\n[')
        res = []
        for entity in entities:
            res += self._parse_word_entity(entity)
        return res

    def _parse_word_entity(self, word):
        items = word.split('\n')
        return [self._parse_item(item) for item in items]

    def _parse_item(self, item):
        return item.split(',')
