from django.test import TestCase
from django.template import Context
from django.template.engine import Engine


class TagTests(TestCase):

    engine = Engine(
        debug=True,
        string_if_invalid="INVALID",
        libraries={"my_templatetags": "jobs.templatetags.my_templatetags"},
    )

    def tag_test(self, template, context, output):
        t = self.engine.from_string("{% load my_templatetags %}" + template)
        self.assertEqual(t.render(Context(context)), output)

    def test_query_transform(self):
        template = "{% for item in search %}{{item}}{% endfor %}"
        context = {"search": ["manager"]}
        output = "manager"
        self.tag_test(template, context, output)
