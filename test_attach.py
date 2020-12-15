import allure
import pytest

def test_attact_a():
    allure.attach(body="这是一段纯文本",name="text内容",attachment_type=allure.attachment_type.TEXT)

def test_attact_b():
    allure.attach("<body>这是一段HTML块</body>",name="HTML内容",attachment_type=allure.attachment_type.HTML)