from unittest import TestCase

from parameterized import parameterized

from text_processing.text_summarization.summarize_text import summarize_text


class TextSummarizationTest(TestCase):
    maxDiff = None

    @parameterized.expand([
        (
                "Single word keyword",
                u"<em>havaz</em> is the best app",
                u"<em>havaz</em> is the ...",
        ),
        (
                "kw in the first of a sentence",
                u"<em>ứng</em> <em>dụng</em> <em>havaz</em> rất tuyệt vời và hữu dụng",
                u"<em>ứng</em> <em>dụng</em> <em>havaz</em> rất tuyệt ...",
        ),
        (
                "Only conains keyword",
                u"<em>ứng</em> <em>dụng</em> <em>havaz</em>",
                u"<em>ứng</em> <em>dụng</em> <em>havaz</em>",
        ),
        (
                "Keyword in the center of a sentence",
                u"Tôi xử dụng <em>ứng</em> <em>dụng</em> <em>havaz</em> rất tiện lợi",
                u"... xử dụng <em>ứng</em> <em>dụng</em> <em>havaz</em> rất tiện ...",
        ),
        (
                "Keyword in the lef of a sentence",
                u"Thấy <em>ứng</em> <em>dụng</em> <em>havaz</em> có vẻ được đấy",
                u"Thấy <em>ứng</em> <em>dụng</em> <em>havaz</em> có vẻ ...",
        ),
        (
                "Keyword in the right of a sentence",
                u"Thấy cái <em>ứng</em> <em>dụng</em> <em>havaz</em> được",
                u"Thấy cái <em>ứng</em> <em>dụng</em> <em>havaz</em> được",
        ),
        (
                "Multi keywords: 2 keywords",
                "dung <em>ung</em> <em>dung</em> <em>havaz</em> haha kaka hoho hehe meme <em>tram</em> <em>xe</em> don",
                "dung <em>ung</em> <em>dung</em> <em>havaz</em> haha kaka ... hehe meme <em>tram</em> <em>xe</em> don",
        ),
        (
                "Multi keywords: 3 keywords",
                "dung <em>ung</em> <em>dung</em> <em>havaz</em> haha kaka hoho hehe meme <em>tram</em> <em>xe</em> don tiep chu dao <em>day</em> <em>nui</em> cao",
                "dung <em>ung</em> <em>dung</em> <em>havaz</em> haha kaka ... hehe meme <em>tram</em> <em>xe</em> don tiep chu dao <em>day</em> <em>nui</em> cao",
        ),
    ])
    def test_summarize_text(self, name, test_data, expected):
        result = summarize_text(test_data, max_num_words=4)
        self.assertEqual(expected, result)
